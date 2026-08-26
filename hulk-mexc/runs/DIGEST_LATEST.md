# Hulk DIGEST — 2026-08-26T00:45:16Z

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
| PYTHUSDT | IDLE | 2.85 | 5.77 | 2.36 | 0.0 | 2202608.25 | 1.97 | tvl≈116,225,421 |
| XRPUSDT | IDLE | 2.21 | 5.12 | 3.42 | -0.05 | 73942073.77 | 2.8 | n/a |
| CCUSDT | IDLE | 1.78 | 3.62 | 1.78 | -0.04 | 535516.73 | 7.53 | no_map |
| HBARUSDT | IDLE | 1.77 | 3.52 | 2.99 | -0.03 | 768905.88 | 1.29 | empty_tvl |
| WUSDT | IDLE | 2.33 | 4.36 | 2.53 | -0.04 | 319679.42 | 5.35 | tvl≈1,568,751,203 |
| BIOUSDT | IDLE | 2.65 | 5.06 | 1.62 | -0.01 | 111669.36 | 3.43 | n/a |
| ZBCNUSDT | IDLE | 2.12 | 3.76 | 3.15 | -0.01 | 171649.7 | 23.43 | n/a |
| RIZEUSDT | IDLE | 2.67 | 5.62 | 2.04 | 0.04 | 51138.81 | 46.34 | no_map |
| REDUSDT | IDLE | 2.16 | 5.55 | 2.24 | 0.01 | 81548.3 | 11.25 | tvl≈2,063,363 |
| QAITUSDT | IDLE | 2.07 | 5.67 | 0.85 | 0.04 | 12802.86 | 59.59 | no_map |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
