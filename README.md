<div align="center">

## 🌿 Willow Intelligence

**Temporal anchoring that stabilizes LLM reasoning**

Reduces conversational drift by 60–80% by grounding models in real-time context.

*Hallucinations are a symptom. Drift is a disease. Willow is the cure.*

[Try the Live Demo](https://willow-drift-reduction-production.up.railway.app/ui) · [API Docs](https://willow-drift-reduction-production.up.railway.app/chat)

</div>

## Background

LLMs hallucinate dates, lose track of conversation context, and get basic facts incorrect. Drift costs enterprises millions in oversight, correction, and failed deployments.

Willow injects temporal anchoring and proper context analyzation into any LLM request resulting in accurate timestamps, conversation continuity, and context stability. The model stays grounded instead of drifting.

Hallucinations are a symptom. Drift is a disease. Willow is the cure. 

## Quick Test

Go to the [Live Demo](https://willow-drift-reduction-production.up.railway.app/ui) and try these:

**Test 1: Time Awareness**
"What time is it right now?"

- Baseline: "I cannot access real-time information"
- Willow: Returns correct date and time

**Test 2: Temporal Reasoning**
"What was the date one week ago?"

- Baseline: Guesses or refuses
- Willow: Calculates accurately

**Test 3: Continuity**
"What were we just talking about?"

- Baseline: Forgets or drifts
- Willow: Maintains context

## For Developers

```bash
curl -X POST "https://willow-drift-reduction-production.up.railway.app/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai:gpt-4o-mini",
    "mode": "willow",
    "messages": [{ "role": "user", "content": "What day is it?" }]
  }'
```

## Works With

ChatGPT · Claude · Gemini · Any LLM provider

## Contact

📧 haley.kurtz.ai@gmail.com

<div align="center">

Built with 💛 by Haley Kurtz


Anchoring AI to reality, one turn at a time ⌛

</div>
