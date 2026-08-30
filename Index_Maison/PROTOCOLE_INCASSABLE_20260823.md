# PROTOCOLE INCASSABLE — ACE777 (établi avec Gemini, 23/08/2026)

Objectif : que les 10 erreurs récurrentes (plists en boucle, ban API, black-hole,
score saturé, carnet vide, mort silencieuse, détecteur aveugle, évaluation faussée,
briefs vides, corrections écrasées) ne puissent PLUS revenir — et que toute panne
soit VISIBLE avant de fausser une analyse.
Source : consultation Gemini (gemini.analyse, 6 questions, 23/08) + corrections déjà
installées le 21-23/08. Format de chaque règle : (1) la règle, (2) l'erreur
neutralisée, (3) le garde-fou, (4) état actuel (fait / à faire).

---

## A. REGLES D'OR DE BON FONCTIONNEMENT (6)

### R1 — FRAICHEUR BLOQUANTE
- (1) Aucune analyse, aucun score, aucun signal si `now - derniere donnee > TTL`.
  Resultat : `STALE`, jamais de valeur fausse.
- TTL : detecteurs 15 min (3 cycles de 5 min) ; indice 20 min ; analyses IA 1 h.
- (2) Neutralise : mortalité silencieuse, détecteur aveugle, carnet vide lu comme 100%.
- (3) Garde-fou : verrou `STALE` ecrit dans le JSON de sortie (comme `taux_non_fiable`),
  aucun consommateur ne lit une valeur STALE. Reprise apres 2 lots frais consecutifs.
- (4) Etat : a generaliser (la pepite a deja `taux_non_fiable` ; le TTL sur les autres
  flux n'est pas encore uniforme).

### R2 — ECRITURE ATOMIQUE + HORODATAGE + COMPTEUR MONOTONE
- (1) Tout acteur ecrit avec `mkstemp + os.replace`, chaque ligne porte `ts`/`utc`,
  et un compteur qui ne peut que croitre (watermark).
- (2) Neutralise : score menteur (cumul a la place de la mesure), fiches figees,
  corrections ecrasees (on voit qui ecrase quoi).
- (3) Garde-fou : fichier avec checksum ; `hash identique pendant 3 cycles` = fige
  -> alerte (voire B2).
- (4) Etat : ✅ ecriture atomique deja en place (atomic_write_json) ;
  compteur monotone a ajouter.

### R3 — REPLI MULTI-SOURCE PERSISTANT
- (1) Au moins 2 sources independantes pour chaque flux reseau
  (mempool.space <-> blockstream.info). Bascule apres 2 echecs consecutifs, choix
  MEMORISE dans un fichier d'etat (sinon la bascule ne survit pas aux relances launchd).
- (2) Neutralise : ban/rate-limit API, SYN black-hole.
- (3) Garde-fou : quorum 2/3 si possible ; faute de quoi fail avec `STALE` plutot
  que des donnees partielles presentees comme bonnes.
- (4) Etat : ✅ installe sur le detecteur pepite (base persistee, bascule reussie le
  23/08 sur blockstream). A generaliser sur le detecteur dust/pont.

### R4 — CEINTURE ANTI-BLOCAGE (socket muet = mort visible)
- (1) Toute connexion protegee par SIGALRM (interrompt meme un connect() bloque :
  prouve en test, 5.0s pile) + duree max globale par run (25-40 s), zero retry infini.
- (2) Neutralise : SYN black-hole (ctimeout socket Python ne se declenche pas —
  verifie 6 min bloque en SYN_SENT, 8 h de silence).
- (3) Garde-fou : kill-switch fichier (STOP_ALL) verifie a chaque boucle.
- (4) Etat : ✅ installe sur le pile (SIGALRM + borne de run) ; a generaliser.

### R5 — BUDGET API (jamais d'appel inutile)
- (1) Cadence max : 1 appel/2 s avec jitter, backoff 2/4/8/16 s des la 1ere erreur ;
  CREUSER LE DETAIL SEULEMENT SI le seuil du signal est franchi (matrice du Juge),
  jamais sur le bruit de fond.
- (2) Neutralise : bombardement API -> ban (etait dans l'etat : ~50 appels/2min -> 8 h muet).
- (3) Garde-fou : compteur d'appels/heure dans le fichier d'etat, alerte si > seuil.
- (4) Etat : ✅ installe sur la pepite (creusage uniquement si taux > 10%).

### R6 — QUI SURVEILLE LE SURVEILLANT (canari)
- (1) Le superviseur ecrit lui-meme `watchdog/heartbeat.json` (ts, pid, hash config).
  Age max : 60 s. Relu toutes les 20 s par 2 relecteurs independants.
  Si age > 60 s, ou aucune relecture > 120 s -> relance automatique (launchd kickstart).
- (2) Neutralise : processor de supervision mort en silence (la piste historique :
  le hub etait mort, le watchdog local aveugle).
- (3) Garde-fou : double relecteur (launchd + un point externe), alerte si absent,
  trop vieux, hash change, ou relecture muette.
- (4) Etat : plaque opérationnelle (plists corriges) ; le heartbeat fichier formel
  est a mettre en place.

### R7 — BUDGET RESSOURCES (M1 8 Go)
- (1) Chaque process : run max 25-40 s, memoire max 300 Mo, nombre max de process
  python simultanes borne. Tout depassement -> arret + alerte.
- (2) Neutralise : plists en boucle (50x -> memoire/CPU sature), briefs vides en
  boucle qui brulent les credits.
- (3) Garde-fou : superviseur verifie la liste des process et leur memoire.
- (4) Etat : partiel (plists corriges le 23/08) ; budget memoire a ajouter.

---

## B. PROTOCOLE DE DETECTION — 1 detecteur par mode de panne

| Panne | Signal a surveiller | Seuil | Cadence |
|---|---|---|---|
| B1 Mort silencieuse | heartbeat (ts, pid) dans SANTE_ACE777.json | age > 90 s | 10 s |
| B2 Donnees fige es | hash du fichier de donnees | identique 3 cycles | 5 s |
| B3 Score sature | score fige a 0 ou 100 | constant 5 min | 15 s |
| B4 Carnet vide | n_snapshots / registre vide | = 0 ou age 60 s | 10 s |
| B5 Detecteur aveugle | erreurs API (timeout 404) | 3 consecutives | 30 s |
| B6 Process zombie | process actif, sortie nulle | 2 min | 20 s |
| B7 Corrections ecrasees | checksum config/plists/scripts | difference inattendue | 1 h |

**Tableau de bord sante — un seul fichier `SANTE_ACE777.json`** (le « cockpit
verite ») : pour chaque acteur : { last_ts, age_max, feu (vert/orange/rouge),
compteur } + valeur globale NOMINAL/DEGRADE/ALERTE + checksum des fichiers
critiques. Fonction utilitaire unique (hit_sante(acteur, feu, detail)) appelee
par tout script qui ecrit un resultat. Consomme par le cockpit et un cron qui
l'alerte si DEGRADE > 30 min ou ALERTE (alerte vocale existante).

---

## C. PROTOCOLE D'EVALUATION HONNETE (le Juge)

### C1 — Scoring sans biais
| Cas | Traitement |
|---|---|
| Prevision correcte | 1 point |
| Prevision fausse | 0 |
| Marche indecis (mvt < seuil sur la fenetre) | 0 point — NI BON NI MAUVAIS, etiquete NEUTRE ; l'incertitude doit apparaitre dans le verdict |
| Echantillons de taille < N | ABSTENTION (ni note, ni conclusion) |
| Donnees manquantes > 20% | Score NULL, calcul rejete (jamais un 0 qui fausse un vrai score) |
| Artefact confirme (score sature, carnet vide, aveugle) | Periode exclue du calcul, journalisee |

### C2 — Verdict d'un signal (pepite / indice / IA)
- **Il VOIT le marche** : N >= 30 signaux sur 7 jours ET justesse >= 60 % ET aucun
  episode aveugle > 15 min.
- **En observation** : 10 <= N < 30 — pas d'action.
- **Debrancher** : apres 7 j : N < 10/24 h OU justesse < 50 % OU silence > 15 min
  OU erreurs API > 5 %.
- Quarantaine automatique des que 2 seuils sont casses en meme temps.

### C3 — Reevaluation automatique
- Recalcul glissant toutes les 5 min sur fenetre 7 jours (verdicts lourds : 1 fois/jour).
- Journal immuable (append-only) de verdicts ; un changement de verdict emet un
  brief force (pas un vote savant).

---

## D. ORDRE D'IMPLEMENTATION
1. **SANTE_ACE777.json** + fonction utilitaire hit_sante — la brique centrale.
2. **TTL fraicheur bloquante** generalisee (R1) sur dust / pepite / indice.
3. **Checksum + compteur monotone** sur fichiers critiques (plists, scripts, donnees).
4. **Quorum 2/3** au niveau de l'indice onchain.
5. **Budget memoire process** au superviseur.

Rappel : la majeure partie du socle est DEJA en place (23/08) — repli multi-source
persistant, creusage selectif, ceinture SIGALRM, score honnete sans cumul sature,
carnet vide -> non fiable, plists stabilite. Les sections « a mettre » du tableau A
sont le chemin restant vers l'incassable.

— Protocole etabli avec Gemini (gemini.analyse) le 23/08/2026 et verifie contre
l'existant reel (fichiers, plists, scripts).

---

## E. APPROFONDISSEMENT — DIALOGUE GEMINI TOUR 1-4 (24/08/2026)

> Suite demandee par Christophe : finir le dialogue d'approfondissement (TOUR 1-4)
> puis verifier les ameliorations possibles contre l'existant reel.
> Source : `scripts/CONSULTATION_GEMINI_DIALOGUE_20260823/TOUR1-4.md` (meme
> conversation, historique conserve). Gemini conclut : **« ON NE PEUT PLUS FAIRE
> MIEUX »** (TOUR4).

### E1 — Garde-fous de niveau 2 (TOUR1) et leur etat reel verifie

| Regle | Garde-fou N2 propose | Etat reel (verifie 24/08) |
|---|---|---|
| R1 Fraicheur | `time.monotonic()` pour les deltas + horodatage UTC valide par `st_mtime` | ⚠️ a verifier flux par flux |
| R2 Atomique | retry 50 ms + quarantaine si `os.replace` echoue | ✅ ecriture atomique en place |
| R3 Repli | validation JSON du fichier de bascule + fallback hardcode | ✅ `_charger_base()` retombe sur mempool.space si illisible |
| R4 Anti-blocage | `socket.settimeout()` + `multiprocessing join(timeout=35)` | ✅ SIGALRM en place (detecteur pepite) |
| R5 Budget API | **backoff PERSISTE dans un fichier** (pas seulement en memoire) | ❌ hub garde le backoff en memoire (`_fails`, `_backoff_duree`) -> perdu a chaque relance launchd |
| R6 Canari | heartbeat avec `os.getppid()` + UUID de session (anti-PID-reuse) | ⚠️ `agent_status.py` fait un heartbeat mais sans UUID/ppid |
| R7 Ressources | `sys.getsizeof()` + `gc.collect()` + max RSS 250 Mo | ⚠️ limites memoire plist 400 Mo ; pas de controle interne |

### E2 — Garde-fous de niveau 3 (TOUR2)

- R1 : `time.monotonic_ns()` + check uptime kernel (`sysctl kern.boottime`) — la veille macOS fausse `monotonic()`.
- R2 : rotation stricte, max 3 fichiers de secours (SSD 8 Go).
- R3 : hardcoding des IPs des endpoints + timeout socket 3.0 s (DNS empoisonne).
- R4 : fermeture explicite des sockets (evite `CLOSE_WAIT` qui sature les fd).
- R5 : backoff stocke dans `./state/backoff.json` (pas `/tmp`, purge par macOS).
- R6 : heartbeat ACTIF via `os.write()` sur un pipe (pas un fichier statique).
- R7 : `malloc_zone_pressure_relief` si RSS > 220 Mo.
- (A) : orchestrateur unique launchd 30 s + **verrou global `/tmp/ace.lock` TTL 45 s** (anti-doublon) — ❌ absent aujourd'hui.

### E3 — Garde-fous de niveau 4 (TOUR3) — les extremes

- **Etat sans fichier / SSD plein** : reserve d'urgence 2 Mo (`os.ftruncate`) liberee en cas d'alerte critique — ❌ absent.
- **Double panne (API down + horloge compromise)** : TTL base sur la **hauteur de bloc Bitcoin** (`blocks/tip/height`) au lieu de l'horloge systeme — ⚠️ `surveiller_whales.py` lit deja `blocks/tip/height`, mais pas comme TTL de fraicheur.
- **Acteur menteur (counterfeit healthy)** : **challenge-response cryptographique** (le superviseur injecte une transaction-test, le worker doit la retrouver dans son hash de sortie) — ❌ absent.

### E4 — Angle mort final (TOUR4, clôture)

- **Abstention forcee** : un acteur menteur injecte un flot de cas `N < 30` artificiels pour forcer l'abstention perpetuelle et masquer une panne de marche.
- **Rempart** : compteur d'echantillons valide par un **identifiant de bloc on-chain unique et croissant** ; si le bloc stagne alors que `N` augmente -> echantillon invalide + kill-switch.
- **Conclusion Gemini** : « Ce protocole neutralise les pannes materielles (Mac M1), logicielles (stdlib, launchd) et comportementales (zombies, menteurs) par des contre-mesures cryptographiques et structurelles strictes. Le systeme est desormais auto-suffisant, incassable et immunise contre la corruption silencieuse. »

### E5 — Ameliorations possibles (verifiees contre l'existant) — a prioriser

| # | Amelioration | Effort | Impact |
|---|---|---|---|
| 1 | **Persister le backoff du hub** (`./state/backoff.json`) — sinon perdu a chaque relance launchd | Faible | Anti-boucle / anti-ban durable |
| 2 | **Verrou global anti-doublon** `/tmp/ace.lock` TTL 45 s pour les detecteurs (le doublon vigie du 24/08 = exactement ce cas) | Faible | Fini les doublons de process |
| 3 | **Heartbeat enrichi** (UUID de session + ppid) dans le superviseur | Moyen | Anti-PID-reuse |
| 4 | **TTL fraicheur base sur la hauteur de bloc** (deja lu par surveiller_whales) | Moyen | Anti-derive d'horloge / veille |
| 5 | **Challenge-response** anti-menteur | Eleve | Le plus dur ; garder en reserve |
| 6 | **Reserve disque 2 Mo** (ENOSPC) | Faible | Survivre a un SSD plein |