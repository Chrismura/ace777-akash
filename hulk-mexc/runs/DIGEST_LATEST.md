# Hulk DIGEST — 2026-08-20T10:23:42Z

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
| XRPUSDT | IDLE | 1.53 | 6.08 | 0.73 | 0.15 | 54249455.05 | 1.73 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 8.52 | 7.45 | 0.09 | 249533.5 | 3.59 | skipped_fast |
| BIOUSDT | IDLE | 2.18 | 19.0 | 3.26 | 0.3 | 257782.12 | 15.33 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 5.07 | 1.4 | 0.15 | 429220.99 | 6.76 | skipped_fast |
| PYTHUSDT | IDLE | 1.34 | 5.51 | 0.56 | 0.16 | 354495.61 | 2.26 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.79 | 8.16 | 0.28 | 187740.16 | 12.52 | skipped_fast |
| WUSDT | IDLE | 1.73 | 3.82 | 0.63 | 0.09 | 306013.26 | 18.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 5.13 | 0.35 | 0.17 | 240787.14 | 18.9 | skipped_fast |
| HBARUSDT | IDLE | 1.41 | 2.85 | 0.45 | 0.08 | 414315.42 | 1.38 | skipped_fast |
| RIZEUSDT | IDLE | 1.3 | 8.62 | 5.57 | 0.11 | 68756.19 | 44.42 | skipped_fast |
| QAITUSDT | IDLE | 2.02 | 5.78 | 3.83 | 0.0 | 10178.0 | 65.65 | skipped_fast |
| QNTUSDT | IDLE | 2.21 | 5.59 | 0.21 | 0.1 | 52711.62 | 1.61 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 4.3 | 2.06 | 0.21 | 102964.04 | 11.09 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 1.84 | 0.44 | 0.07 | 60210.84 | 15.52 | skipped_fast |
| RWAINCUSDT | IDLE | 0.63 | 1.88 | 0.39 | 0.05 | 17312.47 | 22.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.68 | 4.58 | 0.65 | 0.1 | 2871.92 | 21.56 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 4.18 | 0.36 | 0.15 | 201604.32 | 36.06 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.78 | 0.26 | 0.02 | 52855.37 | 8.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
