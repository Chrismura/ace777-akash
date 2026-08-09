# 🥊 BATTERIE A/B — modèles Puter vs deepseek-ai/deepseek-v4-flash-0731 — 2026-08-09

| Modèle | Verdict | Preuve |
|---|---|---|
| openai/gpt-5.4 | **PIRE** | PIRE - trois risques demandés, deux fournis. |
| claude-sonnet-4-5 | **EGAL** | EGAL - Deux risques et parades équivalents. |
| google/gemini-3-flash | **INACCESSIBLE** | HTTP 400 {"error":"Model not found: google/gemini-3-flash","message":"Model not  |
| deepseek/deepseek-v4-pro | **INACCESSIBLE** | reponse vide |
| x-ai/grok-4.20 | **INACCESSIBLE** | HTTP 402 {"error":"No usage left for request.","message":"No usage left for requ |

> Aucun modèle n'a battu la référence -> grok-4.3 (EGAL, accessible) est le seul branché,
> comme complément de résilience (famille différente). Auto-éval quotidienne les re-teste.