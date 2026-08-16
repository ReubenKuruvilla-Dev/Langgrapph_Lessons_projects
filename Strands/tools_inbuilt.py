
# ============================================================
# COMPLETE LIST OF BUILT-IN STRANDS TOOLS
# ============================================================
#
# ── MATH & TIME ─────────────────────────────────────────────
#
#   calculator      → Performs math operations using SymPy.
#                     Handles arithmetic, algebra, calculus,
#                     symbolic math, and unit conversions.
#                     Example: "What is the integral of x^2?"
#
#   current_time    → Returns the current UTC date and time
#                     in ISO 8601 format.
#                     Example: "What time is it right now?"
#
# ── FILE SYSTEM ─────────────────────────────────────────────
#
#   file_read       → Reads files from disk. Supports plain
#                     text, CSV, JSON, PDF, and more.
#                     Example: "Read the contents of data.csv"
#
#   file_write      → Writes or overwrites content to a file
#                     on disk with user confirmation.
#                     Example: "Save this report to output.txt"
#
#   editor          → Makes iterative edits across multiple
#                     files. Designed for code editing tasks.
#                     Example: "Fix the bug in main.py line 42"
#
# ── WEB & NETWORKING ────────────────────────────────────────
#
#   http_request    → Makes HTTP requests (GET, POST, PUT,
#                     DELETE) with headers and auth support.
#                     Example: "Fetch data from this API URL"
#
#   browser         → Controls a real browser (Playwright).
#                     Can browse websites, click, fill forms.
#                     Example: "Go to google.com and search X"
#
#   tavily          → AI-powered web search via Tavily API.
#                     Returns summarised search results.
#                     Example: "Search the web for latest AI news"
#
#   rss             → Reads and parses RSS/Atom news feeds.
#                     Example: "Get headlines from BBC RSS feed"
#
#   exa             → Semantic web search via Exa API.
#                     Finds relevant pages by meaning, not keyword.
#
# ── CODE & SHELL ────────────────────────────────────────────
#
#   python_repl     → Executes Python code in a sandboxed
#                     REPL environment and returns output.
#                     Example: "Run this Python snippet for me"
#
#   shell           → Runs shell commands (bash/PowerShell)
#                     on the host machine.
#                     Example: "List all files in /tmp"
#
#   code_interpreter→ Managed code sandbox via AWS Bedrock
#                     AgentCore for secure execution.
#
# ── AI & AGENTS ─────────────────────────────────────────────
#
#   think           → Lets the agent reason step-by-step
#                     before answering. Improves accuracy on
#                     complex problems.
#                     Example: Used internally for chain-of-thought
#
#   use_llm         → Creates a fresh LLM instance inside
#                     the agent. Useful for sub-tasks.
#
#   use_agent       → Spawns a new Strands Agent with its
#                     own prompt, model, and tools.
#                     Example: Delegate a sub-task to another agent
#
#   swarm           → Coordinates a TEAM of AI agents working
#                     together to solve a complex problem.
#                     Example: "Use 3 agents to research this topic"
#
#   agent_graph     → Creates a graph of agents where each
#                     node is an agent. Enables multi-agent
#                     pipelines and DAG-style workflows.
#
# ── MEMORY & KNOWLEDGE ──────────────────────────────────────
#
#   memory          → Stores and retrieves data in an Amazon
#                     Bedrock Knowledge Base (vector store).
#
#   retrieve        → Semantic retrieval from a Bedrock
#                     Knowledge Base. Used for RAG workflows.
#
#   agent_core_memory→ Persistent memory using AWS Bedrock
#                      AgentCore Memory API.
#
#   elasticsearch_memory → Stores agent memory in Elasticsearch.
#
#   mem0_memory     → Persistent memory using the Mem0 platform.
#
#   mongodb_memory  → Stores agent memory in MongoDB Atlas.
#
# ── IMAGES & MEDIA ──────────────────────────────────────────
#
#   generate_image  → Generates images from text prompts
#                     using Stable Diffusion via AWS Bedrock.
#                     Example: "Draw a sunset over mountains"
#
#   generate_image_stability → Image generation via the
#                     Stability AI API directly.
#
#   image_reader    → Reads an image file from disk and
#                     prepares it for the vision model.
#                     Example: "What is in this image?"
#
#   nova_reels      → Generates short video reels using
#                     Amazon Nova via AWS Bedrock.
#
#   chat_video      → Enables video understanding —
#                     the agent can "watch" and answer about it.
#
#   search_video    → Searches for videos by query.
#
# ── AUDIO ───────────────────────────────────────────────────
#
#   speak           → Converts text to speech and plays it
#                     out loud on the host machine.
#                     Example: "Read this message aloud"
#
# ── WORKFLOW & SCHEDULING ───────────────────────────────────
#
#   sleep           → Pauses the agent for N seconds.
#                     Example: Used between polling loops
#
#   stop            → Stops the current agent event loop.
#                     Used to terminate agent execution early.
#
#   cron            → Schedules recurring tasks using cron
#                     expressions on the host machine.
#                     Example: "Run this check every hour"
#
#   handoff_to_user → Pauses the agent and hands control
#                     back to a human for review or input.
#                     Example: "Ask the user to confirm before proceeding"
#
# ── DIAGRAMS & VISUALIZATION ────────────────────────────────
#
#   diagram         → Generates flowcharts and architecture
#                     diagrams using Graphviz.
#                     Example: "Draw a diagram of this system"
#
# ── EXTERNAL INTEGRATIONS ───────────────────────────────────
#
#   mcp_client      → Connects to any external MCP (Model
#                     Context Protocol) server and uses its
#                     tools dynamically.
#
#   slack           → Sends messages to a Slack channel.
#                     Example: "Send a Slack alert to #alerts"
#
#   bright_data     → Web scraping via the Bright Data API.
#
#   a2a_client      → Agent-to-Agent communication protocol
#                     client for distributed agent systems.
#
#   journal         → Logs thoughts and notes to a journal
#                     file for long-running agent sessions.
#
#   graph           → General graph data structure for
#                     representing relationships between nodes.
#
#   batch           → Runs multiple agent tasks in parallel
#                     as a batch job (AWS Bedrock Batch).
#
#   load_tool       → Dynamically loads a tool from a file
#                     path or module at runtime.
#
#   environment     → Reads environment variables from the
#                     host system.
#
# ── AWS ─────────────────────────────────────────────────────
#
#   use_aws         → Executes any AWS SDK (boto3) operation.
#                     Example: "List my S3 buckets"
#
# ============================================================
# NOTE: Some tools require extra packages or AWS credentials.
# Install only what you need. For example:
#   pip install feedparser      # for rss
#   pip install graphviz        # for diagram
#   pip install nest_asyncio    # for browser
#   AWS credentials             # for memory, generate_image, use_aws
# ============================================================



from strands import Agent
# pyrefly: ignore [missing-import]
from strands_tools import calculator, current_time
from model_setup import model

agent = Agent(
    model=model,
    tools=[calculator,current_time],
    system_prompt="You are a helpful assistant that can answer questions about math and time."
)
result = agent("what is 2+2?")

print(result)

result2 =  agent("what time is it?")

print(result2)
