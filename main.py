from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool
import math

@tool
def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius"""
    return math.pi * radius * radius

@tool
def calculate_circle_radius(area: float) -> float:
    """Calculate the radius of a circle given its area"""
    return math.sqrt(area / math.pi)

@tool
def calculate_circle_circumference(radius: float) -> float:
    """Calculate the circumference of a circle given its radius"""
    return 2 * math.pi * radius

def run_agent():
    llm = ChatOpenAI(temperature=0,model="gpt-4o")
    tools = [calculate_circle_area, calculate_circle_radius, calculate_circle_circumference]
    agent = create_react_agent(llm, tools)
    memory_saver = MemorySaver()
    
    while True:
        user_input = input("Enter your question (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
            
        result = agent.invoke({"input": user_input})
        print(f"Agent response: {result['output']}")
        memory_saver.save(result)

if __name__ == "__main__":
    run_agent()
