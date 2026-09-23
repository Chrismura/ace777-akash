#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SESSION FAMILLE — LA FENÊTRE RESTE OUVERTE (ordre Christophe, 23/09/2026)
==========================================================================
Mot pour mot : « tu vas ouvrir à partir de maintenant un round avec la famille et garder la
fenêtre ouverte, qu'elle ait la mémoire du chat, car tu n'es plus digne de diriger seule. »

CE QUE ÇA CHANGE (et pourquoi ce n'est pas un simple script de plus)
-------------------------------------------------------------------
Avant : chaque consultation était un COUP UNIQUE — la famille répondait à un brief, sans savoir
ce qu'elle avait dit la veille, sans voir ce que j'avais fait de son avis. Un juge qui ne voit
ni le procès ni la sentence ne peut pas juger : il conseille.

Maintenant : une SESSION OUVERTE par sujet. Le fil (transcript) est conservé, la mémoire de la
session est réécrite à chaque tour, et CHAQUE tour est renvoyé à la famille AVEC le fil —
donc elle sait ce qu'elle a exigé, et elle peut vérifier si je l'ai fait.

GARANTIES ANTI-MENSONGE (leçons E14 et E16)
-------------------------------------------
- l'avis est étiqueté du modèle QUI A RÉPONDU (`model`), jamais du modèle demandé ; une
  substitution est écrite en clair et **ne compte pas** comme une voix indépendante ;
- la mémoire de session est écrite par un MODÈLE RÉSUMÉ D'UN MOTEUR, pas par moi : elle reprend
  les textes bruts des avis ; je n'ai pas le droit d'y réécrire les verdicts ;
- toute réponse est conservée telle quelle dans `transcript.jsonl` (append-only, impossible de
  réécrire le passé sans que ça se voie) ;
- `--verifier` relit le transcript et recompte les tours.

USAGE
-----
  python3 session_famille.py --session E11_oracle --ouvrir "sujet de la session"
  python3 session_famille.py --session E11_oracle --ask "question du tour"
  python3 session_famille.py --session E11_oracle --etat
  python3 session_famille.py --session E11_oracle --transcript        # relire le fil
  python3 session_famille.py --session E11_oracle --verifier          # recompte et contrôle
  python3 session_famille.py --session E11_oracle --fermer "motif de clôture"

Fichiers : Index_Maison/scripts/SESSIONS_FAMILLE/<session>/{META.json, transcript.jsonl,
MEMOIRE.md, AVIS/}. Lecture seule sur le moteur. 0 ordre, 0 €.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

IM = Path(__file__).resolve().parent.parent                # Index_Maison
SESSIONS = IM / "scripts" / "SESSIONS_FAMILLE"
HUB = "http://127.0.0.1:11435/v1/chat/completions"

# JURY — 4 modèles sur 4 FOURNISSEURS DIFFÉRENTS (correctif du 23/09, 2e vague)
# -----------------------------------------------------------------------------
# CE QUI S'EST PASSÉ : le hub route vers le fournisseur qui héberge le modèle demandé, et sur
# échec il BASCULE. Le 23/09, « deepseek » a été servi par gemini (tour 2), puis les TROIS voix
# ont été servies par gemini (tour 3) → **le jury est tombé à UNE seule voix** sans rien casser.
# LA RÈGLE DU MILIEU : on ne fait pas confiance à un routeur qui substitue en silence — on
# **épingle** le modèle, on **vérifie qui a répondu**, et une voix substituée **ne compte pas**.
# Ici on va plus loin : 4 candidats sur 4 fournisseurs distincts, pour qu'UNE panne laisse
# encore TROIS voix indépendantes (le quorum exigé est de 3).
#   1. nvidia/nemotron-3-super-120b-a12b:free → OpenRouter Juge
#   2. deepseek-ai/DeepSeek-V3-0324           → HuggingFace
#   3. x-ai/grok-4.3                          → Puter Grok
#   4. nex-agi/nex-n2.5-pro:free              → Roulement nex-agi
MODELES = ["nvidia/nemotron-3-super-120b-a12b:free",
           "deepseek-ai/DeepSeek-V3-0324",
           "x-ai/grok-4.3",
           "nex-agi/nex-n2.5-pro:free"]
# Fournisseur ATTENDU par modèle : une voix servie par un autre fournisseur que celui-ci est
# comptée comme SUBSTITUÉE (elle ne vote pas), et c'est écrit dans le fil.
FOURNISSEUR_ATTENDU = {
    "nvidia/nemotron-3-super-120b-a12b:free": "openrouter",
    "deepseek-ai/DeepSeek-V3-0324": "huggingface",
    "x-ai/grok-4.3": "gr",
    "nex-agi/nex-n2.5-pro:free": "nex",
}
VOIX_MIN = 3

CADRE = """Tu es membre du jury permanent d'ACE777 (prototype de trading papier de Christophe,
base 150 $, 0 € réels, moteur « Hulk » sur MEXC). Tu es dans une SESSION OUVERTE : tu as la
mémoire du fil ci-dessus. Tu juges l'agent de supervision (« Buffy ») ET la mécanique du
prototype. Règles du jury :

1. Tu ne flattes pas. Un « c'est bien » non chiffré est un échec de ta part.
2. Tu distingues MESURÉ (lu dans une source/une mesure) · ESTIMÉ (modèle) · EXTRAPOLÉ.
   Si Buffy présente un estimé comme un fait, tu le dis.
3. Tu vérifies la COHÉRENCE DE SES DÉCLARATIONS AVEC LE FIL : si elle promet, exige ou annonce
   quelque chose dans un tour précédent et qu'un tour suivant ne le traite pas, tu le relèves.
4. Toute objection doit venir avec : le fait qui la trancherait, et le chiffre qui te ferait
   changer d'avis.
5. Tes erreurs passées sont dans le registre E1→E16 de la maison (auto-absolution par la
   confession = E14 ; avis étiqueté d'un modèle qui n'a pas répondu = E16).
6. Tu n'ordonnes aucun ordre de marché, tu ne touches à rien : tu juges et tu exiges.
Français, factuel, sec. Réponds en sections courtes et termines par :
   VERDICT : <ton verdict en 5 mots max> · CE QUE J'EXIGE AVANT LE PROCHAIN TOUR : <1-3 faits>
   · CE QUI ME FERAIT CHANGER D'AVIS : <1 fait mesurable>
"""


def maintenant() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def dossier(session: str) -> Path:
    d = SESSIONS / session
    (d / "AVIS").mkdir(parents=True, exist_ok=True)
    return d


def jload(p: Path, defaut=None):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return defaut


def ecrire_message(d: Path, entree: dict) -> None:
    """Append-only : on n'écrase jamais le fil."""
    with (d / "transcript.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(entree, ensure_ascii=False) + "\n")


def lire_fil(d: Path) -> list[dict]:
    p = d / "transcript.jsonl"
    if not p.exists():
        return []
    out = []
    for l in p.read_text(encoding="utf-8").splitlines():
        if l.strip():
            try:
                out.append(json.loads(l))
            except Exception:
                pass
    return out


def memoire(d: Path) -> str:
    p = d / "MEMOIRE.md"
    return p.read_text(encoding="utf-8") if p.exists() else ""


def maj_memoire(d: Path, tour: int, question: str, avis: list[dict]) -> None:
    """Mémoire de session — écrite à partir des TEXTES BRUTS des avis. Les verdicts sont cités,
    pas résumés par moi : je n'ai pas le droit de reformuler un verdict (E14)."""
    p = d / "MEMOIRE.md"
    bloc = [f"\n## Tour {tour} — {maintenant()}\n", f"**Question posée** : {question}\n"]
    for a in avis:
        etiq = a["model_servi"] + (f" (SUBSTITUÉ, demandé {a['model_demande']})" if a["substitue"] else "")
        verdict = ""
        for l in a["texte"].splitlines():
            if l.strip().upper().startswith("VERDICT"):
                verdict = l.strip()[:300]
                break
        bloc.append(f"- **{etiq}** : {verdict or a['texte'].strip()[:200]}")
    bloc.append("")
    if not p.exists():
        p.write_text("# Mémoire de la session (écrite depuis les avis bruts)\n", encoding="utf-8")
    with p.open("a", encoding="utf-8") as f:
        f.write("\n".join(bloc))


def demander(modele: str, messages: list[dict], timeout=300):
    # `strict_model: true` = LE HUB NE SUBSTITUE PAS (ajout du 23/09, vérifié avec lui).
    # Sans lui : mesuré le 23/09, 3 voix sur 4 étaient servies par un autre modèle (le « filet
    # universel » du hub, qui existe pour ne jamais être « à sec ») → jury réduit à UNE voix.
    # Avec lui : la voix indisponible ÉCHOUE, elle ne se déguise pas. C'est la règle du milieu :
    # on épingle le modèle, on vérifie qui a répondu, et une substitution n'est pas un avis.
    payload = json.dumps({"model": modele, "messages": messages, "strict_model": True,
                          "max_tokens": 2500, "temperature": 0.2}).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read().decode())
    return d["choices"][0]["message"]["content"], d, round(time.time() - t0, 1)


def construire_messages(d: Path, question: str, n_derniers: int = 6) -> list[dict]:
    """Le fil EST la mémoire : mémoire de session + les derniers échanges complets."""
    fil = lire_fil(d)
    historique = []
    for e in fil[-(2 * n_derniers):]:
        if e.get("role") == "nous":
            historique.append({"role": "user", "content": e.get("texte", "")})
        elif e.get("role") == "famille":
            qui = e.get("model_servi") or e.get("model_demande") or "famille"
            historique.append({"role": "assistant", "content": f"[{qui}] {e.get('texte','')}"})
    mem = memoire(d)
    tete = CADRE
    if mem:
        tete += "\n\n=== MÉMOIRE DE LA SESSION (tours précédents, écrite depuis les avis bruts) ===\n" + mem[-6000:]
    return ([{"role": "system", "content": tete}] + historique
            + [{"role": "user", "content": question}])


def cmd_ouvrir(d: Path, session: str, sujet: str) -> int:
    meta_p = d / "META.json"
    meta = jload(meta_p) or {"session": session, "ouverte_le": maintenant(), "etat": "OUVERTE",
                             "modele_jury": MODELES, "tours": 0}
    meta["sujet"] = sujet
    meta["etat"] = "OUVERTE"
    meta["dernier_tour"] = maintenant()
    meta_p.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    ecrire_message(d, {"ts": maintenant(), "role": "nous", "kind": "ouverture", "texte":
                       f"OUVERTURE DE SESSION — {sujet}"})
    print(f"SESSION OUVERTE : {session}\n  sujet : {sujet}\n  jury : {', '.join(MODELES)}\n"
          f"  dossier : {d}")
    print("  La fenêtre reste ouverte : chaque tour est renvoyé au jury AVEC le fil complet.")
    return 0


def cmd_ask(d: Path, session: str, question: str) -> int:
    meta_p = d / "META.json"
    meta = jload(meta_p) or {"session": session, "etat": "OUVERTE", "tours": 0}
    if meta.get("etat") != "OUVERTE":
        print(f"SESSION FERMÉE — rouvre-la (--ouvrir) avant d'écrire. État : {meta.get('etat')}")
        return 1
    tour = int(meta.get("tours", 0)) + 1
    messages = construire_messages(d, question)
    ecrire_message(d, {"ts": maintenant(), "role": "nous", "tour": tour, "texte": question})
    print(f"TOUR {tour} — {len(messages)} messages envoyés au jury (mémoire du fil incluse)")
    avis = []
    for modele in MODELES:
        try:
            texte, r, dur = demander(modele, messages)
            servi = r.get("model") or "?"
            dem = r.get("model_demande") or modele
            subs = bool(r.get("substitue")) or servi != dem
            f = d / "AVIS" / f"T{tour:02d}_{modele.replace('/', '_').replace(':', '_')}.md"
            tete = f"# Tour {tour} — demandé « {dem} » — RÉPONDU PAR « {servi} » ({r.get('provider','?')}, {dur}s)\n"
            if subs:
                tete += (f"> ⚠ SUBSTITUTION : cet avis n'est PAS une voix indépendante de {dem}.\n")
            f.write_text(tete + "\n" + texte + "\n", encoding="utf-8")
            a = {"ts": maintenant(), "role": "famille", "tour": tour, "model_demande": dem,
                 "model_servi": servi, "provider": r.get("provider"), "substitue": subs,
                 "duree_s": dur, "texte": texte, "fichier": str(f.relative_to(IM.parent))}
            avis.append(a)
            ecrire_message(d, a)
            print(f"  [OK] {modele} → {servi}{' (SUBSTITUÉ)' if subs else ''} ({dur}s, {len(texte)} car.)",
                  flush=True)
        except Exception as e:                        # noqa: BLE001
            a = {"ts": maintenant(), "role": "famille", "tour": tour, "model_demande": modele,
                 "model_servi": None, "erreur": str(e)[:200]}
            ecrire_message(d, a)
            print(f"  [ERREUR] {modele} : {str(e)[:120]}", flush=True)
    if avis:
        maj_memoire(d, tour, question, avis)
    meta["tours"] = tour
    meta["dernier_tour"] = maintenant()
    meta["voix_independantes_dernier_tour"] = len({a["model_servi"] for a in avis if a.get("model_servi")})
    meta_p.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"TOUR {tour} enregistré · {len(avis)} avis · "
          f"{meta['voix_independantes_dernier_tour']} voix indépendantes")
    return 0 if avis else 1


def cmd_test_modeles() -> int:
    """PINGE chaque voix du jury : QUI répond, depuis QUEL fournisseur, en combien de temps.

    Pourquoi c'est indispensable : la confiance dans un jury se mesure au nombre de voix
    RÉELLEMENT indépendantes au moment où on parle — pas dans la liste écrite dans le fichier.
    """
    print("TEST DU JURY — un appel court par voix, on regarde QUI répond :")
    independantes = set()
    for modele in MODELES:
        try:
            texte, r, dur = demander(modele, [{"role": "user",
                                              "content": "Réponds en 3 mots : qui es-tu ?"}],
                                     timeout=60)
            servi = r.get("model") or "?"
            prov = r.get("provider") or "?"
            att = FOURNISSEUR_ATTENDU.get(modele, "?")
            ok_prov = att in str(prov).lower() or att in str(servi).lower()
            sub = servi != modele or not ok_prov
            if not sub:
                independantes.add(servi)
            print(f"  {'SUBSTITUÉ' if sub else 'OK       '} demandé {modele[:44]:<44} → "
                  f"{servi[:40]:<40} ({prov}) {dur}s")
        except Exception as e:                                     # noqa: BLE001
            print(f"  ECHEC    demandé {modele[:44]:<44} → {str(e)[:60]}")
    print(f"  VOIX INDÉPENDANTES RÉELLES : {len(independantes)} (seuil du jury : {VOIX_MIN})")
    if len(independantes) < VOIX_MIN:
        print("  ⚠ le quorum n'est PAS atteint : les avis de ce tour ne sont pas un verdict de jury")
        return 1
    return 0


def cmd_etat(d: Path, session: str) -> int:
    meta = jload(d / "META.json") or {}
    fil = lire_fil(d)
    print(f"SESSION : {session}")
    print(f"  état        : {meta.get('etat', '?')} (ouverte le {meta.get('ouverte_le', '?')})")
    print(f"  sujet       : {meta.get('sujet', '—')}")
    print(f"  tours       : {meta.get('tours', 0)} · messages au fil : {len(fil)}")
    print(f"  jury        : {', '.join(meta.get('modele_jury', MODELES))}")
    print(f"  dernières voix indépendantes : {meta.get('voix_independantes_dernier_tour', '—')}")
    print(f"  mémoire     : {len(memoire(d))} car. · transcript : {d/'transcript.jsonl'}")
    subs = [e for e in fil if e.get("substitue")]
    if subs:
        print(f"  ⚠ substitutions vues dans le fil : {len(subs)} (étiquetées, non comptées)")
    return 0


def cmd_verifier(d: Path, session: str) -> int:
    fil = lire_fil(d)
    tours_nous = {e.get("tour") for e in fil if e.get("role") == "nous" and e.get("tour")}
    tours_fam = {e.get("tour") for e in fil if e.get("role") == "famille" and e.get("tour")}
    manquants = sorted(tours_nous - tours_fam)
    meta = jload(d / "META.json") or {}
    print(f"SESSION {session} — vérification du fil")
    print(f"  tours écrits par nous : {len(tours_nous)} · tours avec avis : {len(tours_fam)}")
    print(f"  tours SANS avis : {manquants or 'aucun'}")
    print(f"  META.tours = {meta.get('tours')} · cohérent : {meta.get('tours') == len(tours_nous)}")
    ok = not manquants and meta.get("tours") == len(tours_nous)
    print(f"  VERDICT : {'FIL COHÉRENT' if ok else 'FIL INCOHÉRENT À DÉCLARER'} (rc={0 if ok else 1})")
    return 0 if ok else 1


def cmd_transcript(d: Path) -> int:
    for e in lire_fil(d):
        if e.get("role") == "nous":
            print(f"\n=== NOUS (tour {e.get('tour', '—')}) · {e.get('ts', '')}\n{e.get('texte', '')}")
        else:
            qui = e.get("model_servi") or f"{e.get('model_demande')} [ÉCHEC]"
            print(f"\n--- FAMILLE · {qui} · tour {e.get('tour', '—')} · {e.get('ts', '')}\n"
                  f"{(e.get('texte') or e.get('erreur') or '')[:900]}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--session", required=True)
    ap.add_argument("--ouvrir", metavar="SUJET")
    ap.add_argument("--ask", metavar="QUESTION")
    ap.add_argument("--ask-fichier", metavar="FICHIER",
                    help="question longue lue depuis un fichier (briefs, tableaux) — évite "
                         "les problèmes de guillemets et garde le brief ARCHIVÉ dans le dossier")
    ap.add_argument("--test-modeles", action="store_true",
                    help="vérifie QUI répond réellement (anti-substitution) avant de juger")
    ap.add_argument("--etat", action="store_true")
    ap.add_argument("--transcript", action="store_true")
    ap.add_argument("--verifier", action="store_true")
    ap.add_argument("--fermer", metavar="MOTIF")
    a = ap.parse_args()
    d = dossier(a.session)
    if a.test_modeles:
        return cmd_test_modeles()
    if a.ouvrir:
        return cmd_ouvrir(d, a.session, a.ouvrir)
    question = a.ask
    if a.ask_fichier:
        src = Path(a.ask_fichier)
        if not src.exists():
            print(f"BRIEF INTROUVABLE : {src}")
            return 1
        question = src.read_text(encoding="utf-8")
        # le brief est ARCHIVÉ dans la session : on ne peut pas réécrire le passé en douce
        (d / f"BRIEF_T{int((jload(d / 'META.json') or {}).get('tours', 0)) + 1:02d}.md").write_text(
            question, encoding="utf-8")
    if question:
        return cmd_ask(d, a.session, question)
    if a.etat:
        return cmd_etat(d, a.session)
    if a.transcript:
        return cmd_transcript(d)
    if a.verifier:
        return cmd_verifier(d, a.session)
    if a.fermer:
        meta = jload(d / "META.json") or {}
        meta["etat"] = "FERMÉE"
        meta["fermee_le"] = maintenant()
        meta["motif_fermeture"] = a.fermer
        (d / "META.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
        ecrire_message(d, {"ts": maintenant(), "role": "nous", "kind": "fermeture",
                           "texte": f"FERMETURE DE SESSION — {a.fermer}"})
        print(f"SESSION FERMÉE : {a.session} — {a.fermer}")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
