# Rapport — L'IA Fantôme (3 points)

**Date :** 27 février 2026

---

## 1. Ollama GPU 100% sans LLM gate visible dans les logs

**Problème :** Ollama affiche 100% GPU alors que launch_250_4h.sh ne montre aucune ligne LLM gate dans les logs. M1 chauffe à vide.

**Cause :** Le LLM gate est activé par fortress (LLM_GATE_ENABLED=TRUE) mais aucun echo n’affiche ce statut au démarrage. Il est donc invisible dans les logs.

**Correction :** Ajouter un echo "LLM gate ON" au démarrage et exporter explicitement LLM_GATE_ENABLED dans launch_250_4h.sh.

---

## 2. Scripts qui disparaissent ou deviennent vides

**Problème :** v8_6_fortress, SOUVERAIN_START.sh disparaissent ou deviennent des dossiers vides.

**Constat :** Aucun script de nettoyage n’a été trouvé dans le projet qui supprime ces fichiers. Les seuls `rm` concernent STOP_ALPHA, STOP_BETA et les fichiers PID. SOUVERAIN_START_ELITE_STYLE.sh existe et est complet.

**À vérifier :** Autre outil, script externe ou action manuelle.

---

## 3. Hachage non filtré sans LLM_GATE_ENABLED

**Problème :** Sans LLM_GATE_ENABLED, l’ACE prend des BETA_SENTINEL_CUT à l’aveugle sur des tensions de 15.14. Passoire assurée.

**Cause :** Le LLM gate filtre avant l’ordre. S’il est désactivé, tout passe.

**Correction :** S’assurer que LLM_GATE_ENABLED=TRUE est toujours exporté par le lanceur (fortress, launch_250_4h.sh).
