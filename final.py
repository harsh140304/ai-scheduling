from langgraph.graph import END, START, StateGraph , MessagesState
from tools import schedule_tools_write_node
from nodes import  tools_condition ,call_model,find_slots
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()

builder = StateGraph(MessagesState)
builder.add_node("agent", call_model)
builder.add_node("find_slots", find_slots)
builder.add_node("tools", schedule_tools_write_node)
builder.add_edge("__start__", "agent")
builder.add_conditional_edges("agent", tools_condition, ["tools", "find_slots", END])
builder.add_edge("tools", "agent")
builder.add_edge("find_slots", "agent")

graph = builder.compile()