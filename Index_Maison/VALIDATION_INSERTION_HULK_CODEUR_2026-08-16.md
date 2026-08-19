# code.ia — insertion HULK disjoncteur (provider Google Gemini, 4.8s)

Ici ACE777. Analyse rigoureuse du point d'insertion dans HULK (`paper_diprip.py`) sans compromettre la logique moteur.

---

### 1) RÉPONSES AUX 4 QUESTIONS

1. **Import direct vs Subprocess :** 
   **Import direct** (`from scripts.disjoncteur import verifier_et_brigader`). 
   *Justification :* Le subprocess lance un interpréteur Python externe, ce qui ajoute une latence inacceptable (10-50ms) sur le carnet d'ordres, consomme des ressources système et complique la gestion des erreurs d'E/S. Un appel direct de fonction dans le même processus est propre (stdlib), rapide et robuste si la fonction est conçue pour ne pas lever d'exception non gérée.

2. **Où EXACTEMENT dans `paper_diprip.py` ?**
   Juste avant la soumission de l'ordre au carnet/exchange, au niveau de la fonction qui prépare ou passe l'ordre (ex: `place_order` ou équivalent), **mais après** le calcul de la taille initiale par la stratégie, et **avant** toute signature ou appel réseau.

3. **Quelle valeur de capital_ref ?**
   Le **capital total courant du compte paper HULK** (ex: `portfolio.get_total_balance()` ou la variable d'état représentant le capital dynamique du bot), et **jamais** une constante en dur. Le pourcentage de perte journalière doit être calculé sur la réalité du portefeuille.

4. **Que faire si le disjoncteur plante (Fail-Closed) ?**
   **Rejeter l'ordre par défaut (Fail-Closed).** Si le module disjoncteur lève une exception (erreur disque JSON, corruption, etc.), la fonction doit intercepter l'erreur, logger un niveau critique, et retourner `0` (taille interdite). *Sécurité maximale.*

---

### 2) DIFF EXACT (Minimal et Non-Invasif)

Voici le diff conceptuel à insérer dans `hulk-mexc/scripts/paper_diprip.py` sans modifier la logique de calcul de la stratégie :

```python
# --- AJOUT ACE777 : Import du disjoncteur (Point d'insertion unique) ---
try:
    from scripts.disjoncteur import verifier_et_brigader
except ImportError:
    # Fallback sécurisé si exécuté depuis un autre répertoire
    import sys
    sys.path.append(os.path.dirname(__file__))
    from disjoncteur import verifier_et_brigader
```

Dans la fonction d'exécution d'ordre (ex: `executer_ordre` ou `passer_ordre`) :

```python
<<<<
def executer_ordre(taille, prix, symbole):
    # Logique d'origine HULK
    placer_ordre_moteur(taille, prix, symbole)
====
def executer_ordre(taille_proposee, prix, symbole):
    # [ACE777] Point d'insertion disjoncteur (Mur de Fer)
    try:
        capital_actuel = obtenir_capital_reel() # Remplacer par la variable/méthode existante dans HULK
        taille_validee = verifier_et_brigader(
            taille_proposée=taille_proposee, 
            capital_ref=capital_actuel
        )
        if taille_validee <= 0:
            logger.error("[DISJONCTEUR] Ordre bloqué ou bridé à 0 par le disjoncteur.")
            return False
    except Exception as e:
        logger.critical(f"[DISJONCTEUR] ERREUR CRITIQUE FAIL-CLOSED: {e}")
        return False # Fail-closed strict

    # Logique d'origine HULK inchangée avec la taille validée
    placer_ordre_moteur(taille_validee, prix, symbole)
>>>>
```

---

### 3) NOTES (Risques & Périmètre)

* **Ce qu'on ne touche PAS :** La génération des signaux, les indicateurs techniques, le calcul des prix d'entrée/sortie, et la boucle principale de `paper_diprip.py`.
* **Risque de dépendance circulaire :** S'assurer que `disjoncteur.py` n'importe pas `paper_diprip.py`. Le disjoncteur doit rester un module autonome dépendant uniquement de la stdlib et de son fichier d'état JSON.
* **Performance :** L'import direct garantit un temps d'exécution inférieur à 1 milliseconde, préservant la réactivité du bot HULK en conditions de marché volatiles.
