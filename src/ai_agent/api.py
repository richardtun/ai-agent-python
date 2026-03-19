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
