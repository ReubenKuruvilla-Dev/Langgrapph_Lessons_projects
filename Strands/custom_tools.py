
from strands import Agent, tool
from model_setup import model


# ----------------------------------------------------------
# CUSTOM TOOL 1: word_count
# ----------------------------------------------------------

# ----------------------------------------------------------
@tool
def word_count(text: str) -> int:
    """Counts the number of words in a given text."""
    return len(text.split())


# ----------------------------------------------------------
# CUSTOM TOOL 2: add
# ----------------------------------------------------------


@tool
def add(a: int, b: int) -> int:
    """Adds two integers together and returns the result."""
    return a + b


# ----------------------------------------------------------
# CREATE THE AGENT WITH CUSTOM TOOLS
# ----------------------------------------------------------
agent = Agent(
    model=model,
    tools=[add, word_count],
    system_prompt="You are a helpful assistant that can perform simple arithmetic and count words."
)




print("\n" + "=" * 60)
print("Q1: How many words are in 'hello world'?")
print("=" * 60)
agent("How many words are in 'hello world'?")


print("\n" + "=" * 60)
print("Q2: What is the average of 1, 2, 3, 4, 5, and 6?")
print("=" * 60)
agent("What is the average of 1, 2, 3, 4, 5, and 6?")
