#!/bin/bash
cd /Users/christophe/ace777-test-day1
/usr/bin/python3 Index_Maison/scripts/cortana_mute.py off
osascript -e 'display notification "Cortana réactivée" with title "ACE777"' 2>/dev/null || true
