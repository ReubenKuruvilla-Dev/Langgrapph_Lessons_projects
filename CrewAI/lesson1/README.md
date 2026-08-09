# Lesson 1 — Your First CrewAI Crew

## What does this code do?

It creates **two AI agents** that work together like coworkers:

1. A **Researcher** — finds the latest AI trends
2. A **Writer** — rewrites the research into a clean email

They work **one after the other** (sequential), and the writer gets the researcher's output automatically.

---

## The 4 Building Blocks

### 1. `Agent` — A worker with a job title
```python
researcher = Agent(
    role="Senior Research Scientist",       # job title
    goal="Find emerging AI trends in 2026", # what they want to achieve
    backstory="You never state anything you cannot back up.", # personality
    llm="gpt-4o-mini",                      # the AI brain they use
    allow_delegation=False,                 # must do the work themselves
)
```
> Think of an Agent like hiring a person. You tell them their role, their goal, and their personality.

---

### 2. `Task` — A specific piece of work
```python
research_task = Task(
    description="Research the current state of {topic}.",  # what to do
    expected_output="6 bullet points with sources.",        # what a good result looks like
    agent=researcher,                                       # who does it
)
```
> A Task is like handing someone a sticky note with instructions.
> `{topic}` is a placeholder — it gets filled in when the crew starts.

---

### 3. `Crew` — The team
```python
crew = Crew(
    agents=[researcher, writer],            # the team members
    tasks=[research_task, write_task],      # the work to do, in order
    process=Process.sequential,             # do tasks one by one
)
```
> The Crew organises who does what and in what order.

---

### 4. `kickoff()` — Press the start button
```python
result = crew.kickoff(inputs={"topic": "AI trends for 2026"})
```
> This starts the whole process. The `topic` you pass in fills the `{topic}` placeholder in the task description.

---

## How to run

```powershell
# 1. Activate the virtual environment (from the CrewAI folder)
.\venv\Scripts\activate.ps1

# 2. Go into lesson1
cd lesson1

# 3. Run the script
python Basic_crew.py
```

---

## What you need in your `.env` file

```
OPENAI_API_KEY=sk-...your key here...
```

---

## The full flow — in plain English

```
You → kickoff("AI trends for 2026")
         ↓
   Researcher reads the task
   Researcher asks GPT-4o-mini to find trends
   Researcher returns 6 bullet points
         ↓
   Writer receives the bullet points
   Writer asks GPT-4o-mini to turn them into an email
   Writer returns a clean email
         ↓
You ← final result printed to the terminal
```
