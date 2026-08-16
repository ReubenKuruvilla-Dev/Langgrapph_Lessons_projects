from strands import Agent
from strands.agent.conversation_manager import SummarizingConversationManager

from model_setup import model

agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant",
    conversation_manager=SummarizingConversationManager(
        summary_ratio=0.3,            # summarize the oldest 30% when trimming
        preserve_recent_messages=4,
    ),
    callback_handler=None
)

for i in range(1, 9):
    agent(f"Remember fact number {i}.")

print("Messages kept in history:", len(agent.messages))