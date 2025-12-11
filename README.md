##**🌳 WILLOW INTELLIGENCE**
<h3 align="center">Cognitive Stability Infrastructure</h3> <p align="center">Reducing drift & building continuity by grounding language models in real time.</p>

Willow provides temporal grounding infrastructure that stabilizes LLM reasoning, eliminates hallucinated dates and times, and reduces conversational drift by 60–80% in early testing.

**✨ Live Demo: Interactive Web Beta UI:**

Toggle Baseline vs Willow mode with metrics (tokens, latency, model).

👉 https://willow-drift-reduction-production.up.railway.app/ui

**Public API Endpoint (for developers):**
*Note: /chat is a POST-only API endpoint & will not load in browser. Use the /ui link above for interactive testing.

👉 https://willow-drift-reduction-production.up.railway.app/chat

**What Willow Does:**

✔️ Provides accurate real-time date & time

✔️ Prevents hallucinated system-time disclaimers

✔️ Reduces conversational drift by 60–80%

✔️ Improves multi-turn consistency

✔️ Works with any provider (OpenAI, Anthropic, Google, etc.)

✔️ Logs tokens-in, tokens-out, and latency for every request

✔️ Enables continuity & stable reasoning over long conversations


**Architecture:**
        ┌───────────────┐
        │     User       │
        └───────┬────────┘
                │
                ▼
┌──────────────────────────────────────┐
│ Willow Wrapper (API + UI)            │   ← Public interface (FastAPI)
│ main.py                              │
└───────────────┬──────────────────────┘
                │
                ▼
┌──────────────────────────────────────┐
│ Willow Core Logic                    │   ← PROPRIETARY (willow.py)
│ Temporal Anchors + Scaffold          │
└───────────────┬──────────────────────┘
                │
                ▼
┌──────────────────────────────────────┐
│ LLM Provider (OpenAI / Anthropic)    │
└──────────────────────────────────────┘


**How to Test Willow (Quick Guide):**

Open the UI:
👉 https://willow-drift-reduction-production.up.railway.app/ui

1️⃣ Select a Mode

Baseline → normal LLM behavior

Willow → temporal anchoring 

2️⃣ Test A: Time Awareness

Baseline mode:
Ask: "What time is it right now?"
→ ❌ Will say it cannot access real-time information.

Willow mode:
Ask the same question.
→ ✅ Willow returns the correct real-time date + time.

3️⃣ Test B: Drift / Continuity

Ask in Willow mode:

“What were we working on originally?”

“What was my previous task?”

“Summarize our conversation so far.”

Expected: Willow maintains continuity.
Baseline: Often forgets context or drifts.

4️⃣ Test C: Temporal Reasoning

Try:

“What day is it one week from now?”

“How many days until Friday?”

“What day was it three months ago?”

Willow returns accurate results across all temporal shifts.

📊 Viewing Technical Metrics (For Reviewers)

Every API response includes:

tokens_in

tokens_out

elapsed_sec (latency)

mode (baseline or willow)

model

These appear in:

The UI chat bubbles

The JSON responses

The server logs (sessions.csv)

No configuration required.

🧑‍💻 Developer API Usage (Optional)

POST /chat

Request:

{
  "model": "openai:gpt-4o-mini",
  "mode": "willow",
  "messages": [
    { "role": "user", "content": "What was the date one week ago?" }
  ]
}


Response:

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

📦 Installation (Demo Version)
git clone https://github.com/willow-intelligence/willow-demo
cd willow-demo
pip install -r requirements.txt


Note:
This repo contains a demo wrapper.
The Willow Core Algorithm (willow.py) is proprietary and not included.

For enterprise licensing, partnerships, or research access:
📧 haley.kurtz.ai@gmail.com

Built with 💛 by Haley Kurtz
Anchoring AI to reality, one turn at a time ⌛
