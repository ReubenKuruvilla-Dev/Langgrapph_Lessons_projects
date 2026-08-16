from strands import Agent
from strands.models.openai import OpenAIModel
from dotenv import load_dotenv
import os

load_dotenv()

model = OpenAIModel(
    client_args={
        "api_key": os.getenv("OPENAI_API_KEY")
    },
    model_id="gpt-4o",
    params={
        "temperature":0.7
    }
)

agent = Agent(
    model= model,
    system_prompt="You are a helpful assistant"
)

response = agent("What is the captial of France and top 3 place to visit?")

print(response)
