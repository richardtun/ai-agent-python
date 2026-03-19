# ai-agent-python

AI Task Agent (Python)
A modular AI task management agent built with Python.
The agent is designed with a clear separation of responsibilities, fallback mechanism, and production-style logging, suitable as a portfolio project.

# ✨ Features

✅ Parse natural language user input

✅ Decide actions via Reasoner (GPT / Mock GPT fallback)

✅ Execute actions (add / list / remove tasks)

✅ In-memory task storage

✅ Robust fallback when GPT fails

✅ Structured logging with daily log rotation

✅ Clean, professional Python project structure

# 🧠 Architecture Overview
User Input
   ↓
Reasoner (GPT → Mock fallback)
   ↓
Decision (action + data)
   ↓
Action Execution
   ↓
Memory Update


# Core components:

- AIAgent: Orchestrates the agent lifecycle
- Reasoner:
    - GPTReasoner (primary, may fail)
    - MockGPTReasoner (fallback)
- Actions: Business logic (add / list / remove tasks)
- Memory: Stores tasks in memory
- Logging:
    - Console logging (INFO level)
    - Daily rotating file logs (DEBUG level)


# Project Structure

ai-agent-python/
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── ai_agent/
│       ├── __init__.py
│       ├── main.py          # Entry point
│       ├── logger.py        # Logging configuration
│       │
│       └── agent/
│           ├── __init__.py
│           ├── agent.py     # Agent orchestration
│           ├── memory.py    # Task storage
│           ├── actions.py   # Agent actions
│           └── reasoner.py  # GPT / Mock reasoning
│
└── tests/

This structure follows industry best practices:
   - Clear entry point
   - Modular responsibilities
   - Absolute imports
   - Easy scalability


# ⚙️ Setup & Run

1️⃣ Clone repository

git clone https://github.com/richardtun/ai-agent-python

cd ai-agent-python

2️⃣ Create & activate virtual environment

python -m venv .venv

source .venv/bin/activate   # Linux / macOS / Codespaces

.venv\Scripts\activate    # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the agent

python src/ai_agent/main.py


# 📄 Logging
- Logs are displayed on the console (INFO level)
- Detailed logs are written to agent.log
- Log files rotate daily
- Old logs are automatically cleaned up

Log files are excluded from version control via .gitignore


# 🧩 Skills Demonstrated
This project demonstrates:

✅ Python fundamentals (OOP, modules, imports)

✅ Clean project structuring (src/ layout)

✅ Virtual environments & dependency management

✅ AI agent design pattern (Reasoning → Action → Memory)

✅ Error handling & graceful fallback strategies

✅ Production-style logging configuration


# 🚀 Future Improvements

- Persist memory using file or database
- Multi-step planning agent
- Web interface (Streamlit / FastAPI)
- Automated tests
- Dockerization


# 👤 Author

Richard Tun

GitHub: https://github.com/richardtun
