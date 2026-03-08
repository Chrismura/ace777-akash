# ACE777 - White Paper Operatoire (Etat des Lieux)

## 1) Objet du document

Ce document formalise la situation actuelle d'ACE777 en environnement de test:

- ce qui a ete valide de maniere reproductible,
- les contraintes techniques/operationnelles rencontrees,
- le niveau de maturite atteint,
- ce qu'il reste a faire avant une phase plus industrielle.

Le texte est volontairement redige en mode "recette", sans exposer les noms internes des briques ni la nomenclature des algorithmes.

## 2) Vision systeme (sans details internes)

ACE777 fonctionne comme une machine de decision et d'execution en plusieurs couches:

1. **Filtrage d'entree**  
   Le systeme ne prend position que si plusieurs conditions minimales sont reunies (momentum, direction, qualite de marche, coherence de contexte).

2. **Orchestration a deux roles**  
   Une jambe "exploratrice" (frequente) et une jambe "compensatrice" (reactive) cooperent via un etat partage.

3. **Gestion du risque en continu**  
   Chaque cycle applique un controle de taille, de stop, de temporisation et de sortie, plus un coupe-circuit global session.

4. **Boucle d'adaptation**  
   Le systeme ajuste sa sensibilite apres gain/perte pour alterner phases offensives et defensives.

5. **Execution strictement contrainte**  
   Les ordres passent par des garde-fous de quantite, precision, et conditions de marche.

## 3) Ce qui a ete teste jusqu'ici

## 3.1 Campagnes de test observees

Les campagnes ont couvre:

- des cycles courts de validation (30 minutes),
- des tests de variation de levier (5 / 8 / 13),
- des phases d'augmentation de frequence d'entree,
- des essais avec stop de la jambe compensatrice relache a 12 bps,
- des runs avec adaptation post-gain/post-perte activee.

## 3.2 Constats quantitatifs clefs

Exemples recents de runs traces:

- **Run A (30 min)**  
  Net positif autour de **+1.55 USDT** pour **36 executions** (22 + 14), avec une activite elevee mais rendement moyen par trade modeste.

- **Run B (30 min, stop compensateur a 12 bps)**  
  Net positif autour de **+6.95 USDT** pour **29 executions** (16 + 13), avec un meilleur ratio resultat/trade.

Lecture: le regime "plus actif" peut produire un gain net significatif, mais la performance depend fortement de la qualite du flux marche sur la fenetre.

## 3.3 Volume de test cumule (journal machine)

Sur la base des fichiers de run disponibles dans `runs/` (segmentation par reset de cycle et/ou rupture temporelle), le volume cumule observe est:

- **Date de consolidation**: **2026-03-03 (UTC)**
- **Periode couverte par les logs**: **2026-02-28T08:39:34Z -> 2026-03-03T01:38:42Z**
- **Tests/sessions executes**: **588**
- **Heures de test cumulees**: **76.27 h**

Note de methode: ce chiffre est volontairement "operationnel" (ce qui est effectivement trace en journal), et non une estimation theorique.

## 4) Contraintes reelles subies (preuve de solidite)

Cette section ne decrit pas des contraintes "theoriques".  
Elle decrit les contraintes effectivement subies en campagne, et la reponse effective du moteur.

## 4.1 Contrainte: longues phases sans signal exploitable

**Ce qui a ete subi**

- series longues de cycles `SKIP` (momentum trop faible, direction incertaine, mismatch tactique),
- faible qualite de mouvement sur certaines fenetres.

**Reponse moteur observee**

- refus d'entree systematique au lieu de forcer des positions,
- maintien de discipline d'execution pendant des centaines de cycles.

**Ce que cela demontre**

- robustesse de filtrage,
- capacite a "ne rien faire" quand le marche ne paie pas.

## 4.2 Contrainte: etat duo parfois non disponible ou perime

**Ce qui a ete subi**

- occurrences `no_state` au demarrage,
- occurrences `stale_state` sur des phases lentes.

**Reponse moteur observee**

- attente defensive de la jambe compensatrice (`duo hunter waiting`) tant que l'information n'est pas fiable,
- reprise automatique des activations des que l'etat redevient valide.

**Ce que cela demontre**

- resilience au desalignement temporel,
- absence de prise de risque sur information obselete.

## 4.3 Contrainte: chocs rapides et inversions de direction

**Ce qui a ete subi**

- alternances brusques gain/perte,
- impulsions courtes suivies de retour violent.

**Reponse moteur observee**

- sorties defensives (stop, trailing, timeout) actives et coherentes,
- adaptation de sensibilite post-gain/post-perte enchainee sans crash logique,
- maintien de la continuité de trading.

**Ce que cela demontre**

- moteur tolerant aux regimes non stationnaires,
- controle de degradation en phase stress.

## 4.4 Contrainte: pression de frequence (mode plus actif)

**Ce qui a ete subi**

- augmentation volontaire de la frequence d'entree,
- hausse potentielle du bruit et du risque de surtrading.

**Reponse moteur observee**

- activite plus dense mais garde-fous conserves (stops, coupe-circuit session, garde de taille),
- maintien d'un resultat net positif sur des runs de reference.

**Ce que cela demontre**

- le moteur ne se desorganise pas quand on augmente le debit,
- il conserve une structure de risque operationnelle.

## 4.5 Contrainte: lisibilite et exploitation en temps reel

**Ce qui a ete subi**

- lecture difficile du resultat en terminal pendant run long,
- ambiguite d'analyse quand plusieurs runs partagent un meme tag.

**Reponse moteur observee**

- ajout d'une coloration live du `pnl=` en terminal,
- mise en place de scripts master valides pour standardiser l'exploitation.

**Ce que cela demontre**

- capacite du systeme a s'ameliorer operationnellement sans modifier sa logique coeur,
- reduction du risque d'erreur humaine de pilotage.

## 5) Niveau de maturite (au regard des contraintes subies)

## 5.1 Ce qui est valide factuellement

- L'architecture a deux roles tient en condition bruitee.
- La logique de reactivation/couverture a ete observee en situation reelle.
- Le coupe-circuit session fonctionne sans blocage systeme.
- Le mode d'adaptation post-gain/perte est actif en production test.
- Une base de configuration validee est formalisee dans master.

## 5.2 Ce qui reste fragile (points ouverts)

- La performance reste sensible au regime intraday.
- Le ratio PnL/trade peut se tasser en mode trop actif.
- Les longues phases sans declenchement restent normales mais doivent etre mieux contextualisees en monitoring.

## 6) Etat actuel de reference (baseline validee)

Baseline actuellement retenue comme "validee":

- configuration duo active,
- profil d'entree plus reactif,
- adaptation post-gain/perte activee,
- stop de la jambe compensatrice releve a 12 bps,
- scripts master de reference disponibles en versions 30 min et 6h30.

Objectif de cette baseline: conserver une dynamique de prise d'opportunites tout en gardant un cadre de risque explicite.

## 7) Ce qu'il reste a faire (roadmap)

## 7.1 Court terme (priorite haute)

1. **Valider la stabilite en run long (6h30)**  
   Mesurer derive, robustesse, et comportement lors des changements de regime.

2. **Standardiser les identifiants de run**  
   Eviter toute ambiguite d'analyse inter-runs (un tag unique par run).

3. **Tableau de bord de comparaison automatique**  
   PnL net, nombre de trades, PnL/trade, taux de blocage, repartition des motifs de sortie.

## 7.2 Moyen terme

1. **Optimisation multi-regime**  
   Ajustements selon regime de volatilite plutot qu'une seule valeur globale.

2. **Renforcement du protocole d'experience**  
   Un seul changement par campagne pour identifier causalite et impact reel.

3. **Gouvernance risque**  
   Limites explicites par session, par jambe, et par tranche temporelle.

## 7.3 Long terme

1. **Auto-calibration supervisee**  
   Propositions automatiques de reglages, validation humaine obligatoire.

2. **Industrialisation de la qualite**  
   Reproducibilite complete, journaux normalises, et procedures d'audit.

## 8) KPI de pilotage recommandes

Pour chaque run, suivre au minimum:

- **PnL net session**
- **Nombre d'executions**
- **PnL moyen par execution**
- **Part des cycles bloques**
- **Part des sorties defensives vs tactiques**
- **Duree moyenne de detention**

Ces KPI permettent de distinguer "plus d'activite" de "meilleure efficacite".

## 9) Conclusion

ACE777 n'est pas "au bout" technologiquement, mais il arrive a un palier de maturite ou:

- la structure de decision est validee,
- le risque est mieux encadre,
- les gains existent en conditions favorables,
- la prochaine progression vient surtout de la discipline experimentale et de la qualite de calibration.

En pratique: la priorite n'est plus d'ajouter des briques, mais de rendre la performance plus robuste et plus previsible sur des runs longs.

