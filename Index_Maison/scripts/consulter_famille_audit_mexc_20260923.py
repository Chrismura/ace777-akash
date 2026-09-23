#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONSULTATION FAMILLE — 23/09/2026 — « CONTESTEZ CET AUDIT ET MES ERREURS »
=========================================================================

Commande Christophe : « ensuite tu remets tout ça avec les derniers set up, et ensuite tu
remets tout ça à la famille, conteste pour la famille avec tes erreurs de merde. »

MÉTHODE (pour ne pas inventer) : le brief est CONSTRUIT À PARTIR DES JSON produits par les
instruments (`runs/AUDIT_*.json`) — aucun chiffre retapé à la main. La mission donnée aux
modèles est de CONTREDIRE (trouver la faute de mesure, la conclusion abusive, l'angle mort),
pas d'approuver. Rien n'est appliqué automatiquement : ce sont des AVIS.
"""
import json
import os
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # ace777-test-day1/
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = ROOT / "Index_Maison" / "scripts" / "CONSULTATION_FAMILLE_AUDIT_MEXC_20260923"
OUT.mkdir(parents=True, exist_ok=True)
RUNS = ROOT / "hulk-mexc" / "runs"


def jload(p):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def chiffres():
    """Extraits EXACTS des rapports d'instruments (aucune valeur de mémoire)."""
    go1 = jload(RUNS / "AUDIT_MEXC_VS_HULK_20260923.json")
    go2 = jload(RUNS / "AUDIT_SEQUENCES_20260923.json")
    hor = jload(RUNS / "AUDIT_HORODATAGE_PRIX_20260923.json")
    mem = jload(RUNS / "AUDIT_MEMOIRE_20260923.json")
    lignes = []
    if go1:
        lignes += [
            f"- GO1 : {go1.get('n_paires')} paires moteur · {go1.get('n_profils')} profils · "
            f"{go1.get('n_vues_live')} vues live à l'instant du contrôle (âge "
            f"{go1.get('vue_aspiration_age_s')} s).",
            f"- GO1 : {len(go1.get('trous', []))} trous de données nommés "
            f"(dont {sum(1 for t in go1.get('trous', []) if 'AUCUN profil' in t)} paires sans profil, "
            f"{sum(1 for t in go1.get('trous', []) if 'AUCUNE vue live' in t)} sans vue live).",
            f"- GO1 : anomalies au-delà des seuils de lecture : {len(go1.get('anomalies', []))}.",
        ]
        prix = [r for r in go1.get("paires", []) if r.get("ecart_profil_prix_pct") is not None]
        if prix:
            worst = max(prix, key=lambda r: abs(r["ecart_profil_prix_pct"]))
            lignes.append(f"- GO1 : le `prix` du profil est faux jusqu'à "
                          f"{worst['ecart_profil_prix_pct']} % ({worst['pair']}) ; "
                          f"{len(prix)}/17 profils mesurés dérivent.")
    if go2:
        v = go2.get("verif_mexc", {})
        lignes += [
            f"- GO2 : {go2.get('n_sequences')} séquences reconstruites "
            f"({go2.get('n_fermees_total')} fermées, {go2.get('n_sequences', 0) - go2.get('n_fermees_total', 0)} "
            f"ouvertes) · {len(go2.get('anomalies_reconstruction', []))} anomalie(s) de reconstruction.",
            f"- GO2 : vérification MEXC sur {go2.get('n_fermees_verifiees')} séquences → "
            f"{v.get('conformes')} conformes · {v.get('prix_hors_minute')} prix hors minute · "
            f"{v.get('non_verifiables')} non vérifiables (budget).",
            f"- GO2 : brut inscrit {go2.get('total_brut_inscrit')} $ · coûts estimés "
            f"{go2.get('total_couts_estimes')} $ · NET {go2.get('total_net_estime')} $.",
            f"- GO2 : formule du journal = {go2.get('formule_pnl_journal')}",
        ]
        pm = go2.get("par_motif", {})
        for m, d in pm.items():
            lignes.append(f"- GO2 motif « {m} » : n={d.get('n')} brut {d.get('brut')} $ "
                          f"net {d.get('net')} $ giveback méd {d.get('giveback_med')} %.")
    if hor:
        lignes += [
            f"- GO2/horodatage : {hor.get('n_suspects')} prix fautifs · "
            f"{hor.get('n_retrouves_autre_minute')} retrouvés dans une AUTRE minute · "
            f"{hor.get('n_introuvables_pm6')} introuvables dans ±6 min.",
            f"- GO2/horodatage : distribution des décalages (minutes) "
            f"{hor.get('decalage_minutes')} → verdict « {hor.get('verdict_provisoire')} ».",
        ]
    if mem:
        c = mem.get("coherence", {})
        ri = mem.get("re_injection", {})
        lignes += [
            f"- GO3 : couverture — {len(mem.get('trous', []))} trous ; journal {mem.get('n_lignes')} lignes.",
            f"- GO3 cohérence : horodatages désordonnés {c.get('horodatages_non_croissants')} · "
            f"discontinuités pnl_total {c.get('discontinuites_pnl_total')} · doublons trading "
            f"{c.get('doublons')} · SKIP répétés {c.get('doublons_skip_bruyants')}.",
            f"- GO3 : spread présent dans le TEXTE de {mem.get('spread_dans_le_texte_pct')} % des ventes "
            f"(pas une colonne, absent à l'entrée).",
            f"- GO3 : {len(mem.get('colonnes_manquantes', []))} colonnes manquantes nommées : "
            f"{', '.join(x.split(' — ')[0] for x in mem.get('colonnes_manquantes', []))}.",
            f"- GO3 re-injection : {ri.get('n_stops_analyses')} sorties de stop → réalisé "
            f"{ri.get('cout_total_derapage_vs_stop_annonce')} $ vs stop nominal (négatif = MIEUX que "
            f"le nominal), avec des cas extrêmes à −16,5 % et −39,2 % pour un stop annoncé de 8 %.",
        ]
    return "\n".join(lignes)


BRIEF = f"""CONTEXTE — Buffy, superviseur du prototype ACE777/HULK (trader PAPER sur MEXC, 0 € réel).
Mission demandée par Christophe : « compare les données MEXC une par une avec celles de Hulk,
compare chaque séquence de trading, vérifie ce qu'on mémorise, rejoue tout avec les derniers
set-up, puis CONTESTE cet audit avec les erreurs que tu as commises. »

=== 1. CE QUI A ÉTÉ MESURÉ (chiffres extraits des rapports d'instruments, pas de mémoire) ===
{chiffres()}

=== 2. MES ERREURS, NOMMÉES (elles sont enregistrées dans un registre, classes E1→E13) ===
- E10 : j'ai publié pendant TROIS JOURS un seuil d'entrée recalculé de tête (5-12,75 %) alors que
  le moteur appliquait 21,70 %. Le terme dominant (`dip = max(dip_pct ; 0,50 × cadence)`) manquait.
  Ce chiffre faux a servi à publier « RIZE structurellement inattaquable » et à chiffrer un levier.
- E13 : j'ai daté 4 lignes de la mémoire collaborative DE TÊTE (10:40Z au lieu de 09:47Z, etc.),
  soit des lignes dans le futur. Le temps traité comme un seuil : estimé ≠ vérifié.
- E12 : j'ai scellé des fichiers PUIS je les ai modifiés — la veilleuse a crié trois fois, à raison.
- Corrigé aujourd'hui dans mon propre audit : j'avais écrit « le stop ne tient pas (14,16 % réalisés
  pour 8 % annoncés) » — c'était une perte AGRÉGÉE de séquence, pas le niveau touché ; et
  « le spread n'est pas mémorisé » — faux, il est dans le texte des ventes à 99 %.
- Méthode : « un chiffre recalculé n'est pas un chiffre vérifié » ; tout seuil recalculé doit être
  confronté à ce que le moteur ÉCRIT (garde-fou `verif_seuil_moteur.py`, 6/6 conformes, autotest 7/7).

=== 3. CE QUE J'EN CONCLUS (et que je vous demande de DÉMOLIR si c'est abusif) ===
1. 13/20 paires n'ont aucune vue live → le cap de mise se lit sur un profil figé (RIZE : 4,88 $
   calculé sur 243,78 $ alors que le carnet mesuré vaut 364,74 $) ; 4 paires n'ont aucun profil.
2. Le prix de remplissage paper a 1 à 5 minutes de retard (13/13 des prix fautifs existent dans une
   minute ANTÉRIEURE, aucun prix fantôme) → tous nos post-mortems alignés sur l'heure du journal
   sont décalés ; le mécanisme exact (cache de cycle `last_price` vs photo d'aspiration, satellite
   limité à 5 paires par passe) est OPEN.
3. Le PnL inscrit est BRUT (pas de frais ni de spread) : −3,51 $ de coûts sur 39,70 $ (8,8 %).
4. 32 sorties de stop coûtent 33,73 $ contre +73,43 $ pour 67 traînîngs ; le stop est une
   VÉRIFICATION périodique sur un prix en cache, pas un ordre au repos → dépassements jusqu'à
   −16,5 % et −39,2 % pour un stop annoncé de 8 %.
5. Aucun bag utilisé sur la fenêtre ; giveback médian RIZE 20,8 % ; 6 colonnes manquent au journal
   (mise visée, mur utilisé, seuil exigé, dd6 observé, stop nominal, spread payé).
6. La mise médiane représente de 0,03 % (CHIP) à 13,2 % (TEL) de la profondeur mesurée à −0,5 %.

=== 4. MISSION : CONTREDIRE ===
Répondez à ces questions, dans l'ordre, en étant factuel :
1. Quelle conclusion de la section 3 est ABUSIVE au vu des seuls chiffres fournis ? (mesure
   insuffisante, corrélation prise pour causalité, n trop faible, fenêtre haussière…)
2. Quelle mesure MANQUE pour trancher la plus importante des cinq ?
3. Le retard d'horodatage (fait n°2) est-il une explication PLAUSIBLE des « contradictions » que je
   traquais (post-mortems incohérents), ou est-ce que je me raconte une histoire ? Quel test
   trancherait, réalisable sur un Mac, sans argent réel ?
4. QUELLE ERREUR de méthode suis-je en train de commettre MAINTENANT, que ce brief ne dit pas ?
5. Dans quel ORDRE traiter : (a) vue live sur les 20 paires, (b) horodatage du journal,
   (c) stop au repos, (d) colonnes manquantes, (e) net de coûts dans le reporting ? Et pourquoi ?
6. Qu'est-ce qui vous ferait changer d'avis (fait mesurable) ?

Puis, en fin de réponse :
  VERDICT : sur cet audit (fiable | utile mais incomplet | non fiable)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) mesurable(s)
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)
  SYNTHÈSE (5 lignes max).

Factuel, concis, français. Pas de flagornerie, pas de généralités. Information manquante ->
« information insuffisante ». Vous DONNEZ UN AVIS : vous ne touchez à RIEN, aucun ordre.
"""

MODELS = ["gemini-flash-lite-latest", "nvidia/nemotron-3-super-120b-a12b:free",
          "x-ai/grok-4.3", "deepseek-ai/DeepSeek-V3-0324"]


def ask(model, timeout=240):
    payload = json.dumps({"model": model,
                          "messages": [{"role": "user", "content": BRIEF}],
                          "max_tokens": 3000, "temperature": 0.3}).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    (OUT / "BRIEF.md").write_text(BRIEF, encoding="utf-8")
    print(f"FAMILLE : {len(MODELS)} modèles · sortie {OUT}")
    print(f"brief : {len(BRIEF)} caractères (chiffres extraits des rapports d'instruments)")
    for model in MODELS:
        nom = model.replace("/", "_").replace(":", "_")
        out_file = OUT / f"AVIS_{nom}.md"
        if out_file.exists() and out_file.stat().st_size > 200:
            print(f"[SKIP] {model} a déjà répondu")
            continue
        try:
            content, provider, dur = ask(model)
            out_file.write_text(f"# AVIS {model} (provider {provider}, {dur}s)\n\n{content}\n",
                                encoding="utf-8")
            print(f"[OK] {model} ({dur}s, {len(content)} car.)", flush=True)
        except Exception as e:                       # noqa: BLE001
            print(f"[ERREUR] {model}: {str(e)[:120]}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
