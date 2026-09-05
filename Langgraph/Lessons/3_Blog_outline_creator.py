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
class BlogState(TypedDict):
    Title: str
    Outline: str
    Blog: str

# LLM def
def create_Outline(state : BlogState) -> BlogState:
    title = state['Title']
    prompt = f"generate a blog outline for the title {title}"
    response=model.invoke(prompt)
    state['Outline']=response.content
    return state

def create_Blog(state : BlogState) -> BlogState:
  outline = state['Outline']
  prompt = f"write a blog based on the outline {outline}"
  response=model.invoke(prompt)
  state['Blog']=response.content
  return state

# Node
graph = StateGraph(BlogState)
graph.add_node('create_outline', create_Outline)
graph.add_node('create_Blog',create_Blog )
#edge 
graph.add_edge(START, "create_outline")
graph.add_edge("create_outline","create_Blog")
graph.add_edge("create_Blog",END)
# compile
workflow = graph.compile()

workflow_invoke=workflow.invoke({'Title':'Langgraph updates - 10th sep 2026'})

print(f"The Title is : \n {workflow_invoke['Title']}\n")
print(f"The Outline is : \n {workflow_invoke['Outline']}\n")
print(f"The Blog is : \n {workflow_invoke['Blog']}")