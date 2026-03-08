# Session Contre-Predation

Objectif:
- Tester une execution plus agressive en regime de chasse aux stops.
- Mesurer si ACE777 capte mieux l'impulsion sans se faire sortir en retard.

## Hypothese

- Entrer plus tot (confiance radar moins stricte).
- Sortir vite quand l'impulsion ralentit.
- Garder une protection locale plus reactive.

## Attention importante

- Dans ce script, le stop est deja gere en logique locale (pas d'OCO place dans le carnet).
- Donc l'idee "stop fantome" est deja en grande partie vraie.

## Variables proposees (corrigees pour ce script)

- `RADAR_MIN_CONF=0.88`
- `MIN_PROFIT_BPS=40`
- `STOP_LOSS_BPS=22`
- `TRAIL_ARM_BPS=15`
- `TRAIL_GIVEBACK_BPS=3`
- `T_BASE=300`
- `K_ENTROPY=0.03`
- `STALL_CONFIRMATIONS=5`
- `BUY_USDT=550`
- `CYCLES=20`
- `SLEEP_SEC=3`

## Comparaison a faire

- Baseline harmonique vs contre-predation
- Nombre de trades executes
- Ratio gains/pertes
- Distribution des `exitReason`
- Impact des sorties rapides (`exit_stall` / `trailing_stop`)
