import os
from dotenv import load_dotenv
from strands.models.openai import OpenAIModel

load_dotenv()

model = OpenAIModel(
    client_args={
        "api_key": os.getenv("OPENAI_API_KEY"),
    },
    model_id="gpt-4o",
    params={"temperature": 0.7},
)