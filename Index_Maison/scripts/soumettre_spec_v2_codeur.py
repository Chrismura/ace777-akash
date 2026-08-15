#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soumettre SPEC v2 (corrigée) au codeur via task code.ia."""
import json, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"

CONTEXTE = (
    "CODE LA SPEC v2 RELANCE DUO (14/08) — tu es le CODEUR : livre le patch COMPLET exact.\n\n"
    "CONTEXTE : le patch v1 (CODE_relance_duo_harmonie.md) avait 2 defauts corriges dans la v2 :\n"
    "1) la fonction reset_duo_harmony etait definie dans GO_VORTEX_V2.sh avant `exec` — exec "
    "remplace le processus, les fonctions bash ne survivent pas (prouve : command not found "
    "rc=127) -> le reset n'aurait jamais eu lieu aux relances. CORRIGE : la fonction est "
    "definie DANS launch_vortex_v2_collab_4h_binance.sh avant la boucle while true.\n"
    "2) `[ \"$rc\" -eq 0 ] && break` ajoute hors SPEC (changement du comportement nominal) -> "
    "INTERDIT dans la v2, ne le reproduis PAS.\n\n"
    "SPEC v2 (ce qu'il faut livrer, rien d'autre) :\n"
    "Cible : launch_vortex_v2_collab_4h_binance.sh UNIQUEMENT (pas GO_VORTEX_V2.sh, pas genesis).\n"
    "Backup avant modif : cp launch_vortex_v2_collab_4h_binance.sh "
    "launch_vortex_v2_collab_4h_binance.sh.BAK_avant_reset_duo_$(date +%Y%m%d_%H%M%S)\n\n"
    "1) Definir la fonction reset_duo_harmony() juste AVANT la ligne `attempt=0` (avant le "
    "while true) :\n"
    "reset_duo_harmony() {\n"
    "  local sd=\"${RUN_DIR:-runs}/duo_state.json\"\n"
    "  local ss=\"${RUN_DIR:-runs}/duo_session.json\"\n"
    "  rm -f \"$sd\" \"$ss\" 2>/dev/null || true\n"
    "  mkdir -p \"${RUN_DIR:-runs}\" 2>/dev/null || true\n"
    "  echo '{\"role\":\"INIT\",\"status\":\"RESET\",\"ts_ms\":0}' > \"$sd\" 2>/dev/null || true\n"
    "  echo '{\"run_state\":{\"current_tier\":13,\"start_ts\":\"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'\",\"last_cycle\":0,\"total_pnl_snapshot\":0.0},\"roles\":{},\"total_pnl\":0.0}' > \"$ss\" 2>/dev/null || true\n"
    "  sync 2>/dev/null || true\n"
    "}\n\n"
    "2) Appeler reset_duo_harmony au debut de CHAQUE iteration, juste apres "
    "`attempt=$((attempt + 1))`.\n\n"
    "3) Apres `rc=$?` (et AVANT le bloc `if [ -f STOP ]` existant), inserer le bloc double-mort :\n"
    "if [ -f \"$RUN_DIR/PROCESS_EXIT.log\" ] && \\\n"
    "   grep -q \"BETA_X5.*rc=1\" \"$RUN_DIR/PROCESS_EXIT.log\" && \\\n"
    "   grep -q \"ALPHA_X13_BURST13.*rc=1\" \"$RUN_DIR/PROCESS_EXIT.log\"; then\n"
    "  last_beta=\"$(grep \"BETA_X5\" \"$RUN_DIR/PROCESS_EXIT.log\" | tail -1)\"\n"
    "  last_alpha=\"$(grep \"ALPHA_X13_BURST13\" \"$RUN_DIR/PROCESS_EXIT.log\" | tail -1)\"\n"
    "  if [ -n \"$last_beta\" ] && [ -n \"$last_alpha\" ]; then\n"
    "    tb=\"$(echo \"$last_beta\" | awk '{print $1}')\"\n"
    "    ta=\"$(echo \"$last_alpha\" | awk '{print $1}')\"\n"
    "    if [ \"$(ruby -rtime -e 'begin; a=Time.parse(ARGV[0]); b=Time.parse(ARGV[1]); puts ((a-b).abs<=300 ? \"1\" : \"0\"); rescue; puts \"0\"; end' -- \"$tb\" \"$ta\" 2>/dev/null || echo \"0\")\" = \"1\" ]; then\n"
    "      echo \"=== DOUBLE MORT DUO détectée ($tb / $ta) — STOP, pas de relance. ===\"\n"
    "      touch STOP STOP_ALPHA STOP_BETA 2>/dev/null || true\n"
    "      break\n"
    "    fi\n"
    "  fi\n"
    "fi\n\n"
    "INTERDIT : aucun `[ \"$rc\" -eq 0 ] && break`, aucun changement du comportement nominal "
    "(STOP -> break ; duree -> break ; sinon relance apres sleep 5).\n\n"
    "CONTRAINTES : bash 3.2 macOS (pas de mapfile, pas de ${var^^}, pas de date -d) ; ruby dispo ; "
    "commentaires concis en français.\n\n"
    "CLAUDE PERMANENTE (Christophe 14/08) : prouve la meilleure logique et applique-la si "
    "possible — 1 amelioration prouvee max (mesurable, bornee, sans effet de bord).\n\n"
    "LIVRE : 1) le patch complet (fonction + 2 insertions) pret a appliquer, 2) la preuve "
    "meilleure logique, 3) la grille 1-4 passee (bash -n ; reset CLI -> INIT/RESET ; double mort "
    "simulee -> STOP ; session propre rc=0 simulee -> sleep 5 + nouvelle iteration, pas d'arret). "
    "Rien d'autre."
)

def main():
    payload = {
        "task": "code.ia",
        "messages": [{"role": "user", "content": CONTEXTE}],
        "max_tokens": 2500,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    out = "/Users/christophe/ace777-test-day1/Index_Maison/CODE_relance_duo_harmonie_v2.md"
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# RÉPONSE CODEUR v2 (task code.ia · {provider}) — 2026-08-14\n\n{content}\n")
    print(f"[CODEUR v2] provider={provider} -> {out}")
    print(content[:1500])

if __name__ == "__main__":
    main()
