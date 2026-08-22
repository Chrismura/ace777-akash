# Hulk DIGEST — 2026-08-22T14:04:09Z

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
| XRPUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| HBARUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| QAITUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| RIZEUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| ZBCNUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| WUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| REDUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| CCUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| PYTHUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| BIOUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| KITEUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| TELUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| CHIPUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| RWAINCUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| EDELUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| QNTUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| FLUIDUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |
| RWAUSDT | ERR | — | — | — | — | — | — | circuit-open api.mexc.com (réseau dégrad |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
