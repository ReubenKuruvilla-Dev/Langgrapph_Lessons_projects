import os
from dotenv import load_dotenv
from strands import Agent
from strands_tools.tavily import tavily_search
from strands_tools.file_write import file_write
from model_setup import model

load_dotenv()

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

research_agent = Agent(
    model=model,
    tools=[tavily_search, file_write],
    system_prompt=(
        "You are a research assistant. Use the Tavily search tool to find accurate, "
        "up-to-date information. Always limit your search to the top 2 results (max_results=2). "
        "Summarize the findings clearly and save the output to research_output.txt using the file_write tool."
    ),
)

if __name__ == "__main__":
    response = research_agent(
        "What are the latest advancements in AI agents? Search for top 2 results only."
    )
    print(response)
