from redis.typing import KeyT
from strands import Agent , tool, ToolContext
from model_setup import model

@tool(context=True)
def remember_fact(key:str , value:str, tool_context: ToolContext) -> str:
    """Store a durable fact about the user.

    Args:
        key: The kind of fact, e.g. "name" or "favorite_language".
        value: The value to remember.
    """
    tool_context.agent.state.set(key, value)
    return f"Noted: {key} = {value}"

@tool(context=True)
def recall_fact(key: str, tool_context: ToolContext) -> str:
    """Retrieve a previously stored fact about the user.

    Args:
        key: The kind of fact to look up.
    """
    value = tool_context.agent.state.get(key)
    return f"{key}: {value}" if value else f"Nothing stored for '{key}'."



agent = Agent(
    model=model,
    tools=[remember_fact, recall_fact],
    system_prompt=(
        "You are a personable assistant. When the user shares durable facts about "
        "themselves, store them with remember_fact. Use recall_fact when you need them."
    ),
)

agent("Hi, I'm Reuben and I live in Mumbai.")
agent("What's my name and where do I live?")

print("\nStored state:", agent.state.get())