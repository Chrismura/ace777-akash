# RELEASE RECEIPT — Onchain v2 CPFP (15/08/2026)

**Validé par :** Christophe (GO) · Famille (GO-AVEC-RÉSERVE gemini 75% / nvidia 68%)
**Supervision :** Buffy · **Codeur :** corrigé 6 fois par la supervision

---

## Fichiers livrés / modifiés

| Fichier | Action | Rôle |
|---|---|---|
| `Index_Maison/scripts/detecter_cpfp.py` | ➕ NOUVEAU | Détecteur CPFP/dust/z-score (observation) |
| `Index_Maison/scripts/pont_onchain.py` | ✏️ MODIF | Injecte cpfpSignal/cpfpScore si actif+confirmé |
| `Index_Maison/scripts/ada_gardienne.py` | ✏️ MODIF | Modulateur CPFP (voilure −7%) |
| `Index_Maison/plists/com.ace777.cpfp.plist` | ➕ NOUVEAU | Cadence 10 min (chargée) |
| `Index_Maison/strategie/REGISTRE_SYNAPSES.json` | ✏️ MODIF | v1.1.0 (19 items, md5 à jour) |

## Non modifiés (volontairement)

- `surveiller_whales.py` (scan actuel INCHANGÉ — option 1)
- `cortana_analyse.py` (déjà branché sur la synthèse onchain)
- Moteur Hulk `paper_diprip.py` (intouché)

## Réversibilité

- **Désactiver la plist :** `launchctl unload ~/Library/LaunchAgents/com.ace777.cpfp.plist`
- **Retirer le pont CPFP :** supprimer les 3 clés ajoutées dans `pont_onchain.py`
  (cpfpSignal/cpfpScore + la lecture de cpfp_detect.json)
- **Retirer Ada :** supprimer le bloc « Modulateur CPFP v2 » dans `calculer_voilure`
- **Retour arrière complet :** restaurer les md5 du registre précédent (v1.0.0) +
  les fichiers d'origine

## Règle veilleuse

Toute nouvelle modif de ces fichiers SANS passer par un chantier =
**INTRUSION** (la veilleuse hurle). Toujours mettre à jour le registre.

## Réserves notées (pour plus tard)

1. Test A/B 7 jours : justesse Cortana avec/sans signal CPFP
2. Calibration des seuils sur le réel (références Cortana à comparer)
3. Panneau cockpit whales (intégration ENSEMBLE, toujours en attente)
