from strands import Agent
from strands.multiagent import GraphBuilder
from model_setup import model

outliner = Agent(
    name="outliner",
    model=model,
    system_prompt="You write a 4-bullet outline for the given topic. Bullets only.",
    callback_handler=None,
)

drafter = Agent(
    name="drafter",
    model=model,
    system_prompt="You turn an outline into a short article of about 150 words.",
    callback_handler=None,
)

reviewer = Agent(
    name="reviewer",
    model=model,
    system_prompt="You review a draft and list 3 concrete improvements. Bullets only.",
    callback_handler=None,
)

builder = GraphBuilder()

builder.add_node(outliner, "outliner")
builder.add_node(drafter, "drafter")
builder.add_node(reviewer, "reviewer")

builder.add_edge("outliner", "drafter")
builder.add_edge("drafter", "reviewer")

builder.set_entry_point("outliner")

builder.set_execution_timeout(300)

graph = builder.build()

result = graph("Write about why cities are getting hotter")