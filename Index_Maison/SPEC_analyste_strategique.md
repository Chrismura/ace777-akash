# SPEC v2 — Système Analyste Stratégique auto-enrichi (ACE777)

> **Version** : 2.0 — 11/08/2026
> **Auteur** : Buffy (chef d'orchestre / chief scientist)
> **Exécution** : codeur du hub, SUR VALIDATION de Christophe
> **Principe** : tout en BRUT (Python standard, zéro framework), outil éprouvé uniquement si indispensable. Une chose à la fois. Décisions de design prises par Buffy (validées par Christophe).

---

## 1. Objectif

Donner à la maison un **analyste stratégique vivant** qui :
1. **Vit en temps réel** : écoute le marché à la seconde (WebSocket), pas de scan périodique
2. **Réagit aux événements** : un changement d'indice OU une nouvelle majeure (taux, carry trade, événement mondial) le déclenche
3. **S'enrichit lui-même** : mémoire froide relue à chaque réveil + boucle de rétroaction sur ses prédictions (VRAIE/FAUSSE)
4. **Travaille sur 3 horizons** : Court terme (événementiel) · Semaine (à la commande) · Tendance long terme (à la commande)
5. **Parle (Vivienne) + écrit** quand c'est pertinent, **silence** sinon
6. S'affiche dans un **volet STRATÉGIE dédié** du cockpit

**Règles de vie** : 0 API payante · Mac froid (8 Go) · pas de briefing sans changement · tout traçable · une chose à la fois.

---

## 2. Architecture globale

```
🔌 VIGIE LIVE (un processus léger, toujours à l'écoute)
   │
   ├─ 📈 Flux PRIX — WebSocket Binance public (BRUT stdlib, prouvé ✅)
   │    chaque trade = événement → comparateur de seuils
   │    écart < seuil → archivé, SILENCE
   │    écart ≥ seuil → ⚡ ALERTE PRIX
   │
   ├─ 📰 Flux NEWS — RSS gratuits (cointelegraph, google news, testés 200 ✅)
   │    nouvelles parutions → filtre mots-clés majeurs (brut, instantané)
   │    info majeure → ⚡ ALERTE NEWS
   │
   ▼
🧠 ANALYSTE (hub Gemini — réveillée SUR alerte, jamais sinon)
   juge la pertinence → si oui : analyse (3 horizons selon le contexte)
   → AVIS VOCAL (Vivienne) + ÉCRIT (STRATEGIE.md + registre)
   │
   ▼
📈 BOUCLE D'AUTO-ENRICHISSEMENT
   prédictions échues → VRAIE/FAUSSE (vérificateur hebdo)
   → bilan dans MEMOIRE_ANALYSTE.md → la prochaine session sait
```

---

## 3. DÉCISIONS DE DESIGN (prises par Buffy — vous validez ou ajustez)

### 3.1 La vigie : UN processus, 2 écoutes

**Une seule entité** (`vigie_live.py`) qui fait les 2 écoutes en parallèle (threads). C'est elle le "radar" — mais un radar qui reçoit, ne scrute pas.

**Écoute prix — WebSocket Binance (prouvé ✅, brut stdlib)** :
- Instruments suivis : **BTCUSDT + ETHUSDT** (les 2 poids lourds, suffisant pour le prototype ; ajoutable en 1 ligne)
- Streams : `btcusdt@aggTrade` + `ethusdt@aggTrade` (trades agrégés, événementiel pur)
- Reconnexion automatique si le flux coupe (boucle with reconnect + backoff 5 s)

**Écoute news — RSS gratuits** :
- Sources : **cointelegraph.com/rss** (crypto) + **Google News RSS** avec mots-clés macro (`fed interest rate`, `carry trade`, `usd`, `recession`) — tous testés ✅ 200
- Cadence : **toutes les 60 s** (les news ne sortent pas à la seconde ; 60 s est plus que suffisant et léger)
- Filtre mots-clés majeurs (brut, instantané, ~0 coût) : `fed`, `interest rate`, `carry trade`, `cpi`, `recession`, `crash`, `war`, `assassination`, `bank`, `default`, `emergency`, `black swan`, `japon`, `nikkei`, `liquidation`… → si 1+ mot-clé : ⚡ ALERTE NEWS

**Filtrage du bruit (LA règle d'or)** :
| Événement | Déclenche si |
|---|---|
| 📈 Prix | variation ≥ **0,5 % sur 60 s**, OU **volume anormal** (agrégé 60 s ≥ 3× la moyenne mobile), OU mouvement ≥ **2 % sur 5 min** |
| 📰 News | **1 mot-clé majeur** dans le titre (filtre brut) PUIS confirmation par l'analyste (elle juge si c'est vraiment majeur) |

Tout le reste (tick normal, news sans impact) → **journal_radar.log** (traçabilité) + silence.

### 3.2 L'analyste : un seul script, 3 modes

**`analyste.py`** — réveillée UNIQUEMENT sur alerte (prix ou news) ou commande explicite.

**Les 3 modes** (selon le déclencheur) :
| Déclencheur | Mode | Sortie |
|---|---|---|
| ⚡ Alerte prix (variation) | **COURT TERME** | Verdict bref : ce qui change, impact sur la stratégie du jour, action ou pas. **VOCAL (Vivienne) + écrit** |
| ⚡ Alerte news (mot-clé majeur) | **COURT TERME** | Idem — mais d'abord : elle Juge si la news est vraiment majeure (sinon silence). **VOCAL + écrit** |
| 🗣️ « analyse la semaine » | **SEMAINE** | Vue 7 jours : niveaux clés, scénarios, points de vigilance. Écrit (vocal optionnel) |
| 🗣️ « où en est la tendance ? » | **TENDANCE** | Phase de marché estimée (accumulation/hausse/sommet/baisse/distribution), où on se situe. Écrit |

**Prompt construit selon le PROTOCOLE_PROMPTING** (techniques #1, #4, #5, #6) :
```
ROLE : analyste stratégique senior ACE777, experte marchés + machine de trading, 20 ans d'expérience.
CONTEXTE INJECTÉ (zéro hallucination, technique #6) :
  [STRATEGIE.md] [MEMOIRE_ANALYSTE.md (20 dernières leçons)] [derniere_analyse.md] [mission.json] [l'alerte]
RAISONNEMENT (technique #4) :
  [UNDERSTAND] Reformule en 1 phrase · [ANALYZE] tendance/momentum/risque
  [STRATEGIZE] 2-3 approches · [EXECUTE] verdict
SORTIE EXACTE (technique #5) : Verdict · Confiance (0-100%) · Hypothèses
  · Ce qui changerait la réponse · Alternative si confiance < 80%
```

**Confiance < 60 % → elle le dit et propose une option de repli.** Elle n'invente jamais.

### 3.3 La mémoire froide (auto-enrichissement)

**Fichiers** (dossier `~/ace777-test-day1/Index_Maison/strategie/`, non protégé TCC) :

| Fichier | Rôle |
|---|---|
| `STRATEGIE.md` | LA mémoire : 3 sections (CT / SEMAINE / TENDANCE). Réécrite à chaque analyse |
| `MEMOIRE_ANALYSTE.md` | Les leçons accumulées (prédictions VRAIE/FAUSSE, ce qui a marché). Jamais supprimé |
| `derniere_analyse.md` | La dernière analyse complète (relue en début de session, affichée au cockpit) |
| `historique_analyses/` | Archives datées |
| `etat_vigie.json` | La référence prix (dernière valeur connue + moyennes mobiles) |
| `journal_radar.log` | TOUT ce que la vigie voit (même le bruit) — traçabilité |

**Règle de session** : le prompt de l'analyste COMMENCE toujours par l'injection de ces fichiers → elle ne prédit jamais dans le vide, elle RELIT son passé. **C'est l'auto-enrichissement.**

### 3.4 La boucle de rétroaction

- `verifier_predictions.py` (déjà en place, launchd lundi 19h) marque les prédictions échues
- **Ajout** : après vérification → les résultats rejoignent `MEMOIRE_ANALYSTE.md` (« 11/08 : prédiction X FAUSSE — leçon : … »)
- → Chaque session suivante lit ses leçons. Elle apprend de ses erreurs, factuellement.

### 3.5 Volet STRATÉGIE du cockpit

**Onglet** `data-tab="strat"` (à côté de board/graph/ops/thermo/vol). Contenu :
1. **3 horizons** : cartes COURT TERME / SEMAINE / TENDANCE (depuis STRATEGIE.md)
2. **Dernière analyse** : `derniere_analyse.md` + horodatage
3. **La vigie en direct** : dernière alerte (indicateur, ancienne → nouvelle valeur, ts) + statut (écoute / en veille)
4. **Registre des prédictions** : les 10 dernières avec statut (⏳/✅/❌)
5. **Commandes** : boutons « Analyse la semaine » et « Où en est la tendance ? »

**Implémentation** : `strategie_feed.py` génère `cockpit/strategie.json` (comme `hub_cockpit_feed.py`) → le JS de l'onglet affiche. Serveur cockpit existant, pas de nouveau serveur.

---

## 4. Fichiers (pour le codeur)

| Fichier | Action |
|---|---|
| `scripts/vigie_live.py` | NOUVEAU : WebSocket brut stdlib + RSS news + filtres + déclenche l'analyste |
| `scripts/analyste.py` | NOUVEAU : prompt injecté (mémoire) → hub → sorties + voix |
| `scripts/strategie_feed.py` | NOUVEAU : génère `cockpit/strategie.json` |
| `strategie/*` (STRATEGIE.md, MEMOIRE, etc.) | NOUVEAUX |
| `cockpit/index.html` | MODIFIÉ : onglet STRATEGIE |
| `routing.json` | MODIFIÉ : tâche `analyste.strategie` (gemini → nvidia) |
| `LaunchAgents/com.ace777.vigie-live.plist` | NOUVEAU : vigie en continu (KeepAlive) |

**Dépendances** : AUCUNE nouvelle. Python standard + edge-tts + yt-dlp (déjà là). WebSocket = stdlib (socket/ssl/struct), prouvé fonctionnel.

---

## 5. Tests de validation (avant livraison)

1. **Vigie prix** : lancer → trades BTC reçus en direct (déjà prouvé ✅)
2. **Filtre bruit** : 5 min d'écoute → aucune fausse alerte sur ticks normaux
3. **Seuil** : simuler une variation (ou attendre une vraie) → alerte déclenchée
4. **News** : déclencher manuellement le filtre → une info majeure produit une alerte
5. **Analyste** : sur alerte → STRATEGIE.md mis à jour + voix + prédiction au registre
6. **Mémoire** : vérifier l'injection STRATEGIE.md + MEMOIRE_ANALYSTE.md dans le prompt
7. **Volet** : `strategie.json` servi, onglet affiche les 3 horizons + vigie + registre
8. **Hub vivant** : `/health` OK après tout
9. **RAM** : vigie mesurée < 100 MB, CPU ~0 % (vérifier avec `ps`)

---

## 6. Hors périmètre (PAS maintenant)

- Cosmétique des graphiques (autre chantier)
- Intégration des données du coffre/Obsidian comme source vigie
- Autres instruments (ajoutable en 1 ligne plus tard)
- Analyse vidéo YouTube dans la vigie (la veille existe déjà séparément)

---

## 7. Points d'honnêteté

- L'analyste ne prédit pas l'avenir : elle raisonne sur la donnée + l'expérience accumulée. Prédictions = hypothèses vérifiables.
- La confiance (0-100 %) est son auto-évaluation ; le registre mesurera sa fiabilité réelle.
- La vigie suit BTC/ETH + news macro ; pas les actions, le forex ni les matières premières (hors périmètre).
- Le WebSocket est gratuit mais public : en cas de panne Binance, reconnexion auto ; en cas d'indisponibilité prolongée, la vigie le signale.
