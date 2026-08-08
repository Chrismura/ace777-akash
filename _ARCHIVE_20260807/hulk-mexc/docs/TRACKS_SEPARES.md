# Deux pistes Hulk — séparées volontairement

## Pourquoi séparer ?

Pour la fin des tests, on veut savoir **qui a mieux anticipé** :
- le **bot paper** (règles froides), ou
- la **veille Qwen** (lecture humaine + digest).

Si on les couple trop tôt, on ne sait plus qui a eu raison.

## PISTE A — Hulk paper (exécution)

```bash
cd /Users/christophe/ace777-test-day1/hulk-mexc
rm -f STOP_PAPER
python3 scripts/paper_diprip.py
```

- Autonome : régimes, mise→2×→bag, volume, sense  
- Preuves : `runs/PAPER_V1_*.csv` + `*_state.json`  
- **Ne lit pas** Qwen / digest  

## PISTE B — Veille / Qwen (anticipation)

```bash
# Une fois
python3 scripts/digest_watch.py

# LIVE direct — AUTRE terminal (enchaîne dès que le scan MEXC finit)
python3 scripts/digest_watch.py --live
# stop : touch STOP_DIGEST
```

- **Pas branché en websocket** : Qwen n’a pas MEXC en direct ; ce script = ses yeux en boucle  
- Délai réel ≈ temps de scan (~20–40s), **plus** de pause artificielle 60s/1800s  
- N’écrit un appel que si **signal nouveau**  
- `DIGEST_LATEST.md` · `VEILLE_ALERT.md` · `VEILLE_CALLS.jsonl` · notes Qwen  

**DefiLlama** = API TVL DeFi (pas Ollama). Qwen = LLM superviseur **manuel**.

## Confrontation (fin de campagne)

Voir `docs/CONFRONTATION.md` : comparer appels veille vs fills paper.
