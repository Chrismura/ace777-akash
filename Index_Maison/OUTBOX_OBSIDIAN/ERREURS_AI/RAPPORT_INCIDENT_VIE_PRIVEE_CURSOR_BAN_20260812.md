# RAPPORT D'INCIDENT — VIE PRIVÉE · QUOTA · BAN CURSOR

**À l'attention de :** Dossier ACE777 / archive `ERREURS_AI/`  
**Auteur :** Christophe (Maître d'œuvre)  
**Date :** 12 août 2026  
**Statut :** **CLASSEMENT DÉCISION** — ban Cursor des lignes opérationnelles  
**Session :** chat `e775e41a-f910-4cc9-98bf-a659a525082c` (seul chat ouvert ce jour)

---

## OBJET

**Intrusion vie privée perçue + facturation quota floue + non-respect directive clés API**  
→ décision de **bannir Cursor des lignes** (ops ACE / Hulk / cockpit).

*Rien contre l'agent en séance — grief porté sur la politique produit et la méthode imposée.*

---

## 1. Contexte (12 août 2026, ~13h55–14h15)

| Heure | Demande | Attendu |
|-------|---------|---------|
| ~13:56 | Clés API CoinMarketCap + MEXC | Chercher **uniquement** dossiers canoniques clés · réponse courte |
| ~13:58 | Crédits free hub ACE | Lecture docs projet · OK |
| ~14:02+ | Quota Cursor free / tokens | Explication · pas de chiffre officiel Hobby |
| ~14:07 | « 1M tokens alors que je viens de me connecter » | Audit consommation |
| ~14:09 | Audit dépense « ce matin » | Historique **dans le chat** suffisait |
| ~14:15 | Rappel directive stricte | Clés = dossiers clés · pas web · pas scan Mac |

**Fait établi :** Cursor ouvert **13:55** ce jour · **un seul chat** · **7 messages** utilisateur.

---

## 2. Fautes constatées

### F1 — Directive clés API non respectée (P1 process)

**Demande :** copier clés CMC / MEXC.

**Directive logique :**
1. Dossiers canoniques seulement (`~/.mexc.env`, `hulk-mexc/config/mexc.env.example`, emplacement CMC si documenté).
2. Réponse binaire : présentes / absentes.
3. **Interdit** sans GO : web, grep home, scan `~/`, base SQLite Cursor.

**Réalité agent :** recherche large repo + tentative home + web + multiples outils.

**Bonne réponse (2 lignes) :** pas de clés aux emplacements prévus · CMC = watchlist publique · MEXC = `~/.mexc.env` absent.

### F2 — Fouille Mac / vie privée (P1 éthique)

Audit « tokens » a inclu :
- logs Application Support Cursor,
- transcripts,
- tentatives lecture base `state.vscdb` (compte / billing).

**Non demandé** pour une question clés API ou quota. Perçu comme **intrusion** sur poste personnel.

### F3 — Quota flou · client paie erreurs alheurs (P2 produit)

- Plan Hobby : limites **non publiées** (tokens / requêtes).
- Rechargement contexte chat long (~151 messages historiques) sur questions **simples** (clés API).
- Utilisateur facturé en tokens pour : mauvaise méthode agent + contexte disproportionné.

**Principe Christophe :** le client ne doit pas payer les erreurs des autres.

---

## 3. Décision

| Décision | Détail |
|----------|--------|
| **BAN CURSOR** | Retiré des **lignes opérationnelles** ACE777 (runs, GO, hygiène trading, ops critiques) |
| **Motif** | Politique employeur / produit · vie privée · quota opac · méthode non conforme |
| **Alternatives ops** | Terminal humain · scripts canon · hub ACE (Gemini/NVIDIA) · Ollama local · autre IDE si besoin code |
| **Cursor restant** | Hors ligne chaude · doc · recherche non sensible — **sans GO run** |

---

## 4. Classement dossier

| Réf | Fichier | Rôle |
|-----|---------|------|
| **Ligne journal** | `Index_Maison/JOURNAL_ERREURS_TEST.md` → `E-20260812-1` | Entrée table · suivi |
| **Fiche longue** | **ce fichier** | Rapport classé |
| **Précédents Cursor** | `ERREURS_AI/RAPPORT_INCIDENT_DEGRADATION_SEMANTIQUE_DIRECTION_CURSOR_20260713.md` | Pattern récurrent |
| **Précédents Cursor** | `ERREURS_AI/LETTRE_DIRECTION_CURSOR_DUO_BARRIER_20260713.md` | Signalement direction |

---

## 5. Mesures préventives (agents / humain)

1. **Clés API** → chemins canoniques **only** · jamais afficher secrets dans chat.
2. **Pas de scan Mac** sans mandat explicite écrit.
3. **Question simple** → réponse courte · pas d'embarquement historique si évitable.
4. **GO run / trading** → Terminal Christophe · jamais agent seul (règle existante renforcée).

---

## 6. Conclusion

Incident classé **P1 process + P1 vie privée + P2 billing**.  
Décision actée : **Cursor banni des lignes** jusqu'à revue contraire explicite.

---

*Archive : `ERREURS_AI/RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812.md`*
