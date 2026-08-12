#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
oral_fr.py - Conversion nombres -> lettres françaises (règles exactes ACE777)
Zéro dépendance, Python 3.9, rapide, sans exception.

V3 (intégration Buffy, 11/08) :
- NE convertit JAMAIS : heures (13:45), dates (11/08/2026), versions (v2.0),
  identifiants (BTCUSDT, lot3), nombres collés à un mot.
- CONVERTIT : entiers compacts (61500, 3486), décimaux à VIRGULE française
  (99,99 -> quatre-vingt-dix-neuf virgule quatre-vingt-dix-neuf),
  pourcentages (18,5 % -> dix-huit virgule cinq pour cent).
- Nombres < 0,0001 : laissés tels quels (le brief dit déjà « quasi nul »).
- Un espace normal ne combine JAMAIS deux nombres (1000 1500 = deux nombres).
"""

import re

# --- Regex précompilées (module level) ---
# Nombre isolé : signe -, entiers compacts, décimale à VIRGULE française optionnelle,
# pourcentage optionnel. Lookarounds stricts (jamais collé à lettre / . / , / : / /).
RE_NOMBRE = re.compile(
    r'(?<![\w.,/:])'
    r'(-?\d{1,3}(?:\d{3})*)(?:,(\d+))?'
    r'(?:\s*%)?'
    r'(?![\w.,/:])',
    re.UNICODE
)

UNITS = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
DIX = ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]
VINGT = ["vingt", "trente", "quarante", "cinquante", "soixante"]

def _chiffre_en_mot(d: int) -> str:
    if 0 <= d <= 9:
        return UNITS[d]
    return ""

def _nombre_moins_100(n: int) -> str:
    if n == 0:
        return "zéro"
    if n < 10:
        return UNITS[n]
    if n < 17:
        return DIX[n - 10]
    if n < 20:
        return f"dix-{UNITS[n-10]}"
    if n < 70:
        dix = (n // 10) - 2
        reste = n % 10
        if reste == 1:
            return f"{VINGT[dix]} et un"
        if reste == 0:
            return VINGT[dix]
        return f"{VINGT[dix]}-{UNITS[reste]}"
    if n < 80:
        reste = n - 60
        if reste == 11:                       # 71 = soixante ET onze
            return "soixante et onze"
        if reste == 0:
            return "soixante"
        return f"soixante-{_nombre_moins_100(reste)}"
    # 80-99
    reste = n - 80
    if n == 80:
        return "quatre-vingts"
    if reste == 1:
        return "quatre-vingt-un"
    return f"quatre-vingt-{_nombre_moins_100(reste)}"

def _nombre_moins_1000(n: int) -> str:
    if n < 100:
        return _nombre_moins_100(n)
    centaines = n // 100
    reste = n % 100
    if centaines == 1:
        cent = "cent"
    else:
        cent = f"{UNITS[centaines]} cent"
        if reste == 0 and centaines > 1:
            cent += "s"
    if reste == 0:
        return cent
    return f"{cent} {_nombre_moins_100(reste)}".strip()

def _grand_nombre(n: int) -> str:
    if n < 1000:
        return _nombre_moins_1000(n)
    if n < 1_000_000:
        milliers = n // 1000
        reste = n % 1000
        if milliers == 1:
            txt = "mille"
        else:
            txt = f"{_grand_nombre(milliers)} mille"
        if reste:
            txt += " " + _grand_nombre(reste)
        return txt
    if n < 1_000_000_000:
        millions = n // 1_000_000
        reste = n % 1_000_000
        txt = f"{_grand_nombre(millions)} million"
        if millions > 1:
            txt += "s"
        if reste:
            txt += " " + _grand_nombre(reste)
        return txt
    milliards = n // 1_000_000_000
    reste = n % 1_000_000_000
    txt = f"{_grand_nombre(milliards)} milliard"
    if milliards > 1:
        txt += "s"
    if reste:
        txt += " " + _grand_nombre(reste)
    return txt

def nombre_en_mots(n: float) -> str:
    """Nombre (entier ou flottant) -> mots français. Gère négatifs et décimales."""
    if n < 0:
        return "moins " + nombre_en_mots(-n)
    if n == 0:
        return "zéro"

    partie_entiere = int(n)
    decimal_str = ""

    if isinstance(n, float) and not n.is_integer():
        decimal_part = str(n).split(".")[1]
        if "e" in decimal_part.lower():      # scientifique -> chiffres un par un
            decimal_str = " ".join(_chiffre_en_mot(int(d)) for d in decimal_part if d.isdigit())
        else:
            decimal_str = _decimales_en_mots(decimal_part)

    if partie_entiere == 0 and decimal_str:
        return "zéro virgule " + decimal_str

    mots = _grand_nombre(partie_entiere)
    if decimal_str:
        mots += " virgule " + decimal_str
    return mots

def _decimales_en_mots(decimal_str: str) -> str:
    if not decimal_str:
        return ""
    # Zéros de tête -> chiffres un par un (0,005 -> zéro virgule zéro zéro cinq)
    if decimal_str.startswith("0"):
        return " ".join(_chiffre_en_mot(int(d)) for d in decimal_str)
    return _grand_nombre(int(decimal_str))

def oraliser(texte: str) -> str:
    """Remplace les nombres lisibles d'un texte par leurs mots français.
    Le texte reste inchangé en cas de problème (sécurité anti-casse)."""
    if not texte:
        return texte
    try:
        def _remplacer(match):
            entier_brut = match.group(1)
            decimale = match.group(2)
            pourcent = "%" in match.group(0)

            if decimale is None:
                try:
                    val = int(entier_brut)
                except ValueError:
                    return match.group(0)
                # trop petit pour être lu (< 0,0001) : laisser tel quel
                if val != 0 and abs(val) < 1:
                    return match.group(0)
                mots = _grand_nombre(abs(val))
                if val < 0:
                    mots = "moins " + mots
            else:
                try:
                    val = float(entier_brut + "." + decimale)
                except ValueError:
                    return match.group(0)
                if val != 0 and abs(val) < 0.0001:
                    return match.group(0)
                if decimale.startswith("0"):
                    dec_mots = " ".join(_chiffre_en_mot(int(d)) for d in decimale)
                else:
                    dec_mots = _grand_nombre(int(decimale))
                if val < 0:
                    mots = "moins " + _grand_nombre(abs(int(val))) + " virgule " + dec_mots
                elif int(val) == 0:
                    mots = "zéro virgule " + dec_mots
                else:
                    mots = _grand_nombre(int(val)) + " virgule " + dec_mots

            if pourcent:
                mots += " pour cent"
            return mots

        return RE_NOMBRE.sub(_remplacer, texte)
    except Exception:
        return texte   # sécurité anti-casse
