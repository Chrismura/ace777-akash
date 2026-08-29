#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — LES 3 ŒUVRES DU 29/08 (audit 1quater, GO Christophe).

Christophe, 29/08 : « faire audit famille. TRÈS IMPORTANT CAR SOUVENT ERREURS
RÉPÉTÉES, BRANCHER NOS ŒUVRES... vérifier TOUT. »

On pose les 3 œuvres SANS révéler nos conclusions (avis indépendant), avec la
clause permanente + PUSH EXCELLENCE + l'angle « qu'est-ce qui peut casser ? ».

Membres : GEMINI, DEEPSEEK, JUGE, ULTRA, INFERX, GROK.
Sortie : CONSULTATION_FAMILLE_OEUVRES_20260829/ (avis.json + md).
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_OEUVRES_20260829")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches : GO / GO AVEC RESERVES / NON."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Robustesse à l'échelle."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Logique interne, pièges."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon pragmatique de la famille ACE777."),
]

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger. "
    "Propose AUTRE CHOSE ou une AMÉLIORATION. Corriger n'est pas suffisant."
)

PUSH = (
    "PUSH EXCELLENCE : Ta première réponse est le PLAFOND, pas le plancher. "
    "Va 30% plus loin. Une réponse confortable est ratée."
)

BRIEF = """CONTEXTE (superviseur Buffy, 29/08/2026) — AUDIT DES 3 ŒUVRES DU JOUR

=== ŒUVRE 1 — PROTOCOLE DE CROISEMENT EXTERNE (règle des 2 sources) ===
On a eu plusieurs fois des données fausses (fichier réécrit → 66M BTC impossibles,
source API down → sonde aveugle 6h). Solution : avant toute décision importante,
nos PRIX sont croisés avec une source externe (MEXC batch + Binance pour BTC/ETH).
Écart > 5 % = data_quality_fail = on NE décide PAS (alerte). Les MURS (moyenne
historique vs profondeur instantanée 5 niveaux) sont un warning informatif
(tolérance x0.05-x20) car le ratio varie naturellement de 0.1x à 200x quand le
carnet se déséquilibre — ce n'est PAS une corruption, c'est le marché.
Test : prix XRP corrompu x10 → détecté (écart 900 %). Registre d'audit jsonl.

=== ŒUVRE 2 — SIGNAL 3 « SQUEEZE DU LIVRE ÉCORCHÉ » ===
Détecte le vacuuming (trou d'air du carnet) : un faux mur, retrait discret de
liquidité, suppression du mur → décrochage instantané. Formule :
spoof_pct > 5 % ET drop > 100 ET spread ≤ 70 bps, persistance 2/3 mesures.
LE CHAÎNON MANQUANT : les manipulateurs n'attaquent pas nos small caps, ils
amorcent sur BTC/ETH et l'onde se propage → si btc_spoof_pct > 5 %, seuils
abaissés de 20 % (origine=contagion_btc). Source : arXiv 2504.15908 (31 % des
grosses ordres spoofent). Testé sur 63 611 mesures : 0 fausse alerte, paires à
risque = XRP (drop 968), ZBCN (313), PYTH (spoof 5,7 %).

=== ŒUVRE 3 — LA POUSSIÈRE INSTITUTIONNELLE (signature RBF plat, Cortana) ===
Vision Cortana (session 4 tours) : un gros acteur qui fragmente des milliers de
BTC en micro-transactions pour passer inaperçu CONNAÎT ses frais par avance →
son taux de RBF est anormalement bas (le retail, lui, tatone avec le RBF).
VALIDÉ par nos données : corrélation micro_tx/RBF = -0.275 sur 13 933 points
(RBF moyen 0.286 quand micro_tx ≥ 0.5 vs 0.599 sinon). Le SAPI (score complet) =
I(z_fee>2)*0.35 + min(1,taux_fantome/0.15)*0.30 + I(micro_tx>seuil)*0.20
- min(1,|delta_spot_book|*10)*0.15, alerte si ≥0.75 ET volume ≥ 500 BTC.
3 termes sur 4 déjà dans nos données ; le 4e (delta carnet spot) a un proxy
(spread_delta_bps). Le SAPI a ANTICIPÉ le pic de blocs privatisés du 28/08
(90,9 %, 555 BTC) de ~2h (SAPI 0.85 à 17:25Z, pic à 19:14Z).

=== LA QUESTION (à trancher en famille) ===
A) Chaque œuvre : est-elle SÛRE (pas de fausse alerte en cascade, pas d'erreur
   de logique, pas de dépendance à une seule source) ? Trouve les failles.
B) Le SAPI poussière est-il prêt à être codé avec le proxy spot_book_delta,
   ou vaut-il mieux attendre la vraie donnée ? Quels faux positifs guettent ?
C) « TRÈS IMPORTANT CAR SOUVENT ERREURS RÉPÉTÉES » : quels pièges de branchage
   (plists, chemins, sources API uniques, formats de fichiers) reviennent sans
   arrêt chez nous ? Comment les rendre STRUCTURELLEMENT impossibles ?
D) Quelles améliorations concrètes proposes-tu pour chacune des 3 œuvres ?

Ne me dis pas « c'est bien, continuez ». Donne des avis indépendants, tranchés,
avec des scénarios de panne précis et des corrections chiffrées.
""" + CLAUSE + "\n\n" + PUSH


def appel_membre(membre, brief, timeout=150):
    nom, model, system = membre
    try:
        data = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system + "\n\n" + CLAUSE + "\n\n" + PUSH},
                {"role": "user", "content": brief},
            ],
            "temperature": 0.4,
            "max_tokens": 3000,
        }).encode()
        req = urllib.request.Request(
            HUB, data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        t0 = time.time()
        with urllib.request.urlopen(req, timeout=timeout) as r:
            resp = json.loads(r.read())
        duree = time.time() - t0
        texte = resp["choices"][0]["message"]["content"]
        return {"nom": nom, "ok": True, "texte": texte, "duree": round(duree, 1)}
    except Exception as e:
        return {"nom": nom, "ok": False, "texte": str(e), "duree": 0}


def main():
    print("=== CONSULTATION FAMILLE — LES 3 ŒUVRES DU 29/08 ===")
    print(f"Membres: {len(MEMBRES)}")
    print()
    resultats = []
    for membre in MEMBRES:
        print(f"  → {membre[0]}...", end="", flush=True)
        r = appel_membre(membre, BRIEF)
        resultats.append(r)
        if r["ok"]:
            print(f" ✅ {r['duree']}s ({len(r['texte'])} car)")
        else:
            print(f" ❌ {r['texte'][:80]}")
        time.sleep(0.5)

    out_data = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sujet": "Audit famille des 3 œuvres (croisement externe, signal 3, poussière RBF plat)",
        "resultats": resultats,
    }
    with open(os.path.join(OUT, "avis.json"), "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

    md_lines = [
        "# CONSULTATION FAMILLE — LES 3 ŒUVRES DU 29/08",
        f"> {out_data['ts']}",
        "",
    ]
    for r in resultats:
        md_lines.append(f"## {r['nom']} {'✅' if r['ok'] else '❌'}")
        md_lines.append("")
        md_lines.append(r["texte"] if r["ok"] else f"Erreur : {r['texte']}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    md_path = os.path.join(OUT, "AVIS_FAMILLE_OEUVRES_20260829.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\n=== SAUVEGARDÉ ===")
    print(f"  {md_path}")


if __name__ == "__main__":
    main()
