#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC CHIEN DE GARDE au CODEUR (task codeur via hub) — conception only.

Règle maison (GO Christophe 10/09) : le codeur CONÇOIT (livre le code + tests),
RIEN n'est déployé en vol. L'exécution/déploiement = un GO famille séparé (V4).
"""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/SPEC_CHIEN_DE_GARDE_20260910.md")).read()

PROMPT = f"""Tu es le CODEUR ACE777. Une SPEC approuvée par Christophe t'est confiée
pour CONCEPTION : tu produis le code et les tests demandés, mais rien ne sera
déployé en vol sans un GO famille séparé (V4). Conçois donc chaque fichier comme
prêt à relire, pas à lancer.

Lis-la ATTENTIVEMENT puis produis les livrables demandés.

=== RÈGLES DE CODE ACE777 ===
- Python 3.9+, stdlib uniquement (pas de dépendances externes).
- Encodage UTF-8, docstring de rôle en tête de chaque fichier.
- Écriture ATOMIQUE (mkstemp + os.replace) pour tout fichier JSON.
- Kill-switch : vérifier Index_Maison/strategie/STOP et STOP_ALL avant toute écriture.
- Robustesse : aucun crash si fichier manquant/corrompu (repli propre).
- Idempotence : relançable sans doublons.
- NE PAS toucher au moteur (paper_diprip.py, universe_profils.json, defaults.env, PAPER_PAIRS).
- Anti-tempête : 1 alerte max par heure et par organe (état interne atomique).
- Voix : alerte via alerte_vocale.py EXISTANT (nohup détaché, killall say avant,
  edge_tts fr-FR-VivienneMultilingualNeural) — ne pas réinventer la voix.

=== LIVRABLES DEMANDÉS (cf. SPEC §5) ===
1. Index_Maison/scripts/chien_de_garde.py (NOUVEAU) — §2 complet : lit le registre
   (fail-fast si corrompu), mesure l'âge réel de chaque organe (mode pouls_direct
   OU produit), compare à fréquence_attendue × tolérance, crie aux 3 endroits
   (1 ligne MEMOIRE_COLLAB append-only + thermo/CHIEN_RAPPORT.json et .md datés +
   alerte_vocale.py nohup), anti-tempête 1h/organe, section grisaille sans cri,
   silence propre si kill-switch ou MAINTENANCE_PREVUE, écrit son propre rapport.
2. Index_Maison/scripts/generer_registre_organes.py (NOUVEAU) — §3 : scan des
   plists com.ace777.* (LaunchAgents + Index_Maison/plists/), extrait StartInterval
   réel, merge NON destructif avec criticite_organes.json, marque zone_grise si
   plist posé non chargé, versionne generated_at + md5 des plists scannés.
3. Index_Maison/strategie/criticite_organes.json (NOUVEAU, squelette) — ~15 organes
   CRITIQUES du jour 1 en mode=produit (hub, cockpit-http, veilleuse_synapses,
   superviseur-core, HULK paper, thermo, L2 snaps, cortana_watch, veille hub,
   disjoncteur, nourrir_disjoncteur, vigie_live, llm_gate_hub_bridge, chien).
4. Index_Maison/plists/com.ace777.chien-de-garde.plist (NOUVEAU) — StartInterval=300,
   RunAtLoad true, logs /tmp/chien.out.log + .err.log.
5. Index_Maison/thermo/CHIEN_RAPPORT.md (GABARIT) — sections : vivant/à l'heure ·
   vieillissant · grisaille · santé du chien.
6. PATCH MINUSCULE scripts/buffy_reveil.py (vault Obsidian) — section « Où on en
   est » lue depuis thermo/CHIEN_RAPPORT.md si présent (repli propre sinon).
7. Index_Maison/scripts/test_chien_de_garde.py — harnais 9 cas minimum (cf. SPEC §5.7),
   assertions dures, style selftest shadow (PASS/FAIL par cas, verdict final).

=== FORMAT DE RÉPONSE EXIGÉ ===
- Pour chaque fichier : bloc ```python (ou ```json ou ```xml) complet et fermé,
  précédé du chemin.
- Une seule section « NOTES » finale : choix faits, limites, ce que le chien ne voit pas.
Réponds en français, factuel."""

payload = json.dumps({
    "model": "gemini",
    "messages": [
        {"role": "system", "content": "Tu es le codeur senior du projet ACE777. Code propre, stdlib, robuste. Conception only : rien n'est déployé sans GO famille."},
        {"role": "user", "content": PROMPT + "\n\n=== SPEC COMPLÈTE ===\n" + SPEC},
    ],
    "max_tokens": 8000, "temperature": 0.2,
}).encode()

req = urllib.request.Request(HUB, data=payload,
                             headers={"Content-Type": "application/json"}, method="POST")
t0 = time.time()
with urllib.request.urlopen(req, timeout=None) as resp:
    d = json.loads(resp.read().decode())
content = d["choices"][0]["message"]["content"]
print(f"Réponse codeur reçue ({round(time.time()-t0,1)}s, {len(content)} chars)")

out = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_CHIEN_DE_GARDE_20260910.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Écrit : {out}")
