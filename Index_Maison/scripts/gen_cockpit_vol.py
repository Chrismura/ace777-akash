#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_cockpit_vol.py — onglet cockpit « vol » (GO Christophe 14/09).
Génère Index_Maison/cockpit/vol_live.js (snapshot JS) + rafraîchit le
cache-buster de vol.html si la page existe. Lecture seule sur la maison :
ne modifie AUCUNE donnée, produit seulement des fichiers dans cockpit/.
Stdlib uniquement.
"""
import json
import re
import subprocess
import time
from pathlib import Path

BASE = Path.home() / "ace777-test-day1"
IM = BASE / "Index_Maison"
COCKPIT = IM / "cockpit"


def age_min(p):
    try:
        return (time.time() - p.stat().st_mtime) / 60.0
    except Exception:
        return None


def jload(p):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return {}


def fmt_age(m):
    if m is None:
        return "—"
    if m < 60:
        return "%.0f min" % m
    return "%.1f h" % (m / 60.0)


def badge(ok):
    return "🟢" if ok else "🔴"


# ── 1. Santé globale ────────────────────────────────────────────────
def lire_sante():
    s = jload(IM / "thermo" / "sante_index_live.json")
    if not s:
        try:
            last = (IM / "data" / "alertes" / "sante_index.log").read_text(
                encoding="utf-8").strip().splitlines()[-1]
            s = json.loads(last)
        except Exception:
            s = {}
    return {
        "etat": s.get("etat", "?"),
        "chaines_ok": s.get("chaines_ok", "?"),
        "anomalies": s.get("anomalies", []),
        "ts": s.get("ts", ""),
    }


# ── 2. Plists en vol (launchctl) ────────────────────────────────────
# Contrat de sortie : certains organes sortent en NON-ZÉRO volontairement
# (c'est un canal d'alerte, pas une panne). Sans cette table, le cockpit
# peignait en rouge des jobs qui font leur travail (leçon 18/09 :
# « une alarme qui sonne pour un comportement normal est un faux positif »).
# 20/09/2026 : la table vit désormais dans strategie/contrat_sortie.json — UNE SEULE
# VÉRITÉ, lue aussi par le chien de garde (qui juge les 44 organes sans produit sur
# leur sortie launchd). Le dict ci-dessous n'est plus que le repli si le fichier
# manque : deux tables divergentes finiraient par dire deux choses différentes.
CONTRAT_SORTIE_DEFAUT = {
    "com.ace777.veilleuse": {"1": "anomalies détectées (par conception, canal d'alerte)"},
    "com.ace777.discipline-quotidienne": {"3": "alertes de discipline (par conception)"},
    # 20/09/2026 (réparation boucle d'alerte) : verif-setup sort en 1 quand la preuve de
    # lecture du coffre est à refaire (gatekeeper). Ce n'est PAS une panne : c'est le
    # garde-fou anti-confiance-aveugle qui dit « relis la carte du coffre avant de
    # valider le setup ». Le classer « échec » faisait croire à un organe cassé
    # (R14 : une alarme doit dire ce qu'elle est, sinon elle devient un faux positif
    # qu'on apprend à ignorer).
    "com.ace777.verif-setup": {"1": "preuve de lecture du coffre à refaire (gatekeeper, par conception)"},
}


def _charger_contrat_sortie():
    try:
        d = json.load(open(IM / "strategie" / "contrat_sortie.json", encoding="utf-8"))
        c = d.get("contrat") if isinstance(d, dict) else None
        if isinstance(c, dict) and c:
            return c
    except Exception:
        pass
    return CONTRAT_SORTIE_DEFAUT


CONTRAT_SORTIE = _charger_contrat_sortie()


def lire_plists():
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True,
                             text=True, timeout=10).stdout
    except Exception:
        return []
    rows = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and parts[2].startswith("com.ace777"):
            pid, exit_code, label = parts[0], parts[1], parts[2]
            contrat = CONTRAT_SORTIE.get(label, {})
            if pid != "-":
                etat, sens = "en vol", ""
            elif exit_code == "0":
                etat, sens = "ok", ""
            elif exit_code in contrat:
                etat, sens = "alerte", contrat[exit_code]
            else:
                etat, sens = "echec", ""
            rows.append({"label": label, "pid": pid, "exit": exit_code,
                         "ok": etat in ("en vol", "ok"), "etat": etat, "sens": sens})
    return sorted(rows, key=lambda r: r["label"])


# ── 3. Marché (live.json) ───────────────────────────────────────────
def lire_marche():
    d = jload(IM / "thermo" / "live.json")
    m = d.get("marche", d)
    return {
        # FIX 16/09 : live.json n'a jamais porté btc_price/prix_btc — le prix vit sous
        # « mark » (vigie). Fear & Greed = clé camelCase « fearGreed » au niveau racine.
        "btc": m.get("btc_price") or m.get("prix_btc") or m.get("mark") or "?",
        "fear": (d.get("feargreed") or {}).get("valeur") or m.get("fear_greed") or d.get("fearGreed") or "?",
        "age": fmt_age(age_min(IM / "thermo" / "live.json")),
    }


# ── 4. Protocoles en test (recensement §3) ──────────────────────────
def extraire_tableau(md, titre_section):
    idx = md.find(titre_section)
    if idx == -1:
        return []
    suite = md[idx:]
    fin = suite.find("\n## ", 1)
    if fin != -1:
        suite = suite[:fin]
    rows = []
    for line in suite.splitlines():
        if line.startswith("|") and "---" not in line:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if cells and cells[0] not in ("", "Organisme", "Capteur"):
                rows.append(cells)
    return rows


def protocoles():
    """Verdicts MESURÉS des protocoles en test (20/09/2026).

    AVANT : la page recopiait le tableau écrit à la main le 14/09
    (RECENSEMENT_OBSERVATIONS_20260914.md §3) → elle affichait des « verdicts » datés
    d'un document, jamais recalculés, alors que les critères sont PRÉ-ENREGISTRÉS (donc
    calculables). Même famille que les autres faux verts réparés aujourd'hui : une page
    qui dit une chose périmée. Désormais la source est thermo/PROTOCOLES_VERDICTS.json,
    écrit par scripts/verdicts_protocoles.py (toutes les 3 h) : chaque ligne porte son
    critère écrit à côté de son résultat, et une ligne ⚠ dit quand un verdict NE PEUT
    PAS être rendu (protocole sans cas, sans matériel, ou au seuil hors d'échelle).
    Le tableau documentaire ne sert plus que de repli si le calcul n'a jamais tourné.
    """
    v = jload(IM / "thermo" / "PROTOCOLES_VERDICTS.json")
    protos = v.get("protocoles") or []
    if protos:
        lignes = [{"cells": ["Protocole", "Critère pré-enregistré (décidé AVANT les données)",
                              "Ce qui est mesuré", "Verdict"]}]
        for p in protos:
            verdict = str(p.get("verdict", "?"))
            if p.get("alerte"):
                verdict += " — ⚠ " + str(p["alerte"])
            lignes.append({"cells": [p.get("protocole", "?"), p.get("critere", ""),
                                      p.get("faits", ""), verdict]})
        return lignes
    md = ""
    try:
        md = (IM / "RECENSEMENT_OBSERVATIONS_20260914.md").read_text(encoding="utf-8")
    except Exception:
        pass
    return [{"cells": r} for r in extraire_tableau(md, "## 3. Les protocoles en test")]


def dormants():
    md = ""
    try:
        md = (IM / "RECENSEMENT_OBSERVATIONS_20260914.md").read_text(encoding="utf-8")
    except Exception:
        pass
    return [{"cells": r} for r in extraire_tableau(md, "## 5. Ce qui dort ou grince")]


# ── 5. Gardiens clés (vérifications directes) ───────────────────────
def gardiens():
    g = []
    v = jload(IM / "thermo" / "VEILLEUSE.md") if False else None
    vmd = IM / "thermo" / "VEILLEUSE.md"
    try:
        txt = vmd.read_text(encoding="utf-8")
        g.append({"nom": "Veilleuse synapses", "ok": "STABLE" in txt,
                  "detail": "STABLE · " + fmt_age(age_min(vmd))})
    except Exception:
        g.append({"nom": "Veilleuse synapses", "ok": False, "detail": "rapport absent"})
    gate = jload(IM / "thermo" / "gatekeeper.json")
    if gate:
        g.append({"nom": "Gatekeeper", "ok": gate.get("ok", False),
                  "detail": gate.get("detail", "")})
    # alertes vocales en vol
    try:
        out = subprocess.run(["ps", "aux"], capture_output=True, text=True, timeout=10).stdout
        n_voc = len([l for l in out.splitlines() if "alerte_vocale.py" in l and "grep" not in l])
        g.append({"nom": "Alertes vocales en boucle", "ok": n_voc == 0,
                  "detail": ("%d en vol" % n_voc) if n_voc else "aucune"})
    except Exception:
        pass
    # CHIEN DE GARDE — on lit SON VRAI RAPPORT (thermo/CHIEN_RAPPORT.json).
    # RÉPARÉ 20/09/2026 (Buffy, GO « incassable ») : ce bloc faisait
    # `tail -1 thermo/chien_rapport.txt` — un fichier QUE PERSONNE N'ÉCRIT. `tail`
    # échouait sur un fichier absent, subprocess ne lève rien pour un code retour
    # non nul → stdout vide → la page affichait « rapport présent » avec un OK VERT.
    # C'était un FAUX VERT PERMANENT sur le gardien le plus important (R14 : une
    # alarme qui ment est pire que pas d'alarme ; et une page qui rassure à tort
    # endort la boucle entière). Désormais : chiffres RÉELS du chien, et les organes
    # VIVANTS MAIS AVEUGLES (décision muette) y sont visibles, pas noyés.
    ch = jload(IM / "thermo" / "CHIEN_RAPPORT.json")
    if ch:
        viv = len(ch.get("vivants") or [])
        vieil = ch.get("vieillissants") or []
        aveugles = ch.get("aveugles") or []
        age_ch = age_min(IM / "thermo" / "CHIEN_RAPPORT.json")
        detail = "%d vivants · %d hors délai · %d aveugle(s)" % (viv, len(vieil), len(aveugles))
        if aveugles:
            detail += " · " + ", ".join(
                "%s (%s nul depuis %.0f min)" % (a.get("organe"), a.get("champ_decision"),
                                                 float(a.get("aveugle_min") or 0))
                for a in aveugles[:2])
        elif vieil:
            detail += " · " + ", ".join(str(v.get("organe")) for v in vieil[:2])
        detail += " · mesure %s" % fmt_age(age_ch)
        # Le chien lui-même peut mourir : un rapport figé n'est pas un feu vert.
        fige = (age_ch is not None and age_ch > 15)
        if fige:
            detail += " — RAPPORT FIGÉ (chien muet > 15 min)"
        g.append({"nom": "Chien de garde", "ok": (not vieil and not aveugles and not fige),
                  "detail": detail})
    else:
        g.append({"nom": "Chien de garde", "ok": False,
                  "detail": "thermo/CHIEN_RAPPORT.json introuvable (chien jamais passé ?)"})
    # agents launchd versionnés (anti-dérive, 19/09) — état écrit par sync_plists.sh,
    # lui-même appelé par git_push_auto.sh (3 h). Rend visible dans le cockpit la
    # classe de panne « 97 installés / 44 versionnés » : une restauration perdait
    # 53 organes en silence.
    pv = jload(IM / "thermo" / "plists_versionnes.json")
    if pv:
        # hors_repo = agent installé ABSENT du repo → perdu à la restauration (danger).
        # a_declarer = installé ≠ repo → preuve dans plists/_derive/, rien n'est écrasé.
        hors = int(pv.get("hors_repo", 0) or 0)
        dec = int(pv.get("a_declarer", 0) or 0)
        detail = "%s agents · %s" % (pv.get("installes", "?"),
                                     ("0 hors repo" if hors == 0 else "%d HORS REPO" % hors))
        if dec:
            detail += " · ⚠ %d à déclarer (_derive/)" % dec
        detail += " · màj %s" % fmt_age(age_min(IM / "thermo" / "plists_versionnes.json"))
        g.append({"nom": "Agents launchd versionnés", "ok": hors == 0, "detail": detail})
    else:
        g.append({"nom": "Agents launchd versionnés", "ok": False,
                  "detail": "état absent (sync_plists.sh jamais passé)"})

    # LE REPO EST L'INSTALLATION (20/09) — état écrit par installer_depuis_repo.sh,
    # lui-même appelé par git_push_auto.sh (3 h). Rend visible POURQUOI l'installation
    # ne peut plus dériver : le fichier installé est un LIEN vers Index_Maison/plists/.
    # ok seulement si TOUS les agents versionnés sont liés et qu'aucun n'est divergent.
    ir = jload(IM / "thermo" / "installation_repo.json")
    if ir:
        lies = int(ir.get("deja_lies", 0) or 0)
        ver = int(ir.get("versionnes", 0) or 0)
        div = int(ir.get("divergents", 0) or 0)
        absents = int(ir.get("absents", 0) or 0)
        detail = "%d/%d agents = lien vers le repo" % (lies, ver)
        if div:
            detail += " · ⚠ %d divergent(s) : %s" % (div, str((ir.get("liste_divergents") or [""])[0])[:60])
        if absents:
            detail += " · %d absent(s)" % absents
        detail += " · màj %s" % fmt_age(age_min(IM / "thermo" / "installation_repo.json"))
        g.append({"nom": "Repo = installation",
                  "ok": (div == 0 and absents == 0 and ver > 0 and lies == ver),
                  "detail": detail})
    else:
        g.append({"nom": "Repo = installation", "ok": False,
                  "detail": "état absent (installer_depuis_repo.sh jamais passé)"})

    # DRILL DE RESTAURATION (19/09) — état écrit par drill_restauration.py, lui-même
    # appelé par git_push_auto.sh (3 h). Rend visible dans le cockpit la seule question
    # qui compte pour une sauvegarde : « si le Mac mourait ce soir, ACE777 reviendrait-il ? »
    # (agents reconstructibles, plists valides, organes présents, scellés alignés).
    dr = jload(IM / "thermo" / "drill_restauration.json")
    if dr:
        verdict = dr.get("verdict", "?")
        trous = dr.get("trous") or []
        detail = "verdict %s" % verdict
        if trous:
            detail += " · %d trou(s) : %s" % (len(trous), str(trous[0])[:90])
        detail += " · màj %s" % fmt_age(age_min(IM / "thermo" / "drill_restauration.json"))
        g.append({"nom": "Drill de restauration", "ok": verdict == "READY", "detail": detail})
    else:
        g.append({"nom": "Drill de restauration", "ok": False,
                  "detail": "jamais lancé (git_push_auto.sh le déclenche toutes les 3 h)"})

    # GARDE-FOU DE MÉTHODE SUR LES SEUILS (23/09, Buffy) — état écrit par
    # hulk-mexc/scripts/verif_seuil_moteur.py, appelé par ce même git_push_auto.sh (3 h).
    # POURQUOI CETTE LIGNE EXISTE : j'ai publié pendant trois jours un seuil RECALCULÉ de
    # mémoire (5 à 12,75 %) alors que le moteur en appliquait 21,70 % — il manquait le
    # terme dominant `dip = max(dip_pct ; 0,50 × cadence)`. Un chiffre recalculé n'est pas
    # un chiffre vérifié (classe F, 23/09). Ici la page ne dit pas « c'est vérifié » : elle
    # dit COMBIEN de refus chiffrés ont été CONFRONTÉS, si un instrument recalcule encore
    # un seuil sans la cadence, et depuis quand. Un état figé n'est pas un feu vert.
    sm_path = IM / "thermo" / "seuil_moteur.json"
    sm = jload(sm_path)
    sm_age = age_min(sm_path)
    if sm:
        n, tot = int(sm.get("refus_lus", 0) or 0), int(sm.get("conformes", 0) or 0)
        instr = sm.get("instruments_a_corriger") or []
        fige = (sm_age is not None and sm_age > 480)   # 8 h = deux passages manqués
        if n == 0:
            detail = "EN ATTENTE (aucun refus chiffré — normal < 1 h après une relance)"
            ok_sm = True
        else:
            detail = "%d/%d refus chiffrés confrontés" % (tot, n)
            ok_sm = bool(sm.get("conforme")) and not instr
            if instr:
                detail += " · %d instrument(s) à corriger : %s" % (len(instr),
                                                                   str(instr[0])[:60])
        if fige:
            detail += " — ÉTAT FIGÉ (>8 h, le contrôle n'est plus passé)"
            ok_sm = False
        detail += " · màj %s" % fmt_age(sm_age)
        g.append({"nom": "Garde-fou seuil moteur", "ok": ok_sm, "detail": detail})
    else:
        g.append({"nom": "Garde-fou seuil moteur", "ok": False,
                  "detail": "état absent (git_push_auto.sh ne l'a jamais produit)"})

    # RÈGLES D'OR (19/09) — état écrit par verifier_regles_or.py (lecture seule), lui-même
    # appelé par git_push_auto.sh. Une règle qu'on ne mesure pas se perd : ici on VOIT
    # lesquelles sont tenues et LAQUELLE lâche. Canon : Index_Maison/REGLE_D_OR.md.
    ro = jload(IM / "thermo" / "regles_or.json")
    if ro:
        regles = ro.get("regles") or []
        tenues = len([r for r in regles if r.get("ok")])
        viol = [r for r in regles if not r.get("ok")]
        detail = "%d/%d tenues" % (tenues, len(regles))
        if viol:
            detail += " · R%s : %s" % (viol[0].get("regle"), str(viol[0].get("detail"))[:80])
        detail += " · màj %s" % fmt_age(age_min(IM / "thermo" / "regles_or.json"))
        g.append({"nom": "Règles d'or", "ok": ro.get("verdict") == "OK", "detail": detail})
    else:
        g.append({"nom": "Règles d'or", "ok": False,
                  "detail": "jamais mesuré (git_push_auto.sh le déclenche toutes les 3 h)"})

    # LE CRI VIVANT (20/09) — état des cris ACTIFS, écrit par le chien (thermo/cris.json).
    # Ce fichier s'AUTO-EFFACE quand la cause disparaît : la page ne peut donc pas
    # afficher un cri résolu (R14 — une alarme qui survit à sa cause apprend à ignorer
    # les autres). Avant, un cri n'existait que comme ligne ajoutée à un log : on ne
    # savait pas s'il était encore vrai. Le champ « voix » dit si la voix a réellement
    # été lancée — un cri muet est un faux cri.
    cris = jload(IM / "thermo" / "cris.json")
    if cris:
        n = int(cris.get("nb") or 0)
        n_crit = int(cris.get("nb_critique") or 0)
        liste = cris.get("cris") or []
        detail = "aucun" if not n else " · ".join(
            "%s %s (voix : %s)" % (c.get("gravite"), c.get("organe"), c.get("voix") or "?")
            for c in liste[:2])
        age_cris = age_min(IM / "thermo" / "cris.json")
        if age_cris is not None and age_cris > 15:
            detail += " · ⚠ état figé (chien muet depuis %s)" % fmt_age(age_cris)
        g.append({"nom": "Cris en cours", "ok": n_crit == 0, "detail": detail})
    else:
        g.append({"nom": "Cris en cours", "ok": False,
                  "detail": "thermo/cris.json absent (chien jamais passé depuis le 20/09)"})

    # REVUE DES ORGANES (20/09) — état écrit par scripts/revue_organes.py (3 h).
    # Rend visible ce que le chien ne peut pas voir : les écarts STRUCTURELS entre ce
    # que le registre DÉCLARE et ce que le disque PROUVE (cadence déclarée ≠ déclencheur
    # réel, produit déclaré non résolu, contenu figé). Un écart n'est pas une panne :
    # c'est une déclaration à faire (strategie/revue_declares.json).
    rv = jload(IM / "thermo" / "revue_organes.json")
    if rv:
        r = rv.get("resume") or {}
        n_a_trancher = int(r.get("a_trancher") or 0)
        detail = "%s/%s OK · %s jugés sur leur sortie · %s assumé(s)" % (
            r.get("ok", "?"), rv.get("total", "?"), r.get("juge_sur_sortie", "?"), r.get("assumes", "?"))
        if n_a_trancher:
            detail += " · ⚠ %d à trancher : %s" % (
                n_a_trancher, str((rv.get("a_trancher") or [{}])[0].get("organe")))
        detail += " · màj %s" % fmt_age(age_min(IM / "thermo" / "revue_organes.json"))
        g.append({"nom": "Revue des organes", "ok": n_a_trancher == 0, "detail": detail})
    else:
        g.append({"nom": "Revue des organes", "ok": False,
                  "detail": "jamais lancée (git_push_auto.sh la déclenche toutes les 3 h)"})

    # ══ 22/09/2026 — LA 6ᵉ PARTIE DU CYCLE, RENDUE VISIBLE (GO 2) ══════════════════
    # POURQUOI ICI : ces trois verdicts vivaient dans des fichiers que PERSONNE ne lit
    # (CRITIQUE_ERREURS_DERNIER.json, SEUILS_FIXES_DERNIER.json, thermo/sortie_mesuree.json).
    # Un verdict qu'on doit aller chercher n'existe pas (R15). Le cockpit « vol » est la
    # page qu'on regarde déjà : c'est là que ça doit crier — pas dans un dossier.
    # LECTURE SEULE : on ne fait que lire des états écrits par les organes eux-mêmes.

    # (a) Le registre des échecs est-il BRANCHÉ, et retombons-nous dans une erreur payée ?
    cr = jload(IM / "CRITIQUE_ERREURS_DERNIER.json")
    if cr:
        nb = len(cr.get("non_branche") or [])
        nr = len(cr.get("recidives") or {})
        detail = "%s classes · %s" % (cr.get("classes", "?"),
                                      ("branché" if nb == 0 else "%d NON BRANCHÉ" % nb))
        detail += " · récidives %d" % nr
        if nr:
            detail += " (" + ", ".join("%s×%s" % (k, v) for k, v in
                                        (cr.get("recidives") or {}).items()) + ")"
        detail += " · màj %s" % fmt_age(age_min(IM / "CRITIQUE_ERREURS_DERNIER.json"))
        g.append({"nom": "Registre des échecs (6ᵉ partie)",
                  "ok": (nb == 0 and nr == 0), "detail": detail})
    else:
        g.append({"nom": "Registre des échecs (6ᵉ partie)", "ok": False,
                  "detail": "état absent (critique_erreurs.py jamais passé)"})

    # (b) R17 : combien de seuils décident SANS mesure, et y en a-t-il un de non rangé ?
    sf = jload(IM / "SEUILS_FIXES_DERNIER.json")
    if sf:
        nc = sf.get("non_classees") or []
        detail = "%s seuils décident sans mesure · %s" % (
            sf.get("decideurs", "?"), "tous rangés" if not nc else "%d NON RANGÉ(s)" % len(nc))
        if nc:
            detail += " : " + ", ".join(nc[:3])
        detail += " · màj %s" % fmt_age(age_min(IM / "SEUILS_FIXES_DERNIER.json"))
        g.append({"nom": "Seuils sans mesure (R17)", "ok": not nc, "detail": detail})
    else:
        g.append({"nom": "Seuils sans mesure (R17)", "ok": False,
                  "detail": "état absent (inventaire_seuils_fixes.py jamais passé)"})

    # (c) La sortie est-elle bien pilotée par la mesure, EN VOL ? (GO 3)
    # Le verdict distingue trois états qu'un œil humain ne peut pas distinguer dans un
    # journal vide : la règle ARMÉE qui attend (normal), la règle ARMÉE qui a tiré, et
    # la règle ÉTEINTE (= régression silencieuse). Un « rien à signaler » ambigu serait
    # exactement le silence qu'on a supprimé (règle #6).
    sm = jload(IM / "thermo" / "sortie_mesuree.json")
    if sm:
        arm = bool(sm.get("regle_armee"))
        nm, na = int(sm.get("n_mesurees") or 0), int(sm.get("n_anomalies") or 0)
        detail = "règle %s · %d sortie(s) mesurée(s)" % ("armée" if arm else "ÉTEINTE", nm)
        if na:
            detail += " · ⚠ %d NON conforme(s)" % na
        detail += " · %s" % str(sm.get("verdict") or "")[:70]
        detail += " · màj %s" % fmt_age(age_min(IM / "thermo" / "sortie_mesuree.json"))
        g.append({"nom": "Sortie pilotée par la mesure",
                  "ok": (arm and na == 0), "detail": detail})
    else:
        g.append({"nom": "Sortie pilotée par la mesure", "ok": False,
                  "detail": "état absent (suivi_sortie_mesuree.py jamais passé)"})
    return g


# ── 6. Banc 20 actifs — risque (dernier run simu_20_actifs.py) ──────
def banc():
    """Dernier run du banc : net, DD max portefeuille et net/DD, base vs notrend.
    C'est la mesure de RISQUE qui a tranché la décision du 18/09 (filtre tendance
    = contrôle de drawdown). Lecture seule d'un JSON du banc — aucun ordre."""
    runs = sorted((BASE / "hulk-mexc" / "runs").glob("SIMU_20_ACTIFS_*.json"))
    if not runs:
        return None
    d = jload(runs[-1])
    res = d.get("resultats") or {}
    lignes = []
    for mode, label in (("base", "base (dip σ + tendance)"),
                        ("notrend", "notrend (sans tendance)")):
        m = res.get(mode) or {}
        f, o = (m.get("full") or {}), (m.get("oos") or {})
        lignes.append({
            "mode": label,
            "net_full": f.get("net"), "dd_full": f.get("dd_portefeuille"),
            "net_dd_full": f.get("net_sur_dd"),
            "net_oos": o.get("net"), "trades_oos": o.get("trades"),
        })
    return {"ts": d.get("ts"), "fichier": runs[-1].name, "lignes": lignes}


def main():
    now = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    snapshot = {
        "ts": now,
        "sante": lire_sante(),
        "marche": lire_marche(),
        "gardiens": gardiens(),
        "plists": lire_plists(),
        "protocoles": protocoles(),
        "dormants": dormants(),
        "banc": banc(),
    }
    js = "window.__VOL__ = " + json.dumps(snapshot, ensure_ascii=False) + ";"
    (COCKPIT / "vol_live.js").write_text(js, encoding="utf-8")
    # NOTE 14/09 : vol.html n'est JAMAIS réécrit par ce générateur — c'est un
    # fichier scellé (registre synapses). Le cache-buster est géré côté client
    # dans vol.html (Date.now()), sinon la veilleuse crie INTRUSION à chaque
    # cycle (leçon du 14/09 12:31 : on ne scelle pas un fichier qu'on réécrit).
    ko = [p["label"] for p in snapshot["plists"] if p["etat"] == "echec"]
    al = [p["label"] for p in snapshot["plists"] if p["etat"] == "alerte"]
    print("vol_live.js généré — %d plists (%d échec, %d alerte métier), %d protocoles, santé %s"
          % (len(snapshot["plists"]), len(ko), len(al), len(snapshot["protocoles"]),
             snapshot["sante"]["etat"]))
    if ko:
        print("   échecs réels : " + ", ".join(ko))


if __name__ == "__main__":
    main()
