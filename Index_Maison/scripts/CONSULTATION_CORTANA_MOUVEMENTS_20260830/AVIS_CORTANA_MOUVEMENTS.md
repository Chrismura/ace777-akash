# AVIS CORTANA — mouvements BTC + correction label (provider Google Gemini)

**CORTANA — ANALYSE FAMILLE ACE777**  
*Contrat : ADVISORY (Proposition pure, justesse estimée : 92%).*

---

### 1. VERDICT SUR LE BILAN DES MOUVEMENTS (30/08/2026)
* **Lecture synthétique :** Accumulation silencieuse et réorganisation structurelle. 
* **Justification chiffrée :** 87% de flux internes (Hot $\leftrightarrow$ Cold) prouvent que les desks et exchanges rebalancent leurs coffres, pas leurs vitrines de vente. Le net $+2\,652$ BTC sur 24h confirme l'absorption. Le pic de poussière (score 50/50, sans CPFP déclenché) est un **bruit de fond technique** (consolidation d'UTXO par des exchanges ou des fonds), pas une attaque. Les vieux coins (553 BTC de 2011-2014) sont de la réallocation marginale, statistiquement insignifiante face aux 87k BTC brassés. 
* **Bilan :** Marché **neutre à tendance haussière (accumulation)**. Aucun signal de panique ou de distribution massive.

---

### 2. LA QUESTION COINBASE : TRACKER OU PAS ?
* **Constat :** Vouloir tracker Coinbase adresse par adresse est une **impasse analytique** (milliers d'adresses, rotation dynamique pour les ETF). 
* **Proposition alternative :** **Abandonner le tracking onchain direct des adresses de détail/cold Coinbase.** C'est une perte de ressources. 
* **Comment l'intégrer sans alourdir Hulk :** 
  1. Remplacer les adresses unitaires par un **suivi macro-régulateur des flux ETF nets (en USD)** publiés chaque soir (données IBIT/Fidelity J+1).
  2. Tracker un **indice proxy onchain de liquidité US** (ex: volume des transactions onchain aux heures de bureau US / Coinbase Prime net inflows agrégés par Arkham via API, sans stocker les adresses dans notre base).
  3. Hulk ne touche *rien* de tout cela : Hulk reste focalisé sur ses petites caps MEXC (dip & rip). La veille baleines reste au niveau macro/exchange global (Binance, OKX, transferts >1000 BTC).

---

### 3. AMÉLIORATION GO-SIZED : LE « PROXY SENTINEL » (Veille Baleines)
Nos sondes ont échoué sur Coinbase et ont failli rater les vieux coins. Corriger les labels ne suffit pas. 

* **Proposition concrète :** Implémenter un filtre de **« Détection d'Ancienneté Dynamique » (DAD)** adossé à un proxy ETF.
  * **Quoi :** Au lieu de chercher *qui* détient l'adresse destinataire de Coinbase, notre script de veille calcule instantanément le *Coin Days Destroyed (CDD)* et l'âge moyen des UTXO déplacés dès qu'un bloc >500 BTC bouge.
  * **Pourquoi :** Si les adresses Coinbase sont introuvables, leurs mouvements massifs pour le compte d'IBIT se traduisent *nécessairement* par des transferts inter-institutionnels ou des créations d'UTXO standardisés. Le CDD détecte le réveil des vieux coins (comme les 553 BTC) sans avoir besoin de connaître le nom du propriétaire.
  * **Impact :** Zéro dépendance aux étiquettes d'adresses obsolètes (Arkham/Whales.json). On traque le *comportement* (l'âge de la monnaie) plutôt que l'*identité* (le label).

---
*Fin du rapport. En attente d'arbitrage de Christophe pour basculer en mode application.*
