
#!/usr/bin/env python3
# scoreur_predictions.py
# Scoreur binaire des prédictions (brique A)
# Python 3.9 stdlib uniquement - Binance REST public

import sys
import argparse
import os
import re
import json
import urllib.request
from datetime import datetime, timezone

def parse_date_iso(ts: str) -> datetime:
    """Parse date ISO 8601 avec Z (UTC)."""
    if ts.endswith('Z'):
        ts = ts[:-1] + '+00:00'
    return datetime.fromisoformat(ts)

def fetch_prix_binance(symbole: str) -> float:
    """Récupère le prix via l'API publique Binance (timeout 15s)."""
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbole}"
    req = urllib.request.Request(url, headers={"User-Agent": "scoreur/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return float(data["price"])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry", action="store_true", help="Affiche sans modifier")
    parser.add_argument("chemin", nargs="?", default="REGISTRE_PREDICTIONS.md")
    args = parser.parse_args()

    chemin = args.chemin
    if not os.path.isfile(chemin):
        print(f"Erreur: fichier introuvable: {chemin}", file=sys.stderr)
        sys.exit(1)

    with open(chemin, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    maintenant = datetime.now(timezone.utc)
    cache_prix = {}
    nouvelles_lignes = []
    modifie = False

    # Regex pour ligne EN ATTENTE exacte
    motif = re.compile(
        r"^(- )⏳ EN ATTENTE \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([\d.]+)\s*$"
    )

    for ligne in lignes:
        m = motif.match(ligne)
        if not m:
            nouvelles_lignes.append(ligne)
            continue

        prefix = m.group(1)
        ts_creation = m.group(2).strip()
        ts_limite_str = m.group(3).strip()
        symbole = m.group(4).strip().upper()
        comparateur = m.group(5).strip()
        cible = float(m.group(6))

        try:
            ts_limite = parse_date_iso(ts_limite_str)
        except Exception:
            nouvelles_lignes.append(ligne)  # malformée → ignorée
            continue

        if ts_limite >= maintenant:
            nouvelles_lignes.append(ligne)
            continue

        # Prix (cache par symbole)
        if symbole not in cache_prix:
            try:
                cache_prix[symbole] = fetch_prix_binance(symbole)
            except Exception as e:
                print(f"Erreur: impossible de récupérer le prix {symbole} ({e})", file=sys.stderr)
                sys.exit(1)

        prix = cache_prix[symbole]

        # Score mécanique
        if comparateur == ">=":
            est_vraie = prix >= cible
            nouveau_statut = "✅ VRAIE" if est_vraie else "❌ FAUSSE"
        elif comparateur == "<=":
            est_vraie = prix <= cible
            nouveau_statut = "✅ VRAIE" if est_vraie else "❌ FAUSSE"
        else:
            nouveau_statut = "⚠️ NON_VERIFIABLE"

        nouvelle_ligne = f"{prefix}{nouveau_statut} | {ts_creation} | {ts_limite_str} | {symbole} | {comparateur} | {cible}\n"
        nouvelles_lignes.append(nouvelle_ligne)
        modifie = True

    if args.dry:
        for l in nouvelles_lignes:
            print(l, end="")
    else:
        with open(chemin, "w", encoding="utf-8") as f:
            f.writelines(nouvelles_lignes)
        if modifie:
            print("Registre mis à jour.", file=sys.stderr)

if __name__ == "__main__":
    main()
