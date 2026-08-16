
from strands import Agent
from model_setup import model

researcher = Agent(
    model=model,
    name="researcher_agent",
    description="Researches a topic and returns organized factual notes.",
    system_prompt=("""You are a research specialist. Given a topic, identify the key aspects, "
        lay out the important facts clearly, and return concise, well-organized notes.")
"""), callback_handler=None)

writer = Agent(
    model=model,
    name="writer",
    description="Turns research notes into a polished, readable article.",
    system_prompt=(
        "You are a content writer. Given research notes, write an engaging article "
        "with a clear introduction, body, and conclusion, for a general audience."
    ),
    callback_handler=None,
)

cordinator = Agent(
    model=model,
    system_prompt=(
        "You coordinate specialists to produce content. First delegate to the "
        "researcher to gather facts, then pass those notes to the writer to produce "
        "the final article. You orchestrate; you do not do the specialized work yourself."
    ),
    tools=[researcher, writer],

)

cordinator("Create a short article about the benefits of renewable energy.")