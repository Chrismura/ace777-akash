#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — PATTERN INSTITUTIONS fin août → septembre (30/08/2026).

Christophe : « soumets à la famille mais sans événement climatique, c'est
too much sinon. Je veux qu'elle analyse, qu'elle ajoute d'autres infos si c'est
le cas, et qu'elle trouve un pattern, ou décryptage entre les lignes. Que font
les grandes institutions fin août début septembre, le marché en septembre ?
C'est à vous de calculer et voir les millions de probabilités. »

CONTEXTE FILTRÉ : événements géostratégique + financier + on-chain VÉRIFIÉS.
VOLONTAIREMENT SANS le climat (canicule, géoingénierie, volcans, glacier Népal)
pour ne pas noyer le signal sous le bruit.

Members : GEMINI, DEEPSEEK, JUGE, ULTRA, INFERX, GROK.
Sortie : CONSULTATION_FAMILLE_PATTERN_INSTITUTIONS_20260830/ (avis.json + md).
Push excellence : chaque membre doit trouver un pattern et des probabilités.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_PATTERN_INSTITUTIONS_20260830")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu vois le pattern macro avant tout le monde."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu demandes la preuve, tu casses les illusions."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches : GO / GO AVEC RESERVES / NON, avec probabilités."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Robustesse à l'échelle, million de scénarios."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Logique interne, pièges, timing."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon pragmatique de la famille ACE777. Tu vois les manœuvres derrière les manœuvres."),
]

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger. "
    "Propose AUTRE CHOSE ou une AMÉLIORATION. Corriger n'est pas suffisant."
)

PUSH = (
    "PUSH EXCELLENCE : Ta première réponse est le PLAFOND, pas le plancher. "
    "Va 30% plus loin. Une réponse confortable est ratée."
)

BRIEF = """CONTEXTE (superviseur Buffy, 30/08/2026) — DÉCRYPTER CE QUE FONT LES GRANDES INSTITUTIONS FIN AOÛT → SEPTEMBRE

=== ÉVÉNEMENTS VÉRIFIÉS (géostratégie + finance + on-chain — SANS le climat) ===

--- ON-CHAIN BTC (notre brut) ---
1) Signature CPFP/Poussière active et PERSISTANTE : bloc anormal de 20 755 BTC
   ≈ 1,8 Md$ (z-score 71,8), 87 344 BTC sortis des coffres froids de Binance +
   Bitbank (15 gros blocs), poussière ~45-50/50, blocs privatisés ~7%.
   Le phénomène a commencé le 25/08 (~00:10 UTC) et dure EN CONTINU depuis
   (143-144 déclenchements/jour), au-delà de toute fenêtre ponctuelle.
2) Direction prix : NEUTRE. BTC calme (~0,7%/24h). Funding calme.

--- GÉOPOLITIQUE / FINANCE ---
3) CIA → Moscou (25/08) : première visite d'un patron de la CIA en Russie
   depuis 2022, secrète, révélée après coup, en pleine escalade Ukraine.
4) GUERRE IRAN-ÉTATS-UNIS (2026) : lancée 28/02 par US+Israël (Op. Epic Fury)
   vs Iran + Axe + Houthis. Moyen-Orient entier. Strait d'Ormuz = point
   ultra-nerveux (péages, trafic à un plus-bas de 3 mois). Cessez-le-feu fin
   août : Khamenei approuve après un « coup de pouce de la Chine » (~28/08).
   Hegseth menace encore de « frappes cinétiques » à Hormuz (24/08).
5) Jackson Hole 2026 (28/08) : symposium Fed de Kansas City, keynote du
   président Warsh (premier discours comme patron de la Fed). En 2022 son
   discours a fait chuter BTC de ~9%. Notre postulat maison (25/08) : purge
   des mineurs puis plancher $65-68K, puis remontée $90-120K fin d'année.
6) Décret Trump 26/08 : ÉTAT D'URGENCE NATIONAL sur le réseau électrique US
   (bulk-power system), interdiction équipements étrangers (vise la Chine),
   motivé par l'IA + la défense + la fabrication avancée.
7) Vatican (11-20/08) : refonte de sa finance interne (8 nouveaux membres au
   Conseil pour l'Économie, retrait d'autorité à la banque du Vatican sur les
   investissements).
8) OR : banques centrales ACHÈTENT fort (289 t au 2e trim., 5× le précédent ;
   89% des banques centrales tablent sur + de réserves). RUSSIE : la Banque de
   Russie LIQUIDE son or (plus bas depuis 2020, vend 43-44 t pour son déficit
   de ~6 tr de roubles) — un État a besoin de cash, pas d'accumuler.

=== LA QUESTION DE CHRISTOPHE ===
« Je veux que vous analysiez, que vous AJOUTIEZ d'autres infos si c'est le cas,
et que vous trouviez un PATTERN, ou un décryptage ENTRE LES LIGNES. Que font
les grandes institutions fin août début septembre ? Le marché en septembre ?
C'est à vous de calculer les millions de probabilités. »

Structure ta réponse ainsi :
1) LE PATTERN que tu vois (le geste commun derrière tous ces événements).
2) CE QUE LES INSTITUTIONS FONT VRAIMENT fin août (et pourquoi maintenant).
3) LE MARCHÉ EN SEPTEMBRE : scénarios pondérés en probabilités (%, avec le
   signal qui validerait / invaliderait chacun).
4) CE QU'ON RATE ENCORE (un angle mort — pas du conformisme).
5) UNE ACTION PRÉCISE pour nous (pas un truc vague).

Ne me dis pas « c'est bien, continuez ». Décrypte. Chiffre. Tranche.
""" + CLAUSE + "\n\n" + PUSH


def appel_membre(membre, brief, timeout=180):
    nom, model, system = membre
    try:
        data = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system + "\n\n" + CLAUSE + "\n\n" + PUSH},
                {"role": "user", "content": brief},
            ],
            "temperature": 0.4,
            "max_tokens": 3500,
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
    print("=== CONSULTATION FAMILLE — PATTERN INSTITUTIONS FIN AOÛT → SEPTEMBRE ===")
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
        "sujet": "Pattern institutions fin août → septembre, sans climat",
        "resultats": resultats,
    }
    with open(os.path.join(OUT, "avis.json"), "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

    md_lines = [
        "# CONSULTATION FAMILLE — PATTERN INSTITUTIONS FIN AOÛT → SEPTEMBRE",
        f"> {out_data['ts']} — sans événements climatiques",
        "",
    ]
    for r in resultats:
        md_lines.append(f"## {r['nom']} {'✅' if r['ok'] else '❌'}")
        md_lines.append("")
        md_lines.append(r["texte"] if r["ok"] else f"Erreur : {r['texte']}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
    md_path = os.path.join(OUT, "AVIS_FAMILLE_PATTERN_INSTITUTIONS_20260830.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\n=== SAUVEGARDÉ ===")
    print(f"  {md_path}")


if __name__ == "__main__":
    main()