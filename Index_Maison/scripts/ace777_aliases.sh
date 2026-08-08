# ACE777 — source une fois dans ~/.zshrc :
#   source ~/ace777-test-day1/Index_Maison/scripts/ace777_aliases.sh
export PATH="$HOME/bin:$PATH"
# binaires déjà dans ~/bin ; alias = raccourci équivalent
alias memoire='python3 ~/ace777-test-day1/Index_Maison/scripts/memoire_log.py'
alias molette='python3 ~/ace777-test-day1/Index_Maison/scripts/molette_log.py'
alias session-debut='bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh'
alias session-fin='bash ~/ace777-test-day1/Index_Maison/scripts/session_fin.sh'
alias sync-obsidian='bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh'

# Ada — lancement de la session (chef d'orchestre) : prepa infra + Freebuff
alias ada='bash ~/Documents/Obsidian_ACE777/scripts/ada.command'
alias cherche-code="bash ~/ace777-test-day1/Index_Maison/scripts/cherche_code.sh"
