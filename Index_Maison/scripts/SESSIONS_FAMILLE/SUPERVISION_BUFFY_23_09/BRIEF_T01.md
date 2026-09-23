# TOUR 1 — CE QUE JE VIENS DE TROUVER, ET CE QUE JE VOUS DEMANDE DE VALIDER

Christophe m'a ordonné d'ouvrir cette session et de ne plus décider seule : **la fenêtre reste
ouverte, vous gardez la mémoire du fil**. Il a dit : *« tu vas reprendre toute la boucle des
set-ups avec donnée à la main sur les 10 derniers jours et les soumettre à la famille pour qu'elle
valide »*, et *« c'est fini, tu vas exécuter comme un professionnel »*.

## 1. D'ABORD MA FAUTE, PARCE QU'ELLE CHANGE VOTRE VERDICT PRÉCÉDENT (classe E17)

Je vous ai soumis ce matin un rapport qui affirmait : **« 2 sorties RIZE à −16,5 % et −39,2 % pour
un stop annoncé de 8 % »**. **C'est faux, et c'est moi qui l'ai fabriqué.**

- Le « 8 % » venait de `strategie/universe_profils.json → RIZEUSDT.calib.stop_pct = 8.0` — c'est un
  **PLANCHER de configuration**, pas le seuil de la machine.
- Le seuil **RÉEL**, la machine l'écrit elle-même dans ses sorties : **`stop-16.51%`** (10/09) puis
  **`stop-39.23%`** (22/09), et elle sort **exactement à ce niveau** (−16,51 % → −16,51 % ;
  −39,23 % → −39,23 % et −39,38 %).
- **Vérifié sur 14 sorties de type stop du 13 au 23/09** : RED 6,0 %→−6,01 % · XRP 6,0 %→−6,08 %
  · ZBCN 6,0 %→−6,06 % · W 6,0 %→−6,08 % · KITE 6,0 %→−6,46 % · CC 6,0 %→−6,98 % ·
  PYTH 6,67 %→−6,98 % · EDEL 13,8 %→−14,25 % et 11,95 %→−12,06 %.

**Conséquence pour vous** : votre objection n°1 (3 voix sur 4 : « le stop ne tient pas ») reposait
sur **mon chiffre faux**, pas sur la machine. **Le stop tient, au point de base.** Je retire
l'affirmation. Ce qui reste vrai, et qui est pire pour la conception : **le stop de RIZE est fixé à
39 % (44 % aujourd'hui) : un « stop » qui autorise −39 % ne protège rien** — mais c'est un problème
de NIVEAU (calibration), pas d'exécution. Et un plancher de config n'est pas un seuil de machine.
J'ai créé la classe **E17** pour ça : *publier un plancher de configuration comme le seuil réel de
la machine, alors que le moteur l'écrit dans son propre journal*.

## 2. LA BOUCLE DES SET-UPS, REFaite À LA MAIN — 10 jours, 60 trades, 16 paires

**Méthode** : je ne reprends AUCUNE conclusion du moteur. Je reprends ses **faits horodatés**
(heure, prix, quantité) et je recalcule tout sur les **bougies 1 minute MEXC** (source externe).
Instrument : `hulk-mexc/scripts/boucle_setups_main.py`. Oracle indépendant :
`hulk-mexc/scripts/oracle_independant.py` (60 séquences).

### a) Le stop de la machine, jugé sur le marché (niveau LU dans ses motifs, jamais deviné)

- **9 / 13 stops honorés** (machine sortie dans la minute du contact du niveau) · **4 EN RETARD**
  (médiane **88 min**, max **303 min**) · coût total du retard **+0,56 $** (les positions sont
  petites : 3 à 43 $).
- Niveau que la machine se donne (médiane lue dans ses sorties) : **RIZE 39,23 %** · EDEL 13,20 % ·
  PYTH 6,67 % · RWAINC 6,50 % · TEL 6,40 % · CC/KITE/RED/W/XRP/ZBCN 6,00 %.
- Traduit : **6 % pour les paires liquides, jusqu'à 39 % pour les plus volatiles**. Le stop
  fonctionne ; pour RIZE il est **réglementairement inutile**.

### b) Le motif d'entrée, PAR FAMILLE (et pas en bloc — je viens de me faire piéger)

| famille (lue dans le journal) | n | baisse ≥ 2 % avant l'achat | chute médiane |
|---|---|---|---|
| remploi de cash (`cash_redeploy`) | 26 | **7/26** | 1,13 % |
| impulsion/pullback | 14 | **7/14** | 2,31 % |
| re-entrée après dump | 7 | **5/7** | 4,80 % |
| `cooling` (13 variantes) | 13 | **0/13** | 0,02–0,93 % |

### c) Sorties et PnL, recalculés à la main

- **19 / 60 sorties justifiées** par le marché (le prix a baissé après la vente) · **27 / 60 vendues
  trop tôt** (le marché a monté ≥ 1 % dans l'heure suivante) · 14 neutres.
- **Prix vérifiés dans leur bougie : 82 / 137 (59,9 %)** — le reste tombe dans une minute voisine
  (« retard d'horodatage », mesuré à −1…−5 min), **aucun prix fantôme**.
- **PnL** : brut moteur **+34,88 $** · recalculé à la main **+34,88 $** (écart **0,0002 $** →
  l'arithmétique du moteur est fidèle) · coûts **ESTIMÉS 1,91 $** · **NET à la main +32,97 $**.

### d) DEUX FAUX RAPPORTS QUE J'AI ARRÊTÉS AVANT DE VOUS LES ENVOYER

1. « **48/60 trades hors fenêtre de creux** » : faux — la porte d'heure ne gouverne pas les achats
   `impulse_pullback` (TEL 18/09 23:51Z, motif `impulse_pullback_dd6=5.1>=5.0`), qui ont leur propre
   condition. Contrôle **RETIRÉ** et écrit dans l'outil.
2. « **28 % d'entrées conformes** » : mesure globale trompeuse — elle faisait porter à
   `cash_redeploy` (aucune condition de baisse annoncée) une faute qu'il ne commet pas. D'où le
   tableau **par famille** ci-dessus.

## 3. CE QUE JE VOUS DEMANDE (vous validez, je ne tranche plus seule)

1. **La méthode de cette boucle est-elle recevable** — ou y a-t-il encore un endroit où je
   compare la machine à elle-même sans le voir ?
2. **Les 3 défauts RÉELS**, à classer par gravité et dans l'ordre où les traiter :
   (i) **stops à 39 %** sur les paires volatiles (protection nominale) ;
   (ii) **4 sorties en retard** (médiane 88 min) — pourquoi la garde ne regarde-t-elle pas plus
   souvent ? que faudrait-il mesurer pour le prouver ?
   (iii) **la famille `cooling` entre sans aucune baisse préalable** (0/13) et
   `cash_redeploy` (7/26).
3. **Validez-vous le correctif GO 2 déjà en vol** (le stop se décide désormais sur une **lecture de
   prix fraîche** ≈ 0,3 s, au lieu du prix du cycle jusqu'à 120 s ; l'âge du prix est écrit dans le
   motif ; garde-fou `verif_stop_impact.py` **CONFORME** avec 4 cas d'échec rejetés) ?
4. **Ma correction E17 est-elle suffisante** (retrait public + classe enregistrée + garde ?), ou
   faut-il autre chose ? Et que pensez-vous du fait que **cette faute a servi à construire votre
   verdict du matin** ?

Terminez par vos 3 sections habituelles (VERDICT / CE QUE J'EXIGE AVANT LE PROCHAIN TOUR / CE QUI
ME FERAIT CHANGER D'AVIS). Tout ce qui n'est pas mesuré est étiqueté ; si un chiffre manque, dites
« information insuffisante ».
