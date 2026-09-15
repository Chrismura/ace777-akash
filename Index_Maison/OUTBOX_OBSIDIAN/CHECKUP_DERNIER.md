# Checkup garage — 20260915T0537Z

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
36516 /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python scripts/paper_diprip.py --resume

### MATCH: digest_watch
1122 /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python scripts/digest_watch.py --live

### MATCH: ollama serve
1243 /Applications/Ollama.app/Contents/Resources/ollama serve

### MATCH: caffeinate ACE
84305 caffeinate -is python3 /Users/christophe/ace777-test-day1/Index_Maison/scripts/v2_confirmation_live.py
```

## 3 — Fichiers PID / cœur RAM

- absent OK : `runs/master.pid`
- absent OK : `runs/nuit_ghost_loop.pid`
- absent OK : `/tmp/alpha_heartbeat.txt`
- `/tmp/ace777_ram_exchange` absent (sera recréé au prochain run)

## 4 — Fichiers STOP (au repos = OK s’ils existent)
- manquant `STOP` (à `touch` avant pre-run)
- OK `STOP_ALPHA`
- OK `STOP_BETA`

## 5 — Champion
- OK genesis md5=`14bcf868d46effba010cac577cbb004c` (préfixe 14bcf868d46effba010cac577cbb004c — source de vérité CHAMPION_ACTIF)

## 6 — RAM Mac
- approx libre : **239 Mo**
- RAM=TIGHT
- → déconseillé pour ACE (mieux ≥400 Mo)

## 7 — Top process RAM (info)

```
  1801 Mo  pid=34134  /Users/christophe/.config/manicode/freebuff
   313 Mo  pid=30429  /Applications/Brave
   122 Mo  pid=16474  /Applications/Brave
    98 Mo  pid=30401  /Applications/Brave
    70 Mo  pid=47541  /Users/christophe/.config/manicode/freebuff
    67 Mo  pid=1795  /Applications/Brave
    67 Mo  pid=540  /System/Library/Frameworks/CoreServices.framework/Frameworks/Metadata.framework/Versions/A/Support/mds_stores
    63 Mo  pid=30413  /Applications/Brave
    57 Mo  pid=35795  /Applications/Brave
    51 Mo  pid=68617  /Applications/Brave
```

## 8 — Cockpit indicateurs (zone test)

```
=== COCKPIT HYGIÈNE (indicateurs) ===

1) Thermo free (Binance public)
[SDI] Calcul en cours...
  [SDI] fetch error https://api.blockchain.info/charts/utxo-pool-value?timespan=30days&format=json: HTTP Error 404: Not Found
[SDI] SDI=0.008 | IPT=0.46 | RBF=0.0 | Alertes=1
[HEALTH] Calcul en cours...
  Score: 0.9 | Mode: ✅ NOMINAL | Issues: 1 | Mult: ×1.0
    ⚠️ google_news: source non vérifiable en direct (alimentée par sniffer) → DOWN
✅ Modèle chargé depuis le disque
[INDICE] score=0.3641 niveau=attention
THERMO_OK climate=ok score=85
THERMO_LIVE /Users/christophe/ace777-test-day1/Index_Maison/thermo/live.json
FUNDING now=8.1e-05 avg30=6.655e-05 prevMonth=6.695e-05
THERMO=OK

2) Mission feed (CSV / Hulk / thermo → mission.json)
SAISON : CALME 🧊 — hiver, ADA dort.
Alignement : 0 haussiers / 2 baissiers.
Scan termine : 0 nouveaux evenements (session depuis 2026-09-09T00:00:00Z)
MISSION_OK combo=0.7028 cycle=5612 alert=nominal since=2026-09-09T00:00Z
  ALPHA fills=7 pnl=-1.9655 (life fills=14 pnl=-1.7804)
  BETA  fills=34 pnl=2.6683 (life fills=71 pnl=2.6828)
  HULK  trades=7 seeds=3 house_bags=0 cash=3 pnl=13.9098
MISSION_FEED=OK

3) Pont Cortana :17777
BRIDGE=OK
{"muted": false, "ok": true, "port": 17777, "bridge": "cortana+mission", "pont": "ON", "ace": {"state": "OFF", "label": "OFF", "ageSec": 476355, "run": "MASTER_BASE_V8_6_FORTRESS_8H20", "live": "MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log"}, "net": {"state": "OK", "label": "OK", "ms": 366}}

4) Indicateurs clés (mission.json + live.json)
  OK  live.funding=8.1e-05
  OK  live.oi=104176.538
  OK  live.fearGreed=69
  OK  live.score=85 climate=ok
  OK  mission.run=MASTER_BASE_V8_6_FORTRESS_8H20
  OK  mission.comboPnl=0.7028
  OK  thermo.indicators n=7
  WARN  LIQ/ETF free flaky — liq=2900591.0 etf_btc=-59.97
INDICATEURS=OK

COCKPIT_HYGIENE=OK
```

## Verdict global
**CHECKUP=NOK** — fantôme / PID / stérilité à traiter avant GO.
