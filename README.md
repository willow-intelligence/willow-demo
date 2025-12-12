# **Willow Intelligence**
Cognitive Stability Infrastructure for LLMs

Reducing drift and building continuity with temporal grounding infrastructure that stabilizes LLM reasoning, eliminates hallucinationss, and reduces conversational drift by 60–80% in early testing.

**Live Demo - Interactive Web Beta UI:**

*Toggle Baseline vs Willow mode and view metrics (tokens, latency, model)*

👉 https://willow-drift-reduction-production.up.railway.app/ui

**Public API Endpoint (for developers):**
*Note: /chat is a POST-only endpoint and will not load in a browser.*

👉 https://willow-drift-reduction-production.up.railway.app/chat

**What Willow Does:**

-Provides accurate real-time date & time
-Prevents hallucinated system-time errors
-Reduces conversational drift by 60–80%
-Improves multi-turn consistency
-Works with any provider (OpenAI, Anthropic, Google, etc.)
-Logs tokens-in, tokens-out, and latency for every request
-Enables continuity & stable reasoning over long conversations



**How to Test Willow (Quick Guide):**
1. Select a Mode

Baseline → normal model behavior
Willow → temporal anchoring 

2. Test A: Time Awareness

Ask: “What time is it right now?”

Baseline mode:
❌ Model will say it cannot access real-time information.

Willow mode:
✔ Returns the correct real-time date + time.

3. Test B: Drift & Continuity

Ask:
“What were we working on originally?”
“What was my previous task?”
“Summarize our conversation so far.”

Willow maintains continuity.
Baseline forgets or drifts.

4. Test C: Temporal Reasoning

Try:
“What day is it one week from now?”
“How many days until Friday?”
“What day was it three months ago?”

Willow returns accurate results across temporal shifts.


**Developer API Example (Optional):**

POST /chat

{
  "model": "openai:gpt-4o-mini",
  "mode": "willow",
  "messages": [
    { "role": "user", "content": "What was the date one week ago?" }
  ]
}


Response Example:

{
  "mode": "willow",
  "model": "openai:gpt-4o-mini",
  "output": "...",
  "metrics": {
    "elapsed_sec": 1.051,
    "tokens_in": 164,
    "tokens_out": 24
  }
}

**Installation (Demo Version):**
git clone https://github.com/willow-intelligence/willow-demo
cd willow-demo
pip install -r requirements.txt


Note: This repo contains a demo wrapper.
The Willow Core Algorithm (willow.py) is proprietary and not included.

For licensing, partnerships, or research access:
📧 haley.kurtz.ai@gmail.com

Built with 💛 by Haley Kurtz
Anchoring AI to reality, one turn at a time ⌛
