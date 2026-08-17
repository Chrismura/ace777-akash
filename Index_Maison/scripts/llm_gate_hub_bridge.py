#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
llm_gate_hub_bridge.py
Pont LLM Gate → HUB ACE777
Remplace Ollama pour le garde-fou des trades (vortex_supervisor_v2_llm.rb)
Python 3.9 stdlib uniquement - macOS - non fatal
"""

import http.server
import socketserver
import json
import urllib.request
import urllib.error
import os
import sys
import time
import hashlib
from datetime import datetime

# === CONFIGURATION (variables d'environnement) ===
PORT = int(os.environ.get("LLM_GATE_PONT_PORT", "11439"))
HUB_URL = os.environ.get("HUB_URL", "http://127.0.0.1:11435/v1/chat/completions")
LLM_MODEL = os.environ.get("LLM_MODEL", "qwen2.5-coder:1.5b")
TIMEOUT_READ = int(os.environ.get("LLM_GATE_HUB_TIMEOUT_READ", "45"))
LOG_FILE = "/tmp/llm_gate_hub.log"

# Cache du juge (validé Christophe 12/08, réglable) : le moteur appelle le pont
# à chaque cycle (~10-15 s), mais le hub cloud met ~13 s et consomme le budget
# cloud (480/j). On ne consulte le hub qu'une fois par tranche de CACHE_SEC
# secondes ; entre-temps, le pont renvoie la dernière réponse (le moteur croit
# qu'on lui répond). Zéro modification du moteur.
# Clé = hash du prompt (revue 12/08) : les 2 chemins du moteur (cohesion vs
# radar) envoient des prompts DIFFÉRENTS avec des schémas de réponse différents
# → on ne doit JAMAIS servir la réponse de l'un à l'autre.
CACHE_SEC = float(os.environ.get("LLM_GATE_PONT_CACHE_SEC", "90"))
_CACHE = {"ts": 0.0, "response": None, "key": None}


def cache_fraiche(prompt):
    """True si la réponse en cache est fraîche ET pour le même prompt."""
    key = hashlib.sha1(prompt.encode("utf-8")).hexdigest()
    return (
        _CACHE["response"] is not None
        and _CACHE["key"] == key
        and (time.time() - _CACHE["ts"]) < CACHE_SEC
    )


def cache_lire():
    return _CACHE["response"]


def cache_ecrire(prompt, reponse):
    _CACHE["ts"] = time.time()
    _CACHE["key"] = hashlib.sha1(prompt.encode("utf-8")).hexdigest()
    _CACHE["response"] = reponse


def log(message: str):
    """Écrit dans le log avec horodatage (non fatal)."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception:
        pass  # jamais fatal


# Message système : force le hub à répondre en JSON strict (le moteur
# attend {"swarm_cohesion": x, "mode": "TREND|CHOP"} — Ollama le faisait
# via format:"json". Sans ce message, grok répond en texte et le parse échoue.
SYSTEM_JSON = (
    "Tu es le juge fail-closed d'un garde-fou de trading ACE777. "
    "Reponds STRICTEMENT en JSON, sans aucun texte autour, au format: "
    '{\"swarm_cohesion\": 0.5, \"mode\": \"CHOP\"} avec swarm_cohesion '
    'entre 0.2 et 1.0 et mode TREND ou CHOP uniquement.'
)


def extract_json(raw: str) -> str:
    """Extrait le premier objet JSON {...} d'une réponse, en ignorant les
    fences markdown (```json) et tout texte avant/après. Retourne le JSON brut
    si trouvé, sinon la réponse telle quelle (le moteur a un regex de secours)."""
    if not raw:
        return raw
    start = raw.find("{")
    end = raw.rfind("}")
    if start != -1 and end > start:
        candidate = raw[start:end + 1]
        try:
            json.loads(candidate)  # valide : c'est bien du JSON
            return candidate
        except json.JSONDecodeError:
            pass  # pas un JSON valide → on laisse tel quel
    return raw


def hub_healthy() -> bool:
    """Vérifie rapidement que le hub répond (health). Timeout court : le
    preflight n'attend que quelques secondes. Non fatal."""
    health_url = HUB_URL.replace("/v1/chat/completions", "/health")
    try:
        req = urllib.request.Request(health_url, method="GET")
        with urllib.request.urlopen(req, timeout=3) as response:
            return response.status == 200
    except Exception:
        return False


def call_hub(prompt: str, max_tokens: int) -> tuple:
    """
    Appelle le HUB en format OpenAI chat completions.
    Retourne (succes: bool, content: str ou message d'erreur)
    """
    payload = {
        "task": "supervise.decision",
        "messages": [
            {"role": "system", "content": SYSTEM_JSON},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.0,
        "max_tokens": max_tokens
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        HUB_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_READ) as response:
            raw = response.read().decode("utf-8")
            hub_response = json.loads(raw)
            content = hub_response.get("choices", [{}])[0].get("message", {}).get("content", "")
            return True, content
    except urllib.error.HTTPError as e:
        log(f"ERREUR HUB HTTP {e.code}: {e.reason}")
        return False, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        log(f"ERREUR HUB URL: {e.reason}")
        return False, str(e.reason)
    except TimeoutError:
        log("ERREUR HUB: timeout lecture")
        return False, "timeout"
    except json.JSONDecodeError:
        log("ERREUR HUB: réponse JSON invalide")
        return False, "json invalide"
    except Exception as e:
        log(f"ERREUR HUB inattendue: {str(e)}")
        return False, str(e)


class LLMGateHandler(http.server.BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        """Désactive les logs console par défaut (tout va dans le fichier)."""
        pass

    def do_GET(self):
        if self.path == "/api/tags":
            # FAIL-CLOSED (revue 12/08) : vérifier que le HUB répond avant de
            # prétendre que le modèle est là. Sans ça, le preflight passerait
            # même si le hub est mort → run démarré SANS juge LLM (danger).
            if not hub_healthy():
                log("GET /api/tags → HUB INJOIGNABLE → 503 (fail-closed)")
                self.send_response(503)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"models": [{"name": LLM_MODEL}]}
            self.wfile.write(json.dumps(response).encode("utf-8"))
            log("GET /api/tags → modèle renvoyé: " + LLM_MODEL)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path != "/api/generate":
            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        log("POST /api/generate reçue")

        try:
            ollama_request = json.loads(post_data)
            prompt = ollama_request.get("prompt", "")
            options = ollama_request.get("options", {})
            num_predict = options.get("num_predict", 45)

            # Cache du juge : si la dernière réponse du hub est fraîche ET pour
            # le même prompt, on la renvoie sans déranger le hub (économie de
            # budget cloud + latence).
            if cache_fraiche(prompt):
                ollama_response = {"response": cache_lire()}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(ollama_response).encode("utf-8"))
                log("CACHE → réponse juge renvoyée (hub non consulté)")
                return

            success, content = call_hub(prompt, num_predict)

            if success:
                # Robustesse (revue 12/08) : certains modèles enveloppent le
                # JSON dans des fences markdown (```json ... ```) ou du texte.
                # Le moteur attend du JSON strict → on extrait le bloc JSON.
                cleaned = extract_json(content)
                cache_ecrire(prompt, cleaned)
                ollama_response = {"response": cleaned}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(ollama_response).encode("utf-8"))
                log("Traduction réussie → réponse Ollama envoyée (hub consulté)")
            else:
                # Fail-closed : on renvoie 503 pour que le moteur fasse son fallback règles
                self.send_response(503)
                self.end_headers()
                log(f"Hub indisponible → 503 renvoyé ({content})")

        except json.JSONDecodeError:
            log("ERREUR: JSON invalide dans la requête Ollama")
            self.send_response(503)
            self.end_headers()
        except Exception as e:
            log(f"ERREUR inattendue dans le pont: {str(e)}")
            self.send_response(503)
            self.end_headers()


def run_server():
    """Démarre le serveur HTTP."""
    # allow_reuse_address : après un kill, le socket reste en TIME_WAIT.
    # Sans ça, TCPServer échoue avec Errno 48 au redémarrage (piège launchd KeepAlive).
    # ThreadingMixIn (fix 17/08) : le pont était mono-thread — pendant qu'un
    # POST /api/generate attendait le hub (~13 s), le GET /api/tags du preflight
    # (timeout 3 s) restait bloqué → « Ollama unreachable » intermittent.
    # Chaque requête est désormais traitée dans son propre thread.
    class ReuseTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        allow_reuse_address = True
        daemon_threads = True

    with ReuseTCPServer(("127.0.0.1", PORT), LLMGateHandler) as httpd:
        log(f"Pont LLM Gate démarré sur le port {PORT}")
        print(f"Pont LLM Gate en écoute sur http://127.0.0.1:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            log("Arrêt du pont (KeyboardInterrupt)")
            print("\nArrêt du pont.")


def test_hub():
    """Mode --test : vérifie la joignabilité du HUB."""
    print("Test de connexion au HUB...")
    success, msg = call_hub('{"test": true}', 10)
    if success:
        print("✓ HUB joignable")
        log("Test --test réussi")
        sys.exit(0)
    else:
        print(f"✗ HUB injoignable: {msg}")
        log(f"Test --test échoué: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_hub()
    else:
        run_server()
