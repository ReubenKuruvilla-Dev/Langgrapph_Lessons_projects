
from langgraph.graph import StateGraph, START , END
from typing import TypedDict

# State 
class BMISTATE(TypedDict):
    weight_kg: float
    height_m: float
    bmi: float
    Category:str
    

# Function to caluculate the BMI
def calculate_bmi(state: BMISTATE) -> BMISTATE:
    weight = state['weight_kg'] 
    height = state['height_m'] 
    bmi = weight/(height**2)
    state['bmi'] = round(bmi, 2)
    return state

def category(state: BMISTATE) -> BMISTATE:
    bmi=state['bmi']
    if bmi<18.5:
        state['Category']="Underweight"
    elif bmi<25:
        state['Category']="Normal Weight"
    elif bmi<30:
        state['Category']="Overweight"
    else:
        state['Category']="Obesity"
    return state   

# Define graph
graph=StateGraph(BMISTATE)
# node
graph.add_node("calc_bmi",calculate_bmi)
graph.add_node("Category",category)
# edges
graph.add_edge(START, "calc_bmi")
graph.add_edge("calc_bmi","Category")
graph.add_edge("Category",END)

# compeile
workflow=graph.compile()
# run
final_state = workflow.invoke({'weight_kg':80, 'height_m':1.73})        
print(f"The BMI is {final_state['bmi']} and the category is {final_state['Category']}")

