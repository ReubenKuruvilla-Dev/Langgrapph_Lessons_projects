import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
load_dotenv()

api = os.environ.get("OPENAI_API_KEY")

researcher = Agent(
    role="Senior Research Scientist",
    goal="Identify the emerging trends in AI in 2026",
    backstory=(
        "You have spent a decade separating hype from substance in AI. "
        "You never state anything you cannot back up."
    ),
    llm="gpt-4o-mini",  
    allow_delegation = False,
    verbose = True,

)


writer = Agent(
     role="Technical Writer",
    goal="Turn research notes into a crisp briefing a busy manager can read",
    backstory="You write short. You cut adjectives. You never pad.",
    llm="gpt-4o-mini",
    verbose=True,
)

research_task = Task(
    description="Research the current state of {topic}. Focus on the last 12 months.",
    expected_output="6 bullet points, each one sentence, each with a source name.",
    agent=researcher,
)

write_task = Task(
    description="Rewrite this as a single, clear, crisp email.",
    expected_output="An email with: a clear subject line, max 3 short paragraphs, and 1 bolded key takeaway at the bottom.",
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff(inputs={"topic": "AI trends for 2026"})
    print("\n\n## RESULT")
    print(result)