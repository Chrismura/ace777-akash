# VERDICT FAMILLE — Chaînes IA + modifications du jour (18/08/2026)

## Verdict : GO-AVEC-RÉSERVE (unanime 3/3)

| Membre | Verdict | Point clé |
|---|---|---|
| gemini | GO-AVEC-RÉSERVE | La chaîne matinale est bien ordonnée, MAIS le double mécanisme est confus |
| groq | GO-AVEC-RÉSERVE | Cohabitation obs-* (direct) + eval (prudent) = confusion logique inutile |
| **JUGE (nara)** | **GO-AVEC-RÉSERVE** | « Toute nouvelle offre, y compris obs-*, doit passer par observation enabled:false pendant 48h avant activation » |

## 🎯 La condition non négociable (unanime)

**UNIFIER le double mécanisme** : toutes les nouvelles intégrations — y compris les `obs-*` de queue_offres — doivent passer par le **sas d'observation 48h** (`enabled:false`) avant d'être activées, avec rollback par **désactivation** uniquement (jamais suppression).

- gemini : « Force queue_offres à passer par le même sas d'observation de 48h que eval_offres »
- groq : « tout doit passer par l'étape d'observation (enabled:false) avant de devenir actif »
- juge : « double sas est contradictoire... 48h avant activation, rollback par désactivation uniquement »

## ✅ Ce qui est validé sans condition

1. **Chaîne matinale bien ordonnée** (7h00 → 7h15, tout avant la session) ✅
2. **Observatoire à 11h00** sécurise l'ensemble ✅
3. **Roulement >2j** : accepté, avec les garde-fous (backup avant, atomique, 1 remplacement max, kill switch STOP_HUB, journal) ✅
4. **Cortana/Ada voient les bots** : pas de réserve émise ✅
5. **Timeout 15s sur les sondes** : pas de réserve ✅

## 📌 Action à appliquer (prochaine étape)

Modifier `queue_offres.py` : les `obs-*` intégrés doivent être créés avec **`enabled:false` + `status:'observation'`** (au lieu de enabled:True actif direct). L'observatoire (déjà étendu) les activera après 48h propres — avec le GO hebdo si nécessaire.

> Règle d'or maintenue : rien ne se supprime, tout est réversible, backup avant chaque écriture.
