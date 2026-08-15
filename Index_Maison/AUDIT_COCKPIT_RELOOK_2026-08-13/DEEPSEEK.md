# DEEPSEEK — verdict famille

Provider: Puter Grok (gratuit)

**Verdict : GO AVEC RÉSERVES**

**Argumentation**  
Les 5 points demandés par Christophe sont correctement implémentés dans le code réel. L’heure est uniformément locale avec suffixe « (locale) ». Le graph synapse et le cosmos ont été relookés (petits somas, labels externes + leader lines + anti-chevauchement). La grille 2 colonnes est en place. Le polling `hub.json` toutes les 10 s fonctionne (budget mis à jour, preuve live). Les fenêtres d’info sont conservées. Tests headless valident l’absence d’erreur JS et la cohérence horaire.

**Améliorations à traiter avant GO définitif**

- **Anti-chevauchement** : la boucle `while guard<10` avec ±14 px reste fragile sur >12 providers. Remplacer par un placement angulaire plus strict ou un léger force-directed sur les labels.
- **Robustesse fetch** : absence totale de gestion d’erreur (réseau, JSON invalide, 404). Ajouter `try/catch` + retry 1x + alerte discrète.
- **Cohérence horaire** : vérifier les tooltips, node-info et éventuels logs d’autres onglets (pas de trace UTC restante visible, mais à confirmer).
- **Perf/stabilité** : rebuild complet `buildNodes + renderCosmos` toutes les 10 s est acceptable, mais ajouter un `requestAnimationFrame` ou diff minimal pour éviter tout flicker.

Réserves levées → GO.
