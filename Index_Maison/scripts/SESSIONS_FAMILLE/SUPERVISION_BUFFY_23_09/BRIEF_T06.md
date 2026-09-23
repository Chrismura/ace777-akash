# TOUR 6 — LA BOUCLE ENTIÈRE RÉ-EXÉCUTÉE : 4 NOUVELLES INCOHÉRENCES

Ordre reçu : « **ré-exécuter toute la boucle ENTIÈRE pour trouver d'autres incohérences et les
corriger** ». Fait. Voici ce que la boucle a crié **contre moi**, avec le chiffre et la source.
Aucun chiffre repris du moteur : tout est recalculé à la main (journal horodaté + bougies 1 min
MEXC). Source : `hulk-mexc/runs/BOUCLE_SETUPS_MAIN_20260923.{txt,json}`.

---

## CE QUI TIENT (je le dis aussi)

- **PnL reconcilié** : brut écrit par le moteur **+26,87 $** · recalculé à la main **+26,87 $**
  (écart **−0,0001 $**) · coûts estimés **1,99 $** → **net à la main +24,88 $**.
- **0 ordre, 0 €** : moteur en papier, aucune écriture de marché.
- Les 4 corrections du tour 5 sont en place et mesurées (pré-déclaration autotest **3/3** ·
  gardien seuil **25/25 + 12/12** + détecteur de termes du profil · R20 écrite).

## INC-A — 40,4 % DES PRIX NE SE RETROUVENT PAS DANS LEUR BOUGIE

```
prix vérifiés dans leur bougie : 84 / 141  (59,6 %)
```

**En clair** : pour **57 prix sur 141** (entrées et sorties), le prix inscrit dans le journal ne
tombe **pas** dans la bougie 1 min MEXC correspondante. Soit l'horodatage est faux, soit le prix
n'est pas celui du marché à cette seconde. **C'est une incohérence de DONNÉES**, pas de stratégie :
si le prix enregistré ment, tout le reste (chute mesurée, stop, PnL) est bâti dessus.
Détail par paire (colonnes `prix hors bougie`) : EDEL 6 · TEL 5 · RED 3 · ETH 3 · ZBCN 3 · W 2 ·
RIZE 1 · KITE 0 · HBAR 0 · XRP 0.

## INC-B — 4 STOPS SUR 15 NE SONT PAS HONORÉS DANS LES 2 MINUTES

```
stops honorés (≤ 2 min après contact) : 11 / 15
```

**En clair** : quand le prix touche le seuil de sortie, la machine ne vend pas dans les 2
minutes dans **4 cas sur 15**. C'est **la ceinture de sécurité** (le point n°1 du jury du tour 1,
jamais réparé) : le stop se décide sur un prix lu au cycle, pas à l'instant du contact.

## INC-C — SEULEMENT 32 % DES SORTIES SONT JUSTIFIÉES PAR LE MARCHÉ

```
sorties justifiées par le marché (bien) : 20 / 62  (32 %)
```

**En clair** : 42 sorties sur 62 ne sont **pas** expliquées par le marché (ni stop touché, ni
retournement). Qu'est-ce qui les décide alors ? Je n'ai **pas** encore la réponse — et je refuse
de l'inventer : c'est précisément le genre de « 68 % inexpliqué » qui, non traité, devient un
chiffre faux publié plus tard.

## INC-D — LE MOTIF D'ENTRÉE « IMPULSION » N'EST PAS VÉRIFIÉ (travail déclaré non fait)

La colonne « chute ≥ seuil » de la boucle est **INDICATIVE** : elle mesure la chute sur les
bougies 1 min, alors que **le moteur écrit SA PROPRE chute** dans le motif
(`impulse_pullback_dd6=5.1>=5.0`). Ce ne sont **pas la même grandeur**. La preuve d'un
franchissement doit être lue **dans le motif du moteur**, et **ce travail n'est PAS fait**.
Conséquence mesurable : « entrées conformes **3/60 (5 %)** » est une borne **pessimiste** qui
peut être fausse dans les deux sens — je l'ai écrit dans le rapport plutôt que de la publier
comme un fait.

---

## CE QUE J'AI CORRIGÉ AU TOUR 5 (rappel, pour que vous vérifiiez)

| exigence (votre tour 5) | état |
|---|---|
| pré-déclaration **avant** toute modification scellée | **FAIT** — `predemodifier.py`, autotest **3/3**, 43 dettes historiques apurées, **0 violation** depuis l'activation |
| un gardien doit lire **tous** les termes du profil, sinon **désactivé** | **FAIT** — section 4 de `verif_seuil_moteur.py` lit la formule du moteur et exige les mêmes clés |
| **interdire** un verdict sous 3 voix | **FAIT** — R20.3 écrite ; ce tour-ci est encore à **2 voix** (Grok 502, nex-agi 502 à l'envoi) → **avis CONSULTATIF**, pas un verdict |

## CE QUE JE VOUS DEMANDE (améliorations exigées, encore une fois)

1. **Sur INC-A (prix hors bougie)** : quel est **le contrôle** qui rend impossible qu'un prix
   entre au journal sans son horodatage source vérifié ? (Je propose : refuser d'écrire une
   ligne dont le prix n'est pas dans la bougie — mais ça peut **bloquer le moteur** : dites-moi
   si on bloque l'écriture ou si on la marque `prix_non_verifie`.)
2. **Sur INC-B (stops non honorés)** : la barre « ≤ 2 min » est-elle la bonne, et faut-il
   **prioriser** le stop sur tout le reste du cycle (une boucle dédiée au stop) ?
3. **Sur INC-C (32 % de sorties justifiées)** : exigez-vous l'**explication des 42 sorties**
   avant tout nouveau chiffre de performance, ou acceptez-vous de les publier comme
   « inexpliquées » ?
4. **Sur INC-D (5 % non prouvé)** : quelle est **la** façon loyale de compter la conformité des
   entrées — la chute du moteur (`dd6`) comme seule vérité, ou deux colonnes (moteur + bougies)
   avec l'écart affiché ?
5. **Évaluation** : depuis le tour 1, **monte** ou **descend** ? Répondez sur les faits du fil.

Terminez par : `VERDICT : … · CE QUE J'EXIGE AVANT LE PROCHAIN TOUR : … · CE QUI ME FERAIT
CHANGER D'AVIS : …`
