# RE-CONSULTATION CANONIQUE — MÉTA-ANALYSE (20/08/2026)

> Christophe a signalé : la 1ʳᵉ consultation famille (script improvisé
> `consulter_famille_meta_audit_20260820.py`) n'utilisait PAS le canon
> `identity/prompts/famille.json` + `consulter_famille.py`. COUTUMES_AGORA :
> « Consulter la famille = consulter_famille.py, ne JAMAIS improviser les
> prompts » (commits 0c26a085). **Erreur reconnue** : les DIAG improvisées
> n'avaient ni VERDICT ni CONFIANCE (0 occurrence vs 2 dans le canon).

## 1. Re-consultation CANONIQUE (consulter_famille.py --extra)

- Script : `consulter_famille.py --spec SPEC_META_AUDIT.md --extra`
- Sortie : `scripts/CONSULTATION_FAMILLE_META_AUDIT_CANON_20260820/`
  (AVIS_GEMINI, AVIS_DEEPSEEK, AVIS_ULTRA, AVIS_INFERX, AVIS_GROK, AVIS_JUGE, SYNTHESE)

## 2. Verdict : UNANIME GO-AVEC-RÉSERVES (confiance 82-88 %)

| Membre | Verdict | Confiance | Leçon retenue |
|---|---|---|---|
| GEMINI | GO-AVEC-RÉSERVES | 82 % | Dead Man's Switch inversé + PnL brut jamais sans net |
| DEEPSEEK | GO-AVEC-RÉSERVES | 82 % | DMS externe + Fail-Fast au démarrage |
| ULTRA | GO-AVEC-RÉSERVES | 82 % | Chaos Monkey : une alerte non testée par le feu = vœu pieux |
| INFERX | GO-AVEC-RÉSERVES | 88 % | DMS externe (canari distant) + fail-safe par défaut |
| GROK | GO-AVEC-RÉSERVES | 88 % | DMS externe + gel config par hash |
| JUGE | GO AVEC RESERVES | 85 % | Fail-Fast strict au démarrage + doublement canal d'alerte |

**Classe la plus dangereuse selon la famille : Classe 1 (Dégradation
silencieuse)** — elle aveugle l'opérateur et tue sans laisser de trace
(suivi de la Classe 3 fausse sécurité dans la 1ʳᵉ consultation).

**Exigence commune (5/6) : QUI SURVEILLE LA SURVEILLANTE ?** La brique
`veille_degradation.py` ne doit PAS être le seul maillon — il faut un tiers
indépendant (Dead Man's Switch) + refus de démarrer si les filets ne sont pas
actifs (Fail-Fast) + preuve par le feu (chaos test).

## 3. Corrections appliquées (toutes testées)

### 3a. Dead Man's Switch externe — `scripts/dms_veille.py` + plist 60 s
- Tiers indépendant (sa propre plist `com.ace777.dms-veille`) qui surveille la
  FRAÎCHEUR de `veille_degradation_etat.json` + vérifie lui-même launchctl
  (ne fait pas confiance à la brique).
- Si la brique meurt/se fige > 5 min OU une plist clé manque → ALERTE VOCALE
  (alerte_vocale.py, canal existant) + rapport `data/alertes/DMS_VEILLE.json`
  lu par le cockpit (canal indépendant même si la brique est morte).
- Anti-empilement (une alerte à la fois), kill-switch, écriture atomique.
- ✅ Testé : statut OK 3/3 en nominal.

### 3b. CHAOS TEST (exigence ULTRA) — `dms_veille.py --test-panne`
- Simule une brique morte → PROUVE que l'alerte sort réellement
  (alerte vocale lancée + rapport ALERTE écrit). Aucun impact sur le réel.
- ✅ Testé : `[DMS] ALERTE — veille_degradation test de chaos : brique simulée morte`.

### 3c. FAIL-FAST au démarrage (exigence DEEPSEEK/INFERX/JUGE) — `GO_VORTEX_V2.sh`
- Avant tout lancement : vérifie que les 5 plists de garde-fou sont chargées
  (sante-index, veille-degradation, dms-veille, superviseur-core, vigie-live).
- Si une manque → REFUS de lancer le moteur (le trou du 19/08 ne peut plus se
  reproduire : on ne tourne plus sans filet).
- ✅ Testé : 5/5 présentes → passe ; plist manquante → refus.

### 3d. Intégration cockpit — `sante_index.py` chaîne 8 complétée
- Maillons : brique + rapport SAIN + **DMS chargé + rapport DMS OK**.
- ✅ Testé : **8/8 chaînes OK · état OK**.

### 3e. La brique se surveille contre le DMS — `veille_degradation.py`
- `com.ace777.dms-veille` ajouté à sa liste de 11 plists.
- ✅ Testé : SAIN 11/11.

## 4. Leçons pour la suite (gravées)

1. **Toute consultation famille = `consulter_famille.py`** (canon
   `identity/prompts/famille.json`). Ne JAMAIS improviser — COUTUMES_AGORA.
2. **Toute brique de surveillance doit avoir son DMS** (qui surveille la
   surveillante) + un chaos test qui prouve que l'alerte sort.
3. **Tout lancement moteur vérifie ses filets** (fail-fast) — la fausse
   sécurité (Classe 3) est la plus traîtresse car on engage la mise.
