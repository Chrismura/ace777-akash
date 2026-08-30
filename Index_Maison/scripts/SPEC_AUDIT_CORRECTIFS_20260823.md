# SPEC — AUDIT FAMILLE DES CORRECTIFS DU 23/08/2026

**Auteur spec** : Buffy (assistante)
**Destinataire** : LA FAMILLE (6 membres — vous donnez votre avis, ne touchez à rien)
**Date** : 23/08/2026 — vérification des correctifs appliqués aujourd'hui
**Contexte** : Christophe demande à la famille de vérifier les dernières mises à jour
et les setup de correction appliqués ce jour (23/08), après des semaines de
« boucles de destruction » systémiques (crédits éclatés, évaluation IA morte,
corrections jamais durables).

---

## PROBLÈMES RACINES IDENTIFIÉS (23/08)

1. **Crédits éclatés** : 9+ plists one-shot avaient `KeepAlive`+`RunAtLoad` injectés
   → launchd relançait les scripts en boucle infinie (roulement_ia.py plantait :
   dépaquetage 2-tuple vs 3-tuple de `sante_provider` ; sniffer envoyait
   `analyse.profonde` toutes les ~5 s ; eval_offres testait des providers en boucle).
   Hier : 2948 appels cloud (budget = 624), dont 2607 sur Mistral payant.
2. **Mode tempête quasi permanent** : `_mode_tempete_actif()` du hub s'activait sur
   toute alarme fraîche (< 1 h) → coupes de budget désactivées en permanence →
   le filet universel pioche tout.
3. **Boucle d'apprentissage MORTE 5 jours** : la coupure des briefs du 19/08
   (volontaire : briefs = bruit) avait emporté PAR ERREUR la production
   (`analyste-cadence`), le professeur (`discipline-quotidienne`) et le scoreur
   (`verif-predictions`) → 0 analyse depuis le 18/08 20:30, justesse figée 46,1 %.
4. **Registre mécanique orphelin** : 2713 lignes dont 2642 DOUBLONS, 2700 échues
   jamais scorées, aucun scoreur branché sur ce registre.

---

## CORRECTIFS APPLIQUÉS (à vérifier)

### C1. Hub — `_mode_tempete_actif()` (prise-ia/hub_prise_ia.py)
Avant : toute `alarme.json` fraîche (< 1 h) = tempête → réserve storm ouverte
(quota cloud contourné). Après : seules les secousses prix ≥ 1 % ouvrent la
réserve ; news et alarmes bénignes (0,5 %/60 s, volume x3) ne la déclenchent plus.
Tests ciblés OK (0,01 %/0,5 %/news/vieille → pas tempête ; 2 % fraîche → tempête).

### C2. Plists one-shot réécrits (KeepAlive/RunAtLoad retirés, horaires conservés)
- 1ʳᵉ passe : `veille-hub`, `queueoffres`, `eval-offres`, `roulement-ia`, `routeur-auto`
- 2ᵉ passe : `sniffer-matin`, `sniffer-ny`, `superviseur`, `couleur-regime-score`
- Vérifié : agents rechargés à PID « - », plus aucun appel entrant en boucle.
- `superviseur.sh`/`superviseur_core.sh` (vrais démons while True) → KeepAlive CONSERVÉ.

### C3. `roulement_ia.py` — fix crash
`sante_provider()` renvoyait 3 valeurs mais `main()` n'en dépaquetait que 2 →
ValueError → boucle KeepAlive. Dépaquetage corrigé + retour cohérent. Exit 0 vérifié.

### C4. Boucle d'apprentissage relancée
- Réactivés : `analyste-cadence` (08:30+20:30, production cortana_analyse.py)
  + `discipline-quotidienne` (07:15, professeur score_justesse + alerte boucle affamée).
- Les vrais briefs-bruit restent désactivés (brief-matin, cortana.horaire, etc.).
- `superviseur_auto.py` : `JOBS_ATTENDUS` retiré brief-matin + cortana.horaire
  (désactivés volontaires) → fin des escalades « jobs invalides » en boucle.

### C5. Surveillance étendue à l'apprentissage — `veille_degradation.py` + DMS
Avant : le DMS (Dead Man's Switch, exigence famille 20/08) ne couvrait QUE le
trading (11 plists) → l'apprentissage pouvait mourir sans alerte (cas réel : 5 jours).
Après : ajout de `analyste-cadence`, `discipline-quotidienne`, `scoreur-registre`
aux plists critiques + heartbeats `analyses_cortana` (48 h), `justesse_v2` (36 h),
`justesse_registre` (36 h) → 14/14 plists OK, alerte DMS déclenchée en réel.

### C6. Registre mécanique rendu utile — `scoreur_registre_mecanique.py` (nouveau)
- Dédup : 2713 lignes → 71 prédictions uniques (2642 doublons éliminés).
- Convention (affinée) : échéance = FIN de journée (23:59:59Z) ; score TOUCH
  (le prix a-t-il ATTEINT la cible pendant la fenêtre [création → échéance]) ;
  filtre d'information : prédiction déjà vraie à la création = ⚪ DÉJÀ VRAIE,
  exclue de la justesse (tautologie sans valeur).
- Résultat : 68 échues → 60 ⚪ tautologies + 8 vrais paris (6 ✅ / 2 ❌) = 75 %.
- `analyste.py` : dédup à l'écriture (clé normalisée au jour) + échéance T23:59:59Z.
- Plist `com.ace777.scoreur-registre` (07:30) + heartbeat surveillé.

### C7. (À vérifier séparément) 502 sur `cortana.analyse`
Cause constatée : saturation des providers gratuits (429 en cascade : Gemini,
Groq, HuggingFace blacklistés, NaraRouter timeout) — pas un bug de code du hub.
Le hub répond 200 sur les petits prompts, 502 sur les gros payloads quand la
chaîne entière est en rate-limit. Non corrigé (état transitoire à surveiller).

---

## QUESTIONS À LA FAMILLE

Q1. Les correctifs C1-C6 sont-ils cohérents et durables ? Y a-t-il un risque de
réintroduire une boucle ou une dégradation silencieuse ?
Q2. La convention de scoring du registre (C6) est-elle saine ? (échéance fin de
journée + touch + exclusion des tautologies)
Q3. Le 502 sur `cortana.analyse` (C7) : faut-il agir (ex. élargir la chaîne de
fallback, réserver un quota pour l'apprentissage) ou attendre la fin de la
saturation ?
Q4. Y a-t-il un maillon de la chaîne d'apprentissage qui n'est toujours PAS
surveillé (leçon 20/08 : « chaque brique de surveillance doit avoir son DMS ») ?
