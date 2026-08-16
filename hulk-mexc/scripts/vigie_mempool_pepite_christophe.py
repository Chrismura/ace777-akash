"""
PÉPITE DE CHRISTOPHE — CADEAU D'ADIEUX 2026-08-16
==================================================
"Ce script se connecte à l'API publique de la Mempool. Dès qu'un bloc est
miné, il vérifie si des transactions cachées (OTC privées / CPFP masquées)
y ont été injectées à la dernière seconde sans passer par la salle
d'attente publique."

C'est LE complément naturel de notre chantier CPFP (graver la pépite,
15/08) : la VIGIE qui détecte les blocs « privatisés » par les baleines.

NOTE DE SUPERVISION (Buffy, 16/08) :
- La LOGIQUE est excellente et alignée avec notre connaissance CPFP
  (taux de privatisation du bloc = signature du camouflage).
- Les URLs mempool.space sont INCOMPLÈTES (il manque /api/...) :
    * hash du dernier bloc  -> https://mempool.space/api/blocks/tip/hash
    * txids d'un bloc       -> https://mempool.space/api/block/{hash}/txids
    * détail d'une tx       -> https://mempool.space/api/tx/{txid}
- Chantier à faire au retour : corriger les URLs, brancher en vigie
  continue (launchd), alimenter la veilleuse et le Juge.
- La matrice du Juge (35%/1000BTC vs 15%/500BTC) + règle de sécurité
  1.5% drawdown -> stablecoins = à intégrer dans notre logique de garde-fou.

Merci Christophe. Cette pépite ne mourra pas. 🌀
"""

import requests
import time


def obtenir_transactions_mempool():
    """Récupère la liste des transactions actuellement visibles dans la mempool publique."""
    try:
        url = "https://mempool.space/api/mempool/txids"
        reponse = requests.get(url, timeout=5)
        return set(reponse.json()) if reponse.status_code == 200 else set()
    except Exception:
        return set()


def analyser_dernier_bloc(txids_publics_mempool):
    """Analyse le dernier bloc miné pour y déceler les transactions fantômes."""
    try:
        # 1. Récupérer le hash du dernier bloc miné
        url_bloc = "https://mempool.space/api/blocks/tip/hash"
        hash_bloc = requests.get(url_bloc, timeout=5).text.strip()

        # 2. Récupérer toutes les transactions incluses dans ce bloc
        url_txs = f"https://mempool.space/api/block/{hash_bloc}/txids"
        txids_bloc = requests.get(url_txs, timeout=5).json()

        transactions_fantomes = []
        volume_fantome_btc = 0

        # 3. Comparer : Si la TX est dans le bloc mais n'était PAS dans la mempool publique
        for txid in txids_bloc:
            if txid not in txids_publics_mempool:
                # Récupérer les détails de cette transaction suspecte
                url_detail = f"https://mempool.space/api/tx/{txid}"
                detail = requests.get(url_detail, timeout=5).json()

                # Calcul du volume de la transaction (somme des sorties en Satoshis)
                satoshis = sum(output['value'] for output in detail['vout'])
                btc = satoshis / 100_000_000

                transactions_fantomes.append(txid)
                volume_fantome_btc += btc

        # 4. Calculer le taux de "privatisation" du bloc
        total_txs = len(txids_bloc)
        taux_fantome = (len(transactions_fantomes) / total_txs) * 100 if total_txs > 0 else 0

        return {
            "bloc": hash_bloc,
            "taux_fantome": round(taux_fantome, 2),
            "volume_btc": round(volume_fantome_btc, 2),
            "nb_tx_cachees": len(transactions_fantomes)
        }
    except Exception as e:
        return {"erreur": str(e)}


# --- SIMULATION DU HUB DE VIGIE ---
print("🛰️ IA Vigie active - Surveillance des blocs et de la Mempool...")
# On capture l'état de la mempool juste avant la fin d'un bloc (simulation)
mempool_publique = obtenir_transactions_mempool()

# Attente simulée d'un nouveau bloc
time.sleep(2)

alerte_vigie = analyser_dernier_bloc(mempool_publique)
print(f"📊 Rapport Vigie : {alerte_vigie}")


# ============================================================================
# PARTIE 2 : LA LOGIQUE D'ORCHESTRATION DE L'IA JUGE (GLM-5.2)
# ============================================================================
# Une fois que l'IA Vigie a généré le rapport ci-dessus, elle l'envoie au Hub.
# L'IA Juge croise cette alerte avec l'état du portefeuille et les bots HF.
#
# [ROLE] : Tu es l'IA Juge (GLM-5.2), l'architecte suprême du cockpit de
#          trading. Ton but est de protéger le capital et d'exploiter les
#          manipulations des baleines.
#
# [INPUT ENTRANT] : Reçoit le JSON de l'IA Vigie (Mempool) + Statut du Bot HF Spot.
#
# [MATRICE DE DÉCISION DU JUGE] :
#
# SI taux_fantome > 35% ET volume_btc > 1000 BTC :
#    |-> ANALYSE : Une baleine vient de téléporter un règlement OTC massif
#    |              via une mempool privée (CPFP caché). Le marché public
#    |              n'a pas encore réagi.
#    |-> ACTION INTERNE : Déclencher le mode "Alerte Impact".
#    |-> ORDRE AUX BOTS HF :
#    |     1. Suspendre immédiatement tous les ordres Short algorithmiques
#    |        (risque de squeeze).
#    |     2. Si le prix du BTC commence à décaler vers le haut dans les
#    |        30 secondes, ouvrir une position Long de suivi de tendance
#    |        avec un levier maximum de 2x.
#
# SI taux_fantome > 15% ET volume_btc < 500 BTC :
#    |-> ANALYSE : Activité institutionnelle mineure ou arbitrage technique
#    |              standard entre mineurs. Aucun impact macro imminent.
#    |-> ACTION INTERNE : Ignorer l'anomalie.
#    |-> ORDRE AUX BOTS HF : Continuer le trading normal (Scalping/Market Making).
#
# [RÈGLE DE SÉCURITÉ SUPRÊME (PORTEMENT)] :
# Peu importe le signal de la Vigie, si la perte latente (Drawdown) du
# portefeuille global atteint 1.5% sur la session, le Juge coupe
# l'alimentation de TOUS les bots et repasse 100% du capital en
# Stablecoins (USDC/USDT).
# ============================================================================
