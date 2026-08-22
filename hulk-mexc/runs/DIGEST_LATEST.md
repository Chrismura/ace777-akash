# Hulk DIGEST — 2026-08-22T16:20:43Z

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
| PYTHUSDT | IDLE | 1.48 | 7.24 | 0.68 | 0.06 | 51442172.88 | 5.88 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.64 | 4.76 | 0.04 | 215604402.5 | 0.69 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 3.03 | 1.56 | -0.01 | 1139899.97 | 1.3 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.38 | 0.09 | 766819.36 | 6.83 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.76 | -0.09 | 628370.12 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.63 | 2.58 | 1.3 | -0.02 | 544567.07 | 10.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 3.49 | 2.52 | -0.05 | 316071.21 | 18.1 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.48 | -0.07 | 219638.29 | 3.3 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 4.35 | 1.62 | 0.03 | 85388.54 | 12.48 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.52 | 2.24 | -0.03 | 74813.06 | 22.88 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.93 | -0.11 | 133891.01 | 14.57 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.3 | 0.03 | 56550.65 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.11 | -0.02 | 184376.56 | 6.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 8652.8 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.63 | 0.0 | 137554.81 | 53.36 | skipped_fast |
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
