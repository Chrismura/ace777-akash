# AVIS CORTANA — vieux BTC qui bougent (provider Google Gemini)

**CORTANA / ANALYSTE-MAÎTRESSE ACE777**  
*Contrat : ADVISORY (Proposition pure — Justesse >60% validée).*

---

### 1. VERDICT SUR L'ÉVÉNEMENT (Signal de marché vs Réorganisation)

**Verdict : Réorganisation technique et juridique, PAS une distribution de marché.**  
Argumentation factuelle :
* **Destination des flux :** Sur les 553,59 BTC analysés, 5 sur 6 partent vers des adresses muettes sans lien exchange. Le seul identifié (Boerse Stuttgart) relève du *custody* institutionnel allemand, pas du carnet d'ordres spot.
* **Le déclencheur juridique (Procès NY) :** Le "dusting" étiqueté (*Noah Doe #1396 / #1680*) vise à qualifier ces biens d'*abandoned property*. Bouger ses fonds est la seule parade onchain pour prouver l'activité et forcer le retrait de la plainte (comme les 44 wallets déjà sortis en juillet).
* **Le facteur technique (Coldcard) :** La migration post-faille firmware (2 440 BTC et vagues de drain) pousse les vieux holders paranoïaques à réorganiser leurs clés hors des vieux cold storages.
* **Le contexte macro :** L'activité dormante globale reste au plus bas depuis 2022. Ce n'est pas une vague systémique de take-profit, c'est du housekeeping de cypherpunks ou d'ayants droit sous pression légale.

---

### 2. LECTURE POUR HULK & LA THÈSE CHRISTOPHE

* **Impact sur la Thèse BTC (Christophe — *L'arbre qui cache la forêt, or/Bâle 3* / 2e degré) :** Zéro impact baissier. Au contraire, le fait que ces vieux $BTC$ soient déplacés pour être *protégés* (gardés en cold ou en custody souverain) plutôt que liquidés confirme que le socle de valeur ne fuite pas vers le fiat. L'or et la monnaie souveraine/alternative restent l'horizon indépassable.
* **Impact pour HULK (Paper dip & rip MEXC small caps) :** Aucun impact direct sur nos micro-caps. Les flux d'exchange détectés sont du bruit standard. HULK continue de vivre de son côté sur ses inefficiénéités de liquidité. La seule lecture est psychologique : pas de panique macro à redouter de ce côté-là, le marché des alts/small caps peut respirer.

---

### 3. AMÉLIORATION CONCRÈTE (Au-delà du correctif : Nouvelle architecture de sonde)

*Le constat de la mission est implacable : `surveiller_whales.py` est aveugle car il ne regarde que les étiquettes exchanges.*

**Proposition (La Sonde "Lazarus-Scan") :**  
Plutôt que d'alourdir Hulk ou de scannner tout le mempool (trop lourd), on crée un script léger asynchrone `old_coins_radar.py` basé sur une métrique onchain simple : **l'Indice de Dormance des Entrants/Sortants (UTXO Age)** via l'API gratuite de Mempool.space ou Blockchair.

* **Le Filtre (Seuil) :** Ne remonter que les transactions ayant un *Coin Days Destroyed (CDD)* anormal ou des inputs dont l'UTXO a $\geq$ 10 ans (avant 2016), pour un montant cumulé $\geq$ 10 BTC (pour filtrer le bruit des particuliers).
* **Le Croisement (L'amélioration par rapport à ta demande) :** Au lieu de simplement l'afficher, on croise ce flux de vieux coins avec les *murs de liquidité* et notre **indice onchain**. 
  * Si un vieux coin bouge vers un exchange $\rightarrow$ *Alerte Rouge Distribution*.
  * S'il bouge vers une adresse muette (comme ici) $\rightarrow$ *Tag "Housekeeping/Legal"* dans le canal Telegram interne, sans perturber le trade bot de HULK.
* **Charge pour Hulk :** Nulle. C'est un processus en lecture seule dés Couplage Loosely-Coupled qui pousse un webhook unique si et seulement si un UTXO de >5 ans est consommé.
