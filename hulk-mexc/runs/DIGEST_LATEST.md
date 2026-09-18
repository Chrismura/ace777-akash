# Hulk DIGEST — 2026-09-18T08:26:37Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.18 | 2.34 | 0.11 | 0.03 | 39976774.03 | 2.25 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.82 | 0.18 | 0.02 | 334859337.58 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.4 | 0.06 | 0.02 | 530571178.28 | 0.36 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 46.36 | 22.1 | 0.07 | 54885.71 | 106.25 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 5.8 | 0.23 | 0.12 | 659327.33 | 9.78 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 5.5 | 1.46 | 0.11 | 608274.75 | 5.0 | skipped_fast |
| WUSDT | IDLE | 1.26 | 3.66 | 0.86 | 0.11 | 367748.56 | 14.67 | skipped_fast |
| KITEUSDT | IDLE | 2.21 | 4.19 | 1.53 | 0.02 | 73747.84 | 10.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.42 | 6.29 | 4.48 | 0.14 | 188165.74 | 18.85 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.22 | 1.18 | 0.04 | 576211.4 | 1.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 3.14 | 0.29 | 0.03 | 250540.8 | 31.16 | skipped_fast |
| BIOUSDT | IDLE | 1.99 | 3.93 | 0.3 | 0.05 | 77523.06 | 7.5 | skipped_fast |
| EDELUSDT | IDLE | 0.77 | 7.93 | 2.04 | -0.08 | 260847.2 | 17.34 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 2.35 | 0.61 | 0.05 | 67817.44 | 16.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.19 | 0.0 | -0.03 | 16065.28 | 5.92 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.12 | 0.81 | 0.03 | 45107.19 | 9.58 | skipped_fast |
| MNSRYUSDT | IDLE | 1.11 | 2.2 | 0.14 | 0.03 | 43016.33 | 9.55 | skipped_fast |
| TELUSDT | IDLE | 0.72 | 1.33 | 0.69 | -0.0 | 72467.05 | 41.72 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.04 | 0.37 | 0.02 | 58139.66 | 44.35 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 148.34 | 21.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
