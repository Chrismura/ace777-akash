# Si le Mac coupe / redémarre — que faire ?

Pas de panique. Rien d’important ne doit se relancer tout seul.

## Règle d’or
Ne relance **pas** les bots de trading (ACE, Hulk) tant que tu n’as pas dit clairement « GO ».  
Ne touche **pas** au fichier champion d’ACE.

## 1. Ouvre la boîte à notes
Ouvre **Obsidian**, coffre **Obsidian_ACE777**.  
Va sur **AGORA**, puis **CONSOLE_GENERALE** : c’est le tableau de bord (vert / rouge).

## 2. Remets les notes à jour (Terminal)
Copie-colle ça :
```bash
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```
Tu dois voir `SYNC_VIA_TERMINAL_DONE` — comme tout à l’heure.

Vérifie que rien ne tourne en cachette :
```bash
pgrep -lf 'GO_USINE|paper_diprip|ollama serve' || echo "OK rien qui tourne"
```
Si ça écrit « OK rien qui tourne » → c’est bon.

## 3. Pour reprendre la veille (lire des posts, pas trader)
```bash
cd ~/ace777-test-day1/veille-punk
./bin/suivi "@Compte colle le texte du post"
./bin/speak_attention
```
Si le Mac est chaud / lent : ajoute `--offline` après `suivi`.

## 4. Si Obsidian plante
Ferme Obsidian. Rouvre **un seul** coffre.  
Le code lourd ne doit **pas** être dans Obsidian (il est déjà rangé dehors).

## 5. Dans Cursor
Écris juste : **reprise après coupure**  
On lit la console ensemble, on ne lance rien sans ton GO.

## Ordre normal (rappel)
1. Lire la console  
2. Nourrir la veille (suivi / voix)  
3. **Seulement après**, Mac froid + ton GO : Hulk papier, puis ACE test  
4. Les gros changements Index = plus tard
