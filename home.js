// ═══════════════════════════════════════════
// MAIN SITE JS — Red Agave Landscape
// All in one IIFE, validated clean
// ═══════════════════════════════════════════
(function () {

  // ── CURSOR ──────────────────────────────
  var cur  = document.getElementById('cur');
  var ring = document.getElementById('cur-ring');
  if (cur && ring) {
    var cmx = 0, cmy = 0, crx = 0, cry = 0;
    document.addEventListener('mousemove', function (e) {
      cmx = e.clientX; cmy = e.clientY;
    });
    (function curTick() {
      // Cursor dot: snaps instantly to mouse
      cur.style.transform = 'translate3d(' + cmx + 'px,' + cmy + 'px,0) translate(-50%,-50%) rotate(45deg)';
      // Diamond ring: very fast lerp — minimal lag
      crx += (cmx - crx) * 0.55;
      cry += (cmy - cry) * 0.55;
      ring.style.transform = 'translate3d(' + crx + 'px,' + cry + 'px,0) translate(-50%,-50%) rotate(45deg)';
      requestAnimationFrame(curTick);
    }());
    document.querySelectorAll('a,button,.svc,.tc,.wm-card,.step,.fcard').forEach(function (el) {
      el.addEventListener('mouseenter', function () {
        cur.style.width  = '14px'; cur.style.height = '14px';
        cur.style.background = 'var(--gold-light)';
        ring.style.width = '30px'; ring.style.height = '30px';
        ring.style.borderColor = 'rgba(201,168,76,0.9)';
      });
      el.addEventListener('mouseleave', function () {
        cur.style.width  = '10px'; cur.style.height = '10px';
        cur.style.background = 'var(--gold)';
        ring.style.width = '22px'; ring.style.height = '22px';
        ring.style.borderColor = 'rgba(201,168,76,0.6)';
      });
    });
  }

  // ── NAV SCROLL ─────────────────────────
  var nav = document.getElementById('nav');
  if (nav) {
    window.addEventListener('scroll', function () {
      nav.classList.toggle('scrolled', window.scrollY > 60);
    });
  }
  var nqb = document.getElementById('nav-quote-btn');
  if (nqb) {
    nqb.addEventListener('click', function () {
      window.location.href = 'contact.html';
    });
  }

  // ── MOBILE MENU ────────────────────────
  var hbg = document.getElementById('hbg');
  var mob = document.getElementById('mob-menu');
  var mopen = false;
  if (hbg && mob) {
    hbg.addEventListener('click', function () {
      mopen = !mopen;
      hbg.classList.toggle('open', mopen);
      mob.classList.toggle('open', mopen);
      document.body.style.overflow = mopen ? 'hidden' : '';
    });
    mob.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mopen = false;
        hbg.classList.remove('open');
        mob.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  // ── SMOOTH ANCHORS ─────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var t = document.querySelector(a.getAttribute('href'));
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
    });
  });

  // ── SCROLL REVEAL (IntersectionObserver — no GSAP needed) ──
  var revObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) e.target.classList.add('in');
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.rev,.rev-l').forEach(function (el) { revObs.observe(el); });

  // ── GSAP ENHANCEMENTS (if CDN loaded) ──
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // ── PREMIUM CLIP-PATH WORD REVEAL ─────────────────────
    // Each title line wipes in with a clip-path reveal — the signature
    // technique of award-winning sites (Awwwards, Apple, Linear etc.)
    // clip-path:inset() cuts from bottom up, revealing text as it rises
    // The .htl wrapper has overflow:hidden to contain the clip
    var reveal = gsap.timeline({ delay: 0.6 });

    reveal
      .fromTo('#s-hint',
        { opacity: 0 },
        { opacity: 1, duration: .6 },
        1.1
      )
      .fromTo('#c1',
        { opacity: 0, x: 30 },
        { opacity: 1, x: 0, duration: .7, ease: 'power3.out' },
        0.9
      )
      .fromTo('#c2',
        { opacity: 0, x: 30 },
        { opacity: 1, x: 0, duration: .7, ease: 'power3.out' },
        1.05
      )
      .fromTo('#c3',
        { opacity: 0, x: 30 },
        { opacity: 1, x: 0, duration: .7, ease: 'power3.out' },
        1.2
      )
      .call(function() {
        document.querySelectorAll('.fcard').forEach(function(c) { c.classList.add('go'); });
      }, [], 1.5);

    // Background parallax — slides up as you scroll
    gsap.to('.hero-bg', {
      yPercent: 26, ease: 'none',
      scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
    });

    // Hero fade on scroll — elegant opacity fade as user scrolls past
    // Fades slowly and stops at 0.25 — title never fully disappears
    gsap.to('.hero-text', {
      opacity: 0.25,
      y: -20,
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: '80% top',
        scrub: 2.5,
      }
    });

    // Hero title — no continuous drift (looked unnatural)
    // Only TOP DESIGN flickers via its own JS block

    // Ghost text: no drift — cursor illumination handled below

    // Stat counters
    document.querySelectorAll('.s-num[data-target]').forEach(function (el) {
      var target = parseInt(el.dataset.target);
      var suf    = el.dataset.suf || '+';
      ScrollTrigger.create({
        trigger: el, start: 'top 85%', once: true,
        onEnter: function () {
          gsap.to({ v: 0 }, {
            v: target, duration: 2.5, ease: 'power4.out',
            onUpdate: function () { el.textContent = Math.round(this.targets()[0].v) + suf; }
          });
        }
      });
    });
  }

  // ── INDEPENDENT CARD MOUSE TILT ─────────
  // Each card has its own resting angle and mouse sensitivity
  var resting = [
    { ry: -24, rx: 6,  rz: -2.5 },
    { ry:  14, rx: 4,  rz:  2.0 },
    { ry:  28, rx: 8,  rz:  3.0 }
  ];
  var cardIds = ['c1i', 'c2i', 'c3i'];
  var sens    = [5, 4, 7];
  var tmx = 0, tmy = 0, smx = 0, smy = 0;

  document.addEventListener('mousemove', function (e) {
    tmx = (e.clientX / innerWidth)  - 0.5;
    tmy = (e.clientY / innerHeight) - 0.5;
  });

  (function tiltTick() {
    smx += (tmx - smx) * 0.055;
    smy += (tmy - smy) * 0.055;
    cardIds.forEach(function (id, i) {
      var inner = document.getElementById(id);
      var wrap  = document.getElementById(id.replace('i', ''));
      if (!inner || !wrap || wrap.matches(':hover')) return;
      var s  = sens[i];
      var r  = resting[i];
      var ry = r.ry + smx * s;
      var rx = r.rx - smy * (s * 0.45);
      inner.style.transform =
        'rotateY(' + ry.toFixed(2) + 'deg) ' +
        'rotateX(' + rx.toFixed(2) + 'deg) ' +
        'rotate('  + r.rz + 'deg)';
    });
    requestAnimationFrame(tiltTick);
  }());

  // ── THREE.JS AMBER DUST PARTICLES ───────
  function initDust() {
    var canvas   = document.getElementById('h-canvas');
    var renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    renderer.setSize(innerWidth, innerHeight);

    var scene  = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(60, innerWidth / innerHeight, 0.1, 1000);
    camera.position.z = 5;

    var count = 3200;
    var pos   = new Float32Array(count * 3);
    var col   = new Float32Array(count * 3);
    var sz    = new Float32Array(count);

    for (var i = 0; i < count; i++) {
      pos[i * 3]     = (Math.random() - 0.5) * 24;
      pos[i * 3 + 1] = (Math.random() - 0.5) * 16;
      pos[i * 3 + 2] = (Math.random() - 0.5) * 8;
      var v = Math.random();
      if      (v > 0.65) { col[i*3]=0.91; col[i*3+1]=0.63; col[i*3+2]=0.08; }
      else if (v > 0.35) { col[i*3]=1.00; col[i*3+1]=0.72; col[i*3+2]=0.23; }
      else if (v > 0.15) { col[i*3]=1.00; col[i*3+1]=0.87; col[i*3+2]=0.55; }
      else               { col[i*3]=1.00; col[i*3+1]=0.95; col[i*3+2]=0.80; }
      sz[i] = Math.random() < 0.08 ? Math.random() * 3 + 1.5 : Math.random() * 1.2 + 0.3;
    }

    var geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color',    new THREE.BufferAttribute(col, 3));
    geo.setAttribute('size',     new THREE.BufferAttribute(sz,  1));

    var mat = new THREE.PointsMaterial({
      size: 0.038, vertexColors: true, transparent: true, opacity: 0.55,
      sizeAttenuation: true, blending: THREE.AdditiveBlending, depthWrite: false
    });

    var pts = new THREE.Points(geo, mat);
    scene.add(pts);

    var vels = [];
    for (var j = 0; j < count; j++) {
      vels.push({
        x:  (Math.random() - 0.5) * 0.0022,
        y:  (Math.random() - 0.5) * 0.0018 + 0.0004,
        z:  (Math.random() - 0.5) * 0.002,
        tw: Math.random() * Math.PI * 2,
        ts: Math.random() * 0.02 + 0.008
      });
    }

    var pmx = 0, pmy = 0, psF = 1, ptick = 0;
    document.addEventListener('mousemove', function (e) {
      pmx = (e.clientX / innerWidth  - 0.5) * 0.25;
      pmy = -(e.clientY / innerHeight - 0.5) * 0.18;
    });
    window.addEventListener('scroll', function () {
      psF = Math.max(0, 1 - scrollY / innerHeight);
    });

    var pA = geo.attributes.position;
    var sA = geo.attributes.size;

    (function animParticles() {
      requestAnimationFrame(animParticles);
      ptick += 0.01;
      for (var k = 0; k < count; k++) {
        var vv = vels[k];
        pA.array[k*3]     += vv.x + Math.sin(ptick * 0.3 + k * 0.1) * 0.001;
        pA.array[k*3 + 1] += vv.y + Math.cos(ptick * 0.2 + k * 0.07) * 0.0008;
        pA.array[k*3 + 2] += vv.z;
        if (pA.array[k*3]     >  12) pA.array[k*3]     = -12;
        if (pA.array[k*3]     < -12) pA.array[k*3]     =  12;
        if (pA.array[k*3 + 1] >   9) pA.array[k*3 + 1] =  -9;
        if (pA.array[k*3 + 1] <  -9) pA.array[k*3 + 1] =   9;
        vv.tw += vv.ts;
        sA.array[k] = sz[k] * (0.6 + 0.4 * Math.abs(Math.sin(vv.tw)));
      }
      pA.needsUpdate = true;
      sA.needsUpdate = true;
      pts.rotation.y = pmx * 0.15;
      pts.rotation.x = pmy * 0.1;
      mat.opacity = 0.55;
      renderer.render(scene, camera);
    }());

    window.addEventListener('resize', function () {
      camera.aspect = innerWidth / innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(innerWidth, innerHeight);
    });
  }
  if (window.matchMedia('(min-width: 901px)').matches && document.getElementById('h-canvas')) {
    var threeScript = document.createElement('script');
    threeScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    threeScript.onload = function () { try { initDust(); } catch (e) {} };
    document.head.appendChild(threeScript);
  }


  // ── TOP DESIGN RANDOM FLICKER ──────────────────────────
  // Sets filter:drop-shadow() DIRECTLY on the element — no CSS vars needed.
  // drop-shadow traces actual letter outlines — zero box artifact possible.
  // Timing is completely random — no mathematical pattern.
  (function() {
    var el = document.querySelector('.hl2');
    if (!el) return;

    function setGlow(intensity, sz) {
      // Set filter directly — this is the only reliable way
      el.style.filter =
        'drop-shadow(0 0 ' + sz + 'px rgba(232,196,90,' + intensity.toFixed(3) + ')) ' +
        'drop-shadow(0 0 ' + (sz * 1.8).toFixed(1) + 'px rgba(201,168,76,' + (intensity * 0.4).toFixed(3) + '))';
    }

    function clearGlow() {
      el.style.filter = 'none';
    }

    function scheduleFlicker() {
      // Random silence between flicker events: 0.5s – 6s
      // Prime-ish numbers multiplied together = no audible pattern
      var wait = 500 + Math.random() * 5500;

      setTimeout(function() {
        // Each event: 1–3 rapid pulses clustered (like a real candle flutter)
        var pulses = 1 + Math.floor(Math.random() * 2);
        var p = 0;

        function doPulse() {
          if (p >= pulses) {
            scheduleFlicker();
            return;
          }
          p++;

          // Intensity: subtle 0.18 → medium 0.62 — never harsh or neon
          var intensity = 0.18 + Math.random() * 0.44;
          // Glow radius: 1px – 3.8px — always tight to letterforms
          var sz        = 1.0 + Math.random() * 2.8;
          // Hold: 35ms – 220ms
          var hold      = 35 + Math.random() * 185;
          // Fade: 100ms – 480ms — varies so no two fades feel the same
          var fadeMs    = 100 + Math.random() * 380;

          // RAMP UP instantly
          el.style.transition = 'filter 0.06s ease';
          setGlow(intensity, sz);

          // HOLD, then fade
          setTimeout(function() {
            el.style.transition = 'filter ' + (fadeMs / 1000).toFixed(3) + 's ease';
            clearGlow();

            // Inter-pulse gap within a cluster
            var gap = fadeMs + 40 + Math.random() * 160;
            setTimeout(doPulse, gap);
          }, hold);
        }

        doPulse();
      }, wait);
    }

    // Start at a random time so it never feels scripted
    setTimeout(scheduleFlicker, 600 + Math.random() * 2200);
  }());

  // ── +BUILD OUTLINE GLOW — same technique, different palette ──
  // Very subtle cream/amber glow traces the outline strokes
  // Completely independent timing from TOP DESIGN
  (function() {
    var el = document.querySelector('.hl3');
    if (!el) return;

    function setGlow3(intensity, sz) {
      // Cream-white glow for the outline text — matches its stroke color
      el.style.filter =
        'drop-shadow(0 0 ' + sz + 'px rgba(240,234,214,' + intensity.toFixed(3) + ')) ' +
        'drop-shadow(0 0 ' + (sz * 2).toFixed(1) + 'px rgba(201,168,76,' + (intensity * 0.3).toFixed(3) + '))';
    }
    function clearGlow3() { el.style.filter = 'none'; }

    function scheduleFlicker3() {
      // Slower, rarer — 1s to 8s between events
      var wait = 1000 + Math.random() * 7000;
      setTimeout(function() {
        // Only single pulses — more subtle than TOP DESIGN
        var intensity = 0.12 + Math.random() * 0.28;  // very subtle
        var sz        = 0.8 + Math.random() * 1.8;    // very tight
        var hold      = 60 + Math.random() * 220;
        var fadeMs    = 200 + Math.random() * 500;

        el.style.transition = 'filter 0.08s ease';
        setGlow3(intensity, sz);

        setTimeout(function() {
          el.style.transition = 'filter ' + (fadeMs / 1000).toFixed(3) + 's ease';
          clearGlow3();
          setTimeout(scheduleFlicker3, fadeMs + 100 + Math.random() * 200);
        }, hold);
      }, wait);
    }

    // Offset start so it never fires at same time as TOP DESIGN
    setTimeout(scheduleFlicker3, 2400 + Math.random() * 3000);
  }());

}());


  // ── PER-CHARACTER ENTRANCE: AUSTIN'S + LANDSCAPER ──
  (function(){
    function splitAndAnimate(el, delay) {
      if(!el) return;
      const text = el.textContent;
      el.innerHTML = text.split('').map(function(ch){
        return '<span class="char-letter">' + (ch === "'" ? "'" : ch) + '</span>';
      }).join('');
      const chars = el.querySelectorAll('.char-letter');
      chars.forEach(function(c, i){
        setTimeout(function(){ c.classList.add('in'); }, delay + i * 55);
      });
    }
    // AUSTIN'S — starts immediately on load
    splitAndAnimate(document.getElementById('hl1-word'), 200);
    // LANDSCAPER — staggered later for a cascade feel
    splitAndAnimate(document.getElementById('hl4-word'), 750);
  })();


  // ── TOP DESIGN gold shimmer sweep on entrance ──
  (function(){
    const el = document.getElementById('hl2-word');
    if(!el) return;
    // After the main entrance, do a gold shimmer sweep through letters
    setTimeout(function(){
      el.style.transition = 'filter 0.4s ease';
      el.style.filter = 'drop-shadow(0 0 18px rgba(232,196,90,0.8)) drop-shadow(0 0 36px rgba(201,168,76,0.4))';
      setTimeout(function(){
        el.style.filter = 'drop-shadow(0 0 6px rgba(232,196,90,0.3))';
      }, 500);
    }, 900);
  })();

  // ── HERO TITLE SCROLL GROW/SHRINK ──
  (function(){
    const title = document.querySelector('.hero-title');
    if(!title) return;
    function onScroll(){
      const scrollY = window.scrollY;
      const heroH = document.querySelector('.hero').offsetHeight;
      // Grow from 1→1.18 in first 30% of hero, then shrink back to 0.85 by 80%
      const progress = Math.min(scrollY / (heroH * 0.8), 1);
      let scale;
      if(progress < 0.35){
        // grow phase
        scale = 1 + (progress / 0.35) * 0.16;
      } else {
        // shrink phase
        const shrinkP = (progress - 0.35) / 0.65;
        scale = 1.16 - shrinkP * 0.34;
      }
      scale = Math.max(0.82, Math.min(1.16, scale));
      title.style.transform = 'scale(' + scale + ')';
      title.style.transformOrigin = 'left bottom';
    }
    window.addEventListener('scroll', onScroll, {passive:true});
  })();

  // ── +BUILD ORGANIC PULSE GLOW ──
  // Natural random pulsations drift across BUILD — no visible path,
  // just warm light appearing and fading organically like fire or embers.
  (function(){
    const wrap  = document.querySelector('.hl3-wrap');
    const blob1 = document.querySelector('.hl3-blob-1');
    const blob2 = document.querySelector('.hl3-blob-2');
    if(!wrap || !blob1 || !blob2) return;

    // Each blob has its own independent wandering target
    var b1 = {x:0.5, y:0.5, tx:0.5, ty:0.5, opacity:0.3, topc:0.3, life:0, maxlife:0};
    var b2 = {x:0.8, y:0.4, tx:0.8, ty:0.4, opacity:0.2, topc:0.2, life:0, maxlife:0};

    function newTarget(b) {
      // Pick random position weighted toward center of word
      b.tx = 0.1 + Math.random() * 0.8;
      b.ty = 0.15 + Math.random() * 0.7;
      b.topc = 0.12 + Math.random() * 0.32;
      b.maxlife = 1800 + Math.random() * 3200; // 1.8–5s per wander
      b.life = 0;
    }

    newTarget(b1);
    newTarget(b2);
    // Offset b2 so they don't sync
    b2.x = 0.7; b2.y = 0.3; b2.life = b2.maxlife * 0.6;

    var last = null;
    function frame(ts) {
      if(!last) last = ts;
      var dt = Math.min(ts - last, 50);
      last = ts;

      var w = wrap.offsetWidth || 200;
      var h = wrap.offsetHeight || 80;

      // Advance blob 1
      b1.life += dt;
      if(b1.life >= b1.maxlife) newTarget(b1);
      var ease1 = dt / 900; // smooth lerp speed
      b1.x += (b1.tx - b1.x) * ease1;
      b1.y += (b1.ty - b1.y) * ease1;
      b1.opacity += (b1.topc - b1.opacity) * (dt / 1200);

      // Advance blob 2
      b2.life += dt;
      if(b2.life >= b2.maxlife) newTarget(b2);
      var ease2 = dt / 1200;
      b2.x += (b2.tx - b2.x) * ease2;
      b2.y += (b2.ty - b2.y) * ease2;
      b2.opacity += (b2.topc - b2.opacity) * (dt / 1500);

      // Apply positions — blobs are centered via transform:translate(-50%,-50%)
      blob1.style.left    = (b1.x * w) + 'px';
      blob1.style.top     = (b1.y * h) + 'px';
      blob1.style.opacity = b1.opacity;

      blob2.style.left    = (b2.x * w) + 'px';
      blob2.style.top     = (b2.y * h) + 'px';
      blob2.style.opacity = b2.opacity;

      requestAnimationFrame(frame);
    }

    requestAnimationFrame(frame);
  })();

  // ── HERO SLIDESHOW — crossfade with prev class to prevent blank gap ──
  (function(){
    const slides = document.querySelectorAll('.hslide');
    const dots   = document.querySelectorAll('.hsdot');
    let cur = 0, timer;
    function goTo(n){
      // Mark old slide as 'prev' — fades out slowly with delay, no blank gap
      slides[cur].classList.remove('active');
      slides[cur].classList.add('prev');
      dots[cur].classList.remove('active');
      var oldIdx = cur;
      // Remove prev after transition completes
      setTimeout(function(){ slides[oldIdx].classList.remove('prev'); }, 3000);
      cur = (n + slides.length) % slides.length;
      slides[cur].classList.remove('prev');
      slides[cur].classList.add('active');
      dots[cur].classList.add('active');
    }
    function next(){ goTo(cur + 1); }
    function startTimer(){ timer = setInterval(next, 6000); }
    dots.forEach(d => d.addEventListener('click', function(){
      clearInterval(timer);
      goTo(+this.dataset.idx);
      startTimer();
    }));
    startTimer();
  })();



// ══ THE RED AGAVE DIFFERENCE — Elyse-style scroll parallax ══
(function() {
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var section = document.querySelector('#difference');
  if (!section) return;

  // Entry: subtle fade-in on .dc-img (no transforms on .dc-col — parallax handles motion)
  gsap.from('#difference [data-diff="img"]', {
    opacity: 0, duration: 1.2, ease: 'power2.out',
    stagger: { each: 0.12, from: 'center' },
    scrollTrigger: { trigger: section, start: 'top 85%', toggleActions: 'play none none none' }
  });

  // Sides parallax — moderate drift, unified scrub for smoothness
  gsap.to('#difference .dc-col--left [data-diff="img"], #difference .dc-col--right [data-diff="img"]', {
    yPercent: 32, ease: 'none',
    scrollTrigger: { trigger: section, start: 'top bottom', end: 'bottom top', scrub: 1.2 }
  });

  // Center parallax — reveals upward, same scrub value as sides to keep motion coherent
  gsap.fromTo('#difference .dc-col--center [data-diff="img"]',
    { yPercent: 0 },
    { yPercent: -14, ease: 'none',
      scrollTrigger: { trigger: section, start: 'top bottom', end: 'bottom top', scrub: 1.2 }
    }
  );

  // Title drifts DOWN as you scroll — subtle depth effect
  gsap.fromTo('#difference [data-diff="title"]',
    { yPercent: -6 },
    { yPercent: 18, ease: 'none',
      scrollTrigger: { trigger: section, start: 'top bottom', end: 'bottom top', scrub: 1.2 }
    }
  );

  // Left body text — hidden, fades in from left as section scrolls into view
  gsap.fromTo('#difference .diff-body',
    { opacity: 0, x: -18 },
    { opacity: 1, x: 0, duration: 1.1, ease: 'power2.out',
      scrollTrigger: { trigger: section, start: 'top 52%', toggleActions: 'play none none none' }
    }
  );

  // Title opacity: semi-transparent → solid as section enters viewport
  gsap.fromTo('#difference [data-diff="title"]',
    { opacity: 0.18 },
    { opacity: 1, ease: 'power2.out',
      scrollTrigger: { trigger: section, start: 'top 80%', end: 'top 25%', scrub: 0.8 }
    }
  );

  // Foot — drift up slightly slower
  gsap.fromTo('#difference [data-diff="content"]',
    { yPercent: 12, opacity: 0.4 },
    { yPercent: -22, opacity: 1, ease: 'none',
      scrollTrigger: { trigger: section, start: 'top bottom', end: 'bottom top', scrub: 1.4 }
    }
  );
})();

// ══ WHAT MAKES — Option B: kinetic-glass cards + scroll-driven horizontal title drift ══
(function() {
  var section = document.querySelector('#whatmakes');
  if (!section) return;
  var title = document.getElementById('wm-title');
  var titleTrack = document.getElementById('wm-title-track');
  var bg = section.querySelector('.wm-bg');
  var cards = section.querySelectorAll('.wm-card');
  var cursor = document.getElementById('wm-cursor');
  var isDesktop = window.matchMedia('(hover:hover) and (min-width: 901px)').matches;

  // Scroll reveal — add .in when title enters viewport
  if (title) {
    var obs = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if (e.isIntersecting) { title.classList.add('in'); obs.disconnect(); } });
    }, { threshold: 0.25 });
    obs.observe(title);
  }

  // Combined scroll handler — bg parallax + title drifts to the right as section enters/exits
  function onScroll(){
    var r = section.getBoundingClientRect();
    var vh = window.innerHeight;
    if (r.bottom < 0 || r.top > vh) return;
    // progress: 0 when section enters bottom of viewport, 1 when its bottom passes top
    var progress = 1 - (r.top + r.height/2) / (vh/2 + r.height/2);
    progress = Math.max(0, Math.min(1, progress));
    if (bg) bg.style.transform = 'translateY(' + (progress * -18).toFixed(1) + 'px) scale(1.06)';
    // ── Title grows as the section scrolls: starts at full size when first visible
    //    and scales up to ~1.18× by the time the section bottom passes the viewport top.
    //    transform-origin:center keeps the growth centered horizontally on the title.
    if (titleTrack) {
      var s = (1 + progress * 0.18).toFixed(3);
      titleTrack.style.transform = 'scale(' + s + ')';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mini gold-dot cursor — only inside this section
  if (cursor && isDesktop) {
    section.addEventListener('mouseenter', function(){ cursor.classList.add('on'); });
    section.addEventListener('mouseleave', function(){ cursor.classList.remove('on'); });
    section.addEventListener('mousemove', function(e){
      cursor.style.left = e.clientX + 'px';
      cursor.style.top  = e.clientY + 'px';
    }, { passive: true });
  }

  // Kinetic 3D tilt + cursor-tracked spotlight on each card
  if (isDesktop) {
    cards.forEach(function(card){
      card.addEventListener('mousemove', function(e){
        var r = card.getBoundingClientRect();
        var x = e.clientX - r.left;
        var y = e.clientY - r.top;
        var cx = r.width / 2, cy = r.height / 2;
        var rx = ((y - cy) / cy) * -7;   /* tilt X (top tilts back) */
        var ry = ((x - cx) / cx) *  7;   /* tilt Y (right tilts away) */
        var angle = Math.atan2(y - cy, x - cx) * (180 / Math.PI) + 90;
        card.style.setProperty('--mouse-x', x + 'px');
        card.style.setProperty('--mouse-y', y + 'px');
        card.style.setProperty('--glare-angle', angle + 'deg');
        card.style.transform = 'perspective(1100px) rotateX(' + rx + 'deg) rotateY(' + ry + 'deg) scale3d(1.02,1.02,1.02)';
      });
      card.addEventListener('mouseleave', function(){
        card.style.transform = 'perspective(1100px) rotateX(0) rotateY(0) scale3d(1,1,1)';
      });
    });
  }
})();

// ══ HERO SCROLL SCALE — title grows then shrinks, never fades out ══
(function() {
  var title = document.querySelector('.hero-title');
  if (!title) return;
  window.addEventListener('scroll', function() {
    var sy = window.scrollY;
    var vh = window.innerHeight;
    // grows 0→40% scroll, shrinks 40→100% — opacity handled by GSAP only
    var ratio = sy / (vh * 0.4);
    var scale;
    if (ratio <= 1) {
      scale = 1 + ratio * 0.18; // max 1.18
    } else {
      var r2 = Math.min((sy - vh*0.4) / (vh*0.6), 1);
      scale = 1.18 - r2 * 0.18;
    }
    title.style.transform = 'scale(' + scale.toFixed(3) + ')';
    // NO opacity change here — GSAP handles it at a gentle min of 0.25
  }, { passive: true });
})();


// (wm-card tilt/scale/mouse handlers removed — flip is now handled purely via CSS :hover on .wm-inner)

// ══ PATH TOWARDS YOUR DREAM LANDSCAPE — GSAP ScrollTrigger pin ══
(function(){
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;
  var section = document.getElementById('process');
  if (!section) return;

  var totalSteps = 4;
  var nums     = section.querySelectorAll('.path-num');
  var contents = section.querySelectorAll('.path-content');
  var photos   = section.querySelectorAll('.path-photo');
  var rails    = section.querySelectorAll('.path-rail-row');
  var progBar  = document.getElementById('path-progressbar');
  var last     = -1;

  function setActive(idx){
    if (idx === last) return;
    last = idx;
    nums.forEach(function(n,i){ n.classList.toggle('is-on', i===idx); });
    contents.forEach(function(n,i){ n.classList.toggle('is-on', i===idx); });
    photos.forEach(function(n,i){ n.classList.toggle('is-on', i===idx); });
    rails.forEach(function(n,i){ n.classList.toggle('is-on', i===idx); });
  }

  // Pin #process itself (100vh) for an additional 260vh of scrolling = 4 stages × 65vh each
  ScrollTrigger.create({
    trigger: section,
    start: 'top top',
    end: '+=900vh',
    pin: true,
    pinSpacing: true,
    onUpdate: function(self){
      var p = self.progress;
      setActive(Math.min(totalSteps - 1, Math.floor(p * totalSteps)));
      if (progBar) progBar.style.setProperty('--p', p.toFixed(4));
    }
  });
  setActive(0);
})();

// ══ BANNER 2 — count-up via GSAP ScrollTrigger (matches site pattern) ══
(function(){
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;
  var bnr2 = document.getElementById('bnr2-section');
  if (!bnr2) return;
  ScrollTrigger.create({
    trigger: bnr2,
    start: 'top 85%',
    once: true,
    onEnter: function(){
      bnr2.querySelectorAll('.bnr2-num[data-count]').forEach(function(n, i){
        var target = parseInt(n.getAttribute('data-count'), 10);
        var suffix = n.getAttribute('data-suffix') || '';
        gsap.to({v: 0}, {
          v: target,
          duration: 2.5,
          ease: 'power4.out',
          delay: i * 0.14,
          onUpdate: function(){ n.textContent = Math.round(this.targets()[0].v) + suffix; }
        });
      });
    }
  });
})();

// ══ BANNER 2 — Service Area town rotator ══
(function(){
  var el = document.getElementById('bnr2-town');
  if (!el) return;
  var towns = ['ATX','WESTLAKE','TARRYTOWN','CIRCLE C','BEE CAVE','BARTON CREEK','DRIPPING SPGS','STEINER RANCH'];
  var idx = 0;
  function next(){
    el.classList.add('fade-out');
    setTimeout(function(){
      idx = (idx + 1) % towns.length;
      el.textContent = towns[idx];
      el.classList.remove('fade-out');
    }, 460);
  }
  setInterval(next, 7800);
})();

// ══ HERO TITLE: scale up on scroll, then fade ══
(function() {
  var title = document.querySelector('.hero-title');
  if (!title) return;
  // Store original letter-spacing to prevent BUILD "I" distortion
  title.style.letterSpacing = '2px';
  title.style.transformOrigin = 'left center';

  window.addEventListener('scroll', function() {
    var sy = window.scrollY;
    var vh = window.innerHeight;
    var ratio = Math.min(sy / (vh * 0.35), 1);
    var scaleDown = Math.min(sy / (vh * 0.7), 1);
    var scale = 1 + ratio * 0.16 - scaleDown * 0.16;
    scale = Math.max(1, Math.min(1.16, scale));
    title.style.transform = 'scale(' + scale.toFixed(3) + ')';
  }, { passive: true });
})();


// ══ TESTIMONIALS — 3D Perspective Carousel ══
(function(){
  var stage   = document.getElementById('td-stage');
  var progBar = document.getElementById('td-prog-bar');
  var counter = document.getElementById('td-counter');
  var prevBtn = document.getElementById('td-prev');
  var nextBtn = document.getElementById('td-next');
  if (!stage) return;
  var cards   = Array.from(stage.querySelectorAll('.td-card'));
  var total   = cards.length;
  var current = 0;
  var dur     = 7000;
  var startTs = null;
  var paused  = false;
  function posFor(idx){
    var diff = idx - current;
    if (diff >  Math.floor(total/2)) diff -= total;
    if (diff < -Math.floor(total/2)) diff += total;
    return diff;
  }
  function render(){
    cards.forEach(function(card){
      var idx = parseInt(card.getAttribute('data-idx'),10);
      var raw = posFor(idx);
      var pos = Math.max(-2, Math.min(2, raw));
      card.setAttribute('data-pos', pos);
      card.style.display = Math.abs(raw) > 2 ? 'none' : '';
    });
    if (counter) counter.textContent = (current + 1) + ' / ' + total;
  }
  function goTo(idx){ current = ((idx % total) + total) % total; render(); startTs = null; }
  if (prevBtn) prevBtn.addEventListener('click', function(){ goTo(current - 1); paused = true; setTimeout(function(){ paused = false; }, 15000); });
  if (nextBtn) nextBtn.addEventListener('click', function(){ goTo(current + 1); paused = true; setTimeout(function(){ paused = false; }, 15000); });
  cards.forEach(function(card){
    card.addEventListener('click', function(){
      var pos = parseInt(card.getAttribute('data-pos'),10);
      if (pos === 1) goTo(current + 1);
      else if (pos === -1) goTo(current - 1);
    });
  });
  function tick(ts){
    if (!startTs) startTs = ts;
    if (paused) { startTs = ts - (current * dur); requestAnimationFrame(tick); if (progBar) progBar.style.transform = 'scaleX(0)'; return; }
    var elapsed = (ts - startTs) % dur;
    if (progBar) progBar.style.transform = 'scaleX(' + (elapsed / dur).toFixed(4) + ')';
    var shouldBe = Math.floor((ts - startTs) / dur) % total;
    if (shouldBe !== current){ current = shouldBe; render(); }
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
  render();
})();

// ══ BOOKING FORM — date slot picker + survey + file upload + submit ══
(function(){
  var SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwyPaQpjdyYbO_zSo9SaXIy99buqABta2Uk3ba6Tkd8vAb-nD3lry1TYQl7w5y4r74s/exec';
  var bookedSlots = [];

  function pad(n){return n<10?'0'+n:String(n)}
  function isoDate(d){return d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())}
  function fmtDate(d){
    var months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    return months[d.getMonth()]+' '+d.getDate();
  }

  function buildSlotGrid(){
    var container = document.getElementById('bk-slot-grid');
    if (!container) return;
    container.innerHTML = '';
    var today = new Date(); today.setHours(0,0,0,0);
    var dayConfig = [{wd:2,name:'Tuesday'},{wd:3,name:'Wednesday'},{wd:4,name:'Thursday'}];
    var times = ['10:00','11:00','12:00'];
    var timeLabels = ['10 AM','11 AM','12 PM'];
    for (var week = 0; week < 3; week++) {
      var weekDiv = document.createElement('div'); weekDiv.className = 'slot-week';
      var firstDate = null;
      dayConfig.forEach(function(dc){
        var d = new Date(today);
        var diff = (dc.wd - today.getDay() + 7) % 7 || 7;
        diff += week * 7; d.setDate(today.getDate() + diff);
        if (!firstDate) firstDate = d;
      });
      if (firstDate) {
        var wl = document.createElement('div'); wl.className = 'slot-week-label';
        wl.textContent = week===0?'Next Available':week===1?'Following Week':'Two Weeks Out';
        weekDiv.appendChild(wl);
      }
      dayConfig.forEach(function(dc){
        var d = new Date(today);
        var diff = (dc.wd - today.getDay() + 7) % 7 || 7;
        diff += week * 7; d.setDate(today.getDate() + diff);
        var iso = isoDate(d); var dateLabel = fmtDate(d);
        var dayGroup = document.createElement('div'); dayGroup.className = 'slot-day-group';
        var dayName = document.createElement('div'); dayName.className = 'slot-day-name';
        dayName.innerHTML = dc.name + '<span class="slot-date-tag">' + dateLabel + '</span>';
        dayGroup.appendChild(dayName);
        var timesDiv = document.createElement('div'); timesDiv.className = 'slot-times';
        times.forEach(function(t, ti){
          var slotKey = iso + ' ' + t;
          var el = document.createElement('div');
          el.className = 'slot' + (bookedSlots.indexOf(slotKey) !== -1 ? ' booked' : '');
          el.dataset.slotKey = slotKey;
          el.innerHTML = '<div class="slot-time">' + timeLabels[ti] + '</div>';
          if (bookedSlots.indexOf(slotKey) === -1) {
            el.addEventListener('click', function(){
              container.querySelectorAll('.slot').forEach(function(s){s.classList.remove('selected')});
              el.classList.add('selected');
              document.getElementById('bk-selected-slot').value = dc.name + ' ' + dateLabel + ' ' + timeLabels[ti];
              document.getElementById('bk-selected-slot-key').value = slotKey;
            });
          }
          timesDiv.appendChild(el);
        });
        dayGroup.appendChild(timesDiv);
        weekDiv.appendChild(dayGroup);
      });
      container.appendChild(weekDiv);
    }
  }

  fetch(SCRIPT_URL + '?action=getBooked')
    .then(function(r){return r.json()})
    .then(function(res){bookedSlots = (res.booked||[]); buildSlotGrid();})
    .catch(function(){buildSlotGrid();});

  // Survey toggle
  document.querySelectorAll('#bk-form .survey-opt').forEach(function(opt){
    function toggle(){
      var group = opt.dataset.group;
      var isMulti = !!opt.closest('.multi');
      if (!isMulti) { document.querySelectorAll('[data-group="'+group+'"]').forEach(function(o){o.classList.remove('active');o.setAttribute('aria-pressed','false')}); }
      var nowActive = opt.classList.toggle('active');
      opt.setAttribute('aria-pressed', nowActive ? 'true' : 'false');
      var vals = Array.from(document.querySelectorAll('[data-group="'+group+'"].active')).map(function(o){return o.textContent.trim()}).join(', ');
      var map = {'bk-budget':'bk-budget-val','bk-services':'bk-services-val','bk-timeline':'bk-timeline-val'};
      var el = document.getElementById(map[group]); if (el) el.value = vals;
    }
    opt.addEventListener('click', toggle);
    opt.addEventListener('keydown', function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();toggle();}});
  });

  // File upload preview
  var photoInput = document.getElementById('bk-photo-input');
  if (photoInput) {
    photoInput.addEventListener('change', function(){
      var prev = document.getElementById('bk-photo-preview'); prev.innerHTML = '';
      Array.from(this.files).forEach(function(f){
        if (f.type.startsWith('image/')) {
          var r = new FileReader();
          r.onload = function(e){ var img = document.createElement('img'); img.src = e.target.result; img.className = 'upload-thumb'; prev.appendChild(img); };
          r.readAsDataURL(f);
        } else {
          var d = document.createElement('div'); d.className = 'upload-file-name'; d.textContent = f.name; prev.appendChild(d);
        }
      });
    });
  }

  // Form submit
  var bkForm = document.getElementById('bk-form');
  if (bkForm) {
    bkForm.addEventListener('submit', function(e){
      e.preventDefault();
      var btn = document.getElementById('bk-submit');
      var txt = document.getElementById('bk-btn-text');
      var fn = document.getElementById('bk-fn').value.trim();
      var fp = document.getElementById('bk-fp').value.trim();
      var fe = document.getElementById('bk-fe').value.trim();
      var fa = document.getElementById('bk-fa').value.trim();
      if (!fn || !fp || !fe || !fa) { alert('Please fill in your name, phone, email, and property address.'); return; }
      if (!document.getElementById('bk-selected-slot-key').value) { alert('Please select a consultation date and time.'); return; }
      btn.style.opacity = '.7'; txt.textContent = 'Sending...';
      var data = {
        name: fn, phone: fp, email: fe,
        address: fa + ' ' + document.getElementById('bk-fc').value + ' ' + document.getElementById('bk-fz').value,
        slot: document.getElementById('bk-selected-slot').value,
        slotKey: document.getElementById('bk-selected-slot-key').value,
        budget: document.getElementById('bk-budget-val').value,
        services: document.getElementById('bk-services-val').value,
        timeline: document.getElementById('bk-timeline-val').value,
        notes: document.getElementById('bk-fnotes').value,
        referral: document.getElementById('bk-fref').value
      };
      fetch(SCRIPT_URL, { method:'POST', mode:'no-cors', body:JSON.stringify(data), headers:{'Content-Type':'text/plain'} })
        .then(function(){
          btn.style.opacity = '1'; btn.classList.add('sent'); txt.textContent = 'Request Sent ✓';
          var s = bkForm.querySelector('.slot.selected');
          if (s) { s.classList.remove('selected'); s.classList.add('booked'); }
        })
        .catch(function(){
          btn.style.opacity = '1'; txt.textContent = 'Request My Consultation →';
          alert('Could not send. Please call or text: 512-695-7566');
        });
    });
  }
})();

(function () {
  function load(el) {
    var src = el.getAttribute('data-bg');
    if (el.hasAttribute('data-bg-m') && window.matchMedia('(max-width: 768px)').matches) src = el.getAttribute('data-bg-m');
    el.style.backgroundImage = "url('" + src + "')";
    el.removeAttribute('data-bg');
    el.removeAttribute('data-bg-m');
  }
  var slides = [].slice.call(document.querySelectorAll('.hslide[data-bg]'));
  window.addEventListener('load', function () {
    setTimeout(function () { slides.forEach(load); }, 1200);
  });
  var lazy = [].slice.call(document.querySelectorAll('[data-bg]')).filter(function (el) {
    return slides.indexOf(el) === -1;
  });
  if (!('IntersectionObserver' in window)) { lazy.forEach(load); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { load(e.target); io.unobserve(e.target); }
    });
  }, { rootMargin: '200px 0px' });
  lazy.forEach(function (el) { io.observe(el); });
})();
