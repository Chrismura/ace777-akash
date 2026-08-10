# AVIS ULTRA (task ultra.analyse)

provider: OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte

Let me audit this carefully. I need to check the stop_ace777.sh and COMMANDES_ARRET_ACE777.md against the spec.

First, let me analyze the stop_ace777.sh:

1. **Order of shutdown**: The script stops watchdog FIRST, then superviseur-core, then cockpit-pont, then cockpit-http. ✓ This matches the critical order requirement.

2. **Method**: Uses `launchctl bootout gui/$(id -u)/<label>` for each service. ✓ This is correct for KeepAlive=true services.

3. **Robustness - Non-fatal**: Each service has an if/else block that checks if bootout succeeded, and if not, checks if the service is still in launchctl list to distinguish between "already stopped" vs "bootout failed". ✓ Good.

4. **Safety net for superviseur-core**: After bootout of superviseur-core, it does a `pgrep -f 'superviseur_core\.sh$'` and kill -9 if found. ✓ This matches the spec.

5. **Exit 0 guaranteed**: The script continues through all sections and ends with the existing cleanup code. No explicit `exit 1` anywhere. ✓

6. **No regression on old processes**: The rest of the script (after the 3ETAGES section) is unchanged - it still kills vortex, genesis, master, radar, old Ruby watchdog, etc. ✓

7. **Scheduled services not touched**: The script only touches the 4 specified services. Other launchd services like com.ace777.observatoire, com.ace777.catalogue, com.ace777.gitpush-vault, com.ace777.cortana.horaire, etc. are NOT touched. ✓

Now let me check the COMMANDES_ARRET_ACE777.md:

1. **One-liner**: Has the 4 bootout commands in correct order (watchdog first). ✓

2. **Verification section**: Has the launchctl list grep and pgrep commands. ✓

3. **Restart section**: Has the 4 bootstrap commands. But wait - the order here is: superviseur-core, watchdog, cockpit-pont, cockpit-http. The spec says "ordre de relance" but doesn't specify a critical order for restart. However, logically, superviseur-core should probably be started before watchdog (since watchdog monitors superviseur-core). But actually, since they're KeepAlive, launchd will manage them. The order in the spec example shows superviseur-core first, then watchdog. The doc matches the spec. ✓

4. **Note about reboot**: Present. ✓

Now let me check for any issues:

**Potential issues in stop_ace777.sh:**

1. Line with `SUPERVISEUR_PID=$(pgrep -f 'superviseur_core\.sh$' 2>/dev/null)` - the regex uses `\.sh$` which means it matches processes ending with "superviseur_core.sh". But the process might be running as `bash superviseur_core.sh` or similar. The `pgrep -f` matches the full command line, so this should work. However, note that the spec says `pgrep -f 'superviseur_core\.sh$'` - the script matches this exactly. ✓

2. The kill -9 uses `$SUPERVISEUR_PID` without quotes in `kill -9 $SUPERVISEUR_PID`. If there are multiple PIDs (unlikely for this specific pattern), this could be an issue. But pgrep returns one PID per line, and the variable would contain newlines. Actually, `pgrep` returns multiple PIDs separated by newlines. If assigned to a variable, it would be a string with newlines. `kill -9 $SUPERVISEUR_PID` would then expand to multiple arguments. This is actually fine for kill. But it's safer to quote or use a loop. However, the spec didn't specify this detail, and it's a minor edge case.

3. The script uses `gui/$(id -u)` for the launchctl domain. This is correct for user-level launch agents on macOS.

4. The script does `touch STOP STOP_ALPHA STOP_BETA 2>/dev/null` after the 3ETAGES section. This is part of the original script logic (signaling files for the running processes). Good.

5. The original script had `pkill -9 -f "watchdog_ace777"` which targets the OLD Ruby watchdog. The new watchdog is `com.ace777.watchdog` (launchd service). These are different. The script correctly handles both: the new one via bootout in the 3ETAGES section, the old one via pkill in the legacy section. ✓

**Potential issues in COMMANDES_ARRET_ACE777.md:**

1. The one-liner for old processes uses `kill -9 -$(cat runs/master.pid 2>/dev/null)` - the `-` before the PID means kill the process group. This is correct for the master process group. But note: if master.pid doesn't exist, `cat` returns empty, so `kill -9 -` would be invalid. However, the `2>/dev/null` on cat and the overall `2>/dev/null` on kill would suppress errors. Actually, `kill -9 -` with no PID argument would be a syntax error. Let me check: `kill -9 -$(cat runs/master.pid 2>/dev/null)` - if the file doesn't exist, cat outputs nothing, so it becomes `kill -9 -` which is invalid. But the original script had this same pattern, so it's not a regression. The spec says "NE PAS toucher au reste du script" and "On AJOUTE, on ne remplace pas." So this pre-existing issue is out of scope.

2. The restart section order: superviseur-core, watchdog, cockpit-pont, cockpit-http. This seems logical (start the core first, then the watchdog that monitors it). The spec example shows this exact order. ✓

3. The verification section uses `launchctl list | grep -E 'superviseur-core|watchdog|cockpit-pont|cockpit-http'` - but the service labels are `com.ace777.superviseur-core`, etc. `launchctl list` shows the label without the `com.ace777.` prefix? Actually, `launchctl list` shows the full label. Let me verify: on macOS, `launchctl list` shows the service name as registered. If the plist has `Label` = `com.ace777.superviseur-core`, then `launchctl list` will show `com.ace777.superviseur-core`. The grep pattern `'superviseur-core|watchdog|cockpit-pont|cockpit-http'` would match because these substrings are in the full labels. So this works. ✓

4. The verification also does `pgrep -f 'superviseur_core\.sh$'` - matches the script name. Good.

**One concern**: In the stop_ace777.sh, the 3ETAGES section is added at the TOP of the script, before the `touch STOP STOP_ALPHA STOP_BETA` and before the legacy kills. This is correct per spec: "au tout début du script (avant les kills des anciens processus)".

**Another concern**: The script does `cd /Users/christophe/ace777-test-day1` at the top. The 3ETAGES section uses `launchctl bootout gui/$(id -u)/...` which doesn't depend on the current directory. Good.

**Exit code**: The script doesn't have an explicit `exit 0` at the end, but bash scripts exit with the status of the last command. The last commands are `./scripts/post_stop_cleanup.sh` (if executable) or the echo "Arrêté." and the state update scripts. Since these are all followed by `|| true`, the script should exit 0. The spec says "exit 0 garanti" - this is satisfied by the `|| true` pattern on the final commands.

**Wait**: The spec says "Le script doit TOUJOURS se terminer proprement (exit 0 même si tout était déjà arrêté)." The current script ends with:
```bash
if [ -x ./scripts/post_stop_cleanup.sh ]; then
  ./scripts/post_stop_cleanup.sh
fi
```
No `|| true` on the if block itself, but the script would exit with the status of the last command executed. If `post_stop_cleanup.sh` fails, the script would exit with non-zero. However, this is pre-existing behavior, not introduced by the 3ETAGES addition. The spec says not to touch the rest. So this is out of scope.

Actually, looking more carefully at the original script provided in the spec context, the ending was:
```bash
echo "Arrêté."

export STATE_PHASE="stopped"
./scripts/update_state_md.sh 2>/dev/null || true
./scripts/post_run_report.sh 2>/dev/null || true

if [ -x ./scripts/post_stop_cleanup.sh ]; then
  ./scripts/post_stop_cleanup.sh
fi
```
The last command could be `post_stop_cleanup.sh` without `|| true`. But again, this is pre-existing.

**Verdict**: The implementation looks solid. It follows the spec correctly:
- Correct order (watchdog first)
- Correct method (bootout)
- Non-fatal handling with informative messages
- Safety net kill for superviseur_core.sh
- No regression on legacy processes
- Scheduled services untouched
- Documentation accurate and complete

I'll give **GO** with maybe a minor reserve about the `kill -9 $SUPERVISEUR_PID` unquoted variable (could handle multiple PIDs better), but that's a very minor edge case and the spec didn't require handling multiple PIDs.

Actually, let me re-read the spec for the safety net: "si un processus traîne encore, kill -9 de ce PID (filet de sécurité, non fatal)." It says "ce PID" (singular), implying at most one. The pgrep pattern is specific enough that multiple matches are unlikely. So this is fine.

One more thing: In the stop_ace777.sh, the watchdog check does:
```bash
if launchctl bootout gui/$(id -u)/com.ace777.watchdog 2>/dev/null; then
    echo "[3ETAGES] com.ace777.watchdog arrete"
else
    if launchctl list | grep -q "com.ace777.watchdog"; then
        echo "[3ETAGES] com.ace777.watchdog WARN bootout echoue"
    else
        echo "[3ETAGES] com.ace777.watchdog absent (deja arrete)"
    fi
fi
```
This is good - it distinguishes between "bootout failed but service still registered" vs "service not registered (already stopped)".

Same pattern for all 4 services. ✓

The COMMANDES_ARRET_ACE777.md one-liner for the 3ETAGES section:
```bash
launchctl bootout gui/$(id -u)/com.ace777.watchdog 2>/dev/null
launchctl bootout gui/$(id -u
