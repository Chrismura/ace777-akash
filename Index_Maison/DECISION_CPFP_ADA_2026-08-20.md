# DÉCISION — CPFP / ADA (due 23/08) — preuves réunies le 20/08

**Rappel du verdict famille (16/08) :** OBSERVER jusqu'au 23/08 : CPFP + ADA — **sinon jetés**.

## Preuves réunies (20/08, après l'événement marché du 19-20/08 : BTC +8 % en 24 h)

### CPFP / "blocs privatisés" — 🔧 À RÉPARER (mesure), PAS à jeter (concept validé)

- **Enquête poussière révisée (20/08, 2ᵉ passe)** : le concept de Christophe est
  réel (tx jamais vues dans la mempool publique = OTC privée / CPFP masqué, matrice
  du Juge 35 %/1000 BTC). Le problème était la **résolution de mesure** : snapshot
  toutes les 10 min vs durée de vie des tx < 10 min → les tx normales à turnover
  rapide étaient faussement "fantômes".
- **Test live décisif (20/08)** : même bloc → 33,6 % de fantômes à 10 min vs
  **8,3 % à 60 s** ; avec historique dense, les blocs donnent 0,5-8,3 % (médiane
  4,7 %). Le résidu dense = candidat réel de tx privées.
- 281/281 blocs stables intra-run → PAS du bruit blanc (mon 1ᵉʳ verdict était faux).
- **Verdict révisé : réparer la mesure (snapshot 60-120 s, exclure carnet vide),
  recalibrer la matrice du Juge sur le taux résiduel, puis activer.** Ne pas jeter
  la pépite Christophe.

### ADA (gardienne de voilure) — ❌ RÉACTIVE, pas prédictive → JETER comme prédicteur

- Historique `ada_gardienne_historique.jsonl` **réinitialisé** : commence le 20/08 08:38, 60 lignes.
- Avant et pendant le +8 % (19/08 06h → 20/08 06h) : **zéro signal**. Le journal radar s'arrête au 19/08 12:10 UTC (vigie morte, cf. n°4).
- Après la perte (−44,44) : hurle `PRENDS_LA_PERTE` / sirène en boucle → **elle constate, elle ne prédit pas**.
- Calibration : 44,4 % (43 analyses) — médiocre.
- **Verdict :** jeter comme prédicteur. **Option de repli :** la garder comme *réacteur de sortie* (constater la perte et couper) — mais ce rôle est déjà couvert par le disjoncteur.

## Recommandation pour le 23/08

1. **CPFP : JETER** — mesure invalidée par l'enquête (artefact d'échantillonnage).
2. **ADA : JETER comme prédicteur** — aucune valeur prédictive démontrée sur l'événement test.
3. **Ce qui a vraiment manqué le 19-20/08 : la vigie morte** (pas un indicateur, une panne d'infra) → corrigée le 20/08 (plist rechargée, journal radar actif).
4. **Le seul garde-fou utile ajouté :** mode "macro tempête" (`detecteur_macro_tempete.py` + `radar_gate.rb`) — bloque les SELL/BUY contre-choc, actif depuis le 20/08.

## Décision à entériner le 23/08 (GO Christophe requis)
- [ ] Jeter CPFP (désactiver la plist `com.ace777.cpfp`)
- [ ] Jeter ADA comme prédicteur (ou garder en réacteur de sortie — choix)
- [ ] Garder le mode macro tempête en observation
