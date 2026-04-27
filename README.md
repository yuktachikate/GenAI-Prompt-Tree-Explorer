# 🌳 GenAI Prompt Tree Explorer  
### Visual debugging and evaluation system for multi-step LLM workflows

> An interactive system to trace, visualize, and debug complex LLM execution chains, enabling engineers to analyze reasoning paths, detect failures, and improve AI system reliability.

---

## 🧠 Problem

As AI systems evolve into multi-step workflows (RAG, agents, tool-calling), debugging becomes difficult because:

- reasoning steps are hidden  
- failures are hard to trace  
- outputs lack transparency  

👉 Developers cannot easily understand **why an LLM failed**

---

## ⚙️ Approach

Built a **full-stack tracing and visualization system** for LLM pipelines.

### System Design

- SDK layer → instruments LLM calls  
- Telemetry backend → captures execution data  
- Visualization UI → displays execution graph  

### Data Flow
LLM Calls → Tracing SDK → Telemetry API → Execution Graph → Interactive UI


### Key Idea

> Treat LLM workflows like distributed systems — **trace, observe, and debug them**

---

## ✨ Key Features

### 🌳 Execution Graph Visualization
- Generates a DAG of multi-step LLM workflows  
- Shows full reasoning chain from input → output  
- Helps identify failure points  

---

### 🔍 LLM Execution Tracing
- Captures:
  - inputs & outputs  
  - token usage  
  - latency  
  - errors  
- Enables deep debugging of model behavior  

---

### ⚡ Lightweight SDK Integration
- Simple decorator-based instrumentation  
- Minimal code changes required  
- Works with existing pipelines  

---

### 🧠 Debugging & Evaluation
- Identify hallucinations and inconsistencies  
- Compare reasoning paths across runs  
- Flag problematic outputs  

---

### 📝 Interactive Annotations
- Add notes directly to execution nodes  
- Track debugging insights across teams  
- Improve collaboration on AI systems  

---

## 🧰 Tech Stack

- Python (FastAPI)  
- LLM APIs (OpenAI-compatible)  
- React + TypeScript  
- Graph Visualization (React Flow)  
- Async telemetry pipelines  

---

## 🏗️ Architecture
LLM APPLICATION
↓
TRACING SDK (Decorator-based)
↓
TELEMETRY API (FastAPI)
↓
GRAPH STORAGE
↓
VISUALIZATION UI (React)


---

## 🚀 Why it matters

This project introduces a key capability:

> **Observability for LLM systems**

### Impact

- Improves reliability of AI workflows  
- Enables debugging of multi-step reasoning  
- Reduces time to diagnose failures  
- Supports evaluation of LLM behavior  

### Applications

- LLM evaluation platforms  
- RAG and agent debugging  
- AI infrastructure tooling  
- Developer productivity systems  

---

## 🔮 Future Improvements

- Add automated scoring for reasoning quality  
- Integrate evaluation metrics (accuracy, hallucination detection)  
- Support multi-agent workflow tracing  
- Add replay and simulation capabilities  

---

## 🎥 Demo

> (Add screenshots or short demo video here)

---

## 💻 Example Usage

```python
from prompt_tree import Tracer, trace_node

tracer = Tracer(session_name="example")

@trace_node(name="LLM Step")
def run_llm(prompt):
    return llm_call(prompt)
