# ============================================================
# Lesson 3 - Stateful Agent (Conversation Memory)
# ============================================================
# A Strands Agent is stateful by default.
# Every time you call agent("..."), it remembers ALL previous
# messages and sends the full history to the model.
# This allows the agent to understand follow-up questions
# without you repeating yourself.
# ============================================================

from strands import Agent
from model_setup import model


# ----------------------------------------------------------
# HELPER FUNCTION
# ----------------------------------------------------------
#
# ----------------------------------------------------------
def get_text(response):
    """Extract the plain text reply from an AgentResult."""
    return response.message["content"][0]["text"]


# ----------------------------------------------------------
# CREATE THE AGENT
# ----------------------------------------------------------


agent = Agent(
    model=model,
    system_prompt="You are a customer support agent for a company that sells electronics."
)


# ----------------------------------------------------------
# TURN 1 — Customer reports a cracked screen
# ----------------------------------------------------------

response1 = agent("Hi there, my iPhone 13 has a cracked screen. Can you help me with a repair?")
print("Response 1:")
print(get_text(response1))
print("=" * 80)


# ----------------------------------------------------------
# TURN 2 — Customer asks about repair cost
# ----------------------------------------------------------
response2 = agent("I'd like to know how much the repair would cost.")
print("\nResponse 2:")
print(get_text(response2))
print("=" * 80)


# ----------------------------------------------------------
# TURN 3 — New topic: return policy
# The agent still has the full conversation in memory.
# ----------------------------------------------------------

response3 = agent("What is the return policy for the new iPhone I purchased last week?")
print("\nResponse 3:")
print(get_text(response3))
print("=" * 80)


# ----------------------------------------------------------
# TURN 4 — Another new topic: order tracking
# ----------------------------------------------------------
response4 = agent("I didn't receive my order yet. The tracking number is #123456.")
print("\nResponse 4:")
print(get_text(response4))
print("=" * 80)


print("\n" + "=" * 80)
print(agent.messages)

