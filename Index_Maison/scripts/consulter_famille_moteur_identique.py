#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulter la FAMILLE (flotille) : confirmer que les 3 runs du 14/08 ont
tourné avec le MEME moteur identique, comprendre le pattern revenge/heartbeat,
et expliquer pourquoi les CSV scellés semblent différents.

Contexte utilisateur (Christophe) : il veut que la famille comprenne le système
ACE avant de se prononcer. Il a vu que les CSV scellés de la nuit et de la veille
sont "différents" et veut confirmation que c'est bien le même moteur qui a tourné
dans les 3 cas (run 4h #1, run V2, run nuit 8h)."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_MOTEUR_IDENTIQUE_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — COMPRENDRE LE SYSTÈME ACE AVANT DE RÉPONDRE

=== 1. LE SYSTÈME ACE (archi duo SCOUT/HUNTER) ===
ACE777 est un moteur de trading BTC (testnet) en deux unités complémentaires :
- BETA x5 = rôle SCOUT : il teste le marché en continu avec des petits trades
  (forte fréquence, ~200 trades/nuit), détecte les signaux, subit les pertes.
- ALPHA x13 = rôle HUNTER : il frappe fort et rarement, en réaction aux signaux
  du SCOUT. Sa taille de position est pilotée par des "modes" (suffer, revenge,
  burst, vacuum_strike...).

Communication DUO : les deux unités partagent un fichier d'état `runs/duo_state.json`
écrit par `duo_publish_state()` (role, status OPEN/CLOSED, bps, pnl_usdt, reason,
hold_sec, ts_ms). ALPHA décide à chaque cycle via `duo_hunter_decide()` en lisant
cet état. Règles clés :
- `revenge` : s'active si role=="SCOUT" && status=="CLOSED" && pnl<0 (perte du
  scout fermée) && raison dans la liste [stop_loss, shock_inversion_stop,
  shock_exit_10bps, fluid_exit_inversion, fluid_exit_brake, beta_sentinel_cut]
  -> ALPHA repart en 1.5x (DUO_HUNTER_REVENGE_MULT). C'est le FIX-SCOUT appliqué
  le 14/08 (il empêche ALPHA de revenge sur SA PROPRE perte).
- `suffer` : si status=="OPEN" && bps<=seuil (le scout souffre en position ouverte)
  -> ALPHA aide sans changer de taille.
- TTL : `DUO_EVENT_TTL_SEC=20` -> l'état n'est valable que 20s avant stale_state.
- HEARTBEAT : `duo_touch_heartbeat()` (ligne 1545 du genesis) rafraîchit ts_ms du
  duo_state à CHAQUE cycle du SCOUT sans changer le reste (évite le stale entre
  trades). C'est un point que Buffy soupçonne de neutraliser le TTL de 20s.

Genesis : genesis_manifest.txt (md5 8d9ee8d6997eeadabf3da642f326d3d7), scellé,
identique pour les 3 runs. Config : DUO_ROLE=SCOUT (BETA) / HUNTER (ALPHA),
DUO_EVENT_TTL_SEC=20, DUO_HUNTER_REVENGE_MULT=1.5.

=== 2. LES 3 RUNS DU 14/08 (même genesis, même config) ===
- Run 4h #1 : 12:51Z -> 15:57Z (marché HAUSSIER +0.40%)
- Run V2     : 16:24Z -> 20:24Z (marché BAISSIER -0.27%)
- Run Nuit   : 21:45Z -> 05:44Z (marché HAUSSIER doux +0.31%)

=== 3. SÉQUENCES DE CYCLES RÉELLES (extraits des CSV scellés, ALPHA) ===
Run 4h #1 (cycle 458->524) :
  13:56:47 cyc=458 BUY qty=0.083 pnl=0.000 exit=fluid_exit_inversion size=strong_conf_full
  14:02:59 cyc=504 BUY qty=0.249 pnl=0.000 exit=shock_inversion_stop size=hunter_revenge_1.5x
  14:04:42 cyc=515 BUY qty=0.249 pnl=+1.295 exit=shock_inversion_stop size=hunter_revenge_1.5x
  14:06:02 cyc=524 BUY qty=0.201 pnl=+1.290 exit=shock_inversion_stop size=hunter_revenge_1.5x
Run V2 (cycle 230->409) :
  16:57:00 cyc=230 BUY qty=0.133 pnl=-0.773 exit=shock_inversion_stop size=strong_conf+aspiration_1.618x
  17:11:52 cyc=341 BUY qty=0.247 pnl=0.000 exit=shock_inversion_stop size=hunter_revenge_1.5x
  17:21:17 cyc=408 BUY qty=0.247 pnl=0.000 exit=shock_inversion_stop size=hunter_revenge_1.5x
  17:21:36 cyc=409 BUY qty=0.247 pnl=+0.123 exit=fluid_exit_brake size=hunter_revenge_1.5x
Run Nuit (cycle 859->872) :
  23:38:37 cyc=859 BUY qty=0.248 pnl=0.000 exit=shock_inversion_stop size=hunter_revenge_1.5x
  23:39:03 cyc=861 BUY qty=0.248 pnl=+5.406 exit=shock_inversion_stop size=hunter_revenge_1.5x
  23:40:19 cyc=869 BUY qty=0.124 pnl=-0.050 exit=fluid_exit_brake size=hunter_revenge_1.5x
  23:40:51 cyc=872 BUY qty=0.083 pnl=0.000 exit=shock_inversion_stop size=strong_conf_full

Note : la colonne `holdSec` du CSV contient en réalité le message détaillé
(radar=... size_note=... soft=... tension=...), la colonne `msg` est vide. Le
vrai hold_sec (durée de détention) n'est pas tracé dans le CSV (il est dans
duo_state.json).

=== 4. LES CHIFFRES CLÉS (analyse Buffy, 3 runs superposés) ===
| Run          | ALPHA trades/PNL | BETA trades/PNL | % ALPHA en revenge | PNL revenge ALPHA |
| Run 4h #1    | 65 / +28.26$     | 155 / +0.40$    | 80%                | +25.61$ (91%)      |
| Run V2       | 37 / +16.61$     | 156 / +1.97$    | 68%                | +9.55$ (57%)       |
| Run Nuit     | 56 / +8.61$      | 204 / +2.51$    | 91%                | +8.28$ (96%)       |
BETA : 0% de trades en revenge sur les 3 runs (100% strong_conf_full).
Trades flat (entrée==sortie, pnl=0) : 25% / 32% / 39% des trades ALPHA.
Corrélation revenge ALPHA <-> perte BETA : seulement 14% des revenge suivent une
perte BETA <=30s (le TTL est 20s), 59% <=5min.

=== 5. LES CSV SCELLÉS "DIFFÉRENTS" — PREUVE QUE C'EST LE MÊME MOTEUR ===
4 CSV scellés (2 par bot) : MASTER_VORTEX_V2_COLLAB_4H_*_20260814-211907Z et
*_20260815-054541Z. Vérification octet par octet (ALPHA) :
- fichier du 14 (scellé 21:19Z) : 17 333 lignes (tout l'historique jusqu'à 20:24Z)
- fichier du 15 (scellé 05:45Z) : 20 962 lignes
- les 17 333 premières lignes sont IDENTIQUES octet pour octet
- le fichier 15 = fichier 14 + 3 629 lignes (le run de nuit)
Conclusion : ce n'est PAS un moteur différent — c'est le MÊME fichier append-only
copié à deux moments du scellement (21:19Z puis 05:45Z). Les 4 signatures portent
le même genesis_md5=8d9ee8d6. Les 4 headers CSV sont identiques :
ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg.

=== QUESTIONS POUR LA FAMILLE ===
1) CONFIRMATION MOTEUR : sur la base des séquences de cycles + la preuve CSV
   (lignes identiques + genesis_md5 identique), confirmez-vous que les 3 runs ont
   tourné avec le MÊME moteur exact identique ? Y a-t-il quoi que ce soit dans les
   séquences qui suggère un comportement différent d'un run à l'autre ?
2) LE PATTERN REVENGE : est-il NORMAL que 68-91% des trades ALPHA soient en mode
   revenge 1.5x, sachant que le design prévoit un revenge PONCTUEL (TTL 20s) après
   une perte du SCOUT ? L'hypothèse de Buffy : le heartbeat (duo_touch_heartbeat
   ligne 1545, rafraîchit ts_ms à chaque cycle SCOUT sans changer le reste)
   neutralise le TTL -> l'état "perte SCOUT" reste frais indéfiniment -> ALPHA
   reste armé en revenge en continu. Validez-vous ce mécanisme ?
3) BETA "INUTILE" : BETA fait 3-4x plus de trades qu'ALPHA mais ne génère que
   0.40$ / 1.97$ / 2.51$ (vs 28.26$ / 16.61$ / 8.61$ pour ALPHA). Est-ce le rôle
   SCOUT normal (il subit, ALPHA frappe) ou un déséquilibre ?
4) LES FLAT : 25-39% des trades ALPHA entrent et sortent au même prix (pnl=0).
   Est-ce le filtre de qualité qui travaille, ou du capital immobilisé pour rien ?
5) LE CSV : la colonne holdSec contient le message détaillé au lieu de la durée de
   détention, msg est vide. Confirmez-vous que c'est une anomalie de traçage ?

Contrainte : répondez factuellement, avec des preuves quand c'est possible.
Surtout : dites-nous si le mécanisme heartbeat qui neutralise le TTL est plausible
ou s'il y a une autre explication au taux de revenge anormalement élevé."""

MODELS = ["gemini", "grok", "nvidia", "deepseek", "juge", "ultra"]

def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2200, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)

def main():
    results = {}
    for m in MODELS:
        try:
            content, provider, secs = ask(m)
            results[m] = content
            f = os.path.join(OUT, f"AVIS_{m}.md")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
            print(f"[OK] {m} -> {f} ({secs}s)")
        except Exception as e:
            print(f"[ERR] {m}: {e}")
        time.sleep(2)
    print(f"\n=== SYNTHESE ===")
    print(f"Consultation terminee : {len(results)}/{len(MODELS)} avis dans {OUT}")

if __name__ == "__main__":
    main()
