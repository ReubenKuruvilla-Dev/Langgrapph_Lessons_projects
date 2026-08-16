from strands import Agent
from strands.agent.conversation_manager import SlidingWindowConversationManager

from model_setup import model

agent = Agent(
    model=model,
    callback_handler=None,
    system_prompt="You are a helpful assistant.",
    conversation_manager=SlidingWindowConversationManager(window_size=6)
)

for i in range(1,8):
    agent(f"this is message number {i}")

    print(f"conversation turns = {len(agent.messages)}")
