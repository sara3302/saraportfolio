import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS Variables
content = content.replace(
    '  :root{\n    --bg:#0A0E17;\n    --surface:#121826;\n    --surface-alt:#1A2233;\n    --line:#232C40;\n    --text:#E8ECF4;\n    --muted:#8792A8;\n    --accent:#F2A93B;\n    --accent-dim:#B87F2C;\n    --accent-glow:rgba(242,169,59,0.18);\n  }',
    '  :root{\n    --bg:#1A1025;\n    --surface:rgba(42, 28, 59, 0.65);\n    --surface-alt:rgba(58, 41, 79, 0.7);\n    --line:rgba(255, 184, 161, 0.2);\n    --text:#FCE8E3;\n    --muted:#C9B5D2;\n    --accent:#FFB8A1;\n    --accent-dim:#F27A9C;\n    --accent-glow:rgba(242, 122, 156, 0.3);\n  }'
)

# 2. Update selection color
content = content.replace('::selection{background:var(--accent);color:#0A0E17;}', '::selection{background:var(--accent);color:#1A1025;}')

# 3. Update buttons hover
content = content.replace(
    '  .btn-accent{\n    background:var(--accent);color:#151016;border:none;font-weight:700;\n    padding:.8rem 1.9rem;border-radius:6px;letter-spacing:.02em;transition:.25s;\n  }\n  .btn-accent:hover{background:#ffbf5c;transform:translateY(-2px);color:#151016;box-shadow:0 10px 30px var(--accent-glow);}',
    '  .btn-accent{\n    background:var(--accent);color:#1A1025;border:none;font-weight:700;\n    padding:.8rem 1.9rem;border-radius:6px;letter-spacing:.02em;transition:.25s;\n  }\n  .btn-accent:hover{background:var(--accent-dim);transform:translateY(-2px);color:#1A1025;box-shadow:0 10px 30px var(--accent-glow);}'
)

# 4. Project Card CSS
content = content.replace(
    '  /* ---- PROJECTS ---- */\n  .project-card{\n    background:var(--surface);border:1px solid var(--line);border-radius:14px;\n    padding:2.1rem;height:100%;transition:.3s;position:relative;overflow:hidden;\n  }\n  .project-card::before{\n    content:\'\';position:absolute;top:0;left:0;right:0;height:3px;\n    background:linear-gradient(90deg,var(--accent),transparent);opacity:0;transition:.3s;\n  }\n  .project-card:hover{transform:translateY(-6px);border-color:var(--accent-dim);box-shadow:0 20px 40px rgba(0,0,0,.35);}',
    '  /* ---- PROJECTS ---- */\n  .project-card{\n    background:var(--surface);border:1px solid var(--line);border-radius:14px;\n    padding:2.1rem;height:100%;transition:.3s;position:relative;overflow:hidden;\n    backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);\n    transform-style: preserve-3d;\n  }\n  .project-card::before{\n    content:\'\';position:absolute;top:0;left:0;right:0;height:3px;\n    background:linear-gradient(90deg,var(--accent),transparent);opacity:0;transition:.3s;\n  }\n  .project-card:hover{border-color:var(--accent-dim);box-shadow:0 20px 40px rgba(0,0,0,.35);}\n  .project-card > * { transform: translateZ(30px); }'
)

# 5. Card Panel CSS
content = content.replace(
    '.card-panel{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:2rem;height:100%;}',
    '.card-panel{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:2rem;height:100%; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);}'
)

# 6. Form Control CSS
content = content.replace(
    '  .form-control{\n    background:var(--surface-alt);border:1px solid var(--line);color:var(--text);\n    padding:.85rem 1rem;border-radius:8px;font-weight:300;\n  }',
    '  .form-control{\n    background:var(--surface-alt);border:1px solid var(--line);color:var(--text);\n    padding:.85rem 1rem;border-radius:8px;font-weight:300;\n    backdrop-filter: blur(10px);\n  }'
)

# 7. Gallery Item CSS
content = content.replace(
    '  .gallery-item{\n    position:relative;border-radius:12px;overflow:hidden;border:1px solid var(--line);\n    aspect-ratio:4/3;cursor:pointer;display:none;\n  }\n  .gallery-item.show{display:block;}\n  .gallery-item img{width:100%;height:100%;object-fit:cover;transition:.5s;}\n  .gallery-item:hover img{transform:scale(1.08);}',
    '  .gallery-item{\n    position:relative;border-radius:12px;overflow:hidden;border:1px solid var(--line);\n    aspect-ratio:4/3;cursor:pointer;display:none;\n    transform-style: preserve-3d;\n  }\n  .gallery-item.show{display:block;}\n  .gallery-item img{width:100%;height:100%;object-fit:cover;transition:.5s; transform: translateZ(20px);}\n  .gallery-item:hover img{transform:scale(1.08) translateZ(20px);}'
)

# 8. Hero CSS
content = content.replace(
    '  /* ---- HERO ---- */\n  #hero{\n    min-height:100vh;display:flex;align-items:center;position:relative;\n    background:\n      radial-gradient(circle at 78% 25%, var(--accent-glow), transparent 45%),\n      radial-gradient(circle at 15% 80%, rgba(242,169,59,0.08), transparent 40%),\n      var(--bg);\n  }\n  #hero-canvas{position:absolute;inset:0;opacity:.5;}',
    '  /* ---- HERO ---- */\n  #hero{\n    min-height:100vh;display:flex;align-items:center;position:relative;\n    background: var(--bg);\n  }'
)

# 9. Hero photo ring
content = content.replace(
    '  .hero-photo-ring{\n    position:absolute;inset:-14px;border:1px dashed rgba(242,169,59,.4);border-radius:50%;\n    animation:spin 26s linear infinite;\n  }',
    '  .hero-photo-ring{\n    position:absolute;inset:-14px;border:1px dashed rgba(255, 184, 161, 0.4);border-radius:50%;\n    animation:spin 26s linear infinite;\n  }'
)

# 10. Tag CSS
content = content.replace(
    '  .tag{\n    display:inline-block;font-size:.74rem;font-weight:600;letter-spacing:.02em;\n    color:var(--accent);background:rgba(242,169,59,.09);border:1px solid rgba(242,169,59,.25);\n    padding:.28rem .7rem;border-radius:20px;margin:0 .35rem .35rem 0;\n  }',
    '  .tag{\n    display:inline-block;font-size:.74rem;font-weight:600;letter-spacing:.02em;\n    color:var(--accent);background:rgba(242,122,156,.15);border:1px solid rgba(242,122,156,.3);\n    padding:.28rem .7rem;border-radius:20px;margin:0 .35rem .35rem 0;\n  }'
)

# 11. HTML hero canvas removal
content = content.replace(
    '<section id="hero">\n  <canvas id="hero-canvas"></canvas>\n  <div class="container position-relative">',
    '<section id="hero">\n  <div class="container position-relative">'
)

# 12. HTML project card data-tilt
content = content.replace(
    '        <div class="project-card">',
    '        <div class="project-card" data-tilt data-tilt-max="5" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.15">'
)

# 13. HTML gallery item data-tilt
content = content.replace(
    'class="col-md-4 gallery-item show"',
    'class="col-md-4 gallery-item show" data-tilt data-tilt-max="10" data-tilt-speed="400"'
)

# 14. Scripts Vendor
content = content.replace(
    '<!-- Vendor JS -->\n<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>\n<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n<script src="https://cdn.jsdelivr.net/npm/glightbox@3.3.0/dist/js/glightbox.min.js"></script>',
    '<!-- Vendor JS -->\n<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>\n<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n<script src="https://cdn.jsdelivr.net/npm/glightbox@3.3.0/dist/js/glightbox.min.js"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>\n<script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.halo.min.js"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.1/vanilla-tilt.min.js"></script>'
)

# 15. JS Canvas to Vanta
old_js = """  // hero canvas: subtle animated node graph
  (function () {
    const canvas = document.getElementById('hero-canvas');
    const ctx = canvas.getContext('2d');
    let w, h, nodes;
    const NODE_COUNT = 46;

    function resize() {
      w = canvas.width = canvas.offsetWidth;
      h = canvas.height = canvas.offsetHeight;
    }
    function init() {
      resize();
      nodes = Array.from({ length: NODE_COUNT }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.25,
        vy: (Math.random() - 0.5) * 0.25
      }));
    }
    function tick() {
      ctx.clearRect(0, 0, w, h);
      nodes.forEach(n => {
        n.x += n.vx; n.y += n.vy;
        if (n.x < 0 || n.x > w) n.vx *= -1;
        if (n.y < 0 || n.y > h) n.vy *= -1;
      });
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const dx = nodes[i].x - nodes[j].x, dy = nodes[i].y - nodes[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 140) {
            ctx.strokeStyle = `rgba(242,169,59,${0.14 * (1 - dist / 140)})`;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(nodes[i].x, nodes[i].y);
            ctx.lineTo(nodes[j].x, nodes[j].y);
            ctx.stroke();
          }
        }
      }
      nodes.forEach(n => {
        ctx.fillStyle = 'rgba(242,169,59,0.55)';
        ctx.beginPath();
        ctx.arc(n.x, n.y, 1.6, 0, Math.PI * 2);
        ctx.fill();
      });
      requestAnimationFrame(tick);
    }
    window.addEventListener('resize', resize);
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      init();
      tick();
    }
  })();"""

new_js = """  // 3D Background with Vanta.js
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    VANTA.HALO({
      el: "#hero",
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.00,
      minWidth: 200.00,
      baseColor: 0xf27a9c,
      backgroundColor: 0x1a1025,
      amplitudeFactor: 1.5,
      size: 1.2
    });
  }
  
  // Initialize Vanilla Tilt explicitly if needed, but the data-tilt attribute should handle it automatically.
"""
content = content.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Success')
