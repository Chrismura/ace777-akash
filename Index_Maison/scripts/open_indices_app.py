#!/usr/bin/env python3
"""Ouvre l'app des Indices ACE777 dans une fenêtre native pywebview."""
import subprocess, sys, time

try:
    import webview
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pywebview", "-q"])
    import webview

URL = "http://127.0.0.1:17800/cockpit/indices.html"

time.sleep(1)
webview.create_window(
    "ACE777 INDICES",
    URL,
    width=1100,
    height=750,
    background_color="#050804",
)
webview.start(debug=False)
