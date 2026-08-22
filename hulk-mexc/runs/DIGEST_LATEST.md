# Hulk DIGEST — 2026-08-22T11:11:29Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 8.0 | -0.0 | 51658250.05 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.73 | 0.06 | 218187770.99 | 3.37 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.69 | 0.11 | 812418.16 | 6.92 | skipped_fast |
| HBARUSDT | IDLE | 1.49 | 5.26 | 4.16 | 0.0 | 1255011.54 | 6.48 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.77 | 0.01 | 595667.53 | 11.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.36 | 5.93 | 5.59 | -0.04 | 401468.57 | 24.52 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.11 | -0.11 | 645336.92 | 3.37 | skipped_fast |
| EDELUSDT | IDLE | 2.79 | 4.93 | 4.37 | -0.05 | 78823.3 | 22.81 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.64 | 4.09 | -0.05 | 238392.39 | 3.27 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 4.3 | 1.44 | 0.03 | 73622.18 | 11.8 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.16 | 2.48 | -0.0 | 2490.36 | 35.86 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.66 | -0.04 | 169310.34 | 58.93 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 4.99 | 0.02 | 154247.75 | 22.65 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | -0.01 | 11311.88 | 59.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 2.89 | 1.82 | -0.01 | 49233.29 | 22.54 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.99 | -0.01 | 189052.04 | 9.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.38 | skipped_fast |
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
