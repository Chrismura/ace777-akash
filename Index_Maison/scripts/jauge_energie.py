#!/usr/bin/env python3
"""jauge_energie.py — JAUGE LIVE de l'energie du hub (09/08/2026)
Serveur HTTP 0.0.0.0:8898 -> JAUGE_ENERGIE (meta-refresh 30s).
Montre : sante hub, RAM libre, appels du jour, budget cloud restant, par provider.
"""
import json, os, subprocess, datetime, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PRISE = os.path.expanduser('~/prise-ia')
HUB = 'http://127.0.0.1:11435'
PORT = 8898


def usage_today():
    today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    per, total, cloud = {}, 0, 0
    p = os.path.join(PRISE, 'usage.jsonl')
    if os.path.exists(p):
        for line in open(p):
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get('ts', '')[:10] == today:
                total += 1
                k = e.get('provider', '?')
                per[k] = per.get(k, 0) + 1
                if e.get('kind') == 'cloud':
                    cloud += 1
    return total, cloud, per


def ram_mb():
    try:
        out = subprocess.check_output(['vm_stat']).decode()
        free = int([l for l in out.splitlines() if 'Pages free' in l][0].split(':')[1].split('.')[0]) * 4096 // 1048576
        wired = int([l for l in out.splitlines() if 'Pages wired down' in l][0].split(':')[1].split('.')[0]) * 4096 // 1048576
        return free, wired
    except Exception:
        return None, None


def health():
    try:
        d = json.loads(urllib.request.urlopen(HUB + '/health', timeout=4).read())
        return d.get('status') == 'ok', d.get('providers')
    except Exception:
        return False, None


def budget():
    try:
        r = json.load(open(os.path.join(PRISE, 'routing.json')))
        return r.get('cloud_daily_budget')
    except Exception:
        return None


CSS = """body{background:#0d1117;color:#e6edf3;font-family:system-ui,sans-serif;margin:0;padding:24px}
h1{font-size:22px;margin:0 0 4px} .sub{color:#8b949e;font-size:12px;margin-bottom:18px}
.cards{display:flex;gap:14px;flex-wrap:wrap}
.card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:14px 18px;min-width:150px}
.card .v{font-size:26px;font-weight:700} .card .l{color:#8b949e;font-size:11px;text-transform:uppercase;letter-spacing:.5px}
.ok{color:#3fb950} .bad{color:#f85149} .warn{color:#d29922}
.bar{height:8px;background:#21262d;border-radius:4px;margin-top:6px;overflow:hidden}
.bar>div{height:100%;background:#3fb950;border-radius:4px}
.bar.blue>div{background:#58a6ff} .bar.warn>div{background:#d29922} .bar.bad>div{background:#f85149}
table{width:100%;border-collapse:collapse;margin-top:8px;font-size:13px}
td,th{padding:5px 8px;border-bottom:1px solid #21262d;text-align:left}
th{color:#8b949e;font-weight:600}"""


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        total, cloud, per = usage_today()
        ok, nb = health()
        free, wired = ram_mb()
        b = budget()
        max_calls = max(per.values()) if per else 1
        rows = ''.join(
            '<tr><td>%s</td><td>%d</td><td><div class="bar blue"><div style="width:%d%%"></div></div></td></tr>'
            % (k, v, int(100 * v / max_calls)) for k, v in sorted(per.items()))
        body = """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="30"><title>JAUGE ENERGIE — ACE777</title>
<style>%s</style></head><body>
<h1>⚡ JAUGE ÉNERGIE — ACE777</h1>
<div class="sub">mise à jour auto toutes les 30 s · %s</div>
<div class="cards">
<div class="card"><div class="v %s">%s</div><div class="l">Hub (%s providers)</div></div>
<div class="card"><div class="v">%d</div><div class="l">Appels aujourd'hui</div></div>
<div class="card"><div class="v">%d</div><div class="l">Cloud aujourd'hui</div></div>
<div class="card"><div class="v %s">%s Mo</div><div class="l">RAM libre</div></div>
<div class="card"><div class="v">%s</div><div class="l">Budget cloud/jour</div></div>
</div>
<h2 style="font-size:15px;margin-top:22px">Répartition des appels</h2>
<table><tr><th>Provider</th><th>Appels</th><th style="width:40%%">Part</th></tr>%s</table>
</body></html>""" % (CSS, datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%MZ'),
                     'ok' if ok else 'bad', ('OK' if ok else 'NOK'), nb or '?', total, cloud,
                     'ok' if (free or 0) > 300 else 'warn', free or '?', b if b else '∞', rows)
        data = body.encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *a):
        pass


if __name__ == '__main__':
    print('Jauge énergie sur http://0.0.0.0:%d (auto-refresh 30s)' % PORT)
    ThreadingHTTPServer(('0.0.0.0', PORT), H).serve_forever()
