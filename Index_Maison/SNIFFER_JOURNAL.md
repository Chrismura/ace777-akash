# SNIFFER DU VRAI — journal (19/08/2026)

## Ce qui a été construit
- `scripts/sniffer_vrai.py` — tire le **brut** (marché + source native) et le
  **narratif** (Fear&Greed + titres Google News + trending), soumet les deux à la
  famille avec le prompt divergence.
- `identity/prompts/divergence.json` — prompt canonique : FAITS BRUTS → NARRATIF
  → DIVERGENCE → VERDICT. Priorité au brut, jamais recopier le narratif.
- `SNIFFER_VRAI.md` — la méthode (3 couches + taxonomie + poussière étalon).
- 2 plists : `sniffer-matin` (8h) + `sniffer-ny` (15h50, post-ouverture NY).

## Registre de sources par actif (« la BONNE source »)
- bitcoin → la **poussière maison** (dust/CPFP/blocs privatisés, live.json.onchain)
- xrp → **XRP Ledger natif** (blockchair ripple + XRPScan)
- ethereum / solana / cardano / … → blockchair {chain}/stats
- autre → marché seul + note « pas de source native »

## Résultats des tests
### Bitcoin
- Brut : **34,47 % blocs privatisés (1277 fantômes)**, dust 0, whales neutres.
- Divergence : « frénésie d'achat des baleines » (titre) vs « baleines nominales » (brut).
- Verdict : marché neutre, narratif = bruit. Seule anomalie : blocs fantômes.

### XRP
- Brut : 0,9997 $ (-0,21 %), ledger 106M, mempool 61 tx (calme).
- Divergence : « chute continue sous 1 $ » vs prix stable ; « baleines +280 % » non corroboré.
- Verdict : le narratif dramatise, le brut = stabilité.

## Leçons (à graver)
1. **Toujours chercher la source, et la BONNE source par actif** (BTC ≠ XRP).
2. **Cerveau fort (NVIDIA) indispensable** sur le rôle sniffer (Mistral a recopié).
3. Le narratif (titres/sentiment) **exagère systématiquement** vs le brut.
4. Le Fear&Greed est un agrégat retardé, pas le flux réel.

## Prochaine étape
- Enquête sur les 34 % de blocs privatisés fantômes (qui les mine, pourquoi).
- Digest du matin (sous le nez) + intégration en un mot.
