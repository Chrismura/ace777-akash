#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# Compat legacy: redirige vers V8.5 IMPACT
exec ./launch_test_master_base_v8_5_impact.sh
