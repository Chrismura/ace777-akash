# COMMENT LIRE LA VISION MOTEUR — Guide de la mécanique

Tu double-cliques sur `Vision_Moteur_Live.command` et tu vois défiler des lignes comme :

```
[ALPHA_LONG] 18:32:00 EXIT trailing_stop @ 77418.81 | pnl brut +0.2447 net -1.5153
[BETA_SHORT] 18:42:00 pos @ 77266.50 | ext=77266.50 | non ARMÉ | cap 76794.49 | H(2h): n=15 [+5.61 +1.64...] = +33.76 → H=1
[ALPHA_LONG] 17:55:00 à plat | H(2h): n=6 sum=+8.50 → H=1 | SLOT :5m → ENTRY programmé
```

Voici ce que chaque morceau veut dire.

---

## 1. `H(2h): n=15 [+5.61 +1.64 +0.40 +7.27] = +33.76 → H=1`

C'est le CŒUR du système : le filtre d'harmonie.

- **n=15** → il y a 15 trades virtuels du shadow dans les 2 dernières heures
- **[+5.61 +1.64 …]** → les 4 derniers, pour que tu voies de quoi la somme est faite
- **= +33.76** → la somme brute de TOUS ces trades sur la fenêtre
- **→ H=1** (vert) si la somme > 0, **→ H=0** (rouge) sinon

**La règle :** la machine n'a le droit d'entrer que si elle GAGNAIT récemment.
C'est le disjoncteur : quand ça saigne, H=0, plus d'entrée.

## 2. `SLOT :5m → ENTRY programmé` / `SKIP`

Le moteur ne regarde le marché qu'aux multiples de 5 minutes (17:55, 18:00, 18:05…).

- **H=1 au slot** → entrée sur le prix d'ouverture de la minute suivante
- **H=0 au slot** (après bootstrap) → `SKIP — attend que la somme 2h repasse > 0`
- **BOOTSTRAP** (les 90 premières minutes seulement) → entrée forcée même si H=0, taguée

## 3. `pos @ 77266.50 | ext=... | ARMÉ / non ARMÉ`

Une position virtuelle est ouverte.

- **entry** → le prix d'entrée
- **ext** = l'extension : le meilleur prix atteint depuis l'entrée (le plus haut pour ALPHA,
  le plus bas pour BETA). C'est la mémoire du "plus loin que le prix est allé en notre faveur".
- **non ARMÉ** → le prix n'a JAMAIS dépassé l'entry : **il n'y a pas encore de stop**.
  Le trade ne peut perdre sa sortie qu'au disjoncteur H.
- **ARMÉ** → le prix a dépassé l'entry ! Le stop naît à : `ext − 30% × (ext − entry)` pour ALPHA
  (miroir pour BETA), et il NE DESCEND JAMAIS (plancher à l'entry = breakeven garanti).
  La ligne te donne le niveau exact du stop et sa distance en $ du dernier close.

## 4. `cap 77856.01 (entry±50$)`

Si le gain atteint +50 USDT, sortie immédiate au cap. C'est la limite haute.

## 5. `EXIT trailing_stop @ 77418.81 | règle : low 77413.90 ≤ stop 77418.81 | pnl brut +0.2447 − frais 1.76 = net -1.5153 | hold 95s`

La sortie, avec la preuve :
- **quelle règle a touché** (le low de la barre est descendu sous le stop ? le cap ? le H→0 ?)
- **pnl brut** = (sortie − entrée) × 0.10593 BTC
- **net** = brut − 1.76 USDT de frais taker (la réalité du marché, celle qui a tué l'ancien ACE)
- **hold** = durée de vie du trade

---

## Les 3 fenêtres de suivi

| Fichier (double-clic) | Rôle |
|---|---|
| `Vision_Moteur_Live.command` | **La mécanique complète en flux** (ce guide) |
| `Voir_Shadow_Live.command` | Le tableau de bord : totaux nets, W/L, compte à rebours |
| `runs/SHADOW_SC_20260902.log` | Le journal interne du moteur |

Tout est en lecture seule : le moteur (le run officiel des 14 jours) n'est jamais touché.
Ctrl+C ferme l'affichage, jamais le run.
