import gradio as gr

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NourishNet</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; scroll-behavior: smooth; }
    body { font-family: 'Inter', sans-serif; background: #F7F5F0; color: #1a1a1a; overflow-x: hidden; }
    .grad {
      background: linear-gradient(120deg, #1D9E75 0%, #0a7a52 60%, #38c98a 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    }
    /* ── NAV ── */
    nav {
      display: flex; align-items: center; justify-content: space-between;
      padding: 18px 48px;
      background: #1D9E75;
      position: sticky; top: 0; z-index: 100;
      border-bottom: 1px solid #0a6350;
    }
    .logo { font-size: 21px; font-weight: 700; color: #fff; cursor: pointer; letter-spacing: -0.01em; }
    .logo span { color: #fff; }
    .nav-links { display: flex; gap: 32px; }
    .nav-link { font-size: 14px; color: #fff; cursor: pointer; transition: color 0.2s; font-weight: 500; }
    .nav-link:hover { color: #fff; }
    .nav-cta {
      font-size: 13px; color: #1D9E75; background: #fff;
      border: none; border-radius: 8px; padding: 9px 20px;
      cursor: pointer; font-weight: 700;
      transition: background 0.2s, transform 0.1s;
    }
    .nav-cta:hover { background: #9FE1CB; transform: translateY(-1px); }
    .tab-btn { font-size:13px;font-weight:600;padding:8px 18px;border-radius:8px;border:1.5px solid #e4e0d8;background:#fff;color:#666;cursor:pointer;font-family:'Inter',sans-serif;transition:all 0.2s; }
    .tab-btn:hover { border-color:#1D9E75;color:#1D9E75; }
    .tab-active { background:#1D9E75 !important;color:#fff !important;border-color:#1D9E75 !important; }
    /* PAGES */
    .page { display: none; animation: fadeIn 0.4s ease; }
    .page.active { display: block; }
    @keyframes fadeIn { from { opacity:0; transform:translateY(14px); } to { opacity:1; transform:translateY(0); } }
    /* ── HERO ── */
    .hero { padding: 100px 48px 84px; text-align: center; max-width: 820px; margin: 0 auto; }
    .hero-eyebrow {
      font-size: 12px; color: #0F6E56; background: #dff4ec;
      display: inline-flex; align-items: center; gap: 6px;
      padding: 6px 14px; border-radius: 20px; margin-bottom: 26px;
      font-weight: 600; letter-spacing: 0.04em; border: 1px solid #b6e8d3;
    }
    .dot { width: 7px; height: 7px; border-radius: 50%; background: #1D9E75; animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.4;transform:scale(1.5)} }
    .hero h1 { font-size: 54px; font-weight: 700; line-height: 1.15; margin-bottom: 24px; letter-spacing: -0.025em; color: #111; }
    .hero p { font-size: 18px; color: #5a5a5a; line-height: 1.8; max-width: 520px; margin: 0 auto 42px; }
    .hero-btns { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
    .btn-primary {
      background: #1D9E75; color: #fff; font-size: 15px; font-weight: 600;
      padding: 15px 32px; border-radius: 10px; border: none; cursor: pointer;
      transition: background 0.2s, transform 0.15s; font-family: 'Inter', sans-serif;
    }
    .btn-primary:hover { background: #0a6350; transform: translateY(-2px); }
    .btn-outline {
      background: transparent; color: #1D9E75; font-size: 15px; font-weight: 600;
      padding: 15px 32px; border-radius: 10px; border: 1.5px solid #1D9E75;
      cursor: pointer; transition: all 0.2s; font-family: 'Inter', sans-serif;
    }
    .btn-outline:hover { background: #dff4ec; transform: translateY(-2px); }
    .hero-sub { font-size: 12px; color: #b0a898; margin-top: 16px; }
    /* STATS */
    .stats-bar {
      display: grid; grid-template-columns: repeat(4,1fr);
      background: #1D9E75;
    }
    .stat { padding: 36px 20px; text-align: center; border-right: 1px solid #0a6350; }
    .stat:last-child { border-right: none; }
    .stat-val { font-size: 32px; font-weight: 700; color: #fff; }
    .stat-lbl { font-size: 13px; color: #fff; margin-top: 6px; font-weight: 500; }
    /* SECTIONS */
    .section { padding: 84px 48px; max-width: 1020px; margin: 0 auto; }
    .section-label { font-size: 12px; color: #999; text-align: center; margin-bottom: 12px; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 600; }
    .section-title { font-size: 36px; font-weight: 700; text-align: center; margin-bottom: 14px; letter-spacing: -0.015em; color: #111; }
    .section-sub { font-size: 16px; color: #666; text-align: center; margin-bottom: 52px; line-height: 1.75; max-width: 560px; margin-left: auto; margin-right: auto; }
    .steps-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; }
    .step-card {
      background: #fff; border: 1px solid #e4e0d8; border-radius: 16px;
      padding: 32px 26px; transition: border-color 0.2s, transform 0.2s;
    }
    .step-card:hover { border-color: #1D9E75; transform: translateY(-4px); }
    .step-icon { width: 48px; height: 48px; border-radius: 12px; background: #dff4ec; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; font-size: 22px; }
    .step-title { font-size: 17px; font-weight: 700; margin-bottom: 10px; color: #111; }
    .step-desc { font-size: 14px; color: #666; line-height: 1.75; }
    /* ROUTING */
    .routing-section { background: #eeeae2; padding: 84px 48px; border-top: 1px solid #e4e0d8; border-bottom: 1px solid #e4e0d8; }
    .routing-inner { max-width: 920px; margin: 0 auto; }
    .routing-grid { display: grid; grid-template-columns: 1fr auto 1fr; gap: 28px; align-items: center; margin-top: 52px; }
    .routing-col { display: flex; flex-direction: column; gap: 12px; }
    .routing-card {
      background: #fff; border: 1px solid #e4e0d8; border-radius: 12px;
      padding: 14px 16px; font-size: 14px; font-weight: 500;
      display: flex; align-items: center; gap: 12px; transition: border-color 0.2s; color: #1a1a1a;
    }
    .routing-card:hover { border-color: #1D9E75; }
    .routing-card .rinfo { font-size: 12px; color: #888; font-weight: 400; margin-top: 2px; }
    .routing-mid { display: flex; flex-direction: column; align-items: center; gap: 10px; }
    .ai-box { background: #1D9E75; color: #fff; border-radius: 14px; padding: 22px 16px; text-align: center; font-weight: 700; font-size: 14px; width: 118px; }
    .ai-box .ai-sub { font-size: 11px; font-weight: 400; opacity: 0.75; margin-top: 5px; }
    .arrow { font-size: 22px; color: #1D9E75; font-weight: 700; }
    /* CTA */
    .cta-section {
      margin: 0 48px 84px; background: #1D9E75;
      border-radius: 24px; padding: 68px 48px; text-align: center;
    }
    .cta-title { font-size: 36px; font-weight: 700; margin-bottom: 14px; letter-spacing: -0.01em; color: #fff; }
    .cta-sub { font-size: 16px; color: #d0f5e8; margin-bottom: 32px; line-height: 1.75; }
    .cta-btn {
      background: #fff; color: #1D9E75; font-size: 15px; font-weight: 700;
      padding: 15px 32px; border-radius: 10px; border: none; cursor: pointer;
      transition: background 0.2s, transform 0.15s; font-family: 'Inter', sans-serif;
    }
    .cta-btn:hover { background: #9FE1CB; transform: translateY(-2px); }
    /* ── APP SHELL ── */
    .app-shell { max-width: 420px; margin: 40px auto; background: #F7F5F0; border: 1px solid #e4e0d8; border-radius: 28px; overflow: hidden; box-shadow: 0 12px 48px rgba(0,0,0,0.10); }
    .app-screen { display: none; flex-direction: column; min-height: 680px; }
    .app-screen.active { display: flex; }
    .app-topbar { padding: 18px 20px 14px; border-bottom: 1px solid #e4e0d8; display: flex; align-items: center; gap: 10px; background: #1D9E75; }
    .app-back { background: none; border: none; font-size: 20px; cursor: pointer; color: #fff; padding: 0; }
    .app-topbar h2 { font-size: 17px; font-weight: 700; flex: 1; color: #fff; }
    .app-body { padding: 18px; flex: 1; overflow-y: auto; background: #eeeae2; }
    .app-nav { display: flex; border-top: 1px solid #e4e0d8; background: #1D9E75; }
    .app-nav-btn { flex: 1; padding: 12px 0 10px; font-size: 10px; color: #d0f5e8; background: none; border: none; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 4px; font-family: 'Inter', sans-serif; font-weight: 600; transition: color 0.2s; }
    .app-nav-btn.active { color: #fff; }
    .app-nav-icon { font-size: 20px; }
    .acard { background: #fff; border: 1px solid #e4e0d8; border-radius: 14px; padding: 16px; margin-bottom: 14px; }
    .acard-title { font-size: 11px; font-weight: 700; color: #999; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.07em; }
    .ametric-row { display: grid; grid-template-columns: repeat(3,1fr); gap: 8px; margin-bottom: 14px; }
    .ametric { background: #f0f7f4; border-radius: 10px; padding: 12px 8px; text-align: center; }
    .ametric-val { font-size: 20px; font-weight: 700; color: #1D9E75; }
    .ametric-lbl { font-size: 10px; color: #888; margin-top: 3px; font-weight: 500; }
    .abadge { display: inline-block; font-size: 11px; padding: 3px 10px; border-radius: 20px; font-weight: 600; }
    .abadge-green { background: #dff4ec; color: #0F6E56; }
    .abadge-amber { background: #FAEEDA; color: #854F0B; }
    .abadge-blue  { background: #E6F1FB; color: #185FA5; }
    .abadge-coral { background: #FAECE7; color: #993C1D; }
    .arow { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
    .abig { font-size: 15px; font-weight: 600; color: #111; }
    .asub { font-size: 12px; color: #888; margin-top: 2px; }
    .adivider { height: 1px; background: #eee; margin: 12px 0; }
    .abtn { width: 100%; padding: 13px; border-radius: 10px; font-size: 14px; font-weight: 600; cursor: pointer; border: none; font-family: 'Inter', sans-serif; transition: transform 0.1s, background 0.2s; }
    .abtn:active { transform: scale(0.98); }
    .abtn-primary { background: #1D9E75; color: #fff; }
    .abtn-primary:hover { background: #0a6350; }
    .abtn-secondary { background: #e4e0d8; color: #1a1a1a; margin-top: 8px; }
    .aprogress { height: 6px; border-radius: 3px; background: #e4e0d8; margin-top: 8px; overflow: hidden; }
    .aprogress-fill { height: 100%; border-radius: 3px; background: #1D9E75; }
    .aicon-circle { width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; }
    select { width: 100%; padding: 10px 12px; border-radius: 10px; border: 1px solid #e4e0d8; font-size: 14px; background: #fff; color: #1a1a1a; margin-bottom: 12px; font-family: 'Inter', sans-serif; }
    input[type=range] { width: 100%; accent-color: #1D9E75; }
    .recipient-card { border: 1px solid #e4e0d8; border-radius: 12px; padding: 13px; margin-bottom: 10px; display: flex; align-items: center; gap: 12px; cursor: pointer; background: #fff; transition: border-color 0.2s, background 0.2s; }
    .recipient-card.selected { border-color: #1D9E75; background: #f0fdf8; }
    .lboard-row { display: flex; align-items: center; gap: 12px; padding: 11px 0; border-bottom: 1px solid #f0ede6; }
    .lboard-rank { font-size: 14px; font-weight: 700; color: #ccc; width: 22px; }
    .lboard-rank.gold { color: #BA7517; }
    .lboard-rank.silver { color: #888; }
    .step-dot { width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0; }
    .step-done   { background: #dff4ec; color: #0F6E56; }
    .step-active { background: #FAEEDA; color: #854F0B; }
    .step-pending{ background: #eee; color: #bbb; }
    .step-connector { width: 2px; height: 18px; background: #e4e0d8; margin: 3px 0 3px 12px; }
    /* ABOUT */
    .about-hero { padding: 84px 48px 64px; text-align: center; max-width: 740px; margin: 0 auto; }
    .about-hero h1 { font-size: 42px; font-weight: 700; margin-bottom: 20px; letter-spacing: -0.015em; color: #111; }
    .about-hero p { font-size: 17px; color: #5a5a5a; line-height: 1.8; }
    .team-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; max-width: 900px; margin: 0 auto 84px; padding: 0 48px; }
    .team-card { background: #fff; border: 1px solid #e4e0d8; border-radius: 16px; padding: 30px 20px; text-align: center; transition: transform 0.2s; }
    .team-card:hover { transform: translateY(-4px); }
    .team-avatar { width: 64px; height: 64px; border-radius: 50%; margin: 0 auto 14px; display: flex; align-items: center; justify-content: center; font-size: 26px; }
    .team-name { font-size: 15px; font-weight: 700; margin-bottom: 5px; color: #111; }
    .team-role { font-size: 13px; color: #888; line-height: 1.5; }
    .mission-section { background: #1D9E75; padding: 76px 48px; text-align: center; }
    .mission-section h2 { font-size: 30px; font-weight: 700; margin-bottom: 18px; color: #fff; }
    .mission-section p { font-size: 16px; color: #d0f5e8; max-width: 600px; margin: 0 auto; line-height: 1.8; }
    /* FOOTER */
    footer { padding: 28px 48px; background: #1D9E75; display: flex; align-items: center; justify-content: space-between; border-top: 1px solid #0a6350; }
    .footer-logo { font-size: 16px; font-weight: 700; color: #fff; }
    .footer-logo span { color: #fff; }
    .footer-links { display: flex; gap: 20px; }
    .footer-link { font-size: 13px; color: #d0f5e8; cursor: pointer; transition: color 0.2s; }
    .footer-link:hover { color: #fff; }
    .footer-text { font-size: 12px; color: #d0f5e8; }
    @media (max-width: 640px) {
      nav { padding: 14px 20px; }
      .nav-links { display: none; }
      .hero { padding: 56px 20px 48px; }
      .hero h1 { font-size: 32px; }
      .stats-bar { grid-template-columns: repeat(2,1fr); }
      .section { padding: 56px 20px; }
      .steps-grid { grid-template-columns: 1fr; }
      .routing-grid { grid-template-columns: 1fr; }
      .cta-section { margin: 0 20px 56px; padding: 40px 24px; }
      footer { padding: 20px; flex-direction: column; gap: 10px; text-align: center; }
      .team-grid { grid-template-columns: 1fr; padding: 0 20px; }
      .about-hero { padding: 56px 20px 40px; }
      .about-hero h1 { font-size: 30px; }
    }
  </style>
</head>
<body>
<nav>
  <div class="logo" onclick="showPage('home')">Nourish<span>Net</span></div>
  <div class="nav-links">
    <span class="nav-link" onclick="showPage('home')">Home</span>
    <span class="nav-link" onclick="showPage('app')">App demo</span>
    <span class="nav-link" onclick="showPage('about')">About</span>
  </div>
  <button class="nav-cta" onclick="showPage('app')">Try the demo</button>
</nav>
<!-- HOME PAGE -->
<div class="page active" id="page-home">
  <section class="hero">
    <div class="hero-eyebrow"><span class="dot"></span> Live in UAE · Powered by AI</div>
    <h1>Turn tonight's surplus<br>into <span class="grad">tomorrow's meal</span></h1>
    <p>3.27 million tons of food wasted in the UAE every year. NourishNet automatically routes your surplus to elderly homes, refugee centers, and families in need.</p>
    <div class="hero-btns">
      <button class="btn-primary" onclick="showPage('app')">Try the app demo</button>
      <button class="btn-outline" onclick="document.getElementById('how').scrollIntoView({behavior:'smooth'})">See how it works</button>
    </div>
    <div class="hero-sub">Free to join · No technical setup · Takes 2 minutes</div>
  </section>
  <div class="stats-bar">
    <div class="stat"><div class="stat-val" id="c1">0</div><div class="stat-lbl">Meals saved</div></div>
    <div class="stat"><div class="stat-val" id="c2">0</div><div class="stat-lbl">Restaurants</div></div>
    <div class="stat"><div class="stat-val" id="c3">0</div><div class="stat-lbl">CO₂ avoided</div></div>
    <div class="stat"><div class="stat-val" id="c4">0</div><div class="stat-lbl">Communities</div></div>
  </div>
  <section class="section" id="how">
    <div class="section-label">How it works</div>
    <div class="section-title">Three steps. <span class="grad">Zero waste.</span></div>
    <div class="section-sub">No complicated setup. No manual coordination. Just surplus food reaching people who need it.</div>
    <div class="steps-grid">
      <div class="step-card">
        <div class="step-icon">📋</div>
        <div class="step-title">Log your surplus</div>
        <div class="step-desc">Tell us what food you have, the quantity, and when it expires. Our simple form takes under 30 seconds.</div>
      </div>
      <div class="step-card">
        <div class="step-icon">🤖</div>
        <div class="step-title">AI routes it instantly</div>
        <div class="step-desc">Our AI analyzes food type, quantity, expiry, and location to match surplus with the perfect recipient community.</div>
      </div>
      <div class="step-card">
        <div class="step-icon">🚗</div>
        <div class="step-title">Volunteer delivers it</div>
        <div class="step-desc">A verified volunteer picks up and delivers. You get a live tracker and confirmed impact report when done.</div>
      </div>
    </div>
  </section>
  <div class="routing-section">
    <div class="routing-inner">
      <div class="section-label">Smart routing engine</div>
      <div class="section-title">Right food. <span class="grad">Right people.</span></div>
      <div class="section-sub">Quantity and food type determine who gets the food — not chance.</div>
      <div class="routing-grid">
        <div class="routing-col">
          <div style="font-size:12px;font-weight:700;color:#999;margin-bottom:6px;letter-spacing:0.06em;text-transform:uppercase">Donors</div>
          <div class="routing-card"><span style="font-size:20px">🍽️</span><div><div>Al Baik Restaurant</div><div class="rinfo">60 portions · halal · 4hrs</div></div></div>
          <div class="routing-card"><span style="font-size:20px">🥖</span><div><div>Sunset Bakery</div><div class="rinfo">120 bread loaves · 2hrs</div></div></div>
          <div class="routing-card"><span style="font-size:20px">🏨</span><div><div>Grand Hyatt Hotel</div><div class="rinfo">200 portions · varied · today</div></div></div>
        </div>
        <div class="routing-mid">
          <div class="arrow">→</div>
          <div class="ai-box">🤖 AI<div class="ai-sub">Matches in seconds</div></div>
          <div class="arrow">→</div>
        </div>
        <div class="routing-col">
          <div style="font-size:12px;font-weight:700;color:#999;margin-bottom:6px;letter-spacing:0.06em;text-transform:uppercase">Recipients</div>
          <div class="routing-card"><span style="font-size:20px">🧓</span><div><div>Al Qasba Elderly Home</div><div class="rinfo">Needs 40–80 · halal ✓</div></div></div>
          <div class="routing-card"><span style="font-size:20px">🛖</span><div><div>Sharjah Refugee Center</div><div class="rinfo">Needs 100+ · any food</div></div></div>
          <div class="routing-card"><span style="font-size:20px">👨‍👩‍👧</span><div><div>Low-income Families</div><div class="rinfo">Flexible · neighborhood</div></div></div>
        </div>
      </div>
    </div>
  </div>
  <section class="section">
    <div class="section-label">Gamification</div>
    <div class="section-title">Donate. Earn. <span class="grad">Compete.</span></div>
    <div class="section-sub">Every donation earns points, badges, and public recognition — turning sustainability into a brand advantage.</div>
    <div class="steps-grid">
      <div class="step-card">
        <div class="step-icon">🏆</div>
        <div class="step-title">City leaderboard</div>
        <div class="step-desc">Compete with restaurants across Dubai and Sharjah. Top donors get featured on Google Maps and press coverage.</div>
      </div>
      <div class="step-card">
        <div class="step-icon">🔥</div>
        <div class="step-title">Donation streaks</div>
        <div class="step-desc">Donate 7 days in a row and earn the Community Hero badge. Keep going to unlock Zero Waste Champion status.</div>
      </div>
      <div class="step-card">
        <div class="step-icon">📊</div>
        <div class="step-title">Impact dashboard</div>
        <div class="step-desc">See exactly who you fed, how much CO₂ you saved, and receive real messages from recipient communities.</div>
      </div>
    </div>
  </section>
  <section class="cta-section">
    <div class="cta-title">Ready to make an impact?</div>
    <div class="cta-sub">Join 186 restaurants already feeding communities across the UAE.<br>Free, takes 2 minutes, first pickup is same-day.</div>
    <button class="cta-btn" onclick="showPage('app')">Try the app demo →</button>
  </section>
  <footer>
    <div class="footer-logo">Nourish<span>Net</span></div>
    <div class="footer-links">
      <span class="footer-link" onclick="showPage('home')">Home</span>
      <span class="footer-link" onclick="showPage('app')">App demo</span>
      <span class="footer-link" onclick="showPage('about')">About</span>
    </div>
    <div class="footer-text">UAE · 2025 · Partnered with UAE Food Bank & Ne'ma</div>
  </footer>
</div>
<!-- APP DEMO PAGE -->
<div class="page" id="page-app">
  <div style="background:#1D9E75;padding:56px 48px 48px;text-align:center">
    <div style="font-size:12px;color:#9FE1CB;letter-spacing:0.1em;text-transform:uppercase;font-weight:600;margin-bottom:12px">Interactive demo</div>
    <div style="font-size:36px;font-weight:700;color:#fff;letter-spacing:-0.02em;margin-bottom:14px">The NourishNet restaurant app</div>
    <p style="color:#9FE1CB;font-size:16px;max-width:480px;margin:0 auto;line-height:1.7">A full walkthrough of how restaurants log surplus, get AI-matched to communities, and track their real-world impact.</p>
  </div>
  <div style="background:#F7F5F0;padding:24px 48px;border-bottom:1px solid #e4e0d8;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
    <button onclick="showAppScreen('as-home');highlightTab(this)" class="tab-btn tab-active">🏠 Home</button>
    <button onclick="showAppScreen('as-donate');highlightTab(this)" class="tab-btn">➕ Donate</button>
    <button onclick="showAppScreen('as-impact');highlightTab(this)" class="tab-btn">📊 Impact</button>
    <button onclick="showAppScreen('as-leaderboard');highlightTab(this)" class="tab-btn">🏆 Leaderboard</button>
  </div>
  <div style="display:grid;grid-template-columns:1fr 420px;gap:48px;max-width:1020px;margin:0 auto;padding:48px">
    <div id="screen-desc" style="padding-top:8px">
      <div id="desc-home">
        <div style="font-size:12px;font-weight:700;color:#1D9E75;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:12px">Home screen</div>
        <div style="font-size:28px;font-weight:700;color:#111;letter-spacing:-0.01em;margin-bottom:16px;line-height:1.25">Your restaurant dashboard at a glance</div>
        <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:24px">The home screen shows this week's impact metrics, the AI's prediction for tonight's surplus, and your current donation streak — all in one place.</p>
        <div style="display:flex;flex-direction:column;gap:12px">
          <div style="display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #e4e0d8;border-radius:12px;padding:16px">
            <div style="width:36px;height:36px;border-radius:9px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0">📊</div>
            <div><div style="font-size:14px;font-weight:700;color:#111;margin-bottom:4px">Live impact metrics</div><div style="font-size:13px;color:#666;line-height:1.6">Meals saved, CO₂ avoided, and points earned update in real time each week.</div></div>
          </div>
          <div style="display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #e4e0d8;border-radius:12px;padding:16px">
            <div style="width:36px;height:36px;border-radius:9px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0">🤖</div>
            <div><div style="font-size:14px;font-weight:700;color:#111;margin-bottom:4px">AI surplus prediction</div><div style="font-size:13px;color:#666;line-height:1.6">The AI predicts tonight's leftover portions before they happen, based on your history.</div></div>
          </div>
          <div style="display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #e4e0d8;border-radius:12px;padding:16px">
            <div style="width:36px;height:36px;border-radius:9px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0">🔥</div>
            <div><div style="font-size:14px;font-weight:700;color:#111;margin-bottom:4px">Donation streak tracker</div><div style="font-size:13px;color:#666;line-height:1.6">Build a streak to unlock badges like Community Hero and Zero Waste Champion.</div></div>
          </div>
        </div>
      </div>
      <div id="desc-donate" style="display:none">
        <div style="font-size:12px;font-weight:700;color:#1D9E75;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:12px">Donate screen</div>
        <div style="font-size:28px;font-weight:700;color:#111;letter-spacing:-0.01em;margin-bottom:16px;line-height:1.25">Log surplus in 30 seconds</div>
        <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:24px">Just tell the app what food you have, how many portions, and when it expires. The AI instantly recommends the best recipient — no manual searching needed.</p>
        <div style="display:flex;flex-direction:column;gap:12px">
          <div style="display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #e4e0d8;border-radius:12px;padding:16px">
            <div style="width:36px;height:36px;border-radius:9px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0">🎚️</div>
            <div><div style="font-size:14px;font-weight:700;color:#111;margin-bottom:4px">Portion slider</div><div style="font-size:13px;color:#666;line-height:1.6">Drag the slider — the AI recommendation updates live as the quantity changes.</div></div>
          </div>
          <div style="display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #e4e0d8;border-radius:12px;padding:16px">
            <div style="width:36px;height:36px;border-radius:9px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0">🗺️</div>
            <div><div style="font-size:14px;font-weight:700;color:#111;margin-bottom:4px">Smart matching</div><div style="font-size:13px;color:#666;line-height:1.6">Small batches go to nearby elderly individuals. Large ones route to refugee centers or food banks.</div></div>
          </div>
          <div style="display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #e4e0d8;border-radius:12px;padding:16px">
            <div style="width:36px;height:36px;border-radius:9px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0">✅</div>
            <div><div style="font-size:14px;font-weight:700;color:#111;margin-bottom:4px">One-tap confirm</div><div style="font-size:13px;color:#666;line-height:1.6">Tap confirm and a volunteer is dispatched automatically — no phone calls needed.</div></div>
          </div>
        </div>
      </div>
      <div id="desc-impact" style="display:none">
        <div style="font-size:12px;font-weight:700;color:#1D9E75;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:12px">Impact screen</div>
        <div style="font-size:28px;font-weight:700;color:#111;letter-spacing:-0.01em;margin-bottom:16px;line-height:1.25">See exactly who you fed</div>
        <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:24px">Every donation creates a story. See which communities received your food, how much CO₂ you saved, and read real thank-you messages from recipients.</p>
        <div style="background:#dff4ec;border:1px solid #9FE1CB;border-radius:14px;padding:20px 22px">
          <div style="font-size:13px;color:#085041;line-height:1.75;font-style:italic">"Your Monday surplus fed 47 elderly residents at Al Qasba Care Home, saving 12kg of CO₂ and providing a warm halal meal to people who needed it most."</div>
          <div style="font-size:12px;color:#1D9E75;margin-top:10px;font-weight:600">— Al Qasba Elderly Home · 2 days ago</div>
        </div>
      </div>
      <div id="desc-leaderboard" style="display:none">
        <div style="font-size:12px;font-weight:700;color:#1D9E75;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:12px">Leaderboard screen</div>
        <div style="font-size:28px;font-weight:700;color:#111;letter-spacing:-0.01em;margin-bottom:16px;line-height:1.25">Compete with restaurants citywide</div>
        <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:24px">A live city leaderboard ranks restaurants by total meals donated. Top spots earn public recognition, press features, and verified sustainability badges on Google Maps.</p>
        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="background:#FAEEDA;border-radius:10px;padding:14px 16px;display:flex;align-items:center;gap:12px">
            <span style="font-size:20px;font-weight:700;color:#BA7517">🥇</span>
            <div><div style="font-size:13px;font-weight:700;color:#633806">Zero Waste Champion</div><div style="font-size:12px;color:#854F0B">Donate the most meals in your city this month</div></div>
          </div>
          <div style="background:#dff4ec;border-radius:10px;padding:14px 16px;display:flex;align-items:center;gap:12px">
            <span style="font-size:20px;font-weight:700;color:#0F6E56">🏅</span>
            <div><div style="font-size:13px;font-weight:700;color:#085041">Community Hero</div><div style="font-size:12px;color:#1D9E75">Maintain a 7-day donation streak</div></div>
          </div>
          <div style="background:#E6F1FB;border-radius:10px;padding:14px 16px;display:flex;align-items:center;gap:12px">
            <span style="font-size:20px;font-weight:700;color:#185FA5">⭐</span>
            <div><div style="font-size:13px;font-weight:700;color:#0C447C">1,000 Meals Badge</div><div style="font-size:12px;color:#185FA5">Reach 1,000 total meals donated</div></div>
          </div>
        </div>
      </div>
    </div>
    <div class="app-shell" style="margin:0">
    <!-- HOME SCREEN -->
    <div class="app-screen active" id="as-home">
      <div class="app-topbar">
        <div>
          <div style="font-size:17px;font-weight:700;color:#fff">Nourish<span style="color:#fff">Net</span></div>
          <div style="font-size:11px;color:#d0f5e8;margin-top:1px">Al Baik Restaurant · Dubai</div>
        </div>
        <div style="margin-left:auto"><span class="abadge abadge-green">● Active</span></div>
      </div>
      <div class="app-body">
        <div style="font-size:11px;font-weight:700;color:#888;margin-bottom:10px;text-transform:uppercase;letter-spacing:0.07em">This week</div>
        <div class="ametric-row">
          <div class="ametric"><div class="ametric-val">142</div><div class="ametric-lbl">Meals saved</div></div>
          <div class="ametric"><div class="ametric-val">38kg</div><div class="ametric-lbl">CO₂ avoided</div></div>
          <div class="ametric"><div class="ametric-val">720</div><div class="ametric-lbl">Points</div></div>
        </div>
        <div class="acard">
          <div class="acard-title">AI prediction — tonight</div>
          <div class="arow">
            <div><div class="abig">~60 surplus portions</div><div class="asub">Lamb kofta · expires in 5 hrs</div></div>
            <span class="abadge abadge-amber">Urgent</span>
          </div>
          <div class="adivider"></div>
          <div style="font-size:12px;color:#888;margin-bottom:10px;font-weight:500">Best AI match</div>
          <div class="arow" style="margin-bottom:14px">
            <div class="aicon-circle" style="background:#dff4ec">🏠</div>
            <div style="flex:1;margin-left:4px">
              <div class="abig" style="font-size:14px">Al Qasba Elderly Home</div>
              <div class="asub">2.1 km · capacity 80 · halal ✓</div>
            </div>
          </div>
          <button class="abtn abtn-primary" onclick="showAppScreen('as-donate')">Log surplus & route →</button>
        </div>
        <div class="acard">
          <div class="acard-title">Donation streak</div>
          <div class="arow" style="margin-bottom:8px">
            <div class="abig">🔥 7 days</div>
            <span class="abadge abadge-blue">Community Hero</span>
          </div>
          <div class="aprogress"><div class="aprogress-fill" style="width:70%"></div></div>
          <div style="font-size:11px;color:#aaa;margin-top:6px">3 more days → Zero Waste Champion</div>
        </div>
        <button class="abtn abtn-secondary" onclick="showAppScreen('as-impact')">View my impact →</button>
      </div>
      <div class="app-nav">
        <button class="app-nav-btn active" onclick="showAppScreen('as-home')"><span class="app-nav-icon">🏠</span>Home</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-donate')"><span class="app-nav-icon">➕</span>Donate</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-impact')"><span class="app-nav-icon">📊</span>Impact</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-leaderboard')"><span class="app-nav-icon">🏆</span>Ranks</button>
      </div>
    </div>
    <!-- DONATE SCREEN -->
    <div class="app-screen" id="as-donate">
      <div class="app-topbar">
        <button class="app-back" onclick="showAppScreen('as-home')">←</button>
        <h2>Log surplus food</h2>
      </div>
      <div class="app-body">
        <div style="font-size:11px;font-weight:700;color:#888;margin-bottom:6px;text-transform:uppercase;letter-spacing:0.07em">Food type</div>
        <select id="food-type" onchange="updateRouting()">
          <option>Cooked meals (halal)</option>
          <option>Baked goods / bread</option>
          <option>Raw produce</option>
          <option>Packaged / dry goods</option>
        </select>
        <div style="font-size:11px;font-weight:700;color:#888;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.07em">Portions: <span id="qty-val" style="color:#1D9E75">60</span></div>
        <input type="range" min="1" max="250" value="60" step="1" id="qty-slider" oninput="updateQty(this.value)" style="margin-bottom:16px">
        <div style="font-size:11px;font-weight:700;color:#888;margin-bottom:6px;text-transform:uppercase;letter-spacing:0.07em">Expires in</div>
        <select id="expiry" onchange="updateRouting()">
          <option>Less than 2 hours</option>
          <option selected>2–6 hours</option>
          <option>Same day</option>
          <option>Tomorrow</option>
        </select>
        <div class="adivider"></div>
        <div style="font-size:12px;font-weight:700;color:#1D9E75;margin-bottom:8px">🤖 AI recommendation</div>
        <div id="ai-rec" style="background:#f0fdf8;border:1px solid #9FE1CB;border-radius:10px;padding:12px 14px;font-size:13px;color:#1D9E75;line-height:1.65;margin-bottom:14px">
          Based on 60 halal portions expiring in 2–6 hrs: best match is an <strong>elderly care home</strong> within 3km.
        </div>
        <div style="font-size:11px;font-weight:700;color:#888;margin-bottom:10px;text-transform:uppercase;letter-spacing:0.07em">Matched recipients</div>
        <div id="recipients">
          <div class="recipient-card selected" onclick="selectRecipient(this)">
            <div class="aicon-circle" style="background:#dff4ec">🏠</div>
            <div style="flex:1"><div class="abig" style="font-size:14px">Al Qasba Elderly Home</div><div class="asub">2.1 km · halal ✓ · 40–80 portions</div></div>
            <span class="abadge abadge-green">Best</span>
          </div>
          <div class="recipient-card" onclick="selectRecipient(this)">
            <div class="aicon-circle" style="background:#E6F1FB">🛖</div>
            <div style="flex:1"><div class="abig" style="font-size:14px">Sharjah Refugee Center</div><div class="asub">4.3 km · halal ✓ · 100–200 portions</div></div>
          </div>
        </div>
        <button class="abtn abtn-primary" onclick="showAppScreen('as-confirm')">Confirm donation →</button>
      </div>
      <div class="app-nav">
        <button class="app-nav-btn" onclick="showAppScreen('as-home')"><span class="app-nav-icon">🏠</span>Home</button>
        <button class="app-nav-btn active"><span class="app-nav-icon">➕</span>Donate</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-impact')"><span class="app-nav-icon">📊</span>Impact</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-leaderboard')"><span class="app-nav-icon">🏆</span>Ranks</button>
      </div>
    </div>
    <!-- CONFIRM SCREEN -->
    <div class="app-screen" id="as-confirm">
      <div class="app-topbar">
        <button class="app-back" onclick="showAppScreen('as-donate')">←</button>
        <h2>Pickup confirmed ✓</h2>
      </div>
      <div class="app-body" style="display:flex;flex-direction:column;align-items:center;padding-top:28px">
        <div style="width:72px;height:72px;border-radius:50%;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:36px;margin-bottom:16px">✓</div>
        <div style="font-size:19px;font-weight:700;margin-bottom:6px;color:#1D9E75">Pickup scheduled!</div>
        <div style="font-size:13px;color:#888;margin-bottom:28px">Volunteer confirmed · ETA 35 mins</div>
        <div class="acard" style="width:100%">
          <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:12px">
            <div class="step-dot step-done">✓</div>
            <div><div class="abig" style="font-size:13px">Surplus logged</div><div class="asub">60 portions · halal cooked meals</div></div>
          </div>
          <div class="step-connector"></div>
          <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:12px">
            <div class="step-dot step-done">✓</div>
            <div><div class="abig" style="font-size:13px">AI matched recipient</div><div class="asub">Al Qasba Elderly Home · 2.1km</div></div>
          </div>
          <div class="step-connector"></div>
          <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:12px">
            <div class="step-dot step-active">→</div>
            <div><div class="abig" style="font-size:13px">Volunteer en route</div><div class="asub">Ahmed K. · pickup at 8:30 PM</div></div>
          </div>
          <div class="step-connector"></div>
          <div style="display:flex;gap:10px;align-items:flex-start">
            <div class="step-dot step-pending">4</div>
            <div><div class="abig" style="font-size:13px;color:#bbb">Delivery confirmed</div><div class="asub">Pending</div></div>
          </div>
        </div>
        <div class="acard" style="width:100%">
          <div class="acard-title">Points earned</div>
          <div class="arow">
            <div class="abig">+120 points</div>
            <span class="abadge abadge-green">Streak +1 🔥</span>
          </div>
          <div style="font-size:12px;color:#888;margin-top:5px">Total: 840 pts · Rank #3 in Dubai</div>
        </div>
        <button class="abtn abtn-primary" style="width:100%" onclick="showAppScreen('as-home')">Back to home</button>
      </div>
    </div>
    <!-- IMPACT SCREEN -->
    <div class="app-screen" id="as-impact">
      <div class="app-topbar">
        <button class="app-back" onclick="showAppScreen('as-home')">←</button>
        <h2>Your impact</h2>
      </div>
      <div class="app-body">
        <div class="ametric-row">
          <div class="ametric"><div class="ametric-val">1,240</div><div class="ametric-lbl">Total meals</div></div>
          <div class="ametric"><div class="ametric-val">312kg</div><div class="ametric-lbl">CO₂ saved</div></div>
          <div class="ametric"><div class="ametric-val">AED 4.2k</div><div class="ametric-lbl">Costs saved</div></div>
        </div>
        <div class="acard">
          <div class="acard-title">Who you've fed</div>
          <div style="margin-bottom:12px">
            <div class="arow" style="margin-bottom:5px"><div style="display:flex;align-items:center;gap:8px"><span>🧓</span><div class="abig" style="font-size:13px">Elderly homes</div></div><div style="font-size:13px;font-weight:700;color:#1D9E75">48%</div></div>
            <div class="aprogress"><div class="aprogress-fill" style="width:48%"></div></div>
          </div>
          <div style="margin-bottom:12px">
            <div class="arow" style="margin-bottom:5px"><div style="display:flex;align-items:center;gap:8px"><span>🛖</span><div class="abig" style="font-size:13px">Refugee centers</div></div><div style="font-size:13px;font-weight:700;color:#185FA5">31%</div></div>
            <div class="aprogress"><div class="aprogress-fill" style="width:31%;background:#185FA5"></div></div>
          </div>
          <div>
            <div class="arow" style="margin-bottom:5px"><div style="display:flex;align-items:center;gap:8px"><span>👨‍👩‍👧</span><div class="abig" style="font-size:13px">Low-income families</div></div><div style="font-size:13px;font-weight:700;color:#BA7517">21%</div></div>
            <div class="aprogress"><div class="aprogress-fill" style="width:21%;background:#BA7517"></div></div>
          </div>
        </div>
        <div class="acard">
          <div class="acard-title">Latest message</div>
          <div style="font-size:13px;color:#333;line-height:1.7;font-style:italic">"Your Monday surplus fed 47 elderly residents at Al Qasba, saving 12kg of CO₂ and providing a warm halal meal."</div>
          <div style="font-size:11px;color:#aaa;margin-top:8px">— Al Qasba Elderly Home, 2 days ago</div>
        </div>
        <div class="acard">
          <div class="acard-title">Badges</div>
          <div style="display:flex;gap:6px;flex-wrap:wrap">
            <span class="abadge abadge-green">Community Hero</span>
            <span class="abadge abadge-blue">7-day streak</span>
            <span class="abadge abadge-amber">Top donor</span>
            <span class="abadge abadge-coral">1,000 meals</span>
          </div>
        </div>
      </div>
      <div class="app-nav">
        <button class="app-nav-btn" onclick="showAppScreen('as-home')"><span class="app-nav-icon">🏠</span>Home</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-donate')"><span class="app-nav-icon">➕</span>Donate</button>
        <button class="app-nav-btn active"><span class="app-nav-icon">📊</span>Impact</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-leaderboard')"><span class="app-nav-icon">🏆</span>Ranks</button>
      </div>
    </div>
    <!-- LEADERBOARD SCREEN -->
    <div class="app-screen" id="as-leaderboard">
      <div class="app-topbar">
        <button class="app-back" onclick="showAppScreen('as-home')">←</button>
        <h2>Dubai leaderboard 🏆</h2>
      </div>
      <div class="app-body">
        <div style="display:flex;gap:8px;margin-bottom:16px">
          <span class="abadge abadge-green" style="cursor:pointer;padding:6px 14px">This month</span>
          <span class="abadge" style="background:#e4e0d8;color:#888;cursor:pointer;padding:6px 14px">All time</span>
        </div>
        <div class="acard" style="padding:8px 16px">
          <div class="lboard-row"><div class="lboard-rank gold">1</div><div class="aicon-circle" style="background:#FAEEDA;font-size:16px">🍽️</div><div style="flex:1"><div class="abig" style="font-size:14px">Ravi's Kitchen</div><div class="asub">2,340 meals · 580kg CO₂</div></div><span class="abadge abadge-amber">Champion</span></div>
          <div class="lboard-row"><div class="lboard-rank silver">2</div><div class="aicon-circle" style="background:#dff4ec;font-size:16px">🌿</div><div style="flex:1"><div class="abig" style="font-size:14px">Green Feast</div><div class="asub">1,980 meals · 494kg CO₂</div></div><span class="abadge abadge-green">Hero</span></div>
          <div class="lboard-row" style="background:#f0fdf8;margin:0 -16px;padding:11px 16px">
            <div class="lboard-rank" style="color:#1D9E75">3</div>
            <div class="aicon-circle" style="background:#fff;font-size:16px;border:1px solid #e4e0d8">🍖</div>
            <div style="flex:1"><div class="abig" style="font-size:14px;color:#1D9E75">Al Baik (You)</div><div class="asub" style="color:#1D9E75">1,240 meals · 312kg CO₂</div></div>
            <span class="abadge abadge-green">You</span>
          </div>
          <div class="lboard-row"><div class="lboard-rank">4</div><div class="aicon-circle" style="background:#f0f0f0;font-size:16px">🥗</div><div style="flex:1"><div class="abig" style="font-size:14px">Salad Days</div><div class="asub">980 meals · 245kg CO₂</div></div></div>
          <div class="lboard-row" style="border-bottom:none"><div class="lboard-rank">5</div><div class="aicon-circle" style="background:#f0f0f0;font-size:16px">🍜</div><div style="flex:1"><div class="abig" style="font-size:14px">Noodle House</div><div class="asub">740 meals · 185kg CO₂</div></div></div>
        </div>
        <div class="acard">
          <div class="acard-title">Your next milestone</div>
          <div class="abig" style="font-size:14px;margin-bottom:6px">740 meals to reach #2</div>
          <div class="aprogress"><div class="aprogress-fill" style="width:62%"></div></div>
          <div style="font-size:11px;color:#aaa;margin-top:6px">Keep donating daily to climb the ranks</div>
        </div>
      </div>
      <div class="app-nav">
        <button class="app-nav-btn" onclick="showAppScreen('as-home')"><span class="app-nav-icon">🏠</span>Home</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-donate')"><span class="app-nav-icon">➕</span>Donate</button>
        <button class="app-nav-btn" onclick="showAppScreen('as-impact')"><span class="app-nav-icon">📊</span>Impact</button>
        <button class="app-nav-btn active"><span class="app-nav-icon">🏆</span>Ranks</button>
      </div>
    </div>
  </div>
  </div>
    </div>
  </div>
  <div style="text-align:center;padding:32px 20px 56px">
    <button class="btn-outline" onclick="showPage('home')">← Back to homepage</button>
  </div>
</div>
<!-- ABOUT PAGE -->
<div class="page" id="page-about">
  <!-- Hero -->
  <div style="background:#1D9E75;padding:80px 48px 72px;text-align:center">
    <div style="font-size:12px;color:#9FE1CB;letter-spacing:0.1em;text-transform:uppercase;font-weight:600;margin-bottom:14px">Our mission</div>
    <h1 style="font-size:48px;font-weight:700;color:#fff;letter-spacing:-0.025em;line-height:1.15;margin-bottom:20px">No food left behind<br>in the UAE</h1>
    <p style="font-size:17px;color:#9FE1CB;max-width:540px;margin:0 auto;line-height:1.8">NourishNet was built to close one of the Gulf's most pressing gaps — 3.27 million tons wasted every year, while thousands go without a meal.</p>
  </div>
  <!-- Impact numbers -->
  <div style="display:grid;grid-template-columns:repeat(3,1fr);background:#F7F5F0;border-bottom:1px solid #e4e0d8">
    <div style="padding:40px 20px;text-align:center;border-right:1px solid #e4e0d8">
      <div style="font-size:36px;font-weight:700;color:#1D9E75;margin-bottom:6px">3.27M</div>
      <div style="font-size:13px;color:#888;font-weight:500">Tons wasted in UAE yearly</div>
    </div>
    <div style="padding:40px 20px;text-align:center;border-right:1px solid #e4e0d8">
      <div style="font-size:36px;font-weight:700;color:#1D9E75;margin-bottom:6px">60%</div>
      <div style="font-size:13px;color:#888;font-weight:500">Food wasted during Ramadan</div>
    </div>
    <div style="padding:40px 20px;text-align:center">
      <div style="font-size:36px;font-weight:700;color:#1D9E75;margin-bottom:6px">$3.5B</div>
      <div style="font-size:13px;color:#888;font-weight:500">Annual economic cost</div>
    </div>
  </div>
  <!-- Story section -->
  <div style="max-width:900px;margin:0 auto;padding:80px 48px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center">
    <div>
      <div style="font-size:12px;font-weight:700;color:#1D9E75;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:14px">Why we built this</div>
      <div style="font-size:28px;font-weight:700;color:#111;line-height:1.3;margin-bottom:18px;letter-spacing:-0.01em">A problem hiding in plain sight</div>
      <p style="font-size:15px;color:#555;line-height:1.85;margin-bottom:16px">Dubai wastes 38% of prepared food daily. Every evening, restaurants throw away perfectly good meals while elderly residents, refugee families, and low-income households nearby go without.</p>
      <p style="font-size:15px;color:#555;line-height:1.85">Existing solutions are manual and one-size-fits-all. They don't distinguish between a refugee center needing 200 portions and an elderly home needing 40 soft halal meals. NourishNet's AI does that automatically, every time.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:14px">
      <div style="background:#fff;border:1px solid #e4e0d8;border-radius:14px;padding:20px 22px;border-left:4px solid #1D9E75;border-radius:0 14px 14px 0">
        <div style="font-size:22px;font-weight:700;color:#1D9E75;margin-bottom:4px">38%</div>
        <div style="font-size:13px;color:#555;line-height:1.6">of prepared food wasted daily in Dubai alone — rising sharply during holiday seasons</div>
      </div>
      <div style="background:#fff;border:1px solid #e4e0d8;border-radius:14px;padding:20px 22px;border-left:4px solid #185FA5;border-radius:0 14px 14px 0">
        <div style="font-size:22px;font-weight:700;color:#185FA5;margin-bottom:4px">80–90%</div>
        <div style="font-size:13px;color:#555;line-height:1.6">of UAE food is imported — making every wasted meal a double economic and environmental loss</div>
      </div>
      <div style="background:#fff;border:1px solid #e4e0d8;border-radius:14px;padding:20px 22px;border-left:4px solid #BA7517;border-radius:0 14px 14px 0">
        <div style="font-size:22px;font-weight:700;color:#BA7517;margin-bottom:4px">50%</div>
        <div style="font-size:13px;color:#555;line-height:1.6">UAE national target to reduce food waste by 2030 — NourishNet is built to help hit that goal</div>
      </div>
    </div>
  </div>
  <!-- How NourishNet is different -->
  <div style="background:#eeeae2;padding:80px 48px;border-top:1px solid #e4e0d8;border-bottom:1px solid #e4e0d8">
    <div style="max-width:1000px;margin:0 auto">
      <div style="font-size:12px;font-weight:700;color:#999;letter-spacing:0.1em;text-transform:uppercase;text-align:center;margin-bottom:12px">What makes us different</div>
      <div style="font-size:34px;font-weight:700;color:#111;text-align:center;margin-bottom:12px;letter-spacing:-0.015em">Not just redistribution. <span class="grad">Smart redistribution.</span></div>
      <div style="font-size:16px;color:#666;text-align:center;max-width:560px;margin:0 auto 52px;line-height:1.75">Every existing platform in the Gulf does the same thing — pass food along. We match it intelligently.</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
        <div style="background:#fff;border:1px solid #e4e0d8;border-radius:16px;padding:28px">
          <div style="font-size:13px;font-weight:700;color:#999;margin-bottom:16px;text-transform:uppercase;letter-spacing:0.06em">Other platforms</div>
          <div style="display:flex;flex-direction:column;gap:10px">
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#666"><span style="color:#E24B4A;font-weight:700;font-size:16px">✗</span> Manual donor-recipient matching</div>
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#666"><span style="color:#E24B4A;font-weight:700;font-size:16px">✗</span> One-size-fits-all distribution</div>
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#666"><span style="color:#E24B4A;font-weight:700;font-size:16px">✗</span> No dietary or cultural filters</div>
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#666"><span style="color:#E24B4A;font-weight:700;font-size:16px">✗</span> No impact tracking for donors</div>
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#666"><span style="color:#E24B4A;font-weight:700;font-size:16px">✗</span> No incentives for restaurants</div>
          </div>
        </div>
        <div style="background:#fff;border:2px solid #1D9E75;border-radius:16px;padding:28px">
          <div style="font-size:13px;font-weight:700;color:#1D9E75;margin-bottom:16px;text-transform:uppercase;letter-spacing:0.06em">NourishNet</div>
          <div style="display:flex;flex-direction:column;gap:10px">
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#111"><span style="color:#1D9E75;font-weight:700;font-size:16px">✓</span> AI-powered smart matching</div>
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#111"><span style="color:#1D9E75;font-weight:700;font-size:16px">✓</span> Quantity-based recipient routing</div>
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#111"><span style="color:#1D9E75;font-weight:700;font-size:16px">✓</span> Halal, dietary & cultural matching</div>
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#111"><span style="color:#1D9E75;font-weight:700;font-size:16px">✓</span> Full impact dashboard per donor</div>
            <div style="display:flex;gap:10px;align-items:center;font-size:14px;color:#111"><span style="color:#1D9E75;font-weight:700;font-size:16px">✓</span> Gamification, badges & leaderboard</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Partners -->
  <section style="padding:80px 48px;max-width:1000px;margin:0 auto">
    <div style="font-size:12px;font-weight:700;color:#999;letter-spacing:0.1em;text-transform:uppercase;text-align:center;margin-bottom:12px">Our partners</div>
    <div style="font-size:34px;font-weight:700;color:#111;text-align:center;margin-bottom:14px;letter-spacing:-0.015em">Built with the <span class="grad">right people</span></div>
    <div style="font-size:16px;color:#666;text-align:center;max-width:500px;margin:0 auto 48px;line-height:1.75">We didn't build NourishNet in isolation. We partnered with the organisations already doing the work on the ground.</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">
      <div class="step-card" style="text-align:center">
        <div style="width:56px;height:56px;border-radius:14px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:28px;margin:0 auto 16px">🏦</div>
        <div style="font-size:16px;font-weight:700;color:#111;margin-bottom:6px">UAE Food Bank</div>
        <div style="font-size:13px;color:#666;line-height:1.65">Our primary distribution partner. Handles last-mile delivery to families and shelters across all seven Emirates.</div>
      </div>
      <div class="step-card" style="text-align:center">
        <div style="width:56px;height:56px;border-radius:14px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:28px;margin:0 auto 16px">🌿</div>
        <div style="font-size:16px;font-weight:700;color:#111;margin-bottom:6px">Ne'ma Initiative</div>
        <div style="font-size:13px;color:#666;line-height:1.65">The UAE's national food waste reduction initiative, targeting 50% reduction by 2030. We're aligned with their roadmap.</div>
      </div>
      <div class="step-card" style="text-align:center">
        <div style="width:56px;height:56px;border-radius:14px;background:#dff4ec;display:flex;align-items:center;justify-content:center;font-size:28px;margin:0 auto 16px">🤖</div>
        <div style="font-size:16px;font-weight:700;color:#111;margin-bottom:6px">Claude AI</div>
        <div style="font-size:13px;color:#666;line-height:1.65">Powers the intelligent routing engine that matches surplus to communities in real time, learning from every donation.</div>
      </div>
    </div>
  </section>
  <!-- CTA -->
  <section class="cta-section">
    <div class="cta-title">Join the movement</div>
    <div class="cta-sub">186 restaurants are already making a difference across the UAE.<br>Your surplus can feed someone tonight.</div>
    <button class="cta-btn" onclick="showPage('app')">Try the app demo →</button>
  </section>
  <footer>
    <div class="footer-logo">Nourish<span>Net</span></div>
    <div class="footer-links">
      <span class="footer-link" onclick="showPage('home')">Home</span>
      <span class="footer-link" onclick="showPage('app')">App demo</span>
      <span class="footer-link" onclick="showPage('about')">About</span>
    </div>
    <div class="footer-text">UAE · 2025 · Partnered with UAE Food Bank & Ne'ma</div>
  </footer>
</div>
<script>
  function highlightTab(el) {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('tab-active'));
    el.classList.add('tab-active');
    const map = {'as-home':'desc-home','as-donate':'desc-donate','as-impact':'desc-impact','as-leaderboard':'desc-leaderboard'};
  }
  function showAppScreen(id) {
    document.querySelectorAll('.app-screen').forEach(s => s.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    const map = {'as-home':'desc-home','as-donate':'desc-donate','as-impact':'desc-impact','as-leaderboard':'desc-leaderboard'};
    document.querySelectorAll('[id^=desc-]').forEach(d => d.style.display='none');
    if(map[id]) document.getElementById(map[id]).style.display='block';
  }
  function showPage(id) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.getElementById('page-' + id).classList.add('active');
    window.scrollTo({top: 0, behavior: 'smooth'});
  }
  function selectRecipient(el) {
    document.querySelectorAll('.recipient-card').forEach(c => c.classList.remove('selected'));
    el.classList.add('selected');
  }
  function updateQty(val) {
    document.getElementById('qty-val').textContent = val;
    updateRouting();
  }
  function updateRouting() {
    const qty = parseInt(document.getElementById('qty-slider').value);
    const food = document.getElementById('food-type').value;
    const expiry = document.getElementById('expiry').value;
    let rec = '', match1 = '', match2 = '';
    if (qty <= 15) {
      rec = `Small batch of ${qty} portions — best routed to <strong>homebound elderly individuals</strong> nearby.`;
      match1 = '🏠 Al Qasba Elderly Home'; match2 = '👨‍👩‍👧 Low-income Families';
    } else if (qty <= 80) {
      rec = `${qty} portions of ${food.toLowerCase()} expiring ${expiry.toLowerCase()} — best match is an <strong>elderly care home</strong>.`;
      match1 = '🏠 Al Qasba Elderly Home'; match2 = '🛖 Sharjah Refugee Center';
    } else if (qty <= 150) {
      rec = `${qty} portions — volume suits a <strong>refugee center</strong> or large shelter.`;
      match1 = '🛖 Sharjah Refugee Center'; match2 = '👨‍👩‍👧 Low-income Families';
    } else {
      rec = `Large batch of ${qty} portions — route to <strong>UAE Food Bank</strong> with full storage capacity.`;
      match1 = '🏛️ UAE Food Bank'; match2 = '🛖 Sharjah Refugee Center';
    }
    document.getElementById('ai-rec').innerHTML = rec;
    const cards = document.querySelectorAll('.recipient-card');
    if (cards[0]) cards[0].querySelector('.abig').textContent = match1;
    if (cards[1]) cards[1].querySelector('.abig').textContent = match2;
  }
  function animateCounter(id, target, suffix) {
    const el = document.getElementById(id);
    if (!el) return;
    let current = 0;
    const step = Math.ceil(target / 60);
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = current.toLocaleString() + suffix;
      if (current >= target) clearInterval(timer);
    }, 24);
  }
  window.addEventListener('load', () => {
    animateCounter('c1', 14200, '');
    animateCounter('c2', 186, '');
    animateCounter('c3', 3800, 'kg');
    animateCounter('c4', 42, '');
  });
</script>
</body>
</html>
"""

with gr.Blocks(css="""
  .gradio-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
  footer { display: none !important; }
  #component-0 { padding: 0 !important; }
""") as demo:
    gr.HTML(html_content)

demo.launch()
