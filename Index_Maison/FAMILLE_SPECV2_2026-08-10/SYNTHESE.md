# ⚖️ SYNTHÈSE FAMILLE — SPEC V2 setup 3 étages (10/08/2026)

## Verdicts

| Membre | Task | Verdict |
|---|---|---|
| GEMINI | audit.protocol | **GO AVEC RÉSERVES** (3 réserves) |
| JUGE | signets.juge | **GO AVEC RÉSERVES** (5 réserves) |

→ **Les deux voix convergent : la SPEC V2 est saine mais doit intégrer des
blindages avant le passage au code** (loi 1quinquies : les réserves doivent
être intégrées → re-validation → GO Christophe).

---

## 📋 RÉSERVES CONSOLIDÉES (8, dédoublonnées, priorisées)

### 🔴 P1 — Fiabilité de state.json (les 2 membres sont d'accord)
1. **Champ de fraîcheur** : state.json doit porter un statut de santé des feeds
   sources — `"status": "HEALTHY" | "STALE" | "DEGRADED"` (ex. live.json figé
   depuis > 15 s → STALE). [GEMINI + JUGE]
2. **Hash d'intégrité** : ajouter `feed_hash` (SHA-256 des 4 feeds agrégés) dans
   state.json pour détecter corruption/tampering. [JUGE]
3. **Fallback feeds bruts** : si state.json absent ou hash invalide → le
   superviseur lit temporairement mission.json + cortana_feed.json + live.json
   et loggue un avertissement. [JUGE]
4. **Tolérance aux pannes du générateur** : try/catch robuste dans
   system_state_generator.py — un feed corrompu ne doit JAMAIS bloquer la mise
   à jour globale de state.json. [GEMINI]

### 🟠 P2 — Latence de réaction
5. **Cadence state.json : 2 min** (au lieu de 5 min) OU mise à jour incrémentale
   à chaque changement de feed — pour que le superviseur (cycle 30 min) voie une
   anomalie au pire 32 min après, pas 35. [JUGE]

### 🟡 P3 — Mirofish (réversibilité)
6. **Documenter la ré-activation** : README dans DESACTIVES_2026-08-10/ avec la
   procédure exacte (restaurer plist, retirer skip_check, launchctl load) pour
   pouvoir réactiver Mirofish sans modification de code. [JUGE]

### 🟡 P4 — Vocal (compatibilité)
7. **Vérification de version du cœur Rust** : lecture d'un fichier VERSION dans
   crypto-voice-assistant-core/ par cortana_cockpit_bridge.py → alerte si
   incompatibilité. [JUGE]

### 🟢 P5 — Contrôle backup léger
8. **I/O légères** : contrôle de présence par métadonnées (os.path.exists /
   stat) à chaque cycle 30 min, SANS lecture récursive ; calcul de taille totale
   espacé (toutes les 6 h) ; idéalement manifeste + hash léger par dossier. [GEMINI + JUGE]

---

## ✅ Ce que la famille a validé (à préserver dans l'exécution)
- Contrat d'harmonie inter-étages (4 feeds, schéma standard, state.json = seule
  source de vérité du superviseur) → **architecture saine** ✅
- Option (c) Mirofish : désactivé, skip_check, code en backup ✅
- Périmètre vocal : 2 services + 9 scripts protégés, cœur Rust hors périmètre ✅
- Contrôle backup : présence + taille dans state.json/cockpit ✅

## 🔜 Prochaine étape (loi 1quinquies)
Intégrer les 8 réserves dans la SPEC V2 (→ SPEC V2.1) → re-soumettre au JUGE
pour validation → GO Christophe → code (Étape 1 : state.json).
