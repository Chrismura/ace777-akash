#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — CIBLE DE LA CORRECTION PANNE ALPHA rc=1 (14/08, 2e round).

Le 1er round (AUDIT_PANNE) a localise la panne : mort silencieuse par
substitution sous set -e. La SPEC envoyee au codeur visait le lanceur, mais
Buffy (superviseur) a verifie les faits : les zones fautives sont dans
genesis_manifest.txt (champion INTANGIBLE), PAS dans le lanceur. Le patch du
codeur est inapplicable tel quel. Le JUGE a valide une SPEC au postulat faux
(angle mort superviseur). Nouvelle question : OU appliquer le correctif de
facon conforme C1, avec le mecanisme reel affine.

Chaque membre : (1) verdict, (2) Option A (ajout minimal genesis + re-scellement,
precedent du trap ligne 90) vs Option B (injection par le lanceur dans le pipe),
(3) le mecanisme reel affirme ou corrige, (4) la liste exacte des zones a
proteger (minimale, pas de sur-engineering), (5) ce qui prouvera la panne au
retest. Clause permanente Christophe : prouver la meilleure logique.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
OUT = os.path.join(ROOT, "Index_Maison", "AUDIT_CIBLE_CORRECTION_2026-08-14")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CONTEXTE = """\
CIBLE DE LA CORRECTION — ALPHA meurt en rc=1 (mort silencieuse, reproduite 2x).
2e round : la 1re SPEC visait le lanceur mais visait en realite des lignes de
genesis (champion INTANGIBLE). A toi de trancher OU appliquer le correctif.

================
FAITS VERIFIES PAR LE SUPERVISEUR (Buffy, pas un recit)
================
1. RUN TEST 14/08 (GEMINI_TEST + crash dump, testnet) : ALPHA rc=1 a
   07:49:10Z (~8 min apres depart, juste apres fill #42). BETA survit.
   Pattern identique au 13/08. FATAL_RC1 VIDE (trap ERR ligne 90 de genesis
   n'a PAS ecrit : sous set -e, le trap ne se propage pas dans les
   sous-shells / substitutions $(...) / pipelines).
2. STRUCTURE REELLE (verifiee) :
   - genesis_manifest.txt = 2517 lignes, champion INTANGIBLE (C1). Contient
     TOUT le code moteur : helpers (json_get ligne 454, as_num/num_* 675-684,
     curl_with_retry 693-717, public_get 717, trend_bps_from_klines 781),
     la boucle de cycle (p1/depth_1 1599-1601, p2/depth_2 1613-1615,
     book_resp 1733-1745, entry/px 2057-2142, exit 2431...).
   - launch_test_master_base_v8_5_impact.sh = 269 lignes, lanceur wrapper :
     grep public_get/json_get/as_num = 0 resultat. Il ne fait QUE
     `tail -n +85 genesis_manifest.txt | bash -s` (run_unit) + env + crash dump.
   - GEMINI_TEST = jumeau du lanceur (294 lignes), meme structure.
3. MECANISME REEL AFFINE (les public_get sont deja proteges) :
   - `public_get` = curl_with_retry (3 tentatives, pause 5s) qui RETOURNE 0
     meme en echec (NET_RETRY_EXHAUSTED -> return 0, "no process kill").
   - Les appels du type p1_resp="$(public_get ... || true)" ont DEJA || true.
   - DONC la mort ne vient pas de public_get lui-meme. Les vrais coupables =
     HELPERS RUBY non proteges dans des substitutions imbriquees, qui peuvent
     sortir rc!=0 (TypeError ruby sur JSON non-hash, ruby absent, argument
     vide) dans une substitution $(...) -> set -e tue le sous-shell ->
     mort silencieuse. Exemple : p1="$(as_num "$(json_get "$p1_resp"
     "price")")" : si json_get sort rc!=0, la substitution interne echoue.
   - 10 occurrences du pattern $(as_num "$(json_get ...)") : lignes 1600,
     1614, 1734, 1735, 2057, 2061, 2071, 2109, 2142, 2431. Plus d'autres
     helpers ruby (trend_bps_from_klines 781, vortex_radar_clamp, bps_change,
     abs_num, num_*) et llm_raw (1992).
4. PRECEDENT : le trap DIAGNOSTIC (ligne 90) est deja DANS genesis (ajout
   14/08) et le champion a ete RE-SCELLE af307996 (= 98c80b5c + trap) par
   decision famille 6/6 (Q2=a). Le mecanisme « ajout minimal justifie dans
   genesis + re-scellement » existe donc deja dans la chaine.
5. LE PATCH DU CODEUR (CODE_correction_panne_alpha.md) est INAPPLICABLE :
   il encapsule des lignes dans le lanceur alors qu'elles sont dans genesis.
   Sa preuve « meilleure logique » (safe_call) reste valable comme OUTIL,
   mais pas son placement.

================
TA MISSION (5 reponses nettes)
================
1. VERDICT : GO / GO AVEC RESERVES / NON sur le principe de la correction
   anti-mort silencieuse (wrapper/neutralisation des substitutions a risque).
2. CIBLE : Option A = ajout minimal dans genesis (protéger les N zones listees)
   + RE-SCELLEMENT du champion (precedent du trap) ; Option B = injection par
   le lanceur dans le pipe (0 touche genesis, mais fragile bash 3.2).
   TRANCHE : A / B / A+B hybride, et JUSTIFIE (C1, robustesse, auditabilite).
3. MECANISME reel : confirme-tu le diagnostic affine (public_get deja protege,
   coupables = helpers ruby dans substitutions imbriquees) ? Corrige si besoin.
4. LISTE EXACTE des zones a proteger (minimale, sans sur-engineering) — donne
   les numeros de lignes + le type de protection (wrapper safe_call autour du
   helper, || true, || echo 0, set +e local...). Bash 3.2 macOS.
5. INDICATEUR de preuve au retest (1 seul, comme demande precedemment) qui
   confirmera la panne si elle se reproduit.
CLAUDE PERMANENTE (Christophe) : « Prouve la meilleure logique et applique-la
dans la correction et l'amelioration si possible. »
Reponds en francais, court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1500,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[INJOIGNABLE] {str(e)[:120]}"


if __name__ == "__main__":
    import sys
    cible = sys.argv[1].upper() if len(sys.argv) > 1 else None
    membres = [(n, t, s) for n, t, s in MEMBRES if cible is None or n == cible]
    if not membres:
        print(f"[ERR] membre inconnu : {cible} (dispo: {[m[0] for m in MEMBRES]})")
        sys.exit(1)
    print(f"=== AUDIT FAMILLE — CIBLE CORRECTION ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
