from langgraph.graph import StateGraph, START , END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPEN_AI_API"),
)

# state
class SimpleLLM(TypedDict):
    question: str
    answer: str

# LLM def
def qa_llm_simple(state : SimpleLLM) -> SimpleLLM:
    question = state['question']
    prompt = f"give answer in short to the question {question}"
    response=model.invoke(prompt)
    state['answer']=response.content
    return state



# Node
graph = StateGraph(SimpleLLM)
graph.add_node("qa_llm_simple",qa_llm_simple)
#edge 
graph.add_edge(START, "qa_llm_simple")
graph.add_edge("qa_llm_simple",END)
# compile
workflow = graph.compile()

workflow_invoke=workflow.invoke({'question':'what is langgraph and how does it help in building agentic ai workflow'})

print(f"The question is : \n {workflow_invoke['question']}\n")
print(f"The answer is : \n {workflow_invoke['answer']}")