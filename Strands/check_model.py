from strands import Agent
from model_setup import model

agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant"
)
result = agent("Say hello in exact 5 words")

print(result)