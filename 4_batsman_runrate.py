from langgraph.graph import StateGraph, START , END
from typing import TypedDict

class BatsMan(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int

    sr: float
    bpb: float
    boundary_percent: float
    summary: str



def cal_bats_sr(state : BatsMan):
    sr = (state['runs']/state['balls'])*100
    return {'sr' : sr}

def cal_bats_bpb(state: BatsMan):
     bpb = state['balls']/(state['fours'] + state['sixes'])
     return {'bpb' : bpb}

def calculate_boundary_percent(state: BatsMan):

    boundary_percent = (((state['fours'] * 4) + (state['sixes'] * 6))/state['runs'])*100

    return {'boundary_percent': boundary_percent} 

def generate_summary(state: BatsMan):

    summary = f"Batsman scored {state['runs']} off {state['balls']} balls. SR : {state['sr']:.2f}, BPB : {state['bpb']:.2f}, Boundary %: {state['boundary_percent']:.2f}%"
    
    return {'summary': summary}

graph = StateGraph(BatsMan)

graph.add_node('cal_sr',cal_bats_sr)
graph.add_node('cal_bpb',cal_bats_bpb)
graph.add_node('calculate_boundary_percent',calculate_boundary_percent)
graph.add_node('generate_summary',generate_summary)

graph.add_edge(START, 'cal_sr')
graph.add_edge(START,'cal_bpb')
graph.add_edge(START,'calculate_boundary_percent')

graph.add_edge('cal_sr','generate_summary')
graph.add_edge('cal_bpb','generate_summary')
graph.add_edge('calculate_boundary_percent','generate_summary')

graph.add_edge('generate_summary',END)

workflow = graph.compile()

result = workflow.invoke({'runs':105 , 'balls':60, 'fours':12,'sixes':3})

print(result)