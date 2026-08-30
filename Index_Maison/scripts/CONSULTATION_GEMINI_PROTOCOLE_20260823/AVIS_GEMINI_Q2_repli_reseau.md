# AVIS GEMINI · Q2_repli_reseau (NaraRouter (7M tokens/jour gratuits) · 91s)

Q2 :
Cadence : 1 appel/2s, jitter ±30 %, 90 req/min. Faiblesse : ban rapide. Garde-fou : backoff 2/4/8/16s dès 429.
Repli : 3 sources, bascule après 2 échecs ou RTT>1500ms. Faiblesse : panne commune. Garde-fou : quorum 2/3.
Anti-blocage : timeout socket inopérant : socket non-bloquant, connect 800ms, TLS 1200ms, lecture 2000ms, Happy Eyeballs IPv4/IPv6. Faiblesse : faux positifs. Garde-fou : sonde témoin.
Run max : 25s, arrêt dur.
