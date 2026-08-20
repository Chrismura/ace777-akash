# SPEC — TOUR 2 : TRANCHER SUR UN PROTOCOLE UNIQUE (20/08/2026)

Tu es membre de la famille ACE777. Au TOUR 1 (contestation), chacun de vous a
contesté le diagnostic de Buffy et proposé un protocole anti-validation-aveugle
(PAA-C1, SVE-C1, PZVC-1, P0-VERIFY, Hard Interlock, Protocole de l'Œil Blanc).
Vos 6 propositions convergent vers le même principe. Vous avez aussi demandé
des informations — elles sont fournies ci-dessous, factuelles.

## CE QUI EST DEMANDÉ — UNE SEULE QUESTION

**Fusionnez vos 6 protocoles en UN SEUL protocole opérationnel**, applicable
par les wrappers (genesis INTACT, C1), mesurable, borné, testable. Répondez en
2 parties :

### PARTIE 1 — LE PROTOCOLE UNIQUE (obligatoire)
Donnez le protocole final sous forme de RÈGLES numérotées (max 8), chacune
avec : (a) la règle exacte, (b) où elle s'applique (wrapper/script/point
d'entrée), (c) comment on la TESTE (preuve de non-régression), (d) son coût.
Le protocole doit inclure au minimum vos points communs :
1. Interdiction de valider ("c'est corrigé", "le système tourne", "c'est sain")
   sans la sortie brute d'une commande système de vérification.
2. Fail-fast absolu au démarrage (aucun lancement si un garde-fou manque).
3. Miroir inversé / Red Team (chercher la preuve d'échec avant de conclure).
4. Double validation d'état (fichier présent ≠ service actif ; 2 checks indépendants).
5. Le terminal a toujours raison (si IA et réel divergent → le réel gagne, l'IA crie).

### PARTIE 2 — TRANCHER LES DIVERGENCES (obligatoire)
Vos propositions divergent sur des points précis. TRANCHER pour chacun :
(a) Un seul démon watchdog unifié (Rust/Python) vs plists launchd multiples ?
(b) L'alerte vocale seule suffit-elle, ou faut-il un canal externe (webhook) ?
(c) Le verrou md5 anti-patch-en-plein-run : obligatoire partout ou seulement
    sur le champion ?
(d) Faut-il un hook git pre-commit exécutant sante_index.py, ou un check
    runtime uniquement ?
(e) 72h d'autonomie sans intervention : est-ce le critère de validation final ?

================ RÉPONSES À VOS DEMANDES D'INFORMATIONS (TOUR 1) ================
(contenu : REPONSES_ENVOI_FAMILLE_2026-08-20.md)

## RÈGLES
- CLAUSE PERMANENTE : ne te contente pas de valider — propose mieux si prouvable.
- Périmètre : genesis INTACT (C1), wrappers/molettes/protocoles seulement.
- Format : VERDICT · CONFIANCE · HYPOTHÈSES · CE QUI CHANGERAIT L'AVIS ·
  AMÉLIORATION PROPOSÉE · SYNTHÈSE (5 lignes max). Français, factuel.


================ REPONSES AUX DEMANDES D INFORMATIONS ================
# RÉPONSES AUX DEMANDES D'INFORMATIONS — FAMILLE (20/08/2026)

> Réponses factuelles aux informations demandées lors de la consultation de
> CONTESTATION (CONSULTATION_FAMILLE_CONTESTATION_META_20260820).
> Demandeurs : JUGE, GEMINI, DEEPSEEK, GROK (dms_veille) · DEEPSEEK+JUGE
> (GO_VORTEX_V2) · ULTRA (sante_index + superviseur).

---

## DEMANDE 1 — GO_VORTEX_V2.sh : le fail-fast est-il bloquant ? (DEEPSEEK, JUGE)

**Réponse : OUI — hard exit, pas informatif.**

```bash
# GO_VORTEX_V2.sh (extrait, lignes 43-58)
# FAIL-FAST SUPERVISION (exigence famille 20/08) — C1 : genesis intact.
_PLISTS_SUPERVISION="com.ace777.sante-index com.ace777.veille-degradation com.ace777.dms-veille com.ace777.superviseur-core com.ace777.vigie-live"
_absents=""
for _p in $_PLISTS_SUPERVISION; do
  launchctl list 2>/dev/null | grep -q "$_p" || _absents="$_absents $_p"
done
if [ -n "$_absents" ]; then
  fail "FAIL-FAST SUPERVISION: plist(s) de garde-fou NON CHARGÉE(S):$_absents — refuse de lancer le moteur sans filet (leçon 19/08)."
fi
echo "[FAIL-FAST] supervision OK: 5/5 plists de garde-fou chargées."
```

- `fail()` = `echo "FAIL: ..." >&2; exit 1` → **le script s'arrête avant tout lancement**.
- En plus : garde-fou filet STOP_MARKET (BPS < 20 → refus), md5 champion vérifié.
- Testé 20/08 : 5/5 présentes → passe ; plist simulée absente → refus confirmé.

---

## DEMANDE 2 — Logs du test de chaos `--test-panne` de dms_veille.py (GEMINI, DEEPSEEK, GROK, JUGE)

**Réponse : le test a été exécuté et l'alerte est réellement partie.**

Sortie console du test (20/08 13:58 UTC) :
```
[DMS] alerte vocale lancée : veille_degradation test de chaos : brique simulée morte
[DMS] ALERTE — veille_degradation test de chaos : brique simulée morte
```

Rapport écrit par le DMS lui-même (canal indépendant), `Index_Maison/data/alertes/DMS_VEILLE.json` :
```json
{
  "timestamp": ...,
  "date": "2026-08-20 13:58:xx",
  "source": "dms_veille (Dead Man's Switch externe, exigence famille 20/08)",
  "brique": {"statut": "TEST_PANNE_SIMULEE", "detail": "test de chaos : brique simulée morte"},
  "anomalies": ["veille_degradation test de chaos : brique simulée morte"],
  "statut": "ALERTE"
}
```

**Précision honnête** : le process d'alerte vocale (`alerte_vocale.py`) est lancé
via `subprocess.Popen` ; en exécution directe dans un terminal de test, le shell
du superviseur l'a tué à la fin de la commande (limitation du banc de test, pas
du DMS). Depuis, le DMS tourne via launchd (`com.ace777.dms-veille`, cycle 60 s)
— ses enfants survivent. **Chaos test 2 à prévoir sous launchd pour preuve
complète de bout en bout** (proposé, non encore exécuté).

---

## DEMANDE 3 — sante_index.py : gestion des faux positifs / zombies (ULTRA)

**Réponse** : `proc_vivant()` vérifie `launchctl list` (label) PUIS `pgrep -fl`.
Un label launchd présent = service chargé (pas zombie) ; le pgrep n'est qu'un
complément. Seuils : DÉGRADÉ (orange) entre seuil et 2× seuil — ralentissement
sans crier ; ALERTE seulement au-delà. Historique append-only
(`data/alertes/sante_index.log`) pour distinguer panne transitoire/durable.
MAINTENANCE_PREVUE respectée (pas d'alerte en maintenance). État actuel :
**8/8 chaînes OK**.

**Limite connue (honnête)** : un process qui tourne mais qui écrit un fichier
frais alors que sa logique est fausse (ex. : vigie vivante mais donnée erronée)
n'est pas détecté — c'est précisément le trou que la classe 3 (fausse sécurité)
couvre via les plages d'indicateurs de `veille_degradation.py`. Les deux se
complètent ; aucun ne détecte seul l'ensemble.

---

## DEMANDE 4 — Log de mort du superviseur.sh (19/08 14:09:12) (ULTRA)

**Réponse : le log montre une mort SANS trace — la classe 1 en preuve directe.**

Dernières lignes AVANT la mort (19/08) :
```
2026-08-19 14:05:11 - vérif | hub:OK | vigie:OK | cockpit:OK
2026-08-19 14:06:11 - vérif | hub:OK | vigie:OK | cockpit:OK
2026-08-19 14:07:11 - vérif | hub:OK | vigie:OK | cockpit:OK
2026-08-19 14:08:12 - vérif | hub:OK | vigie:OK | cockpit:OK
2026-08-19 14:09:12 - vérif | hub:OK | vigie:OK | cockpit:OK   ← DERNIÈRE
```

Puis **SILENCE TOTAL** — aucune trace d'erreur, aucun exit code, aucune stack
trace. Le superviseur.sh (lancé manuellement, sans plist) est mort sans laisser
de message. Reprise seulement le 20/08 14:01 (relance par Buffy après l'audit).

**Cause racine probable** : tué par le système (pression mémoire/charge) —
comme le run du 19/08 tué pour mémoire saturée. Aucune alerte possible : il
n'était couvert par AUCUNE plist de relance (le trou A2). Depuis : relancé via
launchd (`com.ace777.superviseur-process`) + surveillé par sante_index + DMS.

---

