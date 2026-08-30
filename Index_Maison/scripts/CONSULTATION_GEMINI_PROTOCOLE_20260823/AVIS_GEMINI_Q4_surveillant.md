# AVIS GEMINI · Q4_surveillant (NaraRouter (7M tokens/jour gratuits) · 91s)

Canari mort-d : écrire JSON ts, PID, hash config dans /ace777/watchdog/heartbeat.json. Âge max 60s. Relu toutes 20s par sonde externe indépendante. Faiblesse : sonde meurt. Garde-fou : double relecteur cron distant + systemd local ; alerte si absent, >60s, hash changé, aucune relecture depuis 120s.
