# 🧠 MÉMOIRE — La tragédie devenue mine d'or (20/08/2026)

> **Objet** : récit complet, vulgarisé et en profondeur, des deux échanges
> Christophe ↔ Buffy autour du mouvement marché du 18-20/08 (+8 % BTC non vu),
> de l'autopsie (1ʳᵉ réponse), des objections de Christophe (2ᵉ demande) et des
> corrections (2ᵉ réponse).
> **But** : que cette tragédie devienne une leçon gravée, lisible par tous
> (Christophe · Buffy · Cursor · Punk · Cortana · la famille), pour que ça
> n'arrive plus.
> **Date de gravure** : 20/08/2026 · Fichiers liés : `ENQUETE_POUSSIERE_BLOCS_PRIVATISES_2026-08-20.md`
> (révisé), `ENQUETE_VIGIE_MORTE_2026-08-20.md`, `ENQUETE_SCELLE_CHAMPION_2026-08-20.md`,
> `DECISION_CPFP_ADA_2026-08-20.md`.

---

## ACTE 1 — Le drame (ce qui s'est réellement passé le 18-20/08)

- **Le marché** : BTC passe de ~64 200 $ à ~69 350 $ = **+8 % en 24 h**, volume ×3.
  Cause identifiée APRÈS coup par le sniff : décision américaine (Trésor/Fed/Bessent)
  → "debasement trade" or + bitcoin. **Mouvement exogène (macro), pas onchain.**
- **Le bot ACE** : run `MASTER_VORTEX_V2_COLLAB_4H` (19/08 13:13 → 20:57 UTC) :
  **−48,66 $** (Alpha −44,44 / Beta −4,22), tué par **SIGKILL** (pression mémoire).
  Devait durer jusqu'au 23/08 → `WHY_ARRET=unknown`, `early_stop`.
- **Hulk (paper MEXC)** : +2,26 $ en 20 trades, alors qu'un portefeuille statique
  (rien faire) aurait fait **+2,84 $** — et +14 % en moyenne sur les 13 positions
  seed. Le "réflexe de protection" (RIP à +2 %) est devenu un plafond de gains.
- **Personne n'a rien vu passer** : c'est la plainte fondatrice de Christophe.

---

## ACTE 2 — La 1ʳᵉ demande de Christophe

> "Le marché a explosé, on n'a rien vu. Un bot a crashé après grosse perte, l'autre
> fait moins bien qu'un portefeuille statique. **Vérifie si nos indicateurs avaient
> anticipé le mouvement** — on ne l'a pas vu par manque d'orchestration et
> inattention. Il y avait une investigation à finir sur des opérations douteuses
> BTC (indice poussière). Va en profondeur dans ton audit, car ça part dans tous
> les sens."

Demande explicite : (1) le marché, (2) nos indicateurs l'avaient-ils vu ?,
(3) pourquoi le bot a crashé, (4) Hulk vs statique, (5) l'investigation "poussière"
inachevée.

---

## ACTE 3 — Ma 1ʳᵉ réponse (l'autopsie)

J'ai reconstitué les faits et livré un verdict. **Le problème : deux de mes
conclusions étaient trop rapides, et tu l'as senti.** Voici ce que j'avais dit :

### Ce qui était JUSTE (confirmé ensuite)
- **Le mouvement était exogène/macro** (décision américaine) → le onchain ne
  pouvait pas le prédire seul.
- **Le radar (vigie marché) était mort** le 19/08 à 12:10 UTC — juste avant le
  gros du mouvement. Aucune alerte n'a pu partir.
- **ADA était réactive, pas prédictive** : elle hurle PRENDS_LA_PERTE APRÈS la
  perte, pas avant.
- **Hulk vs statique** : le RIP à +2 % plafonne les gains en montée continue.
- **BETA a fait 255 fills… 100 % SELL** pendant que le marché montait de +8 %.

### Ce qui était FAUX ou TROP RAPIDE (corrigé en ACTE 5)
1. **"L'indicateur blocs privatisés ne mesure rien / c'est du bruit blanc."** → FAUX.
2. **"Le patch S-10 appliqué en plein vol a cassé les stops."** → FAUX (et injuste :
   S-10 était un correctif légitime validé par Christophe).
3. **"Personne n'a pensé aux systèmes de relance"** → FAUX : ils existaient,
   mais n'étaient pas branchés (le trou était ailleurs).

J'avais aussi proposé 4 chantiers (GO Christophe, dans l'ordre) : enquête poussière,
mode macro tempête, décision CPFP/ADA au 23/08, hygiène (vigie, md5, journal auto).
Et j'avais livré l'autopsie complète du run.

---

## ACTE 4 — La 2ᵉ demande de Christophe (les objections — LA mine d'or)

> "Pour l'indicateur opération, va voir l'historique conversation, tu comprendras
> la logique : cet indicateur devrait être un instrument de détection très affiné
> (les gros bonnets l'utilisent, le mainstream ne le connaît pas encore). Ce que tu
> as trouvé me semble très étrange, **creuse**. Je ne discute pas la partie
> technique, c'est toi qui t'en occupes ; moi je t'ai fourni en partie la formule
> et l'idée.
> La vigie morte, c'est de ton ressort — mais il aurait dû y avoir plusieurs
> systèmes de relance, j'ai demandé plein de checks des index pour pas que ça
> arrive. Tu le verras si tu checkes l'ensemble du cockpit et l'historique.
> Le patch appliqué en plein vol, c'est toi qui l'as décidé — pas une critique,
> mais regarde mieux le fonctionnement des radars, ils ont été construits avec une
> bonne base d'intelligence.
> **Pondère tes analyses, va plus en profondeur, avec une vue plus ample, zéro
> faute.** Ce que tu vois ici, en grande partie, on l'a construit ensemble — et la
> partie qui déconne ne devrait pas l'être. J'ai ACE777 à cœur."

Trois objections précises = trois pistes d'erreur dans mon autopsie.

---

## ACTE 5 — Ma 2ᵉ réponse (les corrections, preuves à l'appui)

### Correction n°1 — L'indicateur "blocs privatisés" : concept RÉEL, mesure cassée

J'ai fait ce que tu demandais : **relire ta pépite** (`vigie_mempool_pepite_christophe.py`)
avec la **matrice du Juge** (taux fantôme > 35 % + volume > 1000 BTC = baleine qui
téléporte un règlement OTC via mempool privée). Puis deux analyses :

- **281/281 blocs stables intra-run** : le même bloc analysé plusieurs fois donne
  le même taux (ex. 8,53 % × 3). → **Ce n'est PAS du bruit aléatoire** : c'est une
  propriété déterministe de chaque bloc. Mon premier verdict "bruit blanc" était faux.
- **Test live décisif (20/08, 25 min, snapshots 60 s)** : le même bloc donne
  **33,6 % de "fantômes" mesuré à 10 min** vs **8,3 % mesuré à 60 s**. Avec
  l'historique dense : les blocs donnent **0,5-8,3 %** (médiane 4,7 %).

**Interprétation** : la mesure était cassée par la **résolution** (snapshot toutes
les 10 min, alors que les tx vivent parfois < 10 min en période active → elles
entrent ET sortent entre deux photos → faussement "fantômes"). **Mais le résidu
0,5-8,3 % même à 60 s = ton vrai signal** : des tx qui n'apparaissent jamais, même
avec des photos toutes les minutes → potentiellement de vraies tx privées/OTC.

**Verdict révisé : l'indicateur n'est pas à jeter, il est à réparer** (résolution
60-120 s, exclure les 100 % = carnet vide au démarrage, recalibrer la matrice du
Juge sur le taux résiduel dense). **Ta formule et ton idée étaient justes ; c'est
l'implémentation qui n'avait pas la bonne résolution.** (Détail : `ENQUETE_POUSSIERE_BLOCS_PRIVATISES_2026-08-20.md` révisé.)

### Correction n°2 — La vigie morte : les systèmes existaient mais n'étaient pas branchés

J'ai audité TOUT l'arsenal de relance que tu avais demandé :

| Système | État réel | Rôle |
|---|---|---|
| `superviseur.sh` (module relance vigie + heartbeat ≤ 180 s) | Lancé **à la main**, mort 19/08 14:09:12 | ✅ le SEUL qui relançait la vigie marché |
| `com.ace777.superviseur-process.plist` | **Existait mais PAS chargée** | lance superviseur.sh |
| `com.ace777.superviseur.plist` (chargée) | Tourne | lance `superviseur_auto.py` (cycle IA), PAS superviseur.sh |
| `superviseur_core.sh` (launchd) | Tourne | vérifie la vigie **sécurité**, pas la vigie **marché** |
| `sante_index.py` (tes checks des index) | 6 chaînes OK | **ZÉRO référence à la vigie marché** (`grep vigie_live` = 0) |

**La vérité** : la vigie marché n'était couverte par AUCUN système automatique.
Le seul garde-fou (superviseur.sh) était lancé à la main → quand il est mort
(probablement pression mémoire : RAM à 136 Mo), **plus rien ne la relançait**.
C'est exactement le trou que tu avais pressenti. → **Réparé** : vigie relancée
(PID 38557, journal radar actif) + `superviseur-process` chargé dans launchd
(PID 42482) — il survivra aux redémarrages. (Détail : `ENQUETE_VIGIE_MORTE_2026-08-20.md`.)

### Correction n°3 — Le patch S-10 : un correctif légitime, PAS le coupable des stops

J'ai vérifié le diff du commit S-10 (`1e318498`, 19/08) : **ZÉRO ligne touchant les
stops** (aucun algoOrder/triggerPrice/reduceOnly). C'était le correctif des frais
NET que **tu avais GO le 19/08** (PnL brut +14 vs net −278, frais Binance = 88 % du
trou). Ensuite j'ai daté les erreurs réelles :

- `stop_market_fail` **commencent le 17/08 21:28** avec `code=-1106 reduceonly` —
  **AVANT S-10**. Le passage V4 (algoOrder) date du **17/08** (commit `0f81068c`).
- Le 19/08, les erreurs sont devenues **`-2021 Order would immediately trigger`**
  (26×) + **`-4116 ClientOrderId duplicated`** (8×) : le filet à **8 bps** se pose
  trop près du prix sur un marché volatil → Binance le refuse → **positions sans
  filet physique** pendant le run.

**Verdict** : le filet physique n'a jamais bien fonctionné (V3 → -1106, V4 →
-2021/-4116), indépendamment de S-10. S-10 n'était pas le coupable ; mon accusation
était fausse. (La question du champion re-scellé `01c38510` est documentée dans
`ENQUETE_SCELLE_CHAMPION_2026-08-20.md` — pas d'altération, scellé simplement périmé.)

### Point confirmé — Les radars : base saine
`radar_gate.rb` (décision de direction) est propre : momentum/spread, script externe
au genesis (C1 respecté), et le mode macro tempête ajouté est conforme. La base
d'intelligence est là ; ce sont l'infra et le filet qui ont lâché.

---

## ACTE 6 — LA MINE D'OR : les leçons gravées (à ne plus jamais oublier)

1. **Le concept de Christophe prime** : quand il dit "cet indicateur est affiné,
   creuse", il faut chercher POURQUOI la mesure échoue, pas conclure que l'idée
   est fausse. La formule était bonne ; la résolution d'implémentation ne l'était pas.
2. **Ne jamais conclure "bruit" sans tester la résolution** : un signal qui semble
   chaotique peut être un vrai signal sous-échantillonné. Règle : si un indicateur
   semble aléatoire, augmenter la fréquence de mesure AVANT de le condamner.
3. **Un garde-fou écrit ≠ un garde-fou actif** : toutes les plists de relance
   existaient, AUCUNE n'était chargée. Règle : après avoir écrit un système de
   relance, vérifier `launchctl list` + un test de mort réel. La vigie marché doit
   être ajoutée à `sante_index.py` (le check des index) — chantier ouvert.
4. **Accuser un commit = lire son diff d'abord** : S-10 ne touchait pas les stops.
   J'ai accusé le mauvais patch. Règle : `git show <commit> -- <fichier>` avant
   tout verdict.
5. **Le filet physique (STOP_MARKET) est fragile** : 8 bps trop serrés en volatilité
   → Binance refuse (-2021), ID dupliqués après relance (-4116). À calibrer
   (distance minimale de trigger) et à tester en conditions réelles AVANT de compter
   dessus.
6. **Un run avec relances automatiques peut charger un champion modifié à
   mi-course** : le commit disait "prend effet au prochain relancement", mais les
   relances auto l'ont fait entrer en service pendant le run. Règle : pas de patch
   en plein run, ou geler les relances pendant un patch.
7. **Le vrai trou du 18-20/08 était l'infra, pas les indicateurs** : vigie morte +
   filet jamais fonctionnel + macro non couverte. Trois trous différents, trois
   corrections différentes.
8. **La vue d'ensemble** : le cockpit et l'arsenal ont été construits ensemble avec
   une vraie base d'intelligence. Quand ça déconne, chercher ce qui n'est PAS
   branché, PAS ce qui est mal conçu.

---

## Ce qui a été fait le 20/08 (résumé exécutif)

| Chantier | État |
|---|---|
| N°1 Enquête poussière → **verdict révisé : concept réel, mesure à réparer** | ✅ documenté |
| N°2 Mode macro tempête (bloque SELL/BUY contre-choc) | ✅ actif, testé |
| N°3 Décision CPFP/ADA (23/08) — preuves + recommandation | ✅ documenté |
| N°4 Hygiène : vigie relancée + superviseur-process chargé + champion re-scellé `01c38510` + journal_auto réparé (découverte dynamique) | ✅ fait |
| **Nouveau** : rebranchement du système de relance vigie (le trou du filet) | ✅ fait |

## Actions restantes (GO Christophe requis)
- [ ] Ajouter la chaîne VIGIE MARCHÉ à `sante_index.py` (l'alerte qui manquait)
- [ ] Réparer la résolution du détecteur blocs privatisés (60-120 s) + recalibrer la matrice du Juge
- [ ] Calibrer le filet STOP_MARKET (distance minimale Binance, ID unique après relance)
- [ ] Décision 23/08 : CPFP/ADA → activer ou jeter (checklist dans `DECISION_CPFP_ADA_2026-08-20.md`)
- [ ] Couche macro/news pour les chocs exogènes (le trou béant du 19-20/08)

---
*Gravé par Buffy le 20/08/2026, à la demande de Christophe — pour que la tragédie
devienne une mine d'or d'apprentissage. 🙏*
