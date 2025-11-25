import os
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from .schemas import ChatIn, ChatOut

# Load environment variables
load_dotenv()

# --- FastAPI Setup ---
APP = FastAPI(
    title="Willow Demo - Temporal Anchoring API",
    description="Demo interface for Willow's temporal grounding technology",
    version="1.0.0"
)

# Setup CORS middleware
APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Health Check Routes ---
@APP.get("/")
async def root():
    """Root endpoint - health check"""
    return {
        "message": "Willow Demo API - Temporal Anchoring for LLMs",
        "status": "online",
        "version": APP.version,
        "note": "This is a demonstration API. Core algorithm is proprietary."
    }

@APP.get("/health")
def health():
    return {"status": "ok", "version": APP.version}


# --- Chat Endpoint ---
@APP.post("/chat", response_model=ChatOut)
async def chat(inp: ChatIn):
    """
    Demo chat endpoint.
    
    Note: This demo version shows the API interface only.
    The proprietary Willow temporal anchoring algorithm is not included.
    
    For access to the full implementation, contact: haley.kurtz.ai@gmail.com
    """
    
    return ChatOut(
        mode=inp.mode,
        model=inp.model,
        output="This is a demo API. The proprietary Willow algorithm is not included in this public repository. Contact haley.kurtz.ai@gmail.com for enterprise licensing.",
        metrics={
            "elapsed_sec": 0.0,
            "tokens_in": 0,
            "tokens_out": 0,
        }
    )