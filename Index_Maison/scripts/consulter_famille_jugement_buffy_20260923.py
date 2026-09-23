#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONSULTATION FAMILLE — 23/09/2026 — « JUGEZ-MOI : est-ce ACCEPTABLE ? »
=======================================================================

Commande Christophe : « ensuite tu vas évaluer ton ouvrage des deux dernières semaines,
ensuite tu vas le demander à la famille de t'évaluer en fonctions de tes erreurs et de
l'évolution ou la sous-évolution de hulk, et leur demander si tout ceci est acceptable !
Tout ceci devient inacceptable pour l'évolution de ace777. »

MÉTHODE : le brief est construit à partir des JSON d'instruments et du registre — aucun
chiffre de tête (classe E14). La question posée est FERMÉE (acceptable / pas acceptable),
avec obligation de donner un CRITÈRE et un SEUIL : un avis sans critère ne sert à rien.
"""
import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Index_Maison" / "scripts" / "CONSULTATION_FAMILLE_JUGE_BUFFY_20260923"
OUT.mkdir(parents=True, exist_ok=True)
RUNS = ROOT / "hulk-mexc" / "runs"
HUB = "http://127.0.0.1:11435/v1/chat/completions"


def jload(p, d=None):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return d


def bloc_faits() -> str:
    auto = jload(RUNS / "AUTO_EVAL_20260923.json", {}) or {}
    net = jload(RUNS / "PNL_NET_20260923.json", {}) or {}
    go1 = jload(RUNS / "AUDIT_MEXC_VS_HULK_20260923.json", {}) or {}
    go2 = jload(RUNS / "AUDIT_SEQUENCES_20260923.json", {}) or {}
    reg = (ROOT / "Index_Maison" / "REGISTRE_ECHECS_ET_ERREURS.md").read_text(encoding="utf-8")
    classes = re.findall(r"^\|\s*\*\*(E\d+)\*\*\s*\|\s*([^|]+)\|", reg, flags=re.M)
    prog = auto.get("progression_pnl") or []
    etat = auto.get("etat_courant") or {}
    v = go2.get("verif_mexc") or {}
    L = []
    L.append("=== A. CE QUE J'AI PRODUIT EN 14 JOURS (source : mes lignes de mémoire + dates de fichiers) ===")
    L.append(f"- {auto.get('mes_lignes_memoire')} lignes de mémoire dont je suis l'auteur ; "
             f"{len(auto.get('livrables_cites_par_mes_lignes') or [])} livrables cités nommément par ces lignes.")
    L.append(f"- {auto.get('docs_recents')} documents .md et {auto.get('scripts_recents')} scripts .py créés "
             f"dans la fenêtre — ⚠ NON attribuables à moi seul (les autres agents écrivent dans les mêmes dossiers).")
    L.append("")
    L.append("=== B. MES ERREURS, LA LISTE COMPLÈTE (registre interne, classes E1→E14) ===")
    for c, t in classes:
        L.append(f"- {c} : {t.strip()[:150]}")
    L.append("")
    L.append("=== C. L'ÉVOLUTION DE HULK SUR LA MÊME FENÊTRE (source : pnl_total des journaux) ===")
    if prog:
        L.append(f"- premier journal de la fenêtre : {prog[0]['dernier_ts']} → {prog[0]['pnl_total']} $")
        L.append(f"- dernier : {prog[-1]['dernier_ts']} → {prog[-1]['pnl_total']} $")
    L.append(f"- état actuel : {etat.get('pnl_total')} $ · {etat.get('trades')} trades · "
             f"{etat.get('positions')} positions · base de référence 150 $ (paper, 0 € réel).")
    L.append(f"- PnL NET estimé (frais 5 bps/côté ESTIMÉS + spread) : brut {net.get('brut_usdt')} $ → "
             f"NET {net.get('net_estime_usdt')} $ ({net.get('couts_pct_du_brut')} % de coûts).")
    L.append("")
    L.append("=== D. CE QUE L'AUDIT DU JOUR A MESURÉ DE CASSÉ (avant mes correctifs du jour) ===")
    L.append(f"- {sum(1 for t in (go1.get('trous') or []) if 'AUCUNE vue live' in t)} paires sur {go1.get('n_paires')} "
             f"sans AUCUNE vue live → cap de mise sur un profil figé faux de 8 à 82 %.")
    L.append(f"- {sum(1 for t in (go1.get('trous') or []) if 'AUCUN profil' in t)} paires sans même un profil "
             f"(replis du code) — dont 4 des positions ouvertes.")
    L.append(f"- vérification des séquences aux klines MEXC : {v.get('conformes')} conformes, "
             f"{v.get('prix_hors_minute')} prix hors minute, {v.get('non_verifiables')} non vérifiables — "
             f"les prix fautifs existent dans une minute ANTÉRIEURE (retard, pas prix fantôme).")
    L.append(f"- journal sans provenance de prix, sans spread d'entrée, sans mise visée, sans stop nominal "
             f"({len(go2.get('anomalies_reconstruction') or [])} anomalie de reconstruction de quantité).")
    L.append("- stop = vérification périodique sur un prix en cache, pas un ordre au repos : "
             "2 sorties RIZE à −16,5 % et −39,2 % pour un stop annoncé de 8 %.")
    L.append("")
    L.append("=== E. CE QUE J'AI CORRIGÉ AUJOURD'HUI, DANS LE MOTEUR (0 ordre, 0 €) ===")
    L.append("- journal : +5 colonnes (ts du PRIX, âge du prix, spread, source du spread, coût estimé) ;")
    L.append("- satellite : couverture passée de 7-8 paires à 100 % (20/20), avec un mode « léger » pour "
             "tenir la fraîcheur ≤ 25 s après avoir mesuré qu'une passe trop lente provoquait "
             "ASPIRATION_STALE — NO_NEW_ENTRIES ;")
    L.append("- reporting : PnL net calculé à côté du brut et affiché au cockpit (le pnl_total du moteur "
             "reste brut, aucun garde-fou déplacé) ;")
    L.append("- classe E14 créée contre moi-même (conclure au-delà de ses mesures), après que VOUS "
             "l'avez nommée.")
    return "\n".join(L)


BRIEF = f"""CONTEXTE — Buffy, l'agent IA qui supervise le prototype de trading ACE777/HULK depuis 14 jours.
Je vous demande un JUGEMENT, pas un encouragement. Christophe (le propriétaire) a écrit :
« tout ceci devient inacceptable pour l'évolution de ace777 ».

{bloc_faits()}

=== LA QUESTION ===
1. Sur les 14 derniers jours : au vu de ce que j'ai produit (A), de MES erreurs (B) et de l'évolution
   de HULK (C/D), mon ouvrage est-il ACCEPTABLE ou NON ? Répondez par un mot, puis justifiez.
2. Est-ce que HULK a PROGRESSÉ, SOUS-PROGRESSÉ, ou est-ce mon travail qui a créé de la dette ?
   Distinguez ce qui est de la mécanique du prototype et ce qui est de MON fait.
3. DONNEZ UN CRITÈRE MESURABLE et un SEUIL pour trancher « acceptable » à l'avenir (ex. : nombre de
   classes d'erreurs nouvelles par semaine, écart PnL brut/net, taux de conformité des prix, etc.).
   Un avis sans critère n'a aucune valeur ici.
4. Que devrait faire Christophe MAINTENANT : continuer avec moi, changer de méthode, ou arrêter
   ce prototype ? Soyez direct.
5. Quelle est la faute la plus grave de la liste B, et pourquoi celle-là ?
6. Qu'est-ce qui vous ferait dire que je suis irrécupérable (fait mesurable) ?

Puis :
  VERDICT : ACCEPTABLE | ACCEPTABLE SOUS CONDITIONS | INACCEPTABLE
  CONFIANCE : 0-100 %
  CRITÈRE + SEUIL : explicite et mesurable
  CE QUI CHANGERAIT L'AVIS : fait(s) mesurable(s)
  SYNTHÈSE (5 lignes max).

Français, factuel, sans flatterie. Si l'information manque : « information insuffisante ».
Vous ne touchez à RIEN et vous ne donnez aucun ordre de marché."""

MODELS = ["gemini-flash-lite-latest", "nvidia/nemotron-3-super-120b-a12b:free",
          "x-ai/grok-4.3", "deepseek-ai/DeepSeek-V3-0324"]


def ask(model, timeout=300):
    payload = json.dumps({"model": model, "messages": [{"role": "user", "content": BRIEF}],
                          "max_tokens": 3000, "temperature": 0.2}).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read().decode())
    return d["choices"][0]["message"]["content"], d, round(time.time() - t0, 1)


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default=None,
                    help="sous-liste (noms séparés par des virgules) — un modèle par appel, "
                         "pour qu'un modèle lent ne perde pas les réponses déjà reçues")
    a = ap.parse_args()
    cibles = [m for m in MODELS if m in a.models.split(",")] if a.models else MODELS
    (OUT / "BRIEF.md").write_text(BRIEF, encoding="utf-8")
    print(f"FAMILLE (jugement) : {len(cibles)} modèles · brief {len(BRIEF)} car.")
    for model in cibles:
        nom = model.replace("/", "_").replace(":", "_")
        f = OUT / f"AVIS_{nom}.md"
        if f.exists() and f.stat().st_size > 200:
            print(f"[SKIP] {model}")
            continue
        try:
            c, meta, dur = ask(model)
            # FAUTE CORRIGÉE LE 23/09 (classe E16) : j'avais étiqueté cet avis « x-ai/grok-4.3 »
            # alors que le HUB l'avait SUBSTITUÉ (grok → gemini-flash-lite). Le hub expose
            # `model` (qui a RÉPONDU), `model_demande` et `substitue` : les ignorer, c'est
            # publier un avis sous un nom qui n'a rien écrit — même famille que E14.
            servi = meta.get("model") or "?"
            demande = meta.get("model_demande") or model
            substitue = bool(meta.get("substitue"))
            prov = meta.get("provider", "?")
            entete = (f"# AVIS demandé « {demande} » — RÉPONDU PAR « {servi} » (provider {prov}, {dur}s)\n")
            if substitue or servi != demande:
                entete += (f"> ⚠ **SUBSTITUTION** : le hub a servi **{servi}** à la place de "
                           f"**{demande}**. Cet avis ne compte PAS comme une voix indépendante "
                           f"de {demande} (classe E16, 23/09).\n")
            f.write_text(f"{entete}\n{c}\n", encoding="utf-8")
            (OUT / f"META_{model.replace('/', '_').replace(':', '_')}.json").write_text(
                json.dumps({"demande": demande, "servi": servi, "substitue": substitue,
                            "provider": prov, "duree_s": dur, "attempts": meta.get("attempts")},
                           indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"[OK] {model} → servi par {servi} ({dur}s, {len(c)} car."
                  + (", SUBSTITUTION" if (substitue or servi != demande) else "") + ")", flush=True)
        except Exception as e:                       # noqa: BLE001
            print(f"[ERREUR] {model}: {str(e)[:120]}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
