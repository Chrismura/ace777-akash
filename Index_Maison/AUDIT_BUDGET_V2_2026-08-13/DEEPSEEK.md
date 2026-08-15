# AVIS DEEPSEEK (task mission)

provider: Puter Grok (gratuit)

**Verdict : NON**

### Réserves critiques (bloquantes)

**1. Verrou anti-doublon (flock) – Échec total**
- Aucun verrou `flock` n’existe dans les fichiers livrés (`budget_hub.py`, bloc d’intégration `hub_prise_ia.py`, ni dans les tests).
- Le point de vigilance que tu as explicitement demandé (« le lock est relache dans finally apres time.sleep(0.1) alors que le thread trio tourne encore ») ne peut pas être vérifié car **le code de consultation n’est pas présent**. Il n’y a ni pose du verrou au tout début, ni maintien pendant toute la durée du trio (30-60 s). Le bug d’origine (appel 10 s plus tard qui repasse) reste donc possible.

**2. Anti-spam au début, même en échec**
- Aucun anti-spam n’est positionné au début de la consultation dans le code livré.
- Le bloc d’intégration dans `hub_prise_ia.py` ne contient aucune logique d’anti-spam (ni 5 min, ni 60 s en tempête). Il ne traite que le budget après coup.

**3. Mode tempête (ROUGE / alarme / vortex)**
- La fonction `mode_tempete_actif()` ne lit qu’un fichier JSON (`etat_tempete.json`). Elle ne gère **aucun** des déclencheurs mentionnés (zone ROUGE, alarme, vortex >= 2).
- Le cap horaire n’est pas explicitement désactivé en tempête dans le code livré. La phrase « jamais bloque par le cap » n’est pas implémentée de façon robuste.

**4. Code du trio hub réel absent**
- Le livrable ne contient pas le code réel de consultation (`famille_session.py` ou équivalent). Le trio hub est absent ou remplacé par un placeholder implicite.
- Le bloc d’intégration fourni est une surcouche budget uniquement. Il n’est pas intégrable tel quel dans un flux de consultation réel sans le code manquant.

### Points corrects (mais insuffisants)

- La lecture dynamique des gratuits depuis `providers.json` est bien faite (`gratuits_actifs()` + construction du set dans le bloc d’intégration).
- `CAPACITES` est complète pour les providers demandés.
- Réserve storm 20 % et non-coupure des gratuits en calme sont présents.
- Python 3.9 stdlib + typage `Optional` respecté.
- Tests mis à jour (T3 et T6).

### Conclusion

Le travail sur le budget dynamique est globalement conforme à la spec v2, mais **les exigences principales de l’audit** (verrou flock maintenu pendant toute la consultation, anti-spam au tout début même en échec, mode tempête avec déclencheurs ROUGE/vortex, et absence de placeholder sur le trio) ne sont **pas présentes** dans les livrables.

Tant que ces éléments ne sont pas fournis et audités, le code n’est pas validable.
