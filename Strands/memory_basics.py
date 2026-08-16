from strands import Agent
from model_setup import model

agent = Agent(
    model=model,
    callback_handler=None,
    system_prompt="you are a helpful assistant"

)

agent("My name is Reuben  and I loveStrands.")
agent("What's my name and what do I love?")


print("Messages in history:", len(agent.messages))
print("Last reply:", str(agent.messages[-1]["content"][0]["text"]))