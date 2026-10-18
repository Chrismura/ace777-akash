# AVIS DEEPSEEK (task deepseek.analyse · Google Gemini · 2026-10-18T22:05Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 85 %
HYPOTHÈSES : 
1. Le score de performance actuel pénalise lourdement le taux de NEUTRE sans corréler avec la rentabilité réelle du portefeuille BTC.
2. L'infrastructure actuelle permet d'isoler une couche de calcul mathématique externe sans réécrire l'intégralité du pipeline LLM.
3. Les 12 modèles en rotation n'ont pas tous la même sensibilité aux contraintes de format du chat.

CE QUI CHANGERAIT L'AVIS : Un benchmark prouvant que le mélange actuel des 12 modèles surpasse un modèle unique fine-tuné avec un taux d'abstention calibré.

AMÉLIORATION PROPOSÉE : 
1. Implémenter un routeur sémantique amont (type BERT léger ou regex strictes) pour intercepter les questions hors-sujet avant l'appel LLM, éliminant le template forcé.
2. Remplacer la rotation des 12 modèles par un comité fixe (style TradingAgents : Bull/Bear/Risk Manager) ancré sur un modèle unique robuste pour garantir la continuité du state.
3. **Approche alternative (Clause Christophe) :** Instaurer un système de *double-seuil d'hystérésis* pour le NEUTRE : un seuil bas pour entrer en position (ex: < 55%), un seuil haut pour en sortir (ex: > 65%), évitant les bascules binaires toxiques pour le score.

SYNTHÈSE : 
Cortana souffre d'une boucle vicieuse prompts/score, d'une amnésie inter-modèles et d'une rigidité conversationnelle totale. Les remèdes 2026 (TradingAgents et couche maths séparée) frappent juste mais demandent un effort d'architecture lourd. Il faut commencer par dissocier le routage thématique (stopper le délire climat/funding) avant de toucher aux seuils de décision. L'effort doit se concentrer en priorité sur la stabilité du modèle unique et le filtrage des entrées.
