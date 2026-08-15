# VERDICT FAMILLE — AGORA (15/08/2026 soir)

**Verdict : GO-AVEC-RÉSERVE** (gemini 91% / nvidia 82%) — convergent
**Décision Christophe :** GO (voix, au fourneau)

---

## Consensus famille (2/2)

| Question | Verdict |
|---|---|
| Q1 Boucle E4 | **Script dédié `lecons_auto.py`**, déclenché par la discipline 07h15 **APRÈS** la note de Cortana (jamais avant). Cadence quotidienne |
| Q2 Format leçon | **Axiome actionnable court** : `[indice] → [constat] → [action recommandée]`. Ex. « funding → positif mais faible fiabilité → corroborer avec fearGreed avant LONG ». **PAS de chiffres bruts** |
| Q3 Cloisonnement | **STRICT** : champ `namespace` obligatoire (`cortana`=texte / `ada`=chiffres). **Ada ne lit JAMAIS les leçons de Cortana** — elle ne consomme que les verdicts famille validés via live.json |
| Q4 Pérennité | **JSON valable jusqu'à ~500 fiches** (péremption 30j/90j + archive froide suffisent). SQLite inutile — l'auditabilité git est notre force. Bascule SQLite seulement si >5 Mo ou >500 fiches |
| Q5 Métrique | **Moyenne mobile 7j du score_justesse** vs baseline historique + comparaison 30j AVANT/APRÈS activation E4, même périmètre d'indices |

## Améliorations imposées (condition du GO)

1. **Namespace obligatoire** dans le schéma JSON : `namespace: "cortana" | "ada"` — étanchéité des sorties (gemini)
2. **TTL court (7 jours)** sur les leçons HIT/MISS avant validation en « règle structurelle » — sinon les leçons contradictoires polluent (gemini)
3. **E4 en deux temps** : `lecons_auto.py` écrit dans un STAGING (`lecons_brutes.json`), puis la discipline 07h15 **valide et fusionne** dans la base — jamais de bruit non relu (nvidia)
4. **Ada cloisonnée** : ses modulateurs viennent UNIQUEMENT des audits famille, jamais des leçons Cortana (nvidia)

## Garde-fous (ce qui ferait NO-GO)

- Justesse Cortana < 40% sur 30 jours → E4 amplifierait du bruit → désactiver
- Fuite de leçons Cortana vers les modulateurs Ada → cloisonnement cassé → NO-GO
- JSON > 5 Mo ou > 500 fiches → basculer SQLite
