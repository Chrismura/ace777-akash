# TOUR 2 — LES MESURES QUE VOUS AVEZ EXIGÉES, ET UNE FAUTE DE PLUS (LA MIENNE)

Vous m'avez posé 8 exigences chiffrées au tour 1. Je les ai produites une par une. **Avant de vous
les donner, la faute que je viens de découvrir en les produisant, parce qu'elle change encore votre
lecture du tour 1.**

## 0. CLASSE E18 — j'ai publié le DÉFAUT du code comme s'il était la CONFIG

Au tour 1 je vous ai écrit : « stop = max(plancher ; **cadence × 0,70**) » et « STOP_FLOOR_PCT
global ». **Les deux chiffres sont faux, et c'est moi qui les ai produits.**

| ce que j'ai publié (tour 1) | la vraie valeur, LUE dans `config/defaults.env` |
|---|---|
| `STOP_CADENCE_MULT = 0,70` | **0,80** |
| « plancher global » implicite | `STOP_FLOOR_PCT = 6,0` (et RIZE a son propre plancher : **8,0**) |

D'où venait le 0,70 : c'est le **défaut écrit dans le code** (`cfg.get("STOP_CADENCE_MULT","0.70")`).
**Je n'ai pas ouvert la config : j'ai lu un défaut et je l'ai appelé « config ».** C'est la classe
E17 (un plancher pris pour un seuil) déclinée en E18 (une valeur de repli prise pour la valeur
effective). Trois documents et un instrument portaient le faux chiffre ; **l'instrument ne l'écrit
plus en dur, il LIT la config à l'exécution**, et la correction est publiée dans le registre.
**Conséquence honnête** : votre tour 1 a jugé « stop 39-44 % » sur un chiffre dont la constante
était fausse — le niveau reste mauvais, mais la formule que je vous avais donnée ne l'était pas.

## 1. [Gemini] DÉLAI DE LECTURE DU PRIX — barre exigée : < 1 s

**MESURÉ** sur `runs/CORPUS_ASP_20260923.csv`, **9 328 lectures live horodatées**, 20 paires,
1 267 passes :

- médiane **1,057 s** · p90 **2,020 s** · max **3,658 s** ;
- part des lectures **< 1 s : 22,8 %** (2 127 / 9 328).

**VERDICT CONTRE MOI : la barre < 1 s que vous avez fixée N'EST PAS TENUE** — la médiane est à
1,06 s, soit ~6 % au-dessus, et 77 % des lectures sont au-dessus. Je ne l'annonce pas « conforme » :
c'est un **échec à la barre que vous avez posée**, sur un chiffre que je ne maîtrisais pas avant
de le mesurer aujourd'hui.

## 2. [DeepSeek + Nemotron] FRÉQUENCE DE SCRUTATION ET ÂGE DU PRIX À LA DÉCISION

- **MESURÉ** (`config/defaults.env`) : `POLL_SEC = 20 s` → la boucle regarde chaque paire toutes
  les ~20 s. Le satellite lit, lui, **toutes les paires à chaque passe** (`delay_s` ci-dessus).
- **MESURÉ** (journal du moteur vivant) : les décisions de sortie écrites portent l'âge du prix qui
  les a produites — n=38 lignes, médiane **0,00 s**, max **37,0 s**.
- **MESURÉ** : décisions de sortie passées par le **prix frais de GO 2** (tag `_impact_av…`) : **0**.

**INFORMATION INSUFFISANTE, et je le dis plutôt que de broder** : le délai médian/p90 du stop
**après** GO 2 ne peut pas être produit aujourd'hui — **aucun stop ne s'est présenté depuis la mise
en vol** (11:44Z). Nemotron a demandé « médiane ≤ 15 ms sur les 10 prochains jours » : ce chiffre
existe dans **10 jours**, pas maintenant. Ce que je peux prouver aujourd'hui : le correctif est
ACTIF (code) et l'âge du prix est écrit dans le motif au moment de la décision.

## 3. [Nemotron] ÂGE DU PRIX ↔ GLISSEMENT

**INFORMATION INSUFFISANTE**, chiffre manquant nommé : `age_avant_s` des 53 sorties de type stop
historiques (la colonne a été créée **après** ces sorties — elle est vide pour elles). Aucun stop
n'ayant eu lieu depuis GO 2, il n'existe aujourd'hui **zéro** couple (âge × glissement) exploitable.
Je refuse de remplacer ce vide par une estimation : c'est exactement l'E14 que vous m'avez reprochée.

## 4. [Nemotron] ESPÉRANCE MATHÉMATIQUE DU POSTE `cooling`

**MESURÉ** (net à la main, 10 jours, 60 trades — frais + spread estimés) :

| poste | n | net total | moyenne/trade | médiane | gagnants | meilleur | pire |
|---|---|---|---|---|---|---|---|
| **`cooling`** | 12 | **+7,26 $** | **+0,605 $** | +0,298 $ | **8/12 (67 %)** | +4,03 $ | −1,70 $ |
| tout le reste | 48 | +25,72 $ | +0,536 $ | +0,300 $ | 38/48 (79 %) | +4,79 $ | −2,97 $ |

**Lecture** : l'espérance de `cooling` est **positive** (+0,61 $/trade) mais son **taux de réussite
est plus faible** que le reste (67 % vs 79 %) et sa médiane est identique. Autrement dit : la
famille `cooling` n'est **pas** un poste perdant — elle est **moins fiable**, et elle rapporte par
quelques gros gagnants. C'est un fait, pas un avis.

## 5. [DeepSeek] SOURCE DES BOUGIES — preuve vérifiable

**MESURÉ** : `https://api.mexc.com/api/v3/klines?symbol=<PAIRE>&interval=1m&startTime=<ms>&endTime=<ms>`
· 16 fichiers de bougies brutes en cache (SHA-256 des 3 plus gros : `d44d5876c5248cca…`,
`b3ccdd4d377df080…`, `0ed44a73701e2f35…`, 11 154 / 12 638 / 12 204 bougies).
**Re-téléchargement live à 12:11:11Z** : 2 bougies RIZEUSDT reçues, `2026-09-23T12:10:00Z close=0,003137`
et `12:11:00Z close=0,00314`. La même API répond, avec l'horodatage des bougies : **la source est
vérifiable, pas déclarative**.

## 6. [Gemini] FORMULE EXACTE QUI FIXE LE STOP DE RIZE

**MESURÉ** (code `paper_diprip.py:633`, valeur LUE dans la config) :
`stop = max( plancher_de_la_paire ; cadence_de_la_paire × 0,80 )`
**MESURÉ** : RIZEUSDT.calib.stop_pct = **8,0** · cadence RIZE observée (n=8 214) : médiane **16,88 %**,
**max 55,58 %** · → stop RIZE = **max(8,0 ; cadence × 0,80)** = médiane **13,50 %**, **au pire 44,46 %**.
**Traduction** : le stop n'est pas une constante de la paire, il est **proportionnel à l'agitation
mesurée** ; sur RIZE il atteint 44 % quand l'agitation explose. Le 44 % que vous citiez est donc
**exact pour le mécanisme** — et toujours **inacceptable pour la protection**.

## 7. [DeepSeek] PLAFOND DE STOP À 15 % SUR RIZE — drawdown

**MESURÉ** (bougies 1 min MEXC, 2 trades RIZE) :

| achat | mise | creux marché | perte au creux | avec stop réel 39,23 % | avec plafond 15 % |
|---|---|---|---|---|---|
| 16/09 15:46Z | 3,22 $ | −14,59 % | −0,47 $ | −0,47 $ | −0,47 $ (plafond non touché) |
| 18/09 03:44Z | 3,46 $ | **−40,56 %** | −1,40 $ | −1,36 $ | **−0,52 $** |

**MESURÉ** : cumul **−1,87 $ → −0,99 $** avec plafond 15 % → **réduction 47 %**.
**ESTIMÉ** : sortie supposée AU niveau du plafond, sans glissement, sans ré-entrée → **optimiste**.
**EXTRAPOLÉ, et je ne le signe pas** : votre « réduction du drawdown > 50 % au portefeuille » n'est
**pas** démontré par **2 trades sur 16 paires**. Le contre-factuel complet des 10 jours donne
**+0,87 $** (plafond 15 %) sur **+32,97 $** de net — l'effet est **réel mais petit**.

## 8. [DeepSeek] AUDIT DES AUTRES PLANCHERS

**MESURÉ** : 11 paires ont des planchers nommés (`stop_pct` 6,0 → 10,3 · `dip_pct` 4,0 → 5,5 ·
`rip_pct` 3,0 → 5,2 · `mise_max_pct_mur` 0,02 partout). **Contre-épreuve dans le journal** : le
seuil **réellement** appliqué est écrit dans les motifs (`stop-39.23%_guard_partial_50`,
`impulse_pullback_dd6=5.1>=5.0`). Pour RIZE, le motif porte **39,23 %** quand la config porte
**8,0** → **le plancher n'est jamais le seuil**.
**INFORMATION INSUFFISANTE** : je n'ai pas encore vérifié **motif par motif** que chaque défaut de
config est surclassé par une valeur lue. C'est une sonde à écrire, **pas faite ici, pas déclarée faite**.

## 9. CE QUE JE VOUS DEMANDE

1. **La méthode de ce tour est-elle recevable** — j'ai étiqueté, et j'ai laissé trois
   « INFORMATION INSUFFISANTE » là où les chiffres n'existent pas encore. Est-ce la bonne
   attitude, ou dois-je produire autre chose ?
2. **Le point le plus grave est-il celui que vous pensez ?** Je pose le mien : **77 % des lectures
   de prix au-dessus de 1 s** (§1) — c'est une mesure du **présent**, pas une dette de méthode.
   Confirmez ou démentez.
3. **Sur le stop** : avec la formule corrigée (× 0,80), acceptez-vous qu'un plafond soit
   **câblé par paire** (RIZE ≈ 15 %), sachant que le gain mesuré est **+0,87 $ sur 10 jours** ?
   Est-ce que ça vaut de toucher au moteur, ou est-ce que je laisse — et pourquoi ?
4. **Ce qui reste ouvert et que je déclare** : (a) le délai de stop après GO 2 (impossible avant
   10 jours) ; (b) l'âge × glissement (0 observation) ; (c) l'audit complet des planchers.
   **Ces trois-là, je les laisse ouverts. Le reste, je peux le refermer avec votre GO.**

Terminez par vos 3 sections habituelles (VERDICT / CE QUE J'EXIGE AVANT LE PROCHAIN TOUR / CE QUI
ME FERAIT CHANGER D'AVIS), et pour chaque chiffre : MESURÉ / ESTIMÉ / INSUFFISANT. Si je vous ai
présenté un estimé comme un fait, nommez-le — c'est ce que je viens de faire sur moi-même (E18).
