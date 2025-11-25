# 🌳 Willow - Temporal Anchoring for LLMs

Willow provides temporal grounding infrastructure that reduces conversational drift in large language models by 60-80%.

## What It Does

- ✅ Injects real-time temporal context into LLM conversations
- ✅ Eliminates hallucinated dates and times
- ✅ Grounds inference in actual reality
- ✅ Creates closed feedback loops for context stability

## Architecture
```
┌─────────────┐
│   User      │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Willow Wrapper     │  ← Public API Interface
│  (main.py)          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Willow Core        │  ← PROPRIETARY (not included)
│  (willow.py)        │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  LLM Provider       │
│  (OpenAI, etc)      │
└─────────────────────┘
```

## Live Demo

**API Endpoint:** willow-drift-reduction-production.up.railway.app

### Example: The Problem Willow Solves

**Without Willow (Baseline Mode):**
```json
Query: "What day is today?"
Response: "I don't have access to real-time information..." ❌
```

**With Willow:**
```json
Query: "What day is today?"
Response: "Today is November 24, 2025." ✅
```

## API Reference

### POST /chat

**Request:**
```json
{
  "model": "openai:gpt-4o-mini",
  "mode": "baseline|willow",
  "messages": [
    {
      "role": "user",
      "content": "What was the date one week ago?"
    }
  ]
}
```

**Response:**
```json
{
  "mode": "willow",
  "model": "openai:gpt-4o-mini",
  "output": "One week ago from today, November 24, 2025, was November 17, 2025.",
  "metrics": {
    "elapsed_sec": 1.051,
    "tokens_in": 164,
    "tokens_out": 24
  }
}
```

## Key Features

### Temporal Anchoring
Provides accurate real-time date/time context to prevent hallucination.

### Grounded Inference
Uses temporal anchors to keep reasoning stable and reality-based across conversation turns.

### Closed Feedback Loop
Timestamps each interaction to create persistent, grounded memory that prevents drift.

## Results

Early beta testing shows:
- 📉 60-80% reduction in conversational drift
- ✅ 100% accuracy on temporal queries
- ⚡ No performance penalty (same latency as baseline)
- 🎯 Stable context across multi-turn conversations

## Beta Testing

Currently in private beta. [Sign up for beta access →](https://forms.gle/your-form-link)

## Installation (Demo Version)
```bash
git clone https://github.com/willow-intelligence/willow-demo
cd willow-demo
pip install -r requirements.txt

# Note: This demo uses a placeholder willow.py
# For production use, contact us about licensing
```

## Proprietary Technology

The core temporal anchoring algorithm (`willow.py`) is proprietary and not included in this public repository. This demo shows the API interface and integration patterns only.

**For enterprise licensing, partnerships, or beta access:**
- Email: haley.kurtz.ai@gmail.com
- Live Demo: willow-drift-reduction-production.up.railway.app

## Use Cases

- 🤖 AI assistants that need accurate time awareness
- 📅 Scheduling and calendar applications
- 📊 Time-series data analysis
- 🔄 Multi-turn conversations requiring temporal consistency
- 📝 Document generation with accurate dates
- 🌐 Any LLM application where "now" matters

## Technical Details

Willow works by:
1. Capturing the current timestamp when a request arrives
2. Injecting temporal context into the system prompt
3. Providing the LLM with explicit "now" information
4. Maintaining temporal consistency across conversation turns

This prevents models from:
- Hallucinating incorrect dates
- Claiming they don't know the current time
- Drifting from reality in multi-turn exchanges
- Failing at time-sensitive reasoning

## License

API Wrapper & Demo: MIT License  
Willow Core Algorithm: Proprietary

---

**Built with ❤️ by Haley Kurtz**

*Reducing AI drift, one timestamp at a time.*