# 🎯 FICHE SET-UP INDIVIDUEL — EDELUSDT (EDEL) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_EDELUSDT.md` (2288 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_EDELUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 22.57% | Amplitude sur la fenêtre |
| **Creux intraday** | **21h UTC** | Fenêtre d'entrée : **20h / 21h / 22h** |
| **Pic intraday** | **14h UTC** | Fenêtre de sortie : **13h / 14h / 15h** |
| **Pattern jour/nuit** | distribué | Pattern faible (-1.4%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 35.08% | TRÈS ÉLEVÉ — dd15 moyen 35% (rafales brutales, stops serrés obligatoires) |
| **Mur bid max** | 2263.0$ (spoof 1.66%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 14.6% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.68 | moyennement corrélé BTC (+0.68) |
| **Signal divergence** | POMPE_PIEGE (stab 9) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **20h / 21h / 22h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **PARTIEL — attention aux secousses macro** — moyennement corrélé BTC (+0.68).
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 50% au contact / 50% si poussière <10% · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **13h / 14h / 15h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **TRÈS ÉLEVÉ — dd15 moyen 35% (rafales brutales, stops serrés obligatoires)**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : POMPE_PIEGE (stab 9) — à surveiller (instable sur small caps).

---

## 🔬 DÉCOUVERTES 30/08 (analyse croisée approfondie — réponse à « aucun nouveau pattern ? aucune corrélation ? »)

**1. 🚨 LA signature d'EDEL = le régime IMPULSE (pas une heure de la journée).**
| | Hors IMPULSE | En IMPULSE |
|---|---|---|
| Part du temps | 85% | 15% |
| m6 médian (mouvement 6min) | **4.2%** | **70.4%** (17× plus !) |
| p90 m6 | 5.8% | 78.5% |

→ **EDEL ne bouge que par rafales rares et violentes** : 3 rafales en 3 jours (27/08 23h46, 28/08 20h29, 29/08 15h33), toutes en fin de journée. Le reste du temps il est mort (IMPULSE_WAIT).
→ Après chaque rafale, le prix est en hausse 30min plus tard (+0.17%, +0.38%, +0.45%) — mais n=3, à confirmer.

**2. ⚠️ Le creux horaire N'EST PAS stable (contredit la fiche).**
Creux réel par jour : 23h (27/08) → 21h (28/08) → 11h (29/08) → 00h (30/08). Il bouge tous les jours → **aucune fenêtre horaire fiable** : c'est le régime (IMPULSE) qui compte, pas l'heure. La fenêtre 20-22h de la fiche est à déclasser en simple information.

**3. ❌ Corrélations : AUCUNE exploitable.**
| Paire | Corr 15min | Verdict |
|---|---|---|
| RWAINC | +0.146 | faible, instable (+0.23 → +0.07 → −0.08 par jour) |
| QNT | +0.142 | 25 points seulement = bruit |
| BTC | +0.120 | pas de lead/lag (avance −0.02, retard +0.07) |
| MNSRY | **−0.287** | 25 points = bruit (3h de données) |

→ **EDEL est l'actif le plus DÉCOUPLÉ du portefeuille** : il ne suit ni BTC ni personne, il bouge tout seul par rafales. Corr BTC du profil (0.68) = artefact de la fenêtre, pas un lien réel.

**4. Signal POMPE_PIEGE (stab 9)** = le plus haut du portefeuille → cohérent : rafales violentes imprévisibles, c'est LA définition d'un pompe-piège.

**➡️ Conséquence set-up** : pour EDEL, la bonne porte d'entrée n'est PAS une heure, c'est **la détection du régime IMPULSE lui-même** (le moteur le détecte déjà) — entrer/sortir sur l'allumage de la rafale, pas sur le calendrier. À valider avec les jours de mesure qui viennent.

---

## ⚡ SET-UP « RÉGIME » EDEL (30/08 — construit sur la découverte, en observation)

**Le principe** : le moteur détecte déjà l'allumage (`impulse_now = move6 ≥ 8% ou move24 ≥ 9.6%`, régime `IMPULSE` exige pullback `dd6 ≥ ~5%`). On se cale sur CET événement, pas sur une heure.

### Les 4 allumages rejoués (preuves disponibles)
| # | Allumage UTC | Durée | Prix | Pic rafale | +30min | +60min |
|---|---|---|---|---|---|---|
| 1 | 27/08 23:46 | 18pts | 0.01181 | +0.51% | +0.17% | −0.25% |
| 2 | 28/08 20:29 | 138pts | 0.01039 | +1.06% | +0.38% | **−1.64%** |
| 3 | 29/08 15:33 | 198pts | 0.01106 | +2.08% | +0.45% | +0.63% |
| 4 | **30/08 16:05 (EN COURS)** | 4pts | 0.01170 | — | — | — |

**Lecture des 3 rafales complètes** :
- **+30min : 3/3 UP** (moy +0.33%) → la fenêtre de sortie est dans les 30 premières minutes de la rafale.
- **+60min : 2/3 DOWN** (moy −0.42%) → rester trop longtemps dans la rafale fait perdre le gain.
- Pic médian de rafale ≈ **+1%** → objectif de prise de bénéfice réaliste.

### Entrée (tout doit être vrai — AUCUNE fenêtre horaire)
1. **Allumage IMPULSE détecté par le moteur** (régime = IMPULSE, pas IMPULSE_WAIT).
2. **Pullback confirmé** : dd6 significatif (le prix est retombé sous le pic de la rafale, pas en pleine poursuite).
3. Poussière < 15% (déclencheur standard) · mur = INFO seulement.
4. **Exécution** : 50% à l'allumage / 50% si le prix casse le pic de rafale (confirmation).

### Sortie (rapide — c'est LE point)
- **Objectif +0.5% à +1%** (pic médian de rafale) → prendre en 1-2 fois, dans les **30 premières minutes**.
- Stop sous le point d'allumage (si la rafale échoue, le prix retombe) — stop serré, jamais 1.5× range 15min ici (trop large pour ce jeu).
- **Jamais de trailing long** : +60min la rafale retombe 2 fois sur 3.

### Invalidation / risques
- **n = 3 rafales complètes seulement** → set-up en OBSERVATION, à prouver par l'accumulation des allumages (le détecteur `detecter_rafales_impulse.py` les journalise à chaque fois).
- Rafale 30/08 en cours : m6 faible (6%) → allumage naissant, ne pas le traiter comme les 3 autres tant qu'il n'a pas prouvé sa force.
- POMPE_PIEGE (stab 9) : cohérent — rafales imprévisibles, le stop serré est obligatoire.

### La preuve qui s'accumule
`hulk-mexc/runs/rafales_impulse/EDELUSDT.md` — chaque nouvel allumage ajoute une ligne. Dans ~7 jours : si les allumages continuent de donner +30min ≥ 3/4 UP et pic ≥ +0.5%, le set-up régime est VALIDÉ pour EDEL. Sinon, on ajuste (doctrine : jamais statique).

---

## ⏱️ ÉTAT ACTUEL
- **EDELUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_EDELUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_EDELUSDT.jsonl` + `.md`
