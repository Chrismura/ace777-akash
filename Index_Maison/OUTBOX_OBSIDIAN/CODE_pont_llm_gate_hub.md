# RÉPONSE HUB (task code.ia · via Puter Grok (gratuit)) — 2026-08-12T14:40:24

```python
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
from datetime import datetime

# === CONFIGURATION (variables d'environnement) ===
PORT = int(os.environ.get("LLM_GATE_PONT_PORT", "11439"))
HUB_URL = os.environ.get("HUB_URL", "http://127.0.0.1:11435/v1/chat/completions")
LLM_MODEL = os.environ.get("LLM_MODEL", "qwen2.5-coder:1.5b")
TIMEOUT_READ = int(os.environ.get("LLM_GATE_HUB_TIMEOUT_READ", "45"))
LOG_FILE = "/tmp/llm_gate_hub.log"


def log(message: str):
    """Écrit dans le log avec horodatage (non fatal)."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception:
        pass  # jamais fatal


def call_hub(prompt: str, max_tokens: int) -> tuple:
    """
    Appelle le HUB en format OpenAI chat completions.
    Retourne (succes: bool, content: str ou message d'erreur)
    """
    payload = {
        "task": "supervise.decision",
        "messages": [{"role": "user", "content": prompt}],
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

            success, content = call_hub(prompt, num_predict)

            if success:
                ollama_response = {"response": content}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(ollama_response).encode("utf-8"))
                log("Traduction réussie → réponse Ollama envoyée")
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
    with socketserver.TCPServer(("", PORT), LLMGateHandler) as httpd:
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
```

**Patch minimal pour `vortex_supervisor_v2_llm.rb`** (2 lignes à modifier) :

```ruby
http.open_timeout = (ENV["VORTEX_LLM_OPEN_TIMEOUT"] || "1").to_f
http.read_timeout = (ENV["VORTEX_LLM_READ_TIMEOUT"] || "2.0").to_f
```

Place ces deux lignes à l’endroit où les timeouts sont actuellement codés en dur (remplace les valeurs fixes par les variables d’environnement). Les valeurs par défaut restent inchangées, donc le comportement du moteur reste identique tant que les variables ne sont pas définies.
