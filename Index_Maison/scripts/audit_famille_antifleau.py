#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — chantier ANTI-FLÉAU timeout hub début de session (13/08).
Chaque membre reçoit : le problème, les corrections C1-C3 appliquées, le code réel.
Verdict attendu : GO / GO AVEC RÉSERVES / NON, + suggestions logique/perf/stabilité.
"""
import json
import os
import sys
import time
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.expanduser("~/ace777-test-day1/Index_Maison/AUDIT_ANTIFLEAU_2026-08-13")
os.makedirs(OUT, exist_ok=True)

FAMILLE = [
    ("audit.protocol", "GEMINI"),
    ("mission", "DEEPSEEK"),
    ("signets.juge", "JUGE"),
    ("ultra.analyse", "ULTRA"),
    ("inferx.analyse", "INFERX"),
    ("supervise.decision", "GROK"),
]

BRIEF = """Tu es membre de la FAMILLE de validation ACE777 (audit qualité, niveau hedge fund suisse).
Audite ce chantier de CORRECTION DE BUG : le fléau du timeout hub en début de session.

## PROBLÈME (confirmé par les logs du 13/08, boot machine après coupure batterie)
Le hub (launchd RunAtLoad) démarre AVANT que le réseau soit prêt. Les premiers appels
échouent en DNS (Errno 8) / timeout SSL. Ensuite :
1. La PATIENCE (retry x3, timeout plafonné 900s) transformait une panne RÉSEAU en
   attente de 12-25 min PAR PROVIDER (jusqu'à 80 min avec le filet de dernier recours).
2. Les clients (boot.sh max-time 3, scripts timeout 600) abandonnaient -> BrokenPipeError.
3. 3 échecs réseau -> blacklist backoff (15min, 30min...) : les providers sains étaient
   blacklistés à cause du réseau down -> « Toutes les IA ont échoué » -> 502 pour code.ia
   (le codeur). C'est le « avant bidouillage, timeout » : il fallait redémarrer le hub.

## CORRECTIONS APPLIQUÉES dans hub_prise_ia.py
C1 — Nouvelle exception `ReseauIndisponible` levée dans `_raw_call` sur erreur DNS
(socket.gaierror/Errno 8) ou connexion (ConnectionError) ; `call_provider` la capture
SÉPARÉMENT : bascule immédiate, PAS de retry PATIENCE, PAS de _register_result(False)
(donc pas de blacklist d'un provider sain).
C2 — Budget temps global `REQUEST_MAX_SECONDS = 120` (surchargeable routing.json
`request_max_seconds`) démarré AVANT l'injection de contexte ; chaque provider reçoit
`timeout_budget = budget_restant` ; si budget épuisé -> erreur rapide. Une requête ne
dépasse JAMAIS ~2 min (au lieu de 12-80 min).
C3 — `_reseau_disponible()` : test DNS rapide au début de chat_completions ; si KO,
mode dégradé (timeout <= 15s par provider) + log « Reseau pas pret — mode degrade ».
Conservé : PATIENCE pour les vrais timeouts de LECTURE (fix 09/08 DeepSeek 129s),
filet de dernier recours (mais borné par le budget), blacklist backoff pour les vraies
pannes provider, locks, limite payload, cache /health.

## CODE RÉEL INTÉGRÉ (extraits clés)

class ReseauIndisponible(Exception):
    pass
REQUEST_MAX_SECONDS = 120

# dans _raw_call, autour de urlopen :
    except (socket.gaierror, ConnectionError) as e:
        raise ReseauIndisponible(str(e)[:150]) from e
    except urllib_error.URLError as e:
        reason = getattr(e, "reason", None)
        if isinstance(reason, socket.gaierror) or isinstance(reason, ConnectionError):
            raise ReseauIndisponible(str(reason)[:150]) from e
        raise

# dans call_provider (signature : timeout_budget=None) :
    if timeout_budget is not None:
        base = min(base, max(1, int(timeout_budget)))
    ...
    except ReseauIndisponible as e:
        log_event("network", "Reseau indisponible: " + prov["name"], str(e)[:150])
        raise   # PAS de _register_result(False), PAS de retry

# dans chat_completions :
    t0 = time.time()
    max_seconds = REQUEST_MAX_SECONDS  # + surcharge routing.json
    reseau_ok = _reseau_disponible()
    ...
    for prov in providers:
        budget_restant = max_seconds - (time.time() - t0)
        if budget_restant <= 0: break  # erreur rapide
        timeout_eff = min(budget_restant, 15 if not reseau_ok else budget_restant)
        content = call_provider(prov, ..., timeout_budget=timeout_eff)
        except ReseauIndisponible: continue  # bascule immédiate, pas de PATIENCE

# filet de dernier recours : même logique, timeout_eff borné par budget_restant.

## TESTS (4/4 OK en 0,11s, test_hub_antifleau.py)
1. _raw_call vers hôte DNS inexistant -> ReseauIndisponible en < 10s
2. 3 échecs réseau -> _fails reste 0, pas de blacklist
3. _reseau_disponible répond < 5s
4. timeout_budget=5 -> échec rapide au lieu de 600s

## TA MISSION (3 coups une pierre — décision Christophe 13/08)
1. Verdict : GO / GO AVEC RÉSERVES / NON (argumenté sur le code réel ci-dessus)
2. En PLUS du verdict, cherche des AMÉLIORATIONS de logique, performance et stabilité
   que tu juges utiles — même hors du périmètre exact, tant que c'est cohérent et utile.
   Ex : faille dans la distinction réseau vs lenteur ? budget trop court/long ?
   mode dégradé suffisant ? interaction avec la tempête/réserve storm ?
3. Réponds en FRANÇAIS, structuré, concis (max 300 mots)."""


def ask(task, prompt):
    payload = json.dumps({
        "task": task,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1200,
        "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(
        HUB, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read().decode())


def main():
    for task, label in FAMILLE:
        out_path = os.path.join(OUT, label + ".md")
        if os.path.exists(out_path):
            print("[déjà fait]", label)
            continue
        print("[audit]", label, "...")
        try:
            d = ask(task, BRIEF)
            content = d["choices"][0]["message"]["content"]
            provider = d.get("provider", "?")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write("# AUDIT FAMILLE — " + label + "\n\n_provider: " + provider + "_\n\n" + content + "\n")
            print("  -> écrit", label + ".md")
        except Exception as e:
            print("  !! erreur", label, str(e)[:120])
        time.sleep(1)


if __name__ == "__main__":
    main()
