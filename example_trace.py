from prompt_tree import Tracer, trace_node
import time
import random

tracer = Tracer(session_name=f"Example_Session_{random.randint(1000, 9999)}", api_host="http://localhost:8081")

@trace_node(name="Main_Agent")
def main_agent(query):
    print(f"Agent received: {query}")
    time.sleep(0.2)
    step1_result = step1(query)
    step2_result = step2(step1_result)
    return f"Final Answer to '{query}': {step2_result}"

@trace_node(name="Reasoning_Step")
def step1(query):
    print("Thinking...")
    time.sleep(0.5)
    return f"Processed({query})"

@trace_node(name="Tool_Call")
def step2(data):
    print("Calling tool...")
    time.sleep(0.3)
    # Simulate a nested call
    sub_task("config_check")
    return f"Result({data})"

@trace_node(name="Sub_Task")
def sub_task(arg):
    time.sleep(0.1)
    return "OK"

if __name__ == "__main__":
    print("Starting trace...")
    try:
        final = main_agent("What is the capital of France?")
        print(final)
    except Exception as e:
        print(f"Error: {e}")
    
    # Wait for logs to flush
    print("Waiting for logs to flush...")
    time.sleep(2)
    print("Done!")
