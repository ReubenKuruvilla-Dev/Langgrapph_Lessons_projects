from strands import Agent
from strands.multiagent import Swarm
from model_setup import model



planner =  Agent(
    name="planner",
    system_prompt=(
        "You plan features for small apps. "
        "List what to build, then hand off to the coder."
    ),
    callback_handler=None
)

coder = Agent(
    name="coder",
    model=model,
    system_prompt=(
        "You write small, complete Python scripts."
        "For each file, write the *full* file including imports and functions."
    ),
    callback_handler=None
)


verifier = Agent(
    name="verifier",
    model=model,
    system_prompt=(
        "You test code by running it and checking the output. "
        "If it works, say so. If not, explain what went wrong. "
        "Then hand off to the fixer."
    ),
    callback_handler=None,
)

fixer = Agent(
    name="fixer",
    model=model,
    system_prompt=(
        "Fix the bug described by the verifier. "
        "Keep the same style and structure. "
        "Then hand back to the verifier to re-check."
    ),
    callback_handler=None,
)

sarm = Swarm(
    [planner, coder, verifier, fixer],
    entry_point=planner,
    max_handoffs=10,
    max_iterations=10
)
result = sarm("Write a Python script to scrape news headlines")