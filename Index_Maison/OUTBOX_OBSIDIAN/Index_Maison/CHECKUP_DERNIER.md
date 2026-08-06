# Checkup garage — 20260801T0722Z

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
35162 /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python scripts/paper_diprip.py

### MATCH: ollama serve
975 /Applications/Ollama.app/Contents/Resources/ollama serve

```

## 3 — Fichiers PID / cœur RAM

- absent OK : `runs/master.pid`
- absent OK : `runs/nuit_ghost_loop.pid`
- absent OK : `/tmp/alpha_heartbeat.txt`
- `/tmp/ace777_ram_exchange` existe (0 fichiers)

## 4 — Fichiers STOP (au repos = OK s’ils existent)
- OK `STOP`
- OK `STOP_ALPHA`
- OK `STOP_BETA`

## 5 — Champion
- OK genesis md5=`37fca36712d49aa8b97890c5cad5f2e6` (préfixe 37fca367)

## 6 — RAM Mac
- approx libre : **171 Mo**
- RAM=CRITIQUE
- → pas de GO trading tant que RAM critique

## 7 — Top process RAM (info)

```
   534 Mo  pid=603  /Applications/Cursor.app/Contents/Frameworks/Cursor
   199 Mo  pid=53323  /System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent
   189 Mo  pid=57158  /Applications/Obsidian.app/Contents/Frameworks/Obsidian
   180 Mo  pid=35304  /System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent
   133 Mo  pid=436  /Applications/Cursor.app/Contents/MacOS/Cursor
   133 Mo  pid=474  /System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal
   127 Mo  pid=53057  /System/Library/Services/AppleSpell.service/Contents/MacOS/AppleSpell
   121 Mo  pid=53283  /Applications/Cursor.app/Contents/Frameworks/Cursor
   118 Mo  pid=466  /Applications/Brave
   111 Mo  pid=57114  /Applications/Obsidian.app/Contents/MacOS/Obsidian
```

## 8 — Cockpit indicateurs (zone test)

```
=== COCKPIT HYGIÈNE (indicateurs) ===

1) Thermo free (Binance public)
THERMO_OK climate=warn score=62
THERMO_LIVE /Users/christophe/ace777-test-day1/Index_Maison/thermo/live.json
FUNDING now=3.7e-05 avg30=6.081e-05 prevMonth=6.067e-05
THERMO=OK

2) Mission feed (CSV / Hulk / thermo → mission.json)
MISSION_OK combo=0 cycle=46 alert=nominal since=2026-07-31T19:06Z
  ALPHA fills=0 pnl=0.0 (life fills=251 pnl=167.4037)
  BETA  fills=0 pnl=0.0 (life fills=4688 pnl=16.8069)
  HULK  bags=3 pnl=0.0
MISSION_FEED=OK

3) Pont Cortana :17777
BRIDGE=OK
{"muted": false, "ok": true, "port": 17777, "bridge": "cortana+mission", "pont": "ON", "ace": {"state": "OFF", "label": "OFF", "ageSec": 44164, "run": "NUAGE_PROD_4H", "live": "NUAGE_PROD_4H_LIVE_COLOR.log"}, "net": {"state": "SLOW", "label": "SLOW", "ms": 436}}

4) Indicateurs clés (mission.json + live.json)
  OK  live.funding=3.7e-05
  OK  live.oi=109161.22
  OK  live.fearGreed=27
  OK  live.score=62 climate=warn
  OK  mission.run=NUAGE_PROD_4H
  OK  mission.comboPnl=0
  OK  thermo.indicators n=7
  WARN  LIQ/ETF free flaky — liq=None etf_btc=None
INDICATEURS=OK

COCKPIT_HYGIENE=OK
```

## Verdict global
**CHECKUP=NOK** — fantôme / PID / stérilité à traiter avant GO.
