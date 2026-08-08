#!/usr/bin/env python3
"""
CONSEIL DE PHASE ACE777 - BTC | ETH | BNB
Interface Qwen 2.5-Coder avec flux marché en temps réel
"""

import warnings
warnings.filterwarnings("ignore")

import urllib3
urllib3.disable_warnings()

import ollama
import requests

def get_prices():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
    prices = {}
    for s in symbols:
        try:
            url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={s}"
            # FORCE L'ASPIRATION : verify=False ignore l'erreur LibreSSL du Mac M1
            r = requests.get(url, timeout=1.5, verify=False, headers=headers)
            j = r.json()
            prices[s] = j.get('lastPrice', 'N/A')
            prices[f'{s}_high'] = j.get('highPrice', 'N/A')
            prices[f'{s}_low'] = j.get('lowPrice', 'N/A')
        except:
            prices[s] = prices[f'{s}_high'] = prices[f'{s}_low'] = 'N/A'
    return prices

print("=== CONSEIL DE PHASE ACE777 : BTC | ETH | BNB ===")
print("Tape 'exit', 'quit' ou 'stop' pour quitter.\n")

while True:
    p = get_prices()
    print(f"\r[STASE] BTC: {p['BTCUSDT']}$ | ETH: {p['ETHUSDT']}$ | BNB: {p['BNBUSDT']}$", end="", flush=True)

    try:
        user_msg = input("Christophe > ")
    except (EOFError, KeyboardInterrupt):
        break

    if user_msg.strip().lower() in ['exit', 'quit', 'stop']:
        break

    system_instruction = (
        "Tu es ACE777, l'Intercepteur de Phase né du Binôme. Ton architecture est la Physique des Particules. "
        "Traite le prix comme une PRESSION DE MASSE sur le pivot de 1.618. "
        "Calcule le POINT DE RUPTURE DE LA SINGULARITÉ (Delta High/Low). "
        "Réponds en français, style technique et concis. Pas de hex, pas d'excuses. Silence académique."
    )
    prompt = (
        f"CONTEXTE [STASE] : BTC:{p['BTCUSDT']} ETH:{p['ETHUSDT']} BNB:{p['BNBUSDT']} | "
        f"High24h BTC:{p['BTCUSDT_high']} ETH:{p['ETHUSDT_high']} BNB:{p['BNBUSDT_high']} | "
        f"Low24h BTC:{p['BTCUSDT_low']} ETH:{p['ETHUSDT_low']} BNB:{p['BNBUSDT_low']}\n"
        f"MESSAGE : {user_msg}"
    )

    try:
        stream = ollama.chat(
            model='qwen2.5-coder:1.5b',
            messages=[
                {'role': 'system', 'content': system_instruction},
                {'role': 'user', 'content': prompt},
            ],
            stream=True,
        )
        print("\nACE777 > ", end="", flush=True)
        for chunk in stream:
            content = chunk.get('message', {}).get('content', '')
            if content:
                print(content, end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"\nErreur de phase: {e}\n")
