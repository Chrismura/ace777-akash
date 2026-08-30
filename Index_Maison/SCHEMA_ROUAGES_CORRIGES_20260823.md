# ⚙️ SCHÉMA DES ROUAGES CORRIGÉS — 23/08/2026

> Ce que j'ai réparé aujourd'hui, et comment ça circule maintenant.
> Légende : 🟢 corrigé · 🔴 cassé avant · ➡️ flux de données

---

## 1. LA PRODUCTION D'ANALYSES (Cortana)

```
thermo/live.json ──────────┐
thermo/history.jsonl ──────┤
cockpit/mission.json ──────┼──➡️  cortana_analyse.py  ──➡️  hub (route cortana.analyse)
PROMPT_MASTER_ANALYSTE.md ─┘         (08:30 / 20:30)           gemini→groq→hf + filet
     ▲                                                              │
     │                                                              ▼
     │                                                   thermo/analyses/2026-08-XX.jsonl
     │                                                              │
     └── justesse_cockpit.json (sa note) ◀── score_justesse.py ◀───┘
                                              (professeur, 07:15)

🔴 AVANT :  les analyses échouaient (502) → repli « faits bruts » sans AVIS STRICT.
🟢 APRÈS :   production relancée à la main, 3 analyses écrites + scorées.
🔴 AVANT :  FLAT compté au dénominateur → 46% affiché (faux).
🟢 APRÈS :   FLAT exclu du score → 59% réel (49/83).
🔴 AVANT :  prompt disait « sous 60% → préfère NEUTRE » (spirale vers le bas).
🟢 APRÈS :   NEUTRE n'est plus un refuge — la prudence passe par les CONFIANCES.
```

## 2. LA BOUCLE D'APPRENTISSAGE (F1)

```
cortana_analyse.py ──➡️  thermo/analyses/*.jsonl
                              │
                              ▼
                    score_justesse.py (07:15, via discipline_quotidienne)
                              │  parse AVIS STRICT → HIT/MISS/FLAT vs marché
                              ▼
                    justesse_cockpit.json (59%)
                              │
                              ▼
        contexte_systeme() réinjecte la note + leçons dans le PROMPT suivant
                              │
                              └──── boucle fermée (F1)
```

## 3. ADA (déterministe, pas IA)

```
thermo/live.json ──➡️  ada_saison.py ──➡️  strategie/ada_saison_live.json
cockpit/mission.json ─┘          │
                                 ▼
                       ada_gardienne.py ──➡️  strategie/ada_gardienne_live.json
                                 │
                                 └── (appelée par cockpit_mission_feed.py, scan à chaque cycle)
🟢 Tout est branché et frais — ADA n'a pas de score de justesse (normal, déterministe).
```

## 4. LA COULEUR RÉGIME (pour Hulk — EN OBSERVATION, pas dans la chaîne Cortana)

```
onchain (whaleDir) ─┐
Fear&Greed (narratif) ─┼──➡️  couleur_regime.py ──➡️  regime_couleur.json (VERT/JAUNE/ROUGE/NOIR/ORANGE)
avis IA (LONG/SHORT) ─┤            (08:05 / 15:05)
thermo (alert=red) ──┘                │
                                      ▼
                            regime_couleur.jsonl (historique)
                                      │
                                      ▼
                            --score (16:30, dédup par heure)
                                      │
                                      ▼
                            regime_justesse.json = 27,6% 🔴 PEU FIABLE
                                      │
                                      ▼
                            veilleuse_chantiers.py (09:00)
                            « prêt à valider » seulement si n≥5 ET taux≥60%

🔴 AVANT :  --score comptait 10 000 lignes dont 7 804 doublons (boucle KeepAlive) → 34% faux.
🟢 APRÈS :   dédup par créneau → 27,6% réel → 🔴 ne PAS injecter dans Cortana.
🟢 Veilleuse : ne valide plus un signal à 27,6% comme « prêt ».
```

## 5. LES PLISTS (la boucle de destruction)

```
🔴 AVANT :  KeepAlive=true dupliqué dans StartCalendarInterval
            → launchd relançait les scripts en continu (toutes les ~2 min)
            → observatoire réécrivait providers.json (écrasait les correctifs)
            → couleur_regime --score tournait à 57% CPU (10 000 lignes en 3 jours)
            → sniffer inondait le hub (analyse.profonde toutes les ~5s)

🟢 APRÈS :  32 plists corrigés (KeepAlive retiré des one-shot, superviseur-core restauré)
            → cadence normale, fichiers stables, plus de boucles.
🟢 veille_degradation.py classe 4 : détecte ce pattern automatiquement (plus jamais en silence).
```

## 6. LE HUB (providers)

```
🔴 AVANT :  provider mort openai/gpt-oss-20b:free (404) — écrasé en boucle par l'observatoire.
🟢 APRÈS :  remplacé par z-ai/glm-5.2:free · OrcaRouter ajouté (clé installée) → 15 providers.
🔴 AVANT :  saturation 429 → analyses en repli « faits bruts ».
🟢 APRÈS :  production relancée, filet du hub fonctionne (Mistral a répondu).
```

---

## RÉSUMÉ DES CHIFFRES

| Mesure | Avant | Après |
|---|---|---|
| Justesse IA (Cortana) | 46% (FLAT au dénominateur) | **59%** (49/83, FLAT exclu) |
| Couleur régime | 34% affiché (doublons) | **27,6% réel** → ne pas injecter |
| Poussière | « r=-0,67, elle voit le marché » | **FAUX** — score = cumul 48h saturé + boucle KeepAlive. **Mesure réparée 23/08** : score = activité courante (0/0 vue → 0, plus 100 saturé) |
| Plists | 31 en boucle infinie + 1 XML cassé | 32 corrigés, cadence normale |
| Hub | 14 providers, 1 mort | 15 providers, tous vivants |
