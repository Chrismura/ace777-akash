# Hulk × MEXC — dip & rip (dossier séparé)

**But :** watchlist CMC [The Hulk Crypto Portfolio Picks](https://coinmarketcap.com/watchlist/68f096217962d710267cb472/) → trader sur **MEXC** : acheter les descentes, revendre les remontées / spikes.

**Hors scope :** ACE777 NUAGE / genesis champion (`ace777-test-day1` racine) — **jamais modifié** depuis ce dossier.

## Idée marché

Beaucoup de paires Hulk = **peu liquides** mais **gros spikes**.  
→ Opportunité de % élevés, **et** risque : slippage, gap, impossible de sortir.  
On filtre : volume mini + spread max, tout en gardant les candidats « spike ».

## Arborescence

```
hulk-mexc/
  README.md
  config/          # seuils, clés (env), mode paper/live
  data/            # univers, snapshots liquidité
  docs/            # plan, règles stratégie
  scripts/         # inventaire MEXC, paper tests
  runs/            # logs / CSV tests
```

## Phases

| Phase | Contenu | Statut |
|-------|---------|--------|
| 0 | Dossier + univers CMC Hulk | **ici** |
| 1 | Inventaire MEXC (paire USDT + volume 24h) | scripts |
| 2 | Paper : règles dip/rip simples | à faire |
| 3 | Testnet / petit live MEXC | plus tard |

## Commandes utiles

```bash
cd /Users/christophe/ace777-test-day1/hulk-mexc

# 1) Rafraîchir liquidité MEXC
python3 scripts/inventory_mexc.py

# 2) Stop l'ancien paper puis paper v1.5 — TON terminal (PISTE A)
touch STOP_PAPER   # si l'ancien tourne encore
# Ctrl+C sur l'ancien process, puis :
rm -f STOP_PAPER
python3 scripts/paper_diprip.py
# Au boot : SEED ~20$ en tokens (config SEED_*) pour tester aussi les VENTES baissières.

# 3) Veille — AUTRE terminal (PISTE B) — LIVE direct (pas de pause 60s)
python3 scripts/digest_watch.py --live
# enchaîne les scans ; écrit ALERT seulement si signal nouveau
# stop : touch STOP_DIGEST

# Clés MEXC (optionnel, plus tard live) — hors repo
# cp config/mexc.env.example ~/.mexc.env && chmod 600 ~/.mexc.env
```

Pistes séparées : `docs/TRACKS_SEPARES.md` · Confrontation : `docs/CONFRONTATION.md` · Veille : `docs/VEILLE_QWEN.md`.  
**Protocole Ghost** (watchdog 30 min) : `docs/PROTOCOLE_GHOST.md` · `scripts/watchdog_hulk_ghost.sh`.
