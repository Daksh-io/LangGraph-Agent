# Step1: Setup Pydantic Model (Schema Vaildation)
from agent import system_prompt
from aiohttp.hdrs import ALLOW
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    messages: List[str]
    allow_search: bool

# Step2: Setup AI Agent from Frontend Request.

from fastapi import FastAPI
from agent import get_response_from_ai_agent

ALLOW_MODEL_NAMES=["gpt-4o-mini", "llama-3.3-70b-versatile"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the ChatBot using LangGraph and search tools.
    It dynmically selects the model specified in the requset

    """
    if requset.model_name not in ALLOW_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a vaild AI model"}

    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response from it!
    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response

# Step3: Run app & explore Swagger UI Docs.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)

































