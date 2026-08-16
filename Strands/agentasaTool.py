
from strands import Agent, tool, ToolContext
from model_setup import model


# ─── STATE TOOLS ─────────────────────────────────────────────────────────────
# These tools give the coordinator the ability to STORE and RETRIEVE results
# in agent.state — a persistent key-value dictionary that survives across
# multiple agent() calls.

@tool(context=True)
def log_result(key: str, value: str, tool_context: ToolContext) -> str:
    """Store a piece of work output for later reference.

    Args:
        key: A label for the result, e.g. "summary" or "spanish_translation".
        value: The content to store.
    """
    tool_context.agent.state.set(key, value)
    return f"Stored '{key}' successfully."


@tool(context=True)
def get_log(key: str, tool_context: ToolContext) -> str:
    """Retrieve a previously stored result.

    Args:
        key: The label to look up.
    """
    value = tool_context.agent.state.get(key)
    return f"{key}: {value}" if value else f"Nothing stored for '{key}'."


# ─── SUB-AGENT 1: Summarizer ────────────────────────────────────────────────

summarizer = Agent(
    model=model,
    name="summarizer",
    description="Summarizes long text into concise bullet points.",
    system_prompt=(
        "You are a summarization specialist. When given any text, "
        "return a concise bullet-point summary. Do not add commentary."
    ),
    callback_handler=None,
)


# ─── SUB-AGENT 2: Translator ────────────────────────────────────────────────

translator = Agent(
    model=model,
    name="translator",
    description="Translates English text into Spanish.",
    system_prompt=(
        "You are a professional translator. Translate the given English text "
        "into fluent, natural Spanish. Return only the translation."
    ),
    callback_handler=None,
)


# ─── COORDINATOR (Parent Agent) ─────────────────────────────────────────────

coordinator = Agent(
    model=model,
    system_prompt=(
        "You are a coordinator. You have two specialists and two logging tools:\n"
        "  Specialists:  'summarizer' and 'translator'\n"
        "  Logging:      'log_result' and 'get_log'\n\n"
        "Workflow:\n"
        "  1. Call 'summarizer' to condense the text into bullet points.\n"
        "  2. Call 'log_result' with key='summary' to store the summary.\n"
        "  3. Call 'translator' to translate the summary into Spanish.\n"
        "  4. Call 'log_result' with key='spanish_translation' to store it.\n"
        "  5. Present both results clearly to the user."
    ),
    tools=[summarizer, translator, log_result, get_log],
)


# ─── RUN THE PIPELINE ───────────────────────────────────────────────────────
if __name__ == "__main__":
    sample_text = (
        "Artificial intelligence has transformed industries ranging from healthcare "
        "to finance. In healthcare, AI models assist in diagnosing diseases from "
        "medical images with accuracy rivalling human doctors. In finance, algorithmic "
        "trading systems powered by machine learning analyse market patterns in "
        "milliseconds. Meanwhile, natural language processing enables virtual "
        "assistants to understand and respond to human speech with increasing nuance. "
        "Despite these advances, ethical concerns around bias, privacy, and job "
        "displacement remain significant challenges that society must address."
    )

    # First request — summarize and translate
    coordinator(
        f"Please summarize the following text and then translate the summary "
        f"into Spanish:\n\n{sample_text}"
    )

    # Print what was persisted in agent.state
    print("\n" + "=" * 60)
    print("AGENT STATE (persisted key-value pairs):")
    print("=" * 60)
    print(coordinator.state.get())

    # Second request — prove state persists across calls
    print("\n" + "=" * 60)
    print("SECOND CALL — retrieving stored results from state:")
    print("=" * 60)
    coordinator("Can you show me the summary you stored earlier? Use get_log.")
