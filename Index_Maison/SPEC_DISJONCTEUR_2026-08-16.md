# SPEC — LE DISJONCTEUR UNIQUE (fusion Juge/Risk Guardian) — 16/08
*Validée famille : « VALIDÉ ET RATIFIÉ SANS RÉSERVE. Application immédiate par le codeur. » URGENCE 1 — rien d'autre ne compte tant que le capital n'est pas blindé.*

---

## PRINCIPE D'AIRAIN (ratifié famille)
> **« L'IA propose, le code dispose. »** L'IA n'a pas la clé de la porte. Le code a le droit de vie et de mort sur n'importe quel ordre, et l'obligation de le raboter ou de le rejeter s'il dépasse les clous.
> - L'IA (hub, analyste, Cortana, Juge…) **ne passe JAMAIS d'ordre** (C2/C3 : 0 LLM dans le hot path, 1 GO = 1 vol).
> - Le disjoncteur est **Python pur, déterministe, sans LLM** — la dernière barrière.

## CE QUE FAIT LE DISJONCTEUR (2 niveaux, 1 fichier)

### A. BRIDAGE DYNAMIQUE (hard cap à la volée)
Tout ordre proposé (par HULK paper, par une future exécution, par un script) passe par le disjoncteur AVANT d'être écrit/fillé :
- `taille_autorisee = min(taille_proposee, plafond)` où `plafond = capital_total × pct_max_trade` (config).
- Si l'IA/le script demande 10 000 $ mais que le plafond est 2 500 $ → **l'ordre est RÉÉCRIT à 2 500 $** (pas refusé si l'analyse est bonne, pas exécuté au-delà).
- **Le disjoncteur ne crée JAMAIS d'ordre** : il réduit ou rejette, il ne déclenche pas (C3).

### B. COUPURE D'URGENCE (Mur de Fer)
- **Seuil : −1,5 % journalier** sur le portefeuille (perte cumulée du jour, toutes positions confondues).
- **⚠️ Dimensionnement (C7) :** le seuil absolu est `max(1.5%, MAX_GLOBAL_DD_PCT)` — la config garde `MAX_GLOBAL_DD_PCT=8` comme plafond dur combiné ACE+Hulk. Le −1,5 % est le déclencheur journalier, le 8 % est le plafond absolu qui ne peut être dépassé.
- Au déclenchement :
  1. **Coupe à la source** : bloque toutes les nouvelles requêtes d'ordres (fichier de verrou `STOP_ALL` + flag mémoire).
  2. **Annule les ordres pendants** (si l'exchange le permet — paper : purge du carnet).
  3. **Clôture les positions** ? NON par défaut (config `CLOTURER_SUR_MUR_DE_FER=0`) : le Mur de Fer GÈLE, ne liquide pas (sauf si config 1). La famille a dit « coupe les flux, annule les pendants, met en sécurité » — pas « liquide tout ».
  4. **Ordre au cockpit** : met la voilure ADA à 0, allume l'alarme (alerte vocale + `.urgent_alert.json`), écrit `strategie/disjoncteur_state.json` (ts, raison, perte, actions).
  5. **Persiste** : `disjoncteur_history.jsonl` (chaque ouverture/fermeture).

### Réarmement
- Manuel uniquement : fichier `strategie/REARMER_DISJONCTEUR` ou commande `python3 disjoncteur.py --rearmer`. Jamais auto (sinon on se refait la nuit).

## CONTRATS (fichiers)
| Fichier | Rôle |
|---|---|
| `Index_Maison/scripts/disjoncteur.py` | NOUVEAU — la logique (stdlib, déterministe, sans LLM) |
| `Index_Maison/strategie/disjoncteur_state.json` | état en direct (lu par cockpit + pont) |
| `Index_Maison/strategie/disjoncteur_history.jsonl` | historique des déclenchements |
| `Index_Maison/strategie/disjoncteur_config.json` | seuils (pct_journalier=1.5, pct_plafond_max=8, plafond_trade_pct, CLOTURER_SUR_MUR_DE_FER=0) |
| kill-switch lu : `Index_Maison/strategie/STOP` + `~/ace777-test-day1/Index_Maison/STOP_ALL` | le disjoncteur respecte et écrit ces fichiers |

## RÈGLES DE CODE (ACE777)
- Python 3.9+, **stdlib uniquement**. Écriture ATOMIQUE (mkstemp + os.replace). Idempotent (relançable sans doublon). Robustesse : aucun crash si fichier manquant/corrompu. Docstring de rôle en tête.
- **NE PAS toucher** à `paper_diprip.py` (moteur HULK), ni à `hub_prise_ia.py` (juste fini), ni au genesis ACE. Le disjoncteur est un **module externe** appelé/consulté, pas un patch du moteur.
- Interface : `python3 disjoncteur.py --check` (retourne 0/1 + état), `--bridage <taille_proposee>` (imprime taille autorisée), `--rearmer`, `--etat`. Mode `--watch` (boucle, intégré au superviseur) optionnel.

## INTÉGRATION (le codeur propose le diff exact)
1. `superviseur.sh` (ou un nouveau plist `com.ace777.disjoncteur.plist`) : lancer `disjoncteur.py --watch` en continu.
2. Pont cockpit (`cortana_cockpit_bridge.py`) : exposer `disjoncteur_state.json` (petite carte dans le cockpit, comme ADA).
3. HULK paper : **AVANT tout fill**, appeler `--bridage` — MAIS sans toucher à `paper_diprip.py` : le codeur propose le point d'insertion le moins invasif (wrapper ou import propre).

## FORMAT DE RÉPONSE EXIGÉ
- Bloc ```python complet fermé pour `disjoncteur.py`.
- Diffs EXACTS (avant → après) pour les intégrations.
- Section NOTES finale : choix faits, points d'attention, le point d'insertion HULK le moins invasif.
