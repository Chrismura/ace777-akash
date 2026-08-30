# AVIS CODEUR (provider Google Gemini)

**1. VERDICT**
**GO AVEC RÉSERVES TRÈS STRICTES.** 
Raison : Le pattern intraday (creux 15h UTC / pic 01h-05h) est mathématiquement exploitable et s'aligne sur le cycle de liquidité de l'actif, mais l'échantillon de 3 jours est statistiquement insuffisant pour fonder une exécution aveugle.

---

**2. LES ANGLES MORTS**
* **Fragilité du carnet d'ordres (Mur 45k$) :** Sur une market cap de 44M$ et un token ultra-volatile (dd15 à 22%), un mur de 45 240$ peut s'évaporer en une seule impulsion de marché global (BTC/ETH dump). S'y fier comme d'un ancrage absolu à 15h est un piège à liquidité (fakeout).
* **Frais et slippage vs Amplitude :** L'écart jour/nuit est de ~2,4-2,8%. Si les frais de taker/maker sur MEXC et le slippage inhérent à la volatilité 15 min mangent plus de 1% par aller-retour, la marge nette fond de moitié.
* **Extrapolation à 15 paires :** Vouloir répliquer ce "creux horaire" sur 15 paires sans corrélation macro est une hérésie technique. Chaque token a sa propre structure de carnet dictée par son teneur de marché (MM).

---

**3. PROPOSITION D'AMÉLIORATION (Alternative / Architecture)**

*Ne te contente pas de corriger : voici ce qu'il faut implémenter.*

Plutôt qu'un **déclenchement purement horaire** (ex: *acheter à 15h00 UTC parce que le JSONL le dit*), je propose d'implémenter un **State Machine Hybride "Time + Order Book Depth"** dans Hulk :

1. **La Fenêtre Temporelle (Filtre d'opportunité) :** Laisser Hulk surveiller activement la paire **uniquement** entre 14h00 et 17h00 UTC (interdiction d'entrer en dehors, réduisant l'exposition au bruit).
2. **Le Déclencheur Réel (Confirmation technique) :** L'ordre d'achat ne part *que si* le prix touche la zone psychologique/technique **ET** que la "poussière" (tx fantômes) baisse sous un seuil critique, combinée à une annulation de l'aplatissement du mur bid (preuve que le MM absorbe la vente sans fuir).
3. **Le Garde-fou Multi-paires :** Valider ce pattern sur les 14 autres paires non pas par mimétisme horaire, mais en calculant dynamiquement l'*Heure du Creux Local (HCL)* via une moyenne glissante sur 7 jours pour chaque token, plutôt de figer 15h-16h UTC.
