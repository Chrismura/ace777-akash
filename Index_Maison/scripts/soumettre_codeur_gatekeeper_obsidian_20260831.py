#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""soumettre_codeur_gatekeeper_obsidian_20260831.py — Soumet au CODEUR (canal
code.ia) le design du GATEKEEPER pour le pont CLI Obsidian (GO Christophe 31/08,
après validation famille 3/3). Le pont doit valider le contenu AVANT d'écrire :
les agents génèrent un JSON structuré (type + frontmatter + corps), le pont
compile en markdown conforme au schéma du type, rejet si non conforme.

Buffy supervise le patch du codeur avant intégration (comme Phase 1 moteur léger).
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_CODEUR_GATEKEEPER_OBSIDIAN_20260831")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 31/08/2026) — IMPLÉMENTATION GATEKEEPER PONT CLI OBSIDIAN

=== 1. CE QU'ON A DÉJÀ ===
`obsidian_cli_bridge.py` (Index_Maison/scripts/) : pont Python qui écrit dans le
vault Obsidian via la CLI officielle (obsidian-cli v1.13.7, l'app doit tourner).
Fonctions actuelles : write_note(title, content, folder), append(path, content),
read(path), is_alive(), status(). Déjà en place :
- queue séquentielle (threading.Lock) — une écriture à la fois
- timeout 3s par commande CLI + read-back hash (ne croit pas exit code 0)
- fallback disque direct dans le vault si CLI injoignable (fail-open absolu)
- circuit breaker : 3 échecs CLI → disque pur 15 min
- audit jsonl (.ace777_bridge_audit.jsonl) de chaque écriture

MAIS : le pont transporte les octets sans regarder le contenu. Les agents
(~15 scripts) écrivent du markdown brut sans frontmatter → vault non structuré
(0 frontmatter sur 60 fiches, 1341 notes orphelines sur 1733).

=== 2. CE QUE LA FAMILLE A DÉCIDÉ (3/3 : gemini, juge, deepseek) ===
Le GATEKEEPER : le pont doit valider le contenu AVANT d'écrire.
- Un agent ne génère plus un .md brut : il génère un OBJET JSON structuré
  {type, frontmatter (dict), body (str)}.
- Le pont COMPILE ce JSON en markdown conforme au template du type ET VALIDE
  contre un SCHÉMA : type reconnu, propriétés obligatoires présentes, valeurs
  autorisées (ex. statut ∈ {brouillon, valide, archive}).
- Si non conforme → rejet (pas d'écriture), message d'erreur clair pour l'agent.
- « C'est la machine qui éduque les IA, pas l'inverse. »

4 TYPES STRICTS (pas 50 comme l'expert) :
1. actif : {actif (requis), statut (brouillon|valide|archive), date, source, tags}
2. signal : {actif (requis), direction (long|short|neutral), statut (traite|ignore|en_cours), date}
3. synthese_ia : {type_consultation (requis), membres (liste), date, statut}
4. journal : {date, source (agent|script), statut}
Chaque type a : dossier cible, propriétés requises, valeurs autorisées, et un
template markdown (frontmatter YAML + sections).

Day Zero rule : les 1733 notes EXISTANTES ne sont PAS migrées. Le gatekeeper
s'applique aux NOUVELLES écritures via write_note. On garde append() pour les
journaux existants (sans validation stricte).

=== 3. VOTRE MISSION (codeur expert) ===
Produis le PATCH COMPLET de obsidian_cli_bridge.py qui ajoute le gatekeeper :

A) SCHEMAS : un dict TYPES = {type: {folder, required_props, allowed_values,
   template}} pour les 4 types ci-dessus. Le template produit le frontmatter YAML
   (ordonné, échappé) + le corps markdown.

B) NOUVELLE FONCTION write_typed(type, data, title=None) → dict {status,
   path, errors[]} :
   - valide le type, les required_props, les allowed_values
   - compile le markdown (frontmatter + body) via le template
   - appelle l'écriture existante (CLI + read-back + fallback disque) en gardant
     TOUTE la logique actuelle (queue, timeout, cb, audit)
   - si validation KO : {status: "REJECTED", errors: [...]}, AUCUNE écriture
   - si fallback disque : le fichier .md compilé (pas du brut)

C) write_note() EXISTANT : garde sa signature (title, content, folder) pour ne
   pas casser les ~15 scripts actuels, MAIS si content contient déjà un
   frontmatter YAML valide avec "type:", il passe par la validation du type.
   Sinon comportement actuel (écriture brute) + audit avec note "no_type".

D) ERRORS CLAIRES pour les agents : chaque erreur de validation doit être
   actionable (ex: "statut invalide: 'foo', attendu brouillon|valide|archive").

E) YAML ESCAPING correct dans le frontmatter compilé (guillemets, valeurs
   multi-lignes, listes).

CONTRAINTES :
- Python 3.9 (pas de match, pas de | types), stdlib uniquement (pas de PyYAML —
  écrire un mini-émetteur YAML pour le frontmatter simple).
- Ne PAS casser les fonctions existantes (read, append, is_alive, status).
- Ajoute des tests unitaires (validation OK/REJECTED, compilation markdown,
  escaping) dans un bloc if __name__ == "__main__" ou un commentaire de test.
- Donne le patch COMPLET (fichier entier ou diff clair), pas juste des extraits.

Réponds en français, avec le code exact prêt à intégrer."""
# (le reste suit le pattern : ask_codeur + écriture dans OUT)


def ask_codeur(timeout=300):
    payload = json.dumps({
        "task": "code.ia",
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 4000, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    alive = time.time() + timeout
    while time.time() < alive:
        try:
            with urllib.request.urlopen(req, timeout=240) as resp:
                d = json.loads(resp.read().decode())
            return d["choices"][0]["message"]["content"], d.get("provider", "?")
        except Exception as e:
            time.sleep(3)
            last = e
    raise last


def main():
    try:
        content, provider = ask_codeur()
        f = os.path.join(OUT, "RESPONSE_CODEUR.md")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(f"# CODEUR (provider {provider})\n\n{content}\n")
        print(f"[OK] CODEUR -> {f} ({len(content)} chars)")
    except Exception as e:
        print(f"[ERR] CODEUR: {e}")


if __name__ == "__main__":
    sys.exit(main())
