#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — 35 signets X frais (10-14/08) → dernières améliorations ACE777.
Injecte l'état actuel (anti déjà-fait) + les choix du tri du jour en focus.
Demande : 3 améliorations max priorisées, STRATÉGIE + TECHNIQUE, format strict.
"""
import glob, json, os, re, time, urllib.request

SIGNETS_DIR = os.path.expanduser("~/Documents/Obsidian_ACE777/Signets_X/2026-08")
ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_SIGNETS_FRAIS_20260815")
os.makedirs(OUT, exist_ok=True)


def clean(body):
    body = re.sub(r'<[^>]+>', ' ', body)
    body = re.sub(r'\[View on X.*?\]\(.*?\)', '', body)
    body = re.sub(r'\*\*\[@', '@', body)
    body = re.sub(r'\]\(.*?\)', '', body)
    body = re.sub(r'^\*\*', '', body)
    body = re.sub(r'\s+', ' ', body).strip()
    return body


def load_frais():
    files = sorted(glob.glob(os.path.join(SIGNETS_DIR, "2026-08-1*.md")))
    lines = []
    for f in files:
        txt = open(f, encoding="utf-8").read()
        body = txt.split("---", 2)[-1].strip()
        body = clean(body)
        m = re.search(r'author: "(@[^"]+)"', txt)
        d = re.search(r'tweet_date: (\S+)', txt)
        author = m.group(1) if m else "?"
        date = d.group(1) if d else "?"
        if not body:
            continue
        if len(body) > 400:
            body = body[:400] + "…"
        lines.append(f"{date} {author} — {body}")
    return lines


FRAIS = load_frais()
CONDENSE = "\n".join(f"{i}. {l}" for i, l in enumerate(FRAIS, 1))

BRIEF = f"""CONTEXTE (superviseur Buffy, 15/08/2026) — DERNIÈRES AMÉLIORATIONS ACE777 depuis les 35 signets X les plus FRAIS

=== LE BUT ===
Christophe a 35 signets X récents (10-14/08) et veut que la flotille en tire les
**dernières améliorations** pour ACE777 — STRATÉGIE (trading, sizing, risque) ET
TECHNIQUE (hub, agents, mémoire, coûts), classées ensemble.

=== CE QUI EXISTE DÉJÀ (ne propose PAS du déjà-fait — propose du NOUVEAU) ===
- Hulk = paper MEXC dip&rip + bags (paper_diprip.py) : régimes WATCH/COOLING/IMPULSE,
  dip/rip/stop par cadence, mise→2×→bag, DCA, compound, sense MEXC.
- Veille digest_watch.py : timeout 12s + back-off + circuit-breaker + deadline 90s
  + flag degraded (fix appliqué ce matin).
- Kill-switch STANDBY : veille muette >6h → plus de nouveaux achats (l'existant protégé).
- Contrat JSON Cortana↔moteur (cortana_contract.py) : ADVISORY strict — rien d'appliqué
  tant que justesse <60%. Bornes dures (DIP/RIP ±15%, STOP/NOTIONAL ±10%), whitelist,
  fail-safe GELÉ. Cortana propose, le moteur logge, n'applique pas.
- 2 classes de paires : A core liquides (règles actuelles) / B small caps bag
  (BAG_PAIRS=CCUSDT actif : taille ×0,5, pas de stop technique, vol DEAD relaxé,
  plafond 5, bag seedé 10$ entry +8% → boucle bag testable jour 1).
- Discipline continue (launchd 07h15) : Cortana re-notée F1 chaque jour (44% actuel,
  objectif 93% par calibration + NEUTRE forcé <60%), Ada scorée v1 (zone vs BTC 24h),
  rapport + alerte si dérive.
- Mémoire collab Obsidian + fichiers par chantier (déjà ≈ méthode « 6 fichiers de
  suivi » Anthropic : décisions, chantiers, dead ends consignés).
- Hub local 11435 (gemini/nvidia/cortana), 8 Go RAM, 0 API payante, openrouter
  souvent 502 (réseau alpage). Pas de base de données : fichiers Markdown/JSON.

=== LE TRI DU JOUR (consensus famille+Cortana sur 200 signets) — PISTES À APPROFONDIR ===
- N°192 : fuite Anthropic — 6 fichiers de suivi (décisions, dead ends, sources)
  → −84% tokens, +39% précision. (DÉJÀ notre philosophie — reste à l'affiner.)
- N°43+105 : sizing (Burry : c'est la taille de position qui compte) + paradoxe de
  Saint-Pétersbourg → critère de Kelly pour le sizing.
- N°12+53 : mémoire persistante agents (Brain.md Markdown, TencentDB Agent Memory).
- N°30+31 : garde-fous production (Release Receipt 6 points, trou de responsabilité
  multi-agents : propriétaire nommé, clés révocables, plan de reprise).
- N°130+142+44 : alléger/exécuter local (8 formats précision, BitNet CPU, Kimi K3 8 Go).

=== LES 35 SIGNETS FRAIS (10-14/08) ===
{CONDENSE}

=== VOTRE MISSION (format EXACT exigé) ===
1. **3 améliorations MAX, priorisées** (1 = la plus importante), chacune au format :
   - RANG : 1/2/3
   - DOMAINE : STRATÉGIE | TECHNIQUE | LES DEUX
   - IDÉE : 1-2 phrases, ancrée sur un signet PRÉCIS (cite son N° et @auteur) ou une
     nouveauté du marché en lien
   - CHANTIER : nom du chantier concret à ouvrir
   - EFFORT : S (1 session) / M (2-3 sessions) / L (chantier long)
   - BÉNÉFICE ATTENDU : concret, mesurable
   - LIEN : avec quel chantier en cours / en attente
   - RÉVERSIBLE : oui/non
2. **RISQUES / PIÈGES** : 2-3 max, honnêtes.
3. **VERDICT GLOBAL** : GO | GO-AVEC-RÉSERVE | NO-GO (sur « creuser ces pistes maintenant »)
   + CONFIANCE 0-100%.
Puis : SYNTHeSE 5 lignes max. Factuel, concis, français. Info manquante →
« information insuffisante ». Vous DONNEZ UN AVIS, ne touchez à rien."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2400, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    print(f"[i] {len(FRAIS)} signets frais condensés ({len(CONDENSE)} chars)")
    for m in MODELS:
        out_f = os.path.join(OUT, f"AVIS_{m}.md")
        if os.path.exists(out_f) and os.path.getsize(out_f) > 100:
            print(f"[SKIP] {m} déjà écrit")
            continue
        for attempt in (1, 2):
            try:
                content, provider, secs = ask(m)
                with open(os.path.join(OUT, f"AVIS_{m}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
                print(f"[OK] {m} ({secs}s)")
                break
            except Exception as e:
                print(f"[ERR] {m} (tentative {attempt}): {e}")
                time.sleep(3)
        time.sleep(2)


if __name__ == "__main__":
    main()
