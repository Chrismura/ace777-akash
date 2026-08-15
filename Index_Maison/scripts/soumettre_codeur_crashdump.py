#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soumet la SPEC du CRASH DUMP au CODEUR (task code.ia — puter-grok principal,
inferx-coder 2e, gemini filet). Flux zéro faute : la SPEC a été validée par la
famille (JUGE : GO AVEC RÉSERVES + « crash dump » exigé) avant tout code.
"""
import json
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/CODE_crash_dump_moteur.md"

SPEC = """\
Tu es le CODEUR de la famille ACE777 (task code.ia). Écris le code demandé, borné à la tâche.

CONTEXTE (faits vérifiés) : ALPHA (bot de trading testnet) meurt en rc=1 silencieusement
~13 min après chaque départ, juste après un fill. Le bot tourne sous set -euo pipefail
(genesis_manifest.txt) → toute commande qui échoue = mort rc=1 SILENCIEUSE si stderr avalé.
Un trap ERR pose déjà FATAL_RC1 ligne=N cmd=[...] dans /tmp/ace777_fatal_rc1.log.
Pour diagnostiquer au PREMIER crash (sans re-run), la famille (JUGE) exige un CRASH DUMP
automatique au moment du PROCESS_EXIT rc!=0 dans le lanceur.

FICHIER À MODIFIER : ~/ace777-test-day1/launch_test_master_base_v8_5_impact.sh
(c'est le lanceur actif — genesis_manifest.txt fait `exec ./launch_test_master_base_v8_5_impact.sh`).
Le champion genesis est INTANGIBLE : on ne modifie QUE ce lanceur (wrapper), jamais genesis.

FONCTION CONCERNÉE (run_unit, ~ligne 124-140) :
  run_unit() {
    trap '' PIPE
    local unit="$1"
    local live_log="${RUN_DIR}/${tag}_LIVE_COLOR.log"
    local rc=0
    set +e
    set +o pipefail
    tail -n +85 ./genesis_manifest.txt | bash -s 2>&1 | while IFS= read -r line || [ -n "$line" ]; do
      formatted="[${unit}] ${line}"
      printf '%s\\n' "$formatted"
      printf '%s\\n' "$formatted" >> "$live_log" 2>/dev/null || true
    done
    rc=${PIPESTATUS[1]:-0}
    trap - PIPE
    set -o pipefail
    set -e
    local exit_line
    exit_line="$(date -u +%Y-%m-%dT%H:%M:%SZ) PROCESS_EXIT unit=${unit} how=pipe_run_unit why=rc_${rc} rc=${rc}"
    mkdir -p "${RUN_DIR:-runs}"
    echo "$exit_line" >> "${RUN_DIR:-runs}/PROCESS_EXIT.log" 2>/dev/null || true
    echo "[$unit] $exit_line" >> "${live_log}" 2>/dev/null || true
    echo "[$unit] $exit_line"
    return "$rc"
  }

EXIGENCE (crash dump, UNIQUEMENT si rc != 0) :
1. Les 20 dernières lignes de $live_log (fenêtre de mort) → écrire dans runs/CRASH_DUMP_<unit>_<ts>.log
2. Le contenu de /tmp/ace777_fatal_rc1.log s'il existe (trap ERR déjà posé)
3. L'état de la position via l'API testnet si possible : positionRisk (position ouverte ou pas ?)
   — ATTENTION : utilise les variables déjà présentes dans le script (BASE_URL, BINANCE_API_KEY,
   BINANCE_API_SECRET, public_get/private helpers) ; NE PAS inventer de nouveaux helpers ; NE PAS
   faire échouer le run_unit si le dump échoue (|| true partout) ; zéro changement du comportement
   nominal (rc, exit_line, ordre des logs).
4. Reste BORNÉ à cette fonction + éventuellement un helper de dump à côté. Pas d'autre modification.
5. Bash compatible macOS (bash 3.2) — pas de mapfile, pas de ${var^^}. Commentaires concis en français.

RENDS : le bloc bash COMPLET à insérer (fonction run_unit modifiée + helper si besoin), rien d'autre.
"""


def main():
    payload = {
        "task": "code.ia",
        "messages": [{"role": "user", "content": SPEC}],
        "max_tokens": 2200,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    print("=== CODEUR (code.ia) — CRASH DUMP ===", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        rep = d["choices"][0]["message"]["content"].strip()
        provider = d.get("provider", "?")
    except Exception as e:
        rep = f"[CODEUR INJOIGNABLE] {str(e)[:200]}"
        provider = "?"
    print(f"provider: {provider}\n")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(f"# RÉPONSE CODEUR (task code.ia · {provider}) — {__import__('datetime').datetime.utcnow().isoformat()}Z\n\n{rep}\n")
    print(rep)
    print(f"\n[OK] écrit dans {OUT}", flush=True)


if __name__ == "__main__":
    main()
