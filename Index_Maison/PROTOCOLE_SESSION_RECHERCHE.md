# Protocole — session recherche / intérêts (plein régime)

**But :** dès qu’un agent **recherche** (tweet, compte, lien, idée), il **écrit l’Index tout seul** à chaque validation — tu ne redis pas « mets à jour Obsidian ».  
**Pas pour :** GO ACE/Hulk, purge, champion.

---

## Qui fait quoi (2 fenêtres)

| Fenêtre | Rôle | Attitude |
|---------|------|----------|
| **ACTIF** (recherche / sniff / comptes) | Cold path | **Plein régime** — checklist ci-dessous **sans redemander** |
| **PASSIF** (ops / vol en cours) | Hot path | Répond si ping (« check », GO) — **ne pirate pas** la recherche, n’invente pas d’évals |

Un seul agent **écrit** l’Index à la fois. Si doute → demander « qui est ACTIF ? ».

---

## Déclencheur = validation (pas un 2ᵉ GO)

Dès que Christophe (ou l’agent avec son OK) dit en substance :
- pertinent / à garder / oui ajoute / suivi / intéressant / Soft OK / WATCH OK  
→ **c’est le GO d’écrire**. Pas attendre « update Obsidian ».

`LU_PARTIEL` / titre seul / paywall → **ne pas** ajouter au suivi compte.

---

## Checklist ACTIF (à chaque validation) — stacking

Faire **dans la même réponse / même session** :

1. **Verdict** clair : `PERTINENT` · `SOFT` · `WATCH` · `REFUS` · `IGNORER`
2. **Éval** `Evaluations/NN_….md` si PERTINENT|SOFT|WATCH utile (ID Index)
3. **Tableau / BRIEF** : ligne ou MAJ si ça change la carte ([[01_TABLEAU_VIVANT]] · [[BRIEF_IA_SNIFF]])
4. **Thermo ?** si météo / book / levier / vide / tension → ligne **C…** dans tableau + `00_INDICATEURS` (hygiène au fil de l’eau)
5. **Compte** validé → [[Suivi_Info/COMPTES]] + `COMPTE_LIENS` Punk si applicable ([[PREFS_STACK]])
6. **Attention** → note courte `A_Mon_Attention/` + index si besoin
7. **Mémoire** → 1 ligne `MEMOIRE_COLLAB` (Cursor ★ / +)
8. **OUTBOX** → copier les fichiers touchés sous `Index_Maison/OUTBOX_OBSIDIAN/`
9. **Sync** → rappeler ou lancer (Terminal) :  
   `bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh`

**Ne pas** : relancer ACE/Hulk, Ollama lourd, cron LLM, « on fera le fichier plus tard ».

---

## Checklist lecture (avant de conclure)

- [[PROTOCOLE_LIENS]] — lien ≠ lu complet (`LU_COMPLET` / `LU_PARTIEL` / `BLOQUÉ`)
- [[BRIEF_IA_SNIFF]] — axes sniff
- [[VALEUR_INFORMATION]] — A (économie) · B ($) avant de garder
- [[PROTOCOLE_CONTRA_SOFT]] — si « contra » sans preuve

---

## Prompt coller — agent ACTIF (recherche)

```
Mode ACTIF recherche. Lis Index_Maison/PROTOCOLE_SESSION_RECHERCHE.md + BRIEF_IA_SNIFF.md.
Réponds FR, concis. Pas de GO trading.
À CHAQUE validation (pertinent/garder/suivi) : exécute la checklist (éval + tableau/BRIEF + COMPTES si compte + Attention + MEMOIRE + OUTBOX) SANS redemander « je mets à jour Obsidian ? ».
Sujet : […]
```

## Prompt coller — agent PASSIF (ops / autre fenêtre)

```
Mode PASSIF. Vol ACE/Hulk éventuellement ON — ne touche pas aux process.
Tu ne fais PAS la recherche Index (évals, comptes, Attention) sauf si Christophe dit « GO recherche ici ».
Tu réponds seulement aux pings ops : check, RAM, statut run, GO explicite.
Sinon : une ligne « PASSIF — ping si besoin ».
```

---

## Lien registre

Voir [[AUTO_PROCESSUS]] couche B (garage cold).  
Ce protocole = **comportement agent**, pas un LaunchAgent.
