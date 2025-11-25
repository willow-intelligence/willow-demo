from pydantic import BaseModel, Field
from typing import List, Literal, Dict, Any

class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class ChatIn(BaseModel):
    model: str = Field(..., description="e.g., openai:gpt-4o-mini")
    mode: Literal["baseline", "willow"]
    messages: List[Message]

class ChatOut(BaseModel):
    mode: str
    model: str
    output: str
    metrics: Dict[str, Any]