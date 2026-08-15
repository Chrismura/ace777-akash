# Réponse codeur (provider Google Gemini, 1.9s)

```ruby
      j=JSON.parse(File.read(path))
      j["ts_ms"]=(Time.now.to_f*1000).to_i
      tmp="#{path}.tmp.#{$$}"
      File.write(tmp, JSON.generate(j))
      File.rename(tmp, path)
```
⬇️
```ruby
      j=JSON.parse(File.read(path))
      # FIX-HEARTBEAT (15/08) : ne pas rafraîchir ts_ms sur perte close (sinon TTL revenge 20s inopérant)
      unless j["status"].to_s == "CLOSED" && (Float(j["pnl_usdt"]) rescue 0.0) < 0.0
        j["ts_ms"]=(Time.now.to_f*1000).to_i
        tmp="#{path}.tmp.#{$$}"
        File.write(tmp, JSON.generate(j))
        File.rename(tmp, path)
      end
```
VÉRIFICATION : OK (Syntaxe Ruby validée - 0 erreur).
