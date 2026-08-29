#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — DÉCOUVERTES ON-CHAIN + BLOCS PRIVATISÉS (29/08/2026).

Christophe, 29/08 : « fais consultation famille pour ce que tu as découvert...
Les gens en face savent tout ça, et c'est les rois de la manipulation. »

On pose le problème SANS révéler nos conclusions (avis indépendant), avec la
clause permanente + PUSH EXCELLENCE + l'angle manipulation (les acteurs en face
connaissent ces signaux et les retournent).

Membres : GEMINI, DEEPSEEK, JUGE, ULTRA, INFERX, GROK.
Sortie : CONSULTATION_FAMILLE_ONCHAIN_SHORT_20260829/ (avis.json + md).
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_ONCHAIN_SHORT_20260829")
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

BRIEF = """CONTEXTE (superviseur Buffy, 29/08/2026) — ON-CHAIN BTC + BLOCS PRIVATISÉS

=== LES FAITS OBSERVÉS (données réelles) ===
1) Sur 6 jours, 29 gros blocs de mouvements BTC (dédupliqués). Le flux dominant :
   45 910 BTC sont passés du HOT wallet de Binance vers son COLD storage, en
   9 paquets de 2 000 à 7 700 BTC espacés de 8 à 50 heures. Un autre échange
   (Bitbank) a consolidé 20 755 BTC cold→cold le 29/08.
2) Parallèlement, le détecteur de blocs « privatisés » (tx jamais vues dans la
   mempool publique) montre : 20 % des blocs ont >10 % de tx fantômes, des pics
   à 89-99 %, 112 alertes en 8 jours dont des événements à 20 000+ BTC.
   Le 29/08 à ~14:11Z, le même moment où Bitbank a consolidé 20 755 BTC, un bloc
   privé contenait 20 761 BTC « jamais vus ».
3) Contexte marché : BTC ~77 700 $. Mi-août, un short squeeze violent a porté
   BTC de ~62k à 81k en une semaine (+22,7 % hebdo, ~5 Mds$ de positions
   détruites). Catalyst : le Trésor US a doublé ses rachats de liquidité.
   Maintenant : RSI ~82 (extrême), open interest ~58 Mds$, funding redevenu
   positif, 59 % des options en calls. ETF spot US : ~1,92 Mds$ d'inflows la
   semaine du 21/08. Des wallets BTC dormants depuis 7-11 ans se sont réveillés
   en août (16 400 BTC le 03/08, 1 214 BTC le 20/08) MAIS vers des wallets neufs,
   AUCUN vers un exchange.
4) Le protocole DATUM (2026) permet aux mineurs de construire leurs blocs avec
   une mempool privée : un bloc Ocean/DATUM peut avoir 30-90 % de tx « jamais
   vues dans la mempool publique » — c'est structurel, pas anormal.

=== LA QUESTION (à trancher en famille) ===
A) Un « gros short » sur BTC est-il jouable maintenant ? Ou est-ce un piège ?
   Évalue : le RSI extrême et les longs crowdés (argument bear) VS l'hivernage
   de supply par les exchanges et les ETF inflows (argument bull).
B) Les blocs privatisés à gros volume (20 000+ BTC) sont-ils un signal de VENTE
   imminente, d'ACCUMULATION, ou un artefact technique sans signification ?
C) ANGLE MANIPULATION (le point crucial) : « Les gens en face savent tout ça. »
   Un acteur institutionnel qui connaît nos signaux peut-il les utiliser pour
   nous piéger ? Par exemple : déplacer des BTC vers cold storage pour faire
   croire à de l'accumulation puis vendre en OTC ? Ou l'inverse ? Quels signaux
   de manipulation devrions-nous surveiller pour ne pas être dupés ?

Ne me dis pas « c'est bien, continuez ». Donne des avis indépendants, tranchés,
avec des scénarios chiffrés et des signaux de vérification précis.
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
    print("=== CONSULTATION FAMILLE — ON-CHAIN SHORT + BLOCS PRIVATISÉS ===")
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
        "sujet": "On-chain BTC (short) + blocs privatisés + angle manipulation",
        "resultats": resultats,
    }
    with open(os.path.join(OUT, "avis.json"), "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

    md_lines = [
        "# CONSULTATION FAMILLE — ON-CHAIN SHORT + BLOCS PRIVATISÉS",
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

    md_path = os.path.join(OUT, "AVIS_FAMILLE_ONCHAIN_SHORT_20260829.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\n=== SAUVEGARDÉ ===")
    print(f"  {md_path}")


if __name__ == "__main__":
    main()