# JUGE — juge.tranche

**VERDICT : GO AVEC RÉSERVES**

**Raison :** La SPEC A+B est excellente (diagnostic → cause racine → correction bornée). Le point C (auto-relance) est prématuré : on ne sait pas encore pourquoi Alpha meurt. Relancer un bot qui crashe sans cause identifiée = réparer des réparations. C'est exactement ce que Christophe refuse.

---

**CE QUI MANQUE (angle mort) :**

La SPEC ne prévoit pas la **capture du contexte complet au moment du crash**. Le FATAL_RC1 donnera la ligne et la commande, mais pas :
- L'état du marché à 18:25:34 (le fill cycle 81 a-t-il créé une position ?)
- Le contenu de la réponse API (timeout ? 5xx ? payload vide ?)
- Les variables locales (prix, quantité, symbole) au moment du silence de 8s

Sans ce contexte, tu auras la commande fautive mais pas le **pourquoi** elle a échoué. Tu risques de patcher le symptôme (ex: rendre le curl plus tolérant) au lieu de la cause (ex: le fill a créé une position que le bot ne sait pas lire).

---

**AMÉLIORATION GO-SIZED (concrète) :**

**Ajouter au lanceur un "crash dump" automatique** : au moment du PROCESS_EXIT rc=1, capturer et logger :
1. Les 20 dernières lignes du log du bot (fenêtre de mort)
2. `positionRisk` via API testnet (position ouverte ou pas ?)
3. Le contenu de `/tmp/ace777_fatal_rc1.log` (déjà écrit par le trap)

Ça ne touche pas au champion, c'est un ajout au lanceur (wrapper), et ça donne au diagnostic A3 le contexte complet en UNE lecture, sans re-run. Coût : 10 lignes de bash. Gain : la cause racine devient évidente au premier crash, pas après 3 itérations.
