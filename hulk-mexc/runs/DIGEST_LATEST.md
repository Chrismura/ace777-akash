# Hulk DIGEST — 2026-08-29T19:11:28Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 70.44 | 38.01 | 0.0 | 136956.67 | 80.25 | skipped_fast |
| XRPUSDT | IDLE | 0.68 | 1.28 | 0.49 | 0.01 | 18347512.24 | 1.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.67 | 5.18 | 1.38 | 0.0 | 968104.48 | 2.41 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 9.7 | 8.46 | 0.02 | 67896.82 | 11.68 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 7.59 | 5.18 | -0.04 | 36684.84 | 54.83 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.44 | 0.97 | 0.03 | 318054.56 | 4.15 | skipped_fast |
| CCUSDT | IDLE | 1.72 | 3.54 | 0.01 | 0.08 | 204522.59 | 4.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.75 | 3.11 | 2.63 | -0.04 | 190650.61 | 11.89 | skipped_fast |
| WUSDT | IDLE | 0.92 | 1.73 | 0.78 | 0.01 | 181709.66 | 11.99 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.26 | 2.05 | 0.02 | 76741.09 | 10.22 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.2 | 1.04 | -0.01 | 63991.0 | 3.64 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.97 | 0.32 | -0.01 | 188214.9 | 1.32 | skipped_fast |
| RWAINCUSDT | IDLE | 0.59 | 1.18 | 0.0 | -0.02 | 3190.66 | 94.63 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.75 | 0.52 | -0.01 | 67638.85 | 40.26 | skipped_fast |
| QNTUSDT | IDLE | 0.61 | 1.1 | 0.75 | 0.01 | 29410.56 | 4.9 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
