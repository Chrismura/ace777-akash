#!/usr/bin/env python3
"""Envoi du patch STOP_MARKET V1 au codeur (task code.ia) via le hub."""
import json
import os
import time
import urllib.request

D = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
PATCH = open(os.path.join(D, "PATCH_STOPMARKET_V1.md"), encoding="utf-8").read()

SYSTEM = (
    "Tu es le CODEUR de la famille ACE777, un ingénieur senior bash/API Binance Futures. "
    "On te soumet un patch CONCRET à relire. Ton rôle : trouver les erreurs, les pièges, les oublis. "
    "Ne te contente JAMAIS de valider poliment : si tu vois une amélioration qui a du sens, propose-la ; "
    "si un point est risqué, dis-le franchement. Tu réponds en français, structuré. "
    "Termine par: VERDICT: GO / GO-AVEC-RÉSERVE / NO-GO + CONFIANCE: X%"
)

PROMPT = (
    "Voici le patch STOP_MARKET V1 (filet de sécurité physique Binance Futures) que nous avons "
    "validé en round table famille (5/5) et avec le binôme. Il cible le moteur actif "
    "genesis_manifest.txt (setup A, md5 fe2a7bcc).\n\n"
    "CONTEXTE VÉRIFIÉ DANS LE CODE :\n"
    "- private_post() fait un POST codé en dur (ligne 734) -> on ajoute private_delete() pour les DELETE\n"
    "- Le bloc de sortie commun est aux lignes 2431-2437 (exit_resp) : TOUS les chemins de sortie y passent SAUF phase_shift\n"
    "- duo_v63_phase_shift_close() (ligne 1307) ferme en 3 étapes 13/8/5 et est appelé ligne 2422 -> chemin SÉPARÉ qui ne passe PAS par exit_resp\n"
    "- entry_ts_iso=... ligne ~2128 : point d'ancrage du placement du STOP_MARKET après l'entrée\n"
    "- Début de boucle for i ligne 1508 : point d'ancrage du heartbeat anti-orphelin\n"
    "- Le moteur n'a PAS de fonction d'arrondi prix (seulement floor_step_qty pour les quantités)\n"
    "- Variables dispo à l'entrée : $entry_price, $qty, $side, $close_side, $trade_position_side_param, $SYMBOL, $i\n\n"
    f"{PATCH}\n\n"
    "QUESTIONS PRÉCISES POUR TOI :\n"
    "1. Le phase_shift : où exactement injecter le cancel ACESTOP dans ce chemin séparé ? (propose le code)\n"
    "2. reduceOnly=true est-il accepté par Binance Futures sur un STOP_MARKET ? (vérifie)\n"
    "3. workingType : CONTRACT_PRICE (défaut) vs MARK_PRICE pour un filet anti-crash — que recommandes-tu ?\n"
    "4. L'arrondi ruby printf : pour un stop SELL (long), arrondir au plus proche peut-il déplacer le stop du mauvais côté ? (analyse)\n"
    "5. Fenêtre d'entrée sans filet (~200-500ms) : le code continue si le placement échoue (jamais de position sans gestion) — valide ?\n"
    "6. Le heartbeat allOpenOrders rase TOUT sur la paire en début de cycle — dans ce moteur seuls les ACESTOP dorment (entrées/sorties = MARKET immédiats). Confirmes-tu qu'aucun autre ordre légitime ne dort jamais ?\n"
    "7. Amélioration : vois-tu un piège ou une amélioration qui a du sens dans ce patch ? (ne te contente pas de corriger)"
)

def post(payload, timeout=300):
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    f_md = os.path.join(D, "AVIS_CODEUR_V2.md")
    f_json = os.path.join(D, "AVIS_CODEUR_V2.json")
    payload = {
        "model": "groq",
        "task": "code.ia",
        "temperature": 0.3,
        "max_tokens": 3000,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": PROMPT},
        ],
    }
    try:
        t0 = time.time()
        d = post(payload)
        prov = d.get("provider", "?")
        content = d["choices"][0]["message"]["content"]
        with open(f_md, "w", encoding="utf-8") as f:
            f.write("# AVIS CODEUR V2 (provider: %s, %.1fs)\n\n%s\n" % (prov, time.time() - t0, content))
        with open(f_json, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        print("OK codeur -> %s | %d car. (%.1fs)" % (prov, len(content), time.time() - t0))
    except Exception as e:
        print("ERREUR codeur: %s" % e)
        with open(f_json, "w", encoding="utf-8") as f:
            f.write("ERREUR: %s\n" % e)

if __name__ == "__main__":
    main()
