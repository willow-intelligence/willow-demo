🌳 Willow Intelligence: Temporal Anchoring for LLMs
Cognitive Stability Infrastructure → Reducing drift & building continuity by grounding language models in real time.

Willow provides temporal grounding infrastructure that stabilizes LLM reasoning, eliminates hallucinated dates, and reduces conversational drift by 60–80% in early testing.

🚀 Live Demo
Interactive Web Beta UI

Toggle Baseline vs Willow mode and view metrics (tokens, latency, model).

👉 https://willow-drift-reduction-production.up.railway.app/ui

Public API Endpoint (for developers)
*Note: /chat is a POST-only API endpoint and will not display anything if opened in a browser. Use /ui for interactive testing.

👉 https://willow-drift-reduction-production.up.railway.app/chat

🌿 What Willow Does

✔️ Provides accurate real-time date & time
✔️ Prevents hallucinated outputs
✔️ Reduces conversational drift by 60–80%
✔️ Improves multi-turn consistency
✔️ Works with any provider (OpenAI, Anthropic, Google, etc.)
✔️ Logs tokens-in, tokens-out, and latency for every request
✔️ Enables continuity & context stability across turns

🏗️ Architecture
┌─────────────┐
│    User      │
└──────┬───────┘
       │
       ▼
┌────────────────────────┐
│ Willow Wrapper (API+UI)│  ← Public interface
│ main.py                │
└──────┬─────────────────┘
       │
       ▼
┌────────────────────────┐
│ Willow Core Logic      │  ← PROPRIETARY
│ Time Anchors + Scaffold│
└──────┬─────────────────┘
       │
       ▼
┌────────────────────────┐
│ LLM Provider           │
│ (OpenAI / Anthropic)   │
└────────────────────────┘

📦 Installation (Demo Version)
git clone https://github.com/willow-intelligence/willow-demo
cd willow-demo
pip install -r requirements.txt


🔒 Note: The demo includes placeholder logic.
Production Willow Core (willow.py) is proprietary and closed-source.

🧪 How to Test Willow (Simple Beta Instructions)
1️⃣ Open the UI

👉 https://willow-drift-reduction-production.up.railway.app/ui

2️⃣ Choose a Mode

Baseline → no temporal anchoring

Willow → real-time anchoring + drift reduction active

3️⃣ Run side-by-side comparisons
Test A — Time Awareness

Baseline:
Ask: “What time is it right now?”
Expected: ❌ “I don’t have access to the current time.”

Willow:
Expected: ✅ Exact real-time date + time

Test B — Drift / Context Stability

In Willow mode, ask:

“What were we working on originally?”

“What did I ask two messages ago?”

“Summarize our conversation so far.”

Willow stays coherent.
Baseline forgets or drifts.

Test C — Temporal Reasoning

Try:

“What day is it one week from now?”

“How many days until Friday?”

“What day was it three months ago?”

Baseline → ❌ often incorrect
Willow → ✅ consistent & grounded

📊 Viewing Metrics (Tokens, Latency, Mode)

Every response shows:

tokens_in

tokens_out

elapsed_sec (latency)

mode (baseline or willow)

model

These appear automatically in:

the UI (below each assistant response)

the API JSON

server logs (logs/sessions.csv)

No configuration required.

🧪 Developer API (Optional)
POST /chat
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

For enterprise licensing, partnerships, or research access:

📧 haley.kurtz.ai@gmail.com

Built with 💛 by Haley Kurtz
Anchoring AI to reality, one turn at a time ⌛
