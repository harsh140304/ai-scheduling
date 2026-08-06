import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import MessagesState
from tools import schedule_tools_set,make_confirmation_call
from prompt import initial_message
from langchain_core.messages import SystemMessage 
from typing import Literal
from langchain_core.messages import SystemMessage,ToolMessage
import logging

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp")


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)
logger = logging.getLogger(__name__)
# Bind tools to the model
model_with_tools = model.bind_tools(schedule_tools_set + [make_confirmation_call])

# Define the workflow functions
def call_model(state: MessagesState):
    """
    Process messages through the LLM and return the response
    """

    # Get today's date and time
    today_datetime = datetime.datetime.now().isoformat()
    response = model_with_tools.invoke([SystemMessage(content=initial_message.format(today_datetime=today_datetime))] + state["messages"])
    return {"messages": [response]}

async def tools_condition(state: MessagesState) -> Literal["find_slots",  "tools", "__end__"]:
    """
    Determine if the conversation should continue to tools or end
    """
    messages = state["messages"]
    last_message = messages[-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
      for call in last_message.tool_calls:
          tool_name = call.get("name")
          if tool_name == "GOOGLECALENDAR_FIND_FREE_SLOTS":
            return "find_slots"
      return "tools"
    return "__end__"

async def find_slots(state: MessagesState) -> Literal["agent"]:
    """
    Determine if the conversation should continue to tools or end
    """
    messages = state["messages"]
    last_message = messages[-1]

    tool_messages = []

    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
    # Process every call in the list
      for call in last_message.tool_calls:
          logger.info("Processing tool call: %s", call)
          tool_name = call.get("name")
          tool_id = call.get("id")
          args = call.get("args")

          find_free_slots_tool = next((tool for tool in schedule_tools_set if tool.name == tool_name), None)

          if tool_name == "GOOGLECALENDAR_FIND_FREE_SLOTS":

              res = find_free_slots_tool.invoke(args)
              tool_msg = ToolMessage(
                    name=tool_name,
                    content=res,
                    tool_call_id=tool_id  # Use the extracted tool_call_id
                )
              tool_messages.append(tool_msg)
    return {"messages": tool_messages}

