# Note — Ghost fills (0x_Punisher)

**Post :** https://x.com/0x_Punisher/status/2081362888397070432  
**Éval :** [[Evaluations/14_punisher_ghost_fills]]

## L’idée (vulgarisé)
L’API peut dire « ordre matched » alors que la chaîne (ou le fill réel) n’a rien confirmé.  
Si tu comptabilises quand même → **position fantôme**.  
Solution : timeout + vérifier la vérité on-chain/CSV ; sinon `mark_phantom` et on retire.

**Suite frais :** ce n’est pas du goût — fee **en courbe** (grosse au milieu, petite aux extrêmes). Sweeper à 0.99 = zone peu taxée ; descendre à 0.90 ≠ même trade. Taille mini = **fees+gas**, pas la confiance. Latence : mur ~ms, pas µs.

## Pour nous
Renforce **S1** + **S11** + **S12**.  
PnL $32k = bruit. Pattern fills + courbe fees = or.
