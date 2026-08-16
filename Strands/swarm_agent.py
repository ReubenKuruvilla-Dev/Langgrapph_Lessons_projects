from strands import Agent
from strands.multiagent import Swarm
from model_setup import model


intake = Agent(
    model=model,
    name="intake",
    system_prompt=(
        "You triage customer support requests. Summarize the issue, then hand off to "
        "the 'technical' agent for product or bug issues, or the 'billing' agent for "
        "charges and refunds. Do not try to resolve the issue yourself."
    ),
)

technical = Agent(
    model=model,
    name="technical",
    system_prompt=(
        "You are technical support. Diagnose the customer's problem and propose a "
        "concrete solution, then hand off to the 'quality' agent to review your answer."
    ),
)

billing = Agent(
    model=model,
    name="billing",
    system_prompt=(
        "You handle billing issues like duplicate charges and refunds. Resolve the "
        "request, then hand off to the 'quality' agent to review the outcome."
    ),
)

quality = Agent(
    model=model,
    name="quality",
    system_prompt=(
        "You are quality assurance. Review how the issue was handled, confirm it "
        "actually addresses the customer's request, and give a short final summary."
        "After short summary, if you think that it can resolve the issue finish the flow without any further handoff."
        "Otherwise you can do another handoff."
    ),
)


support = Swarm(
    [intake, technical, billing, quality],
    entry_point=intake,
    max_handoffs=10,
    max_iterations=10
)

result = support(
    "I was charged twice for my subscription this month. Can I get a refund for the "
    "duplicate charge?"
)
print("Path taken:", [node.node_id for node in result.node_history])