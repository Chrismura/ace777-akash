# DOSSIER DE VALIDATION — LE COCKPIT ACE777 (11/08/2026)

> Objet : validation en profondeur des derniers setups du cockpit.
> Exigence Christophe : le cockpit doit être **INcASSABLE, RÉSILIENT, AUTO-ADAPTATIF, AUTO-RÉPARANT, AUTO-INTELLIGENT** — c'est le seul setup pour la réalité avec de l'argent.

---

## 1. CE QUI A ÉTÉ LIVRÉ RÉCEMMENT (factuel, vérifié par exécution)

### A. Veille quotidienne élargie — `veille_hub.py` (launchd 07:00)
- Scan de **9 sources** : openrouter (:free), nvidia, inferx, puter, omniroute (43 pools), github awesome lists, huggingface récents, huggingface trending, github search, rss.
- Chaque source est **isolée** (try/except, timeout 20-25s, jamais bloquant). Scan complet en 4s.
- **Principe mise à jour** : ne liste QUE les modèles non intégrés (`providers.json`). Modèle déjà intégré → disparaît de la liste. C'est un check de mise à jour, pas une chasse.
- Rapport : `VEILLE_HUB_<date>.md` avec sections `### ` + lignes `- `, section INTEGRATION AUTO exclue.
- Kill switch `STOP_HUB` respecté.

### B. Matinée automatisée — `brief_offres.py` (launchd 08:10, après le brief 08:00)
- Lit `VEILLE_HUB_<date>.md`, extrait les nouvelles offres, fait rédiger un texte vocal FR par le hub (gemini→nvidia), parle via Vivienne (edge_tts + afplay).
- **Silence d'or** : aucune offre → sortie silencieuse code 0. Jamais de vocal vide.
- Corrigé en intégration : syntaxe py3.10→3.9 (`from __future__ import annotations`), chemin maison, mécanisme TTS exact de cortana_brief.

### C. Onglet STRATÉGIE du cockpit — V2 (11/08)
- Bannière d'état globale : **🟢 tout est à jour / 🟡 N nouvelles / ⚠ erreur source / ◌ veille pas passée**.
- **Cartes fournisseurs** : une carte par fournisseur connu (nom, pastille d'état, compteur, « à jour / nouveau / erreur ») — le check de mise à jour en un clin d'œil.
- **Liste des offres groupée par section**, cases à cocher (max 5), compteur X/5, bouton DÉCOLLER ▶.
- **Panneau exploration** : nouveaux endroits détectés (github/hf/rss) — non testables, affichés à part.
- Ligne « Dernier DÉCOLLAGE » (ts + nb de choix).
- Design thème cockpit (Orbitron, ambre/acid, glow, transitions, scrollbar, responsive ≤1050px).

### D. Backend bridge — `cortana_cockpit_bridge.py` (port 17777, launchd)
- Endpoints : `GET /offres` (dashboard complet : total, sections[{name,count,err,testable}], offres max 25, decollage), `POST /decoller` (écrit CHOIX_OFFRES.json atomiquement tmp+replace, lance `eval_offres.py --choix` en background, max 5 choix), + status/mission/alerts/justesse/préflight existants intacts.
- `GET /offres` sans fichier veille → payload vide ok (bannière « veille pas encore passée »).
- Filtre anti-fuite : section INTEGRATION AUTO exclue, lignes ERR: → statut erreur de section.
- `eval_offres.py --choix` : filtre les candidats aux seuls modèles cochés (37 candidats → N cochés). Cœur A/B intact.

## 2. ÉTAT VÉRIFIÉ PAR EXÉCUTION AUJOURD'HUI

- Compilation Python 3.9 : OK (bridge, eval_offres, veille_hub, brief_offres).
- Node --check sur le JS du cockpit : OK (6 scripts, 6 sections, balises équilibrées).
- GET /offres → total 109, 10 sections comptées (openrouter 11, nvidia 15, inferx 6, puter 5, omniroute 15, github lists 15, hf récents 3, hf trending 15, github search 10, rss 14), offres plafonnées 25.
- POST /decoller → « Évaluation lancée sur 1 offre(s) », CHOIX_OFFRES.json écrit atomiquement.
- Endpoints existants (status, mission, alerts, justesse) : intacts.
- Backups `.bak-f2-*` et `.bak-stratv2-*` de chaque fichier avant modification.
- Système vivant : hub OK, vigie_live 1 process, bridge relancé PID 60441.

## 3. QUESTIONS À LA FAMILLE (répondre sans complaisance, factuel)

1. **INcASSABLE** : quelles sont les failles qui peuvent casser le cockpit ou le laisser muet (bridge down, hub down, fichier veille absent/corrompu, JS exception, quota épuisé) ? Décris chaque scénario de panne et si le comportement actuel est correct.
2. **RÉSILIENT** : que manque-t-il pour qu'une panne ne bloque JAMAIS la journée ? (timeouts, fallbacks, relance automatique, données en cache)
3. **AUTO-RÉPARANT** : qu'est-ce qui doit se réparer seul (sans Christophe) et comment concrètement ? (launchd KeepAlive, health-check, fichiers orphelins)
4. **AUTO-ADAPTATIF** : la veille s'adapte-t-elle vraiment aux nouveaux fournisseurs ? Comment un provider découvert hier devient-il testable demain ? Y a-t-il un maillon manquant ?
5. **AUTO-INTELLIGENT** : propose les 3 améliorations à plus forte valeur (pas de l'usine à gaz, du concret, du mécanique).
6. Termine par :
   VERDICT FINAL : <GARDER | GARDER AVEC GARDE-FOUS RENFORCÉS | REFAIRE>
   CONFIANCE : <haute|moyenne|faible>

## 4. CONTEXTE TECHNIQUE

- macOS, Python 3.9.6 (aucune syntaxe 3.10+ tolérée), pas de dépendances tierces côté scripts maison.
- Hub local : http://127.0.0.1:11435 (4 providers : gemini, nvidia, juge, puter-grok, qwen-local en pause).
- Cockpit : `~/ace777-test-day1/Index_Maison/cockpit/index.html` servi par `cockpit_http_server.py` (port 17800, PID stable depuis le début).
- Bridge : `~/ace777-test-day1/Index_Maison/scripts/cortana_cockpit_bridge.py` (port 17777).
- Veille : `veille_hub.py` 07:00 → brief 08:00 → `brief_offres.py` 08:10.
- Évaluation : `eval_offres.py` (A/B en observation, jamais actif direct).
