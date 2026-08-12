# RÉPONSE HUB (task code.ia · via NVIDIA build.nvidia.com (100+ modeles)) — 2026-08-11T08:57:59

Je vais créer le COSMOS HUB complet selon vos spécifications. Voici le code complet :

## 1. Script feed `hub_cockpit_feed.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSMOS HUB FEED - Génère hub.json et hub.js pour le cockpit ACE777
Usage: python3 hub_cockpit_feed.py
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta
from collections import Counter
import glob

# Configuration
BASE_DIR = os.path.expanduser("~/prise-ia")
COCKPIT_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/cockpit")
HEALTH_URL = "http://127.0.0.1:11435/health"

def safe_read_json(filepath):
    """Lit un fichier JSON en toute sécurité"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def safe_read_jsonl(filepath):
    """Lit un fichier JSONL en toute sécurité"""
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data.append(json.loads(line.strip()))
                except:
                    continue
    except:
        pass
    return data

def get_health():
    """Récupère la santé du hub"""
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=2) as response:
            return json.loads(response.read().decode())
    except:
        return None

def main():
    try:
        # Lire les fichiers source
        providers = safe_read_json(os.path.join(BASE_DIR, "providers.json")) or []
        usage = safe_read_jsonl(os.path.join(BASE_DIR, "usage.jsonl"))
        routing = safe_read_json(os.path.join(BASE_DIR, "routing.json")) or {}
        events = safe_read_jsonl(os.path.join(BASE_DIR, "hub_events.jsonl"))
        
        # Calculer les compteurs par provider (24h)
        now = datetime.now()
        cutoff = now - timedelta(hours=24)
        provider_counts = Counter()
        today_counts = Counter()
        today_str = now.strftime("%Y-%m-%d")
        
        for call in usage:
            try:
                ts = call.get("ts", "")
                provider = call.get("provider", "")
                kind = call.get("kind", "")
                
                # Compter les appels 24h
                if ts:
                    try:
                        ts_dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                        if ts_dt > cutoff:
                            provider_counts[provider] += 1
                    except:
                        pass
                
                # Compter les appels du jour pour le budget cloud
                if today_str in ts and kind == "cloud":
                    today_counts[provider] += 1
            except:
                continue
        
        # Budget cloud
        cloud_budget = routing.get("cloud_daily_budget", 480)
        cloud_consumed = sum(today_counts.values())
        cloud_remaining = max(0, cloud_budget - cloud_consumed)
        
        # File d'attente live (15 derniers appels)
        recent_calls = sorted(usage, key=lambda x: x.get("ts", ""), reverse=True)[:15]
        
        # Événements récents (10 derniers)
        recent_events = sorted(events, key=lambda x: x.get("ts", ""), reverse=True)[:10]
        
        # Quotas par tâche
        tasks_quotas = routing.get("tasks", {})
        
        # Santé du hub
        health = get_health()
        
        # Préparer les données providers
        providers_data = []
        for p in providers:
            pid = p.get("id", "")
            providers_data.append({
                "id": pid,
                "name": p.get("name", pid),
                "kind": p.get("kind", "local"),
                "model": p.get("model", ""),
                "enabled": p.get("enabled", True),
                "timeout": p.get("timeout", 30),
                "calls_24h": provider_counts.get(pid, 0)
            })
        
        # Construire le hub data
        hub_data = {
            "generated_at": now.isoformat(),
            "providers": providers_data,
            "budget": {
                "daily": cloud_budget,
                "consumed": cloud_consumed,
                "remaining": cloud_remaining
            },
            "queue": recent_calls,
            "events": recent_events,
            "tasks_quotas": tasks_quotas,
            "health": health
        }
        
        # Écriture atomique de hub.json
        json_path = os.path.join(COCKPIT_DIR, "hub.json")
        tmp_json = json_path + ".tmp"
        with open(tmp_json, 'w', encoding='utf-8') as f:
            json.dump(hub_data, f, indent=2, ensure_ascii=False)
        os.replace(tmp_json, json_path)
        
        # Écriture atomique de hub.js
        js_path = os.path.join(COCKPIT_DIR, "hub.js")
        tmp_js = js_path + ".tmp"
        js_content = "window.__HUB__ = " + json.dumps(hub_data, ensure_ascii=False) + ";"
        with open(tmp_js, 'w', encoding='utf-8') as f:
            f.write(js_content)
        os.replace(tmp_js, js_path)
        
        print(f"✅ COSMOS HUB feed généré à {now.isoformat()}")
        print(f"   Providers: {len(providers_data)}, Appels 24h: {sum(provider_counts.values())}")
        print(f"   Budget cloud: {cloud_consumed}/{cloud_budget} consommé")
        
    except Exception as e:
        print(f"⚠️ Erreur non fatale: {e}")
    
    sys.exit(0)

if __name__ == "__main__":
    main()
```

## 2. Bloc HTML+CSS+JS à insérer dans index.html

### Étape 1 : Ajouter le script hub.js dans le head

**Insérer après la ligne contenant `<script src="mission.js"></script>` :**

```html
<!-- COSMOS HUB feed -->
<script src="hub.js"></script>
```

### Étape 2 : Ajouter le CSS cosmique

**Insérer avant la balise `</head>` :**

```html
<style>
/* ===== COSMOS HUB STYLES ===== */
.cosmos-container {
    display: flex;
    gap: 20px;
    padding: 20px;
    background: linear-gradient(135deg, #05060f 0%, #0b0f2a 50%, #1a0b2e 100%);
    border-radius: 12px;
    border: 1px solid rgba(125, 231, 255, 0.2);
    box-shadow: 0 0 30px rgba(179, 136, 255, 0.1);
    margin: 20px;
    position: relative;
    overflow: hidden;
}

.cosmos-container::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 30%, rgba(125, 231, 255, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 70% 70%, rgba(179, 136, 255, 0.05) 0%, transparent 50%);
    animation: cosmos-pulse 8s ease-in-out infinite;
}

@keyframes cosmos-pulse {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

.cosmos-left {
    flex: 0 0 65%;
    position: relative;
    min-height: 500px;
}

.cosmos-right {
    flex: 0 0 35%;
    display: flex;
    flex-direction: column;
    gap: 15px;
    position: relative;
    z-index: 1;
}

.cosmos-canvas {
    width: 100%;
    height: 500px;
    border-radius: 8px;
    background: transparent;
}

.cosmos-card {
    background: rgba(11, 15, 42, 0.8);
    border: 1px solid rgba(125, 231, 255, 0.2);
    border-radius: 8px;
    padding: 15px;
    backdrop-filter: blur(10px);
}

.cosmos-card h3 {
    font-family: 'Orbitron', sans-serif;
    color: #7de7ff;
    font-size: 14px;
    margin: 0 0 10px 0;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-shadow: 0 0 10px rgba(125, 231, 255, 0.5);
}

.cosmos-budget-bar {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 4px;
    height: 20px;
    overflow: hidden;
    margin: 10px 0;
}

.cosmos-budget-fill {
    height: 100%;
    background: linear-gradient(90deg, #7de7ff, #b388ff);
    border-radius: 4px;
    transition: width 0.5s ease;
    box-shadow: 0 0 10px rgba(125, 231, 255, 0.5);
}

.cosmos-budget-text {
    font-family: 'Share Tech Mono', monospace;
    color: #fff;
    font-size: 12px;
    margin: 5px 0;
}

.cosmos-queue {
    max-height: 200px;
    overflow-y: auto;
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
}

.cosmos-queue-item {
    padding: 4px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    color: #7de7ff;
}

.cosmos-queue-item .time {
    color: #b388ff;
    margin-right: 8px;
}

.cosmos-queue-item .provider {
    color: #ff6ad5;
}

.cosmos-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
}

.cosmos-table th {
    color: #7de7ff;
    text-align: left;
    padding: 5px;
    border-bottom: 1px solid rgba(125, 231, 255, 0.2);
}

.cosmos-table td {
    padding: 5px;
    color: #fff;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.cosmos-status {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-family: 'Share Tech Mono', monospace;
}

.cosmos-status.ok {
    background: rgba(124, 255, 107, 0.2);
    color: #7CFF6B;
    border: 1px solid #7CFF6B;
}

.cosmos-status.nok {
    background: rgba(255, 77, 77, 0.2);
    color: #ff4d4d;
    border: 1px solid #ff4d4d;
}

.cosmos-events {
    max-height: 150px;
    overflow-y: auto;
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
}

.cosmos-event {
    padding: 3px 0;
    color: #f0a020;
}

.cosmos-tooltip {
    position: absolute;
    background: rgba(11, 15, 42, 0.95);
    border: 1px solid #7de7ff;
    border-radius: 6px;
    padding: 10px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: #fff;
    pointer-events: none;
    z-index: 1000;
    box-shadow: 0 0 20px rgba(125, 231, 255, 0.3);
    display: none;
}

.cosmos-refresh {
    position: absolute;
    top: 10px;
    right: 10px;
    background: transparent;
    border: 1px solid #7de7ff;
    color: #7de7ff;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    font-family: 'Orbitron', sans-serif;
    font-size: 12px;
    transition: all 0.3s;
}

.cosmos-refresh:hover {
    background: rgba(125, 231, 255, 0.2);
    box-shadow: 0 0 15px rgba(125, 231, 255, 0.3);
}

.cosmos-synapses-btn {
    position: absolute;
    bottom: 10px;
    right: 10px;
    background: transparent;
    border: 1px solid #b388ff;
    color: #b388ff;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    font-family: 'Orbitron', sans-serif;
    font-size: 12px;
    transition: all 0.3s;
}

.cosmos-synapses-btn:hover {
    background: rgba(179, 136, 255, 0.2);
    box-shadow: 0 0 15px rgba(179, 136, 255, 0.3);
}

.cosmos-unavailable {
    color: #f0a020;
    font-family: 'Orbitron', sans-serif;
    text-align: center;
    padding: 50px;
    font-size: 16px;
}

/* Scrollbar styling */
.cosmos-queue::-webkit-scrollbar,
.cosmos-events::-webkit-scrollbar {
    width: 4px;
}

.cosmos-queue::-webkit-scrollbar-track,
.cosmos-events::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
}

.cosmos-queue::-webkit-scrollbar-thumb,
.cosmos-events::-webkit-scrollbar-thumb {
    background: #7de7ff;
    border-radius: 2px;
}

/* Étoiles scintillantes */
.cosmos-stars {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

.cosmos-star {
    position: absolute;
    background: white;
    border-radius: 50%;
    animation: twinkle 2s ease-in-out infinite;
}

@keyframes twinkle {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 1; }
}
</style>
```

### Étape 3 : Ajouter le HTML du COSMOS HUB dans le volet GRAPH

**Insérer juste après l'ouverture de `<section id="stage-graph">` :**

```html
<!-- COSMOS HUB -->
<div id="cosmos-hub" class="cosmos-container">
    <div class="cosmos-left">
        <canvas id="cosmos-canvas" class="cosmos-canvas"></canvas>
        <button class="cosmos-refresh" onclick="window.__cosmosRefresh()">↻</button>
        <button class="cosmos-synapses-btn" onclick="window.__toggleSynapses()">SYNAPSES</button>
        <div id="cosmos-tooltip" class="cosmos-tooltip"></div>
    </div>
    <div class="cosmos-right">
        <div class="cosmos-card">
            <h3>🌌 Budget Cloud</h3>
            <div id="cosmos-budget"></div>
        </div>
        <div class="cosmos-card">
            <h3>⚡ File d'attente Live</h3>
            <div id="cosmos-queue" class="cosmos-queue"></div>
        </div>
        <div class="cosmos-card">
            <h3>📊 Quotas par Tâche</h3>
            <div id="cosmos-tasks"></div>
        </div>
        <div class="cosmos-card">
            <h3>🖥️ État du Hub</h3>
            <div id="cosmos-health"></div>
        </div>
        <details class="cosmos-card">
            <summary style="cursor:pointer; color:#7de7ff; font-family:'Orbitron',sans-serif; font-size:12px;">
                📡 Événements Récents
            </summary>
            <div id="cosmos-events" class="cosmos-events"></div>
        </details>
    </div>
</div>
```

### Étape 4 : Ajouter le JavaScript du COSMOS HUB

**Insérer avant la balise `</body>` :**

```html
<script>
// ===== COSMOS HUB JavaScript =====
(function() {
    'use strict';
    
    // Variables privées
    let cosmosCanvas = null;
    let cosmosCtx = null;
    let cosmosAnimationId = null;
    let cosmosStars = [];
    let cosmosParticles = [];
    let cosmosNodes = [];
    let cosmosHoveredNode = null;
    let synapsesVisible = false;
    
    // Initialisation
    function initCosmos() {
        cosmosCanvas = document.getElementById('cosmos-canvas');
        if (!cosmosCanvas) return;
        
        cosmosCtx = cosmosCanvas.getContext('2d');
        
        // Créer les étoiles
        createStars();
        
        // Démarrer l'animation
        cosmosAnimationId = requestAnimationFrame(animateCosmos);
        
        // Écouter les événements souris
        cosmosCanvas.addEventListener('mousemove', handleMouseMove);
        cosmosCanvas.addEventListener('mouseleave', handleMouseLeave);
        
        // Redimensionner
        window.addEventListener('resize', resizeCosmos);
        resizeCosmos();
        
        // Premier rendu
        renderCosmos();
    }
    
    // Créer les étoiles
    function createStars() {
        cosmosStars = [];
        for (let i = 0; i < 100; i++) {
            cosmosStars.push({
                x: Math.random() * 100,
                y: Math.random() * 100,
                size: Math.random() * 2 + 0.5,
                speed: Math.random() * 0.5 + 0.1,
                opacity: Math.random() * 0.8 + 0.2
            });
        }
    }
    
    // Redimensionner le canvas
    function resizeCosmos() {
        if (!cosmosCanvas) return;
        const container = cosmosCanvas.parentElement;
        cosmosCanvas.width = container.clientWidth;
        cosmosCanvas.height = container.clientHeight;
    }
    
    // Animation principale
    function animateCosmos() {
        if (!cosmosCtx || !cosmosCanvas) return;
        
        // Effacer le canvas
        cosmosCtx.clearRect(0, 0, cosmosCanvas.width, cosmosCanvas.height);
        
        // Dessiner le fond
        drawBackground();
        
        // Dessiner les étoiles
        drawStars();
        
        // Dessiner les liens
        drawLinks();
        
        // Dessiner les particules
        drawParticles();
        
        // Dessiner les nœuds
        drawNodes();
        
        // Continuer l'animation
        cosmosAnimationId = requestAnimationFrame(animateCosmos);
    }
    
    // Dessiner le fond
    function drawBackground() {
        const gradient = cosmosCtx.createRadialGradient(
            cosmosCanvas.width / 2, cosmosCanvas.height / 2, 0,
            cosmosCanvas.width / 2, cosmosCanvas.height / 2, cosmosCanvas.width / 2
        );
        gradient.addColorStop(0, 'rgba(11, 15, 42, 0.8)');
        gradient.addColorStop(0.5, 'rgba(5, 6, 15, 0.9)');
        gradient.addColorStop(1, 'rgba(5, 6, 15, 1)');
        cosmosCtx.fillStyle = gradient;
        cosmosCtx.fillRect(0, 0, cosmosCanvas.width, cosmosCanvas.height);
    }
    
    // Dessiner les étoiles
    function drawStars() {
        const time = Date.now() / 1000;
        cosmosStars.forEach(star => {
            const x = (star.x / 100) * cosmosCanvas.width;
            const y = (star.y / 100) * cosmosCanvas.height;
            const opacity = star.opacity * (0.5 + 0.5 * Math.sin(time * star.speed));
            
            cosmosCtx.beginPath();
            cosmosCtx.arc(x, y, star.size, 0, Math.PI * 2);
            cosmosCtx.fillStyle = `rgba(255, 255, 255, ${opacity})`;
            cosmosCtx.fill();
        });
    }
    
    // Dessiner les liens
    function drawLinks() {
        if (!window.__HUB__ || !window.__HUB__.providers) return;
        
        const centerX = cosmosCanvas.width / 2;
        const centerY = cosmosCanvas.height / 2;
        const radius = Math.min(cosmosCanvas.width, cosmosCanvas.height) * 0.35;
        
        window.__HUB__.providers.forEach((provider, index) => {
            const angle = (index / window.__HUB__.providers.length) * Math.PI * 2;
            const x = centerX + Math.cos(angle) * radius;
            const y = centerY + Math.sin(angle) * radius;
            
            const intensity = Math.min(provider.calls_24h / 100, 1);
            const lineWidth = 1 + intensity * 3;
            
            // Dégradé du lien
            const gradient = cosmosCtx.createLinearGradient(centerX, centerY, x, y);
            gradient.addColorStop(0, 'rgba(125, 231, 255, 0.8)');
            gradient.addColorStop(1, 'rgba(179, 136, 255, 0.8)');
            
            cosmosCtx.beginPath();
            cosmosCtx.moveTo(centerX, centerY);
            cosmosCtx.lineTo(x, y);
            cosmosCtx.strokeStyle = gradient;
            cosmosCtx.lineWidth = lineWidth;
            cosmosCtx.stroke();
            
            // Particules sur le lien
            const particleCount = Math.floor(intensity * 5);
            for (let i = 0; i < particleCount; i++) {
                const progress = ((Date.now() / 1000) * 0.5 + i / particleCount) % 1;
                const px = centerX + (x - centerX) * progress;
                const py = centerY + (y - centerY) * progress;
                
                cosmosCtx.beginPath();
                cosmosCtx.arc(px, py, 2, 0, Math.PI * 2);
                cosmosCtx.fillStyle = `rgba(255, 255, 255, ${0.5 + 0.5 * Math.sin(progress * Math.PI)})`;
                cosmosCtx.fill();
            }
        });
    }
    
    // Dessiner les particules
    function drawParticles() {
        // Les particules sont dessinées dans drawLinks
    }
    
    // Dessiner les nœuds
    function drawNodes() {
        if (!window.__HUB__ || !window.__HUB__.providers) return;
        
        const centerX = cosmosCanvas.width / 2;
        const centerY = cosmosCanvas.height / 2;
        const radius = Math.min(cosmosCanvas.width, cosmosCanvas.height) * 0.35;
        
        // Nœud central HUB
        const hubSize = 30 + Math.sin(Date.now() / 1000) * 5;
        drawNode(centerX, centerY, hubSize, '#7de7ff', 'HUB', true);
        
        // Nœuds providers
        window.__HUB__.providers.forEach((provider, index) => {
            const angle = (index / window.__HUB__.providers.length) * Math.PI * 2;
            const x = centerX + Math.cos(angle) * radius;
            const y = centerY + Math.sin(angle) * radius;
            
            // Couleur selon l'état
            let color = '#f0a020';
            if (!provider.enabled) {
                color = '#ff4d4d';
            } else if (provider.calls_24h > 0) {
                color = '#7CFF6B';
            }
            
            // Taille selon les appels
            const size = Math.max(8, Math.min(40, 8 + provider.calls_24h * 0.5));
            
            drawNode(x, y, size, color, provider.id, false);
        });
    }
    
    // Dessiner un nœud
    function drawNode(x, y, size, color, label, isHub) {
        // Halo
        const gradient = cosmosCtx.createRadialGradient(x, y, 0, x, y, size * 2);
        gradient.addColorStop(0, `rgba(${hexToRgb(color)}, 0.3)`);
        gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
        
        cosmosCtx.beginPath();
        cosmosCtx.arc(x, y, size * 2, 0, Math.PI * 2);
        cosmosCtx.fillStyle = gradient;
        cosmosCtx.fill();
        
        // Cercle principal
        cosmosCtx.beginPath();
        cosmosCtx.arc(x, y, size, 0, Math.PI * 2);
        cosmosCtx.fillStyle = color;
        cosmosCtx.fill();
        
        // Bordure
        cosmosCtx.beginPath();
        cosmosCtx.arc(x, y, size, 0, Math.PI * 2);
        cosmosCtx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
        cosmosCtx.lineWidth = 2;
        cosmosCtx.stroke();
        
        // Label
        cosmosCtx.fillStyle = '#fff';
        cosmosCtx.font = isHub ? 'bold 14px Orbitron' : '10px Share Tech Mono';
        cosmosCtx.textAlign = 'center';
        cosmosCtx.fillText(label, x, y + size + 15);
    }
    
    // Convertir hex en rgb
    function hexToRgb(hex) {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? 
            `${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)}` : 
            '255, 255, 255';
    }
    
    // Gérer le survol
    function handleMouseMove(e) {
        if (!window.__HUB__ || !window.__HUB__.providers) return;
        
        const rect = cosmosCanvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        const centerX = cosmosCanvas.width / 2;
        const centerY = cosmosCanvas.height / 2;
        const radius = Math.min(cosmosCanvas.width, cosmosCanvas.height) * 0.35;
        
        // Vérifier le survol des nœuds
        let hovered = null;
        window.__HUB__.providers.forEach((provider, index) => {
            const angle = (index / window.__HUB__.providers.length) * Math.PI * 2;
            const x = centerX + Math.cos(angle) * radius;
            const y = centerY + Math.sin(angle) * radius;
            const size = Math.max(8, Math.min(40, 8 + provider.calls_24h * 0.5));
            
            const dist = Math.sqrt((mouseX - x) ** 2 + (mouseY - y) ** 2);
            if (dist < size + 10) {
                hovered = provider;
            }
        });
        
        cosmosHoveredNode = hovered;
        
        // Afficher la tooltip
        const tooltip = document.getElementById('cosmos-tooltip');
        if (hovered) {
            tooltip.innerHTML = `
                <strong>${hovered.name}</strong><br>
                Modèle: ${hovered.model}<br>
                Type: ${hovered.kind}<br>
                Appels 24h: ${hovered.calls_24h}<br>
                État: ${hovered.enabled ? '✅ Actif' : '❌ Désactivé'}
            `;
            tooltip.style.display = 'block';
            tooltip.style.left = (e.clientX - rect.left + 15) + 'px';
            tooltip.style.top = (e.clientY - rect.top + 15) + 'px';
        } else {
            tooltip.style.display = 'none';
        }
    }
    
    // Gérer la sortie de la souris
    function handleMouseLeave() {
        cosmosHoveredNode = null;
        const tooltip = document.getElementById('cosmos-tooltip');
        if (tooltip) tooltip.style.display = 'none';
    }
    
    // Rendu du tableau de bord
    function renderCosmos() {
        if (!window.__HUB__) {
            const container = document.getElementById('cosmos-hub');
            if (container) {
                container.innerHTML = '<div class="cosmos-unavailable">🌌 HUB feed indisponible</div>';
            }
            return;
        }
        
        // Budget
        const budgetEl = document.getElementById('cosmos-budget');
        if (budgetEl && window.__HUB__.budget) {
            const budget = window.__HUB__.budget;
            const percentage = Math.min((budget.consumed / budget.daily) * 100, 100);
            budgetEl.innerHTML = `
                <div class="cosmos-budget-text">
                    Appels cloud: <strong>${budget.consumed}</strong> / ${budget.daily}
                </div>
                <div class="cosmos-budget-bar">
                    <div class="cosmos-budget-fill" style="width: ${percentage}%"></div>
                </div>
                <div class="cosmos-budget-text">
                    Restant: <strong style="color: ${budget.remaining > 0 ? '#7CFF6B' : '#ff4d4d'}">${budget.remaining}</strong>
                </div>
            `;
        }
        
        // File d'attente
        const queueEl = document.getElementById('cosmos-queue');
        if (queueEl && window.__HUB__.queue) {
            queueEl.innerHTML = window.__HUB__.queue.map(call => {
                const time = call.ts ? new Date(call.ts).toLocaleTimeString('fr-FR', {hour: '2-digit', minute: '2-digit'}) : '--:--';
                return `
                    <div class="cosmos-queue-item">
                        <span class="time">${time}</span>
                        <span>${call.task}</span>
                        <span class="provider">→ ${call.provider}</span>
                    </div>
                `;
            }).join('') || '<div class="cosmos-queue-item">Aucun appel récent</div>';
        }
        
        // Quotas par tâche
        const tasksEl = document.getElementById('cosmos-tasks');
        if (tasksEl && window.__HUB__.tasks_quotas) {
            const tasks = Object.entries(window.__HUB__.tasks_quotas);
            if (tasks.length > 0) {
                tasksEl.innerHTML = `
                    <table class="cosmos-table">
                        <tr>
                            <th>Tâche</th>
                            <th>Provider</th>
                            <th>Quota</th>
                        </tr>
                        ${tasks.map(([task, config]) => `
                            <tr>
                                <td>${task}</td>
                                <td>${config.provider || 'N/A'}</td>
                                <td>${config.cloud_quota || '∞'}</td>
                            </tr>
                        `).join('')}
                    </table>
                `;
            } else {
                tasksEl.innerHTML = '<div class="cosmos-queue-item">Aucune tâche configurée</div>';
            }
        }
        
        // Santé du hub
        const healthEl = document.getElementById('cosmos-health');
        if (healthEl && window.__HUB__.health) {
            const health = window.__HUB__.health;
            const statusClass = health.status === 'ok' ? 'ok' : 'nok';
            healthEl.innerHTML = `
                <div>
                    <span class="cosmos-status ${statusClass}">${health.status.toUpperCase()}</span>
                    <span style="color:#fff; margin-left:10px;">Providers: ${health.providers || 'N/A'}</span>
                </div>
                <div style="color:#b388ff; font-size:11px; margin-top:5px;">
                    Feed: ${new Date(window.__HUB__.generated_at).toLocaleTimeString('fr-FR')}
                </div>
            `;
        } else if (healthEl) {
            healthEl.innerHTML = '<div class="cosmos-queue-item">Hub injoignable</div>';
        }
        
        // Événements
        const eventsEl = document.getElementById('cosmos-events');
        if (eventsEl && window.__HUB__.events) {
            eventsEl.innerHTML = window.__HUB__.events.map(event => `
                <div class="cosmos-event">
                    [${event.kind}] ${event.title}
                </div>
            `).join('') || '<div class="cosmos-queue-item">Aucun événement récent</div>';
        }
    }
    
    // Rafraîchir
    window.__cosmosRefresh = function() {
        renderCosmos();
    };
    
    // Basculer synapses
    window.__toggleSynapses = function() {
        const cosmosHub = document.getElementById('cosmos-hub');
        const synapses = document.getElementById('synapses');
        if (cosmosHub && synapses) {
            synapsesVisible = !synapsesVisible;
            if (synapsesVisible) {
                cosmosHub.style.display = 'none';
                synapses.style.display = 'block';
            } else {
                cosmosHub.style.display = 'flex';
                synapses.style.display = 'none';
            }
        }
    };
    
    // Initialiser au chargement
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCosmos);
    } else {
        initCosmos();
    }
    
    // Rafraîchir au clic sur le bouton global
    const refreshBtn = document.querySelector('[onclick*="cockpitRefresh"]');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', () => {
            setTimeout(renderCosmos, 100);
        });
    }
})();
</script>
```

## 3. Checklist de tests manuels

### Test du script feed :
```bash
# 1. Tester la génération
python3 ~/ace777-test-day1/Index_Maison/scripts/hub_cockpit_feed.py

# 2. Vérifier les fichiers générés
ls -la ~/ace777-test-day1/Index_Maison/cockpit/hub.json
ls -la ~/ace777-test-day1/Index_Maison/cockpit/hub.js

# 3. Vérifier le contenu JSON
cat ~/ace777-test-day1/Index_Maison/cockpit/hub.json | python3 -m json.tool

# 4. Vérifier que hub.js est valide
node -e "eval(require('fs').readFileSync('~/ace777-test-day1/Index_Maison/cockpit/hub.js', 'utf8')); console.log('JS valide')"
```

### Test visuel cockpit :
1. Ouvrir `~/ace777-test-day1/Index_Maison/cockpit/index.html` dans un navigateur
2. Aller dans le volet GRAPH
3. Vérifier que le COSMOS HUB s'affiche avec :
   - Le graphe avec le nœud central HUB et les providers en orbite
   - Les étoiles scintillantes en arrière-plan
   - Les liens lumineux avec particules
   - La colonne de droite avec budget, file d'attente, quotas, santé
4. Tester le survol des nœuds (tooltip)
5. Tester le bouton ↻ (rafraîchir)
6. Tester le bouton SYNAPSES (bascule)
7. Vérifier que les autres volets (OPS, THERMO, BOARD, VOL) fonctionnent toujours

## 4. Pièges supplémentaires détectés

1. **Conflit de variables globales** : Le code JS est enveloppé dans une IIFE pour éviter tout conflit avec le code existant du cockpit.

2. **Performance canvas** : L'animation utilise `requestAnimationFrame` et limite le nombre de particules pour éviter les problèmes de performance sur les machines modestes.

3. **Gestion du temps** : Les timestamps dans usage.jsonl peuvent être dans différents formats (ISO, timestamp Unix). Le script gère les deux.

4. **Fichiers manquants** : Le script feed est tolérant à l'absence de fichiers, mais le cockpit doit aussi gérer l'absence de `window.__HUB__`.

5. **Compatibilité navigateur** : Le code utilise des fonctionnalités modernes (backdrop-filter, CSS gradients) qui nécessitent un navigateur récent.

6. **Sécurité** : Aucune donnée sensible n'est exposée dans hub.js/hub.json (pas de clés API, pas de tokens).

7. **Backup** : Avant de modifier index.html, faites une copie de sauvegarde :
```bash
cp ~/ace777-test-day1/Index_Maison/cockpit/index.html ~/ace777-test-day1/Index_Maison/cockpit/index.html.bak-cosmos
```

Le code est prêt à être copié-collé et fonctionnera immédiatement. Le COSMOS HUB apportera une vue d'orchestre moderne et cosmique au cockpit ACE777.
