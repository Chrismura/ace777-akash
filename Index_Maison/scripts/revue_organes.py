#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
revue_organes.py — LA REVUE DES ORGANES (20/09/2026, GO Christophe « doit tout être
incassable auto-réparant »).

POURQUOI : le chien de garde mesure la FRAÎCHEUR d'un produit (et, depuis le 20/09,
le silence de la décision). Il ne pouvait pas voir les écarts STRUCTURELS entre ce
que la maison DÉCLARE et ce que le disque PROUVE :

  · une cadence déclarée qui ne correspond pas au déclencheur réel du plist
    (ex. suivi-setup-red, tâche QUOTIDIENNE, déclarée à 300 s : le jour où son
    produit cesse d'être écrit, le seuil tombe à 600 s → faux positif permanent,
    ou l'organe est classé « sans produit » et plus jamais jugé — c'était le cas) ;
  · un produit DÉCLARÉ que plus rien ne résout (globs `*` traités comme des chemins
    littéraux) → l'organe n'était jugé que sur sa sortie launchd : une panne de son
    produit était invisible ;
  · un produit FRAIS mais dont le CONTENU n'avance plus (organe vivant à vide).

CE QUE FAIT CETTE REVUE : elle mesure les 99 organes et rend chaque écart VISIBLE
au lieu de le laisser dormir. Elle ne répare rien toute seule : un écart n'est pas
une panne, c'est une DÉCLARATION À FAIRE. Chaque ligne se ferme en l'inscrivant dans
strategie/revue_declares.json (raison + date) — et le chien cesse alors de la crier.

UNE SEULE VÉRITÉ : la résolution des produits est celle du chien
(`chien_de_garde.resoudre_chemin_produit`). Deux résolutions divergentes finiraient
par juger deux choses différentes.

Lecture seule sur la maison : n'écrit que thermo/revue_organes.json + thermo/REVUE_ORGANES.md.
Stdlib uniquement.
"""
import importlib.util
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

IM = Path(__file__).resolve().parent.parent
BASE = IM.parent
REGISTRE = IM / "strategie" / "REGISTRE_ORGANES.json"
CRITICITE = IM / "strategie" / "criticite_organes.json"
DECLARES = IM / "strategie" / "revue_declares.json"
OUT_JSON = IM / "thermo" / "revue_organes.json"
OUT_MD = IM / "thermo" / "REVUE_ORGANES.md"


def charger(p, defaut=None):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return defaut if defaut is not None else {}


def charger_chien():
    """Importe chien_de_garde (sans exécuter main) pour réutiliser SA résolution."""
    try:
        spec = importlib.util.spec_from_file_location("chien_de_garde", IM / "scripts" / "chien_de_garde.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception:
        return None


def _ts(valeur):
    if valeur is None:
        return None
    if isinstance(valeur, (int, float)):
        # PIÈGE CONNU : juste_prix_hist.jsonl écrit « ts » en MILLISECONDES sur les
        # lignes récentes et pas du tout sur les anciennes. Un ts > 1e11 est en ms.
        v = float(valeur)
        return v / 1000.0 if v > 1e11 else v
    try:
        return datetime.fromisoformat(str(valeur).replace("Z", "+00:00")).timestamp()
    except Exception:
        try:
            v = float(valeur)
            return v / 1000.0 if v > 1e11 else v
        except Exception:
            return None


def age_contenu(chemin: Path, champ: str):
    """Âge (s) du CONTENU : valeur du champ déclaré dans la dernière entrée.

    On ne devine pas : le champ est donné (revue_declares.json → contenu_surveille).
    Accepte json, jsonl et une clé pointée (« derniere.ts_emission »).
    """
    def lire_pointe(obj, key):
        for bout in key.split("."):
            if not isinstance(obj, dict) or bout not in obj:
                return None
            obj = obj[bout]
        return obj

    try:
        if str(chemin).endswith(".jsonl"):
            taille = chemin.stat().st_size
            with open(chemin, "rb") as f:
                f.seek(max(0, taille - 200000))
                lignes = [l for l in f.read().decode("utf-8", "ignore").split("\n") if l.strip()]
            for ligne in reversed(lignes):
                try:
                    d = json.loads(ligne)
                except Exception:
                    continue
                t = _ts(lire_pointe(d, champ))
                if t:
                    return max(0.0, time.time() - t)
            return None
        d = charger(chemin, None)
        if not isinstance(d, dict):
            return None
        t = _ts(lire_pointe(d, champ))
        return max(0.0, time.time() - t) if t else None
    except Exception:
        return None


def main():
    maintenant = datetime.now(timezone.utc)
    registre = charger(REGISTRE, {}) or {}
    organes = registre.get("organes") or []
    crit = {o.get("organe"): o for o in (charger(CRITICITE, {}) or {}).get("organes", [])}
    declares = charger(DECLARES, {}) or {}
    cad_declarees = declares.get("cadences") or {}
    contenu_surveille = {c.get("organe"): c.get("champ")
                         for c in (declares.get("contenu_surveille") or []) if isinstance(c, dict)}
    non_resolus_declares = declares.get("produits_non_resolus") or []
    chien = charger_chien()

    analyse = []
    a_trancher = []
    candidats_figes = []
    seaux = {}

    def classer(nom, classe, **kw):
        seaux[classe] = seaux.get(classe, 0) + 1
        e = {"organe": nom, "classe": classe}
        e.update(kw)
        analyse.append(e)
        return e

    for org in organes:
        nom = org.get("organe")
        if org.get("zone_grise", False):
            classer(nom, "ASSUMÉ (zone grise)")
            continue
        if org.get("dormant", False):
            classer(nom, "ASSUMÉ (dormant)")
            continue

        produit = org.get("chemin_pouls_ou_produit")
        chemin = chien.resoudre_chemin_produit(org) if chien else None
        existe = bool(chemin and chemin.exists())
        freq = org.get("frequence_attendue_sec") or 300
        tolerance = org.get("tolerance_mult", 2.0) or 2.0
        seuil = freq * tolerance

        if not produit:
            # Chargé, aucun produit déclaré : jugé sur sa sortie launchd (assumé).
            classer(nom, "JUGÉ SUR SORTIE (aucun produit déclaré)")
            continue

        if not existe:
            # Produit DÉCLARÉ mais introuvable : l'organe n'est jugé sur rien.
            # C'est l'écart le plus dangereux : une panne du produit est invisible.
            if nom in non_resolus_declares:
                classer(nom, "DÉCLARÉ (produit non résolu assumé)")
            else:
                classer(nom, "À TRANCHER (produit déclaré non résolu)", produit=produit)
                a_trancher.append({
                    "organe": nom,
                    "quoi": "produit déclaré non résolu",
                    "fait": "%s → introuvable (%s)" % (produit, org.get("declencheur", "?")),
                    "declaration_attendue": ("corriger le chemin au registre, ou déclarer la ligne "
                                             "dans revue_declares.json → produits_non_resolus"),
                })
            continue

        age = max(0.0, time.time() - os.stat(chemin).st_mtime)
        info = {"produit": str(chemin.relative_to(BASE)) if str(chemin).startswith(str(BASE)) else str(chemin),
                "age_sec": round(age), "seuil_sec": round(seuil),
                "declencheur": org.get("declencheur")}

        # 1. Cadence déclarée vs déclencheur RÉEL du plist.
        cad_plist = org.get("cadence_plist_sec")
        if cad_plist and int(cad_plist) != int(freq):
            humain = (crit.get(nom) or {}).get("frequence_attendue_sec_critique")
            if humain or nom in cad_declarees:
                info["cadence"] = "DÉCLARÉE (produit %ss vs déclencheur %ss)" % (freq, cad_plist)
            else:
                info["cadence"] = "écart non déclaré"
                a_trancher.append({
                    "organe": nom,
                    "quoi": "cadence déclarée ≠ déclencheur réel",
                    "fait": "registre %ss vs plist %ss (%s)" % (freq, cad_plist, org.get("declencheur", "?")),
                    "declaration_attendue": ("déclarer frequence_attendue_sec_critique (cadence du "
                                             "PRODUIT, défendable) ou corriger le registre"),
                })

        # 2. Fraîcheur (le chien le crie déjà ; ici c'est le fait, pour le rapport).
        if age > seuil:
            classer(nom, "HORS DÉLAI", **info)
        else:
            classer(nom, "OK", **info)

        # 3. Contenu : seulement si la maison a DÉCLARÉ le champ qui doit avancer.
        if nom in contenu_surveille:
            ac = age_contenu(chemin, contenu_surveille[nom])
            if ac is not None and ac > seuil:
                candidats_figes.append({"organe": nom, "champ": contenu_surveille[nom],
                                        "age_contenu_sec": round(ac),
                                        "age_fichier_sec": round(age),
                                        "fige": age <= seuil})
        elif produit and str(chemin).endswith((".json", ".jsonl")):
            # Candidat INFORMATIF (aucune alarme) : produit frais, contenu peut-être figé.
            # Un champ « date » (jour) ou un compteur peut donner un faux candidat —
            # c'est pour ça que cette liste n'est PAS une alarme, juste à lire.
            for champ in ("ts", "ts_iso", "generated_at", "updated"):
                ac = age_contenu(chemin, champ)
                if ac is not None:
                    if age <= seuil and ac > seuil:
                        candidats_figes.append({"organe": nom, "champ": champ,
                                                "age_contenu_sec": round(ac),
                                                "age_fichier_sec": round(age), "fige": True})
                    break

    cris = charger(IM / "thermo" / "cris.json", {}) or {}
    sortie = {
        "ts": maintenant.isoformat(timespec="seconds"),
        "total": len(organes),
        "seaux": seaux,
        "a_trancher": a_trancher,
        "candidats_contenu_fige": candidats_figes,
        "resume": {
            "a_trancher": len(a_trancher),
            "ok": seaux.get("OK", 0),
            "juge_sur_sortie": seaux.get("JUGÉ SUR SORTIE (aucun produit déclaré)", 0),
            "assumes": sum(v for k, v in seaux.items() if k.startswith("ASSUMÉ")),
            "hors_delai": seaux.get("HORS DÉLAI", 0),
            "cris_actifs": cris.get("nb"),
        },
        "note": ("Chaque ligne « à trancher » se ferme en la DÉCLARANT (raison + date) dans "
                 "strategie/revue_declares.json. Aucun organe n'est réparé automatiquement : "
                 "un écart n'est pas une panne, c'est une déclaration à faire."),
        "analyse": analyse,
    }
    OUT_JSON.write_text(json.dumps(sortie, indent=2, ensure_ascii=False), encoding="utf-8")

    # ── Rapport lisible ──────────────────────────────────────────────────────
    md = ["# 🔎 REVUE DES ORGANES", "*%s — lecture seule sur la maison*" % maintenant.strftime("%Y-%m-%d %H:%M:%S UTC"), ""]
    md.append("**%d organes** · %d OK · %d jugés sur leur sortie (aucun produit déclaré) · "
              "%d assumés (zone grise/dormant) · **%d à trancher** · %d hors délai"
              % (len(organes), seaux.get("OK", 0),
                 seaux.get("JUGÉ SUR SORTIE (aucun produit déclaré)", 0),
                 sum(v for k, v in seaux.items() if k.startswith("ASSUMÉ")),
                 len(a_trancher), seaux.get("HORS DÉLAI", 0)))
    md.append("")
    md.append("## 🔴 À TRANCHER (%d)" % len(a_trancher))
    if a_trancher:
        for x in a_trancher:
            md.append("- **%s** — %s : %s" % (x["organe"], x["quoi"], x["fait"]))
            md.append("  - à faire : %s" % x["declaration_attendue"])
    else:
        md.append("- (aucun : chaque écart entre le déclaré et le prouvé est déclaré ou corrigé)")
    md.append("")
    md.append("## 🔍 Candidats « produit frais, contenu peut-être figé » (%d)" % len(candidats_figes))
    md.append("*Information, pas alarme : un champ « date » de jour ou un compteur donne un faux "
              "candidat. Seuls les organes dont le champ est DÉCLARÉ dans revue_declares.json "
              "(contenu_surveille) peuvent déclencher, via le chien.*")
    if candidats_figes:
        for c in candidats_figes:
            md.append("- %s : `%s` vieux de %.1f h alors que le fichier a été réécrit il y a %.1f h"
                      % (c["organe"], c["champ"], c["age_contenu_sec"] / 3600.0, c["age_fichier_sec"] / 3600.0))
    else:
        md.append("- (aucun)")
    md.append("")
    md.append("## ✅ OK — produit frais ET cadence cohérente (%d)" % seaux.get("OK", 0))
    for e in analyse:
        if e["classe"] == "OK":
            cad = (" · " + e["cadence"]) if e.get("cadence") else ""
            md.append("- %s : %s (âge %ds / seuil %ds%s)%s"
                      % (e["organe"], e.get("produit", "?"), e.get("age_sec", 0),
                         e.get("seuil_sec", 0), " · " + e["declencheur"] if e.get("declencheur") else "", cad))
    md.append("")
    md.append("## ⚪ Jugés sur leur sortie launchd (aucun produit déclaré) (%d)"
              % seaux.get("JUGÉ SUR SORTIE (aucun produit déclaré)", 0))
    md.append("- " + ", ".join(e["organe"] for e in analyse
                               if e["classe"] == "JUGÉ SUR SORTIE (aucun produit déclaré)"))
    md.append("")
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    print("Revue des organes : %d/%d OK · %d à trancher · %d cris actifs"
          % (seaux.get("OK", 0), len(organes), len(a_trancher), cris.get("nb") or 0))
    for x in a_trancher[:8]:
        print("   À TRANCHER %s : %s — %s" % (x["organe"], x["quoi"], x["fait"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
