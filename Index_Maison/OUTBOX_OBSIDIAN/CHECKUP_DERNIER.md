# Checkup garage — 20260814T1056Z

**But :** détecter process fantômes / PID orphelins / état Mac avant tout GO.

Références :
- `plaintes/PROTOCOLE_STERILITE_BINAIRE_20260714.md` (protocole officiel)
- `scripts/verif_sterilite.sh`
- `ERREURS_AI/RAPPORT_IA_FANTOME_3_POINTS.md` (phénomènes IA fantôme)
- `hulk-mexc/docs/PROTOCOLE_GHOST.md` (watchdog Hulk « Ghost » ≠ parasite ACE)

## 1 — Stérilité ACE
STERILE=OK
- Verdict : **STERILE=OK**

## 2 — Chasse aux fantômes (pgrep élargi)

```
### MATCH: paper_diprip
68481 /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python scripts/paper_diprip.py

### MATCH: ollama serve
1149 /Applications/Ollama.app/Contents/Resources/ollama serve

```

## 3 — Fichiers PID / cœur RAM

- absent OK : `runs/master.pid`
- absent OK : `runs/nuit_ghost_loop.pid`
- absent OK : `/tmp/alpha_heartbeat.txt`
- `/tmp/ace777_ram_exchange` absent (sera recréé au prochain run)

## 4 — Fichiers STOP (au repos = OK s’ils existent)
- OK `STOP`
- OK `STOP_ALPHA`
- OK `STOP_BETA`

## 5 — Champion
- **FAIL** genesis md5=`d6977337a13e14c7867df6a832467d36`

## 6 — RAM Mac
- approx libre : **136 Mo**
- RAM=CRITIQUE
- → pas de GO trading tant que RAM critique

## 7 — Top process RAM (info)

```
  1419 Mo  pid=77196  /Users/christophe/.config/manicode/freebuff
   226 Mo  pid=37993  /Applications/Obsidian.app/Contents/Frameworks/Obsidian
   142 Mo  pid=75882  /Applications/Brave
   120 Mo  pid=37989  /Applications/Obsidian.app/Contents/MacOS/Obsidian
   102 Mo  pid=606  /System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal
    84 Mo  pid=542  /System/Library/Frameworks/CoreServices.framework/Frameworks/Metadata.framework/Versions/A/Support/mds_stores
    73 Mo  pid=75900  /Applications/Brave
    67 Mo  pid=80178  /Users/christophe/.config/manicode/freebuff
    61 Mo  pid=75921  /Applications/Brave
    59 Mo  pid=99666  /System/Applications/Stocks.app/Contents/PlugIns/StocksWidget.appex/Contents/MacOS/StocksWidget
```

## 8 — Cockpit indicateurs (zone test)

```
=== COCKPIT HYGIÈNE (indicateurs) ===

1) Thermo free (Binance public)
THERMO_OK climate=warn score=68
THERMO_LIVE /Users/christophe/ace777-test-day1/Index_Maison/thermo/live.json
FUNDING now=1.3e-05 avg30=5.464e-05 prevMonth=6.081e-05
THERMO=OK

2) Mission feed (CSV / Hulk / thermo → mission.json)
SAISON : CHAUFFE 🌡️ — température warn, bassin long.
Alignement : 2 haussiers / 1 baissiers.
Le vortex tourne fort (-1.33 % sur 24h) — le mouvement est là.
Scan termine : 0 nouveaux evenements (session depuis 2026-08-14T10:32:00Z)
MISSION_OK combo=0.563 cycle=147 alert=amber since=2026-08-14T10:32Z
  ALPHA fills=0 pnl=0.0 (life fills=635 pnl=115.6724)
  BETA  fills=15 pnl=0.563 (life fills=2328 pnl=10.9587)
  HULK  bags=6 pnl=-1.2234
MISSION_FEED=OK

3) Pont Cortana :17777
BRIDGE=OK
{"muted": true, "ok": true, "port": 17777, "bridge": "cortana+mission", "pont": "ON", "ace": {"state": "OFF", "label": "OFF", "ageSec": 271, "run": "MASTER_VORTEX_V2_COLLAB_4H", "live": "MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log"}, "net": {"state": "SLOW", "label": "SLOW", "ms": 467}}

4) Indicateurs clés (mission.json + live.json)
  OK  live.funding=1.3e-05
  OK  live.oi=113483.391
  OK  live.fearGreed=29
  OK  live.score=68 climate=warn
  OK  mission.run=MASTER_VORTEX_V2_COLLAB_4H
  OK  mission.comboPnl=0.563
  OK  thermo.indicators n=7
  WARN  LIQ/ETF free flaky — liq=21109999.0 etf_btc=-81.61
INDICATEURS=OK

COCKPIT_HYGIENE=OK
```

## Verdict global
**CHECKUP=NOK** — fantôme / PID / stérilité à traiter avant GO.
