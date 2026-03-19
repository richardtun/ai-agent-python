from fastapi import FastAPI
from pydantic import BaseModel

from ai_agent.agent.agent import AIAgent
# from ai_agent.logger import setup_logger


# Setup
# setup_logger()
app = FastAPI(title="AI Task Agent API")

agent = AIAgent()


# ===== Request / Response models =====
class AgentRequest(BaseModel):
    message: str


class AgentResponse(BaseModel):
    response: str


# ===== API endpoint =====
@app.post("/agent", response_model=AgentResponse)
def run_agent(req: AgentRequest):
    result = agent.run(req.message)
    return AgentResponse(response=result)


class TasksResponse(BaseModel):
    tasks: list[str]

@app.get("/tasks", response_model=TasksResponse)
def get_tasks():
    tasks = agent.get_tasks()
    return TasksResponse(tasks=tasks)


class ResetResponse(BaseModel):
    status: str
    message: str


@app.post("/reset", response_model=ResetResponse)
def reset_agent():
    agent.reset()
    return ResetResponse(
        status="ok",
        message="Agent state has been reset"
    )
