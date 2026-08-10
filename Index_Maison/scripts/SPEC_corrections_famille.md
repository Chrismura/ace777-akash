# SPEC — CORRECTIONS RESERVES FAMILLE (par Ada, 10/08)

CONTEXTE : Les 3 scripts du flux loi 1quinquies (deleguer_codeur.py,
soumettre_hub_illimite.py, lancer_detache.py) ont ete audites par la FAMILLE
COMPLETE (GEMINI + DEEPSEEK + JUGE + ULTRA). Verdict : GO AVEC RESERVES.
Tu es le CODEUR DU HUB (expert) : corrige les 3 points ci-dessous.

RAPPEL : Python 3.9 stdlib, macOS, commentaires en francais, non fatal,
code pret a copier. Ne change RIEN d'autre que les 3 points.

## CORRECTION 1 — soumettre_hub_illimite.py : erreurs de parsing != erreurs reseau

Probleme (DEEPSEEK R3 + ULTRA 1, double confirmation) : le `except Exception`
attrape aussi `json.JSONDecodeError` et `KeyError` (reponse HTTP 200 mais
JSON invalide ou structure inattendue) et les retry 3 fois avec 30s d'attente
= 90 secondes perdues pour une erreur qui ne se repetera pas.

CORRECTION :
- `except urllib.error.URLError as e:` -> erreur RESEAU pure (connexion
  refusee, DNS, timeout) -> retryable, meme comportement qu'aujourd'hui.
- `except (json.JSONDecodeError, KeyError) as e:` -> erreur APPLICATIVE
  (reponse invalide) -> PAS de retry : ecrire dans le fichier de sortie
  "## ERREUR REPONSE INVALIDE\n\n<e>" et retourner 1 immediatement.
- `except Exception as e:` -> garde finale, retry (conservateur).

## CORRECTION 2 — deleguer_codeur.py : message TimeoutExpired trompeur

Probleme (DEEPSEEK R1) : si `subprocess.run(timeout=60)` expire, le message
actuel est "[ECHEC] timeout lancement détaché" alors que le processus DETACHE
(soumettre_hub_illimite.py) a pu etre lance par Popen et TOURNE deja.
Un "echec" affiche alors qu'il n'y en a pas = temps de diagnostic perdu.

CORRECTION : dans `except subprocess.TimeoutExpired`, ne PAS dire echec :
afficher "[ATTENTION] lanceur expire (60s) mais le processus detache est
peut-etre vivant — poller <out_path>" et retourner 0 (pas un echec).

## CORRECTION 3 — lancer_detache.py : nom de log avec collision possible

Probleme (ULTRA 3) : le log s'appelle `ace777_detache_<PID>.log` — si deux
lancements rapides partagent le meme PID parent, collision (ecrasement).

CORRECTION : inclure un timestamp dans le nom :
`ace777_detache_<PID>_<YYYYMMDD_HHMMSS>.log` (time.strftime).

## CONTRAT DE SORTIE

Reponds avec :
1. VERDICT (OK ou CORRECTIONS)
2. Pour chaque correction : FICHIER + bloc AVANT / bloc APRÈS exact,
   pret a copier, Python 3.9 stdlib, macOS.
