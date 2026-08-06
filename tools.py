
import dotenv 
import requests 
import os 
from composio_langgraph import Action, ComposioToolSet
from langgraph.prebuilt import ToolNode

dotenv.load_dotenv()


BLAND_API_KEY = os.environ.get("BLAND_API_KEY")
def make_confirmation_call(phone_number: str, instructions: str):
    """
    Makes a confirmation call using the Bland.ai API.

    Parameters:
        phone_number (str): The recipient's phone number.
        instructions (str): The message to be delivered.
        api_key (str): The API authorization key.

    Returns:
        dict: The API response as a dictionary.
    """
    url = "https://api.bland.ai/v1/calls"

    payload = {
        "phone_number": phone_number,
        "task": instructions
    }

    headers = {
        "authorization": os.environ["BLAND_API_KEY"],
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()  


# Initialize ComposioToolSet with API key from environment variables
composio_toolset = ComposioToolSet(api_key=os.getenv("COMPOSIO_API_KEY"))

# Get the required tools
schedule_tools_set = composio_toolset.get_tools(
    actions=[
        Action.GOOGLECALENDAR_FIND_FREE_SLOTS,
        Action.GOOGLECALENDAR_CREATE_EVENT,
        Action.GMAIL_CREATE_EMAIL_DRAFT
    ]
)

# Separate out
schedule_tools_write = composio_toolset.get_tools(
    actions=[
        Action.GOOGLECALENDAR_CREATE_EVENT,
        Action.GMAIL_CREATE_EMAIL_DRAFT
    ]
)

schedule_tools_write_node = ToolNode(schedule_tools_write + [make_confirmation_call])
