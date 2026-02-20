# 🌳 GenAI Prompt Tree Explorer

> **An interactive visualization and debugging tool for multi-step LLM execution chains.**

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.0%2B-blue)](https://reactjs.org/)

## 📖 Overview
As Generative AI applications move from single-prompt scripts to complex, agentic workflows (RAG, ReAct, multi-agent systems), debugging the execution chain becomes incredibly difficult. 

**Prompt Tree Explorer** is an Engineering Productivity (EngProd) tool designed to improve developer velocity and code health. It provides a lightweight SDK to trace LLM calls and a visual UI to explore, annotate, and debug the execution tree in real-time.

### ✨ Key Features
* **Visual Debugging:** Automatically generates a Directed Acyclic Graph (DAG) of your prompt execution flow.
* **Execution Tracing:** Captures inputs, outputs, token usage, latency, and exceptions at every node.
* **Zero-Friction Integration:** Use a simple `@trace` decorator to instrument your existing Python code.
* **Interactive Annotations:** Flag problematic prompt outputs and leave notes directly in the UI to streamline team debugging.

## 🏗️ Architecture
The system is decoupled into three main components:
1.  **Tracker SDK (`/sdk`):** A lightweight Python client that instruments LLM calls and asynchronously ships telemetry data.
2.  **Telemetry API (`/backend`):** A FastAPI service that ingests execution logs and manages the relational graph state.
3.  **Visualization UI (`/frontend`):** A React/React Flow application for interactive debugging and system diagnosis.

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* Node.js 18+

### 1. Start the Backend API
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8081
```

### 2. Start the Frontend UI
```bash
cd frontend
npm install
npm run dev
```

### 💻 Developer Usage (SDK Integration)
Instrumenting your GenAI application requires just two lines of code.

```python
from prompt_tree import Tracer, trace_node
import openai

# Initialize the tracer session
tracer = Tracer(session_name="RAG_Document_QA", api_host="http://localhost:8081")

@trace_node(name="Extract_Context", parent_id=None)
def extract_context(query: str):
    # Your standard LLM call goes here
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Extract info for: {query}"}]
    )
    return response.choices[0].message.content

# The execution is automatically logged and visualized in the UI!
context = extract_context("How do I setup Kubernetes?")
```

### 🛠️ System Health & Testability
This tool was built with production reliability in mind:

* **Asynchronous Logging:** The SDK uses background tasks to ensure API latency never impacts the host application's performance.
* **Data Sanitization:** Configurable filters allow developers to mask PII or sensitive data before it is shipped to the tracing backend.

## 🤝 Contributing
Contributions to improve developer velocity and visualization capabilities are welcome! Please ensure all pull requests pass the automated test suite before requesting a review.
