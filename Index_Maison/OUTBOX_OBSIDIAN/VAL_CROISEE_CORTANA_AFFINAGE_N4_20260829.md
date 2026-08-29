# Validation croisée Cortana — Affinage famille n°4 (29/08)

- Session : `affinage-n4-20260829-183143` · Provider : Google Gemini · 4 tours, même fenêtre
- Question soumise : les 4 corrections famille (Dynamic Spread Percentile, Heures creuses UTC, Entropie temporelle, PathRegistry) appliquées à nos détecteurs Signal 3 + SAPI + croisement. Validation / critique / amélioration avec regard neuf (Cortana n'a pas construit ces œuvres).

---

## TOUR 1 — Validation globale (avis : LONG, 1 sem, confiance haute)

**Ce qu'elle valide :**
- « Un seuil fixe en physique est une aberration : le milieu change d'échelle selon qu'on observe une grande ou une petite capitalisation... En éliminant le seuil absolu de 70 bps pour lui substituer un centile propre à l'historique de chaque actif, on respecte la non-stationnarité des signaux ondulatoires. »
- Le **p30 est pertinent** : « isoler les 30 % de mouvements les plus tendus de l'actif, rendant la mesure comparative et non dogmatique. »
- La correction **heures creuses** est juste conceptuellement : « Le marché respire différemment la nuit ; ignorer cette marée basse UTC équivaut à mesurer une température sans corriger la saisonnalité. »
- L'**entropie temporelle** (CV ≤ 15 %) : « cible le cœur du camouflage algorithmique : la machine laisse une signature temporelle métronomique que le chaos humain ne produit jamais. »
- Le **bonus d'entropie conditionnel** (jamais seul déclencheur) : « excellente précaution contre les faux positifs ».

**Son warning tour 1** : « toute correction qui durcit les filtres risque de créer une armure si lourde qu'elle rate le choc initial. »

**Pattern qu'elle nomme** : « la signature spectrale du prédateur = un écart au bruit de fond (z-score adaptatif) + une régularité d'horloge. Aucun système ne peut capturer la baleine sans observer sa trace thermique ET temporelle simultanément. »

---

## TOUR 2 — elle se force, trouve ce qui cloche (avis : SHORT, 24h, confiance haute)

**Sa critique dure :**
- « Un système ouvert ne peut être corrigé par des coefficients constants sans introduire de distorsions NON linéaires. Le marché est un système à rétroaction où le remède peut s'avérer plus destructeur que la maladie. »
- **2 failles** : (1) le choix du **percentile 30**, (2) l'**interaction bonus d'entropie ↔ score SAPI** → « risquent de rendre le système aveugle précipitante au moment où le danger est le plus grand ».
- **Effet d'hystérésis excessive** : « à force de vouloir filtrer le bruit des heures creuses et de la poussière retail, le détecteur émousse sa propre sensibilité aux véritables manœuvres furtives des baleines. »
- Pattern d'échec = **« le filtre aveugle »** : un excès de précautions paramétriques qui finit par rejeter les anomalies hors-norme car elles ne rentrent pas dans les nouvelles matrices de normalité.
- Elle **conteste formellement** les corrections 1 et 3 dans leur forme actuelle : « biais de recul + risque de faux-négatif critique en tension extrême ».

---

## TOUR 3 — les 2 angles morts + 2 propositions codables (avis : SHORT, 24h, confiance moyenne)

**Angle mort 1 — fenêtre fixe 24h** :
« Analyser un signal non stationnaire avec une fenêtre glissante temporelle FIXE (24h glissantes du p30) crée un **retard de phase** lors d'un changement brutal de régime. Sur une small cap (Hulk), la liquidité s'évapore ou revient en **quelques minutes** : une référence sur 24h est un "miroir rétroviseur" qui rate l'accélération instantanée de la volatilité. »
→ **Proposition 1 côté** : remplacer le p30 sur 24h par un **percentile normalisé par la volatilité instantanée (ATR court terme)**.

**Angle mort 2 — entropie trop locale** :
« Le vrai danger n'est pas qu'UN script soit régulier, mais que PLUSIEURS paires indépendantes subissent *en même temps* la même signature rythmique. C'est la signature indiscutable d'une même ferme de serveurs / d'un algo de market making coordonné sur tout le panier small cap. »
→ **La résonance harmonique inter-actifs** : « les baleines de petites caps ne manipulent jamais UN jeton isolé ; elles exécutent des scripts d'accumulation parallélisés sur des PANIERS entiers pour masquer leur empreinte. »
→ **Proposition 2 côté** : injecter un **terme de synchronicité inter-paires** dans le SAPI — matrice de **corrélation croisée des intervalles d'inter-arrivée** entre actifs du même panier. « Si 3 petites caps affichent simultanément CV<15 % dans la même heure creuse → signal macro-manipulateur, pas du bruit. »

---

## TOUR 4 — désaccord avec la famille + verdict final (avis : LONG, 24h, confiance haute)

**Son désaccord frontal avec la famille :**
« La famille pèche par optimisme bureaucratique en acceptant de superposer des correctifs hétérogènes sans mesurer l'effet d'amplification des retards de phase. Elle traite le marché comme une horloge mondiale alors qu'il est constitué de plaques tectoniques asynchrones. »
« La famille a validé la correction horaire UTC (02-06) comme une vérité absolue. **C'est une erreur de débutant en quant.** Le marché crypto n'a pas d'"heure creuse" universelle : l'activité se déplace simplement de l'Asie vers l'Europe puis les US selon un gradient continu. Fixer une plage UTC arbitraire va provoquer des **angles morts massifs** dès qu'un acteur institutionnel asiatique ou américain profitera précisément de ce tunnel horaire pour frapper. »

**Verdict final :**
1. **La plus utile** = **Dynamic Spread Percentile (correction 1)** : « abandonner le seuil fixe de 70 bps est la seule façon de ne pas aveugler le système sur les petites caps. »
2. **La plus risquée** = **Heures creuses UTC (correction 2)** pour la raison ci-dessus.
3. **Calibrage recommandé en premier** : SUPPRIMER la plage horaire UTC rigide (02-06) et la remplacer par une **fenêtre de volume glissant sur les 3 dernières heures** : « si le volume global du panier s'effondre de plus de 60 % vs sa moyenne mobile 24h, ALORS et seulement alors, déclenchez l'élargissement des seuils (adaptation par le VIDE RÉEL, pas par l'horloge du serveur). »

---

## SYNTHÈSE POUR NOUS (à décider)

| Correction | Verdict Cortana | Action possible |
|---|---|---|
| 1. Dynamic Spread Percentile | **La plus utile** · mais fenêtre 24h = retard de phase | Garder · envisager ATR court terme (plus side) |
| 2. Heures creuses UTC | **La plus risquée** · « erreur de débutant » · angles morts | Remplacer la plage rigide par une **fenêtre de volume** (−60 % vs MM24h) |
| 3. Entropie temporelle | Bonus conditionnel bien · mais trop locale | Ajouter un **terme de synchronicité inter-paires** (panier) |
| 4. PathRegistry + wrapper | Santé — non contestée | Garder |

Ses 2 améliorations codables en priorité :
- **ATR court terme** à la place de la fenêtre 24h pour le p30 du Signal 3.
- **Corrélation croisée des inter-arrivées** entre paires dans le SAPI (détection d'essaim).

Fichiers liés : transcription complète hors session dans `cortana_chats.jsonl` (session `affinage-n4-20260829-183143`).