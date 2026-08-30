#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_juge_t7_t8.py — Tests T7 + T8 de la SPEC_JUGE_ECLAIRE_20260824 (24/08, Buffy).

  T7 : pont (llm_gate_hub_bridge.py) avec fake hub -> le pavé d'indicateurs
       apparait dans la requete envoyee au hub ; cache : 2e requete meme prompt
       -> reponse servie SANS nouveau pavé (hub non re-consulte).
  T8 : 2 superviseurs (vortex_supervisor_v2_llm.rb) simultanes (simules) ->
       au plus 1 appel au pont (verrou flock runs/vortex_llm.lock).

Hermetique : tout se passe en /tmp, aucun fichier reel touche (fake hub, fake
ollama, lock/last/control temporaires, CSV inexistant -> fallback CHOP sans
appel reseau de vortex_regime_compute.rb).

Usage: python3 test_juge_t7_t8.py <Index_Maison/scripts_dir>
       (le superviseur est resolu relativement: <racine>/scripts/)
"""
import http.server
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from http.client import HTTPConnection

SCRIPTS = sys.argv[1]
if not os.path.isdir(SCRIPTS):
    print("Usage: python3 test_juge_t7_t8.py <scripts_dir>")
    sys.exit(2)
# Le superviseur vit dans <racine>/scripts/ (pas Index_Maison/scripts/)
SUP_SCRIPTS = os.path.join(os.path.dirname(os.path.dirname(SCRIPTS)), "scripts")


class FakeHub(http.server.BaseHTTPRequestHandler):
    bodies_file = None

    def log_message(self, *a):
        pass

    def _record(self, body):
        with open(self.bodies_file, "a") as fh:
            fh.write(body.decode("utf-8", "replace") + "\n---BODY---\n")

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok": true}')

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n)
        self._record(body)
        rep = json.dumps({
            "choices": [{"message": {"content": '{"swarm_cohesion": 0.42, "mode": "CHOP"}'}}]
        }).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(rep)


class FakeOllama(http.server.BaseHTTPRequestHandler):
    count_file = None

    def log_message(self, *a):
        pass

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        self.rfile.read(n)
        with open(self.count_file, "a") as fh:
            fh.write("x\n")
        rep = json.dumps({"response": '{"swarm_cohesion": 0.55, "mode": "CHOP"}'}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(rep)


def serve(klass, port, **attrs):
    for k, v in attrs.items():
        setattr(klass, k, v)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", port), klass)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    return srv


def attendre_port(port, timeout=15):
    import socket
    fin = time.time() + timeout
    while time.time() < fin:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                return True
        except OSError:
            time.sleep(0.1)
    return False


def test_t7():
    print("=== T7 : pont + fake hub (pave injecte, cache preserve) ===")
    tmp = tempfile.mkdtemp(prefix="t7_")
    hub_port, pont_port = 12935, 12939
    bodies = os.path.join(tmp, "hub_bodies.txt")
    FakeHub.bodies_file = bodies
    hub = serve(FakeHub, hub_port)

    env = dict(os.environ)
    env["HUB_URL"] = "http://127.0.0.1:%d/v1/chat/completions" % hub_port
    env["LLM_GATE_PONT_PORT"] = str(pont_port)
    env["PYTHONPATH"] = SCRIPTS
    bridge = subprocess.Popen(
        [sys.executable, os.path.join(SCRIPTS, "llm_gate_hub_bridge.py")],
        env=env, cwd=tmp, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        assert attendre_port(pont_port), "pont pas monte a temps"
        raw = "TEST_T7_RAW_PROMPT 777"
        payload = json.dumps({"prompt": raw, "options": {"num_predict": 45}})

        conn = HTTPConnection("127.0.0.1", pont_port, timeout=10)
        conn.request("POST", "/api/generate", body=payload,
                     headers={"Content-Type": "application/json"})
        r1 = json.loads(conn.getresponse().read().decode("utf-8"))
        conn.request("POST", "/api/generate", body=payload,
                     headers={"Content-Type": "application/json"})
        r2 = json.loads(conn.getresponse().read().decode("utf-8"))
        conn.close()

        with open(bodies) as fh:
            contenu = fh.read()
        nb_hits = contenu.count("---BODY---")

        assert nb_hits == 1, "le hub a ete consulte %d fois (attendu 1)" % nb_hits
        assert "CONTEXTE MARCHE" in contenu, "pave absent de la requete hub"
        assert raw in contenu, "prompt brut absent de la requete hub"
        assert r1["response"] == r2["response"], "cache : reponses differentes"
        assert "swarm_cohesion" in r1["response"], "reponse hub non transmise"
        marques = re.findall(r"\[([a-z_]+)\]", contenu)  # [taux_fantome] etc
        assert marques, "aucun indicateur dans le pave"

        print("  OK : 1 seul hit hub, pave present (%s), 2e requete servie par le cache"
              % ",".join(sorted(set(marques))))
        print("  OK : reponses identiques (cache), contenu : %s" % r1["response"][:60])
        print("T7 OK")
    finally:
        bridge.terminate()
        bridge.wait(timeout=5)
        hub.shutdown()
        shutil.rmtree(tmp, ignore_errors=True)


def test_t8():
    print("=== T8 : 2 superviseurs simultanes -> au plus 1 appel (verrou flock) ===")
    tmp = tempfile.mkdtemp(prefix="t8_")
    o_port = 12941
    count_file = os.path.join(tmp, "ollama_hits.txt")
    FakeOllama.count_file = count_file
    srv = serve(FakeOllama, o_port)

    sup = os.path.join(SUP_SCRIPTS, "vortex_supervisor_v2_llm.rb")
    env = dict(os.environ)
    env["LOG_BETA"] = os.path.join(tmp, "fake_beta.csv")  # inexistant -> fallback CHOP
    env["LLM_OLLAMA_URL"] = "http://127.0.0.1:%d" % o_port
    env["VORTEX_LLM_LOCK"] = os.path.join(tmp, "vortex_llm.lock")
    env["VORTEX_LLM_LAST_FILE"] = os.path.join(tmp, "vortex_llm_last.json")
    env["VORTEX_CONTROL_FILE"] = os.path.join(tmp, "vortex_control.json")
    env["SWARM_TELEMETRY_FILE"] = os.path.join(tmp, "swarm_telemetry.json")
    env["JUGE_DEBUG"] = "1"

    try:
        for ronde in (1, 2, 3):
            for f in ("vortex_llm.lock", "vortex_llm_last.json", "vortex_control.json"):
                p = os.path.join(tmp, f)
                if os.path.exists(p):
                    os.remove(p)
            if os.path.exists(count_file):
                os.remove(count_file)

            procs = []
            for _i in (1, 2):
                procs.append(subprocess.Popen(["ruby", sup], env=env, cwd=tmp,
                                              stdout=subprocess.DEVNULL,
                                              stderr=subprocess.DEVNULL))
            for p in procs:
                p.wait(timeout=30)
            time.sleep(0.3)  # laisser l'ecriture du compteur se terminer

            hits = 0
            if os.path.exists(count_file):
                with open(count_file) as fh:
                    hits = len(fh.readlines())
            assert hits <= 1, "ronde %d : %d appels (le verrou n'a PAS bloque)" % (ronde, hits)
            print("  Ronde %d : %d appel(s) au pont (2 superviseurs simultanes)" % (ronde, hits))
            assert os.path.exists(os.path.join(tmp, "vortex_llm_last.json")), \
                "ronde %d : vortex_llm_last.json non ecrit" % ronde
        print("T8 OK (3 rondes : jamais 2 appels)")
    finally:
        srv.shutdown()
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    test_t7()
    test_t8()
    print("TESTS T7+T8 OK")
