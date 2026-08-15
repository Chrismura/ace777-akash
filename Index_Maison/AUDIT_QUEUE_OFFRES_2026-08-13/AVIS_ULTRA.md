# ULTRA — inferx.analyse

**ULTRA (ACE777). Audit de code — `QUEUE_OFFRES.PY`**

---

### 1. Verdict GO / NO-GO
**GO** 
*Raison :* Le script est robuste, intègre les garde-fous essentiels (verrou PID, écriture atomique, kill switch, gestion des erreurs HTTP 429/404) et le cycle de vie (essai/poubelle/réserve) est validé par des tests réels concluants. Prêt pour l'automatisation `launchd`.

---

### 2. Point de risque ou régression possible
**Le risque de pollution du routage dynamique par les observations.**
Si le hub charge automatiquement tous les providers du fichier `providers.json` marqués `free: True` et `enabled: True`, un "candidat observation" non validé par un humain pourrait être appelé en production par le routeur principal si sa priorité (`order`) le place avant les ténors de la famille. 
*Vérification indispensable :* S'assurer que le hub ACE777 ignore explicitement les providers dont la note/le statut est `"observation"` tant que la famille ou le juge n'ont pas validé la promotion définitive.

---

### 3. Suggestion d'amélioration concrète (Stabilité / Logique)
**Purge automatique des vieilles entrées en "poubelle" ou "mortes".**
Actuellement, la file risque de grossir indéfiniment avec les faux positifs et les 3 essais échoués (qui finissent en échec définitif). 
*Suggestion :* Implémenter un mécanisme de nettoyage (TTL) dans le JSON qui supprime ou archive (dans un `poubelle.json` séparé) les offres ayant atteint `MAX_ESSAIS` ou n'ayant pas bougé depuis plus de 14 jours, afin de garder un fichier `QUEUE_OFFRES.json` léger et ultra-rapide à scanner pour les passes suivantes.
