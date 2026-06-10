# -*- coding: utf-8 -*-
"""Assemble cover + gray + glow into a single index.html deck.
Extracts verbatim CSS/slide/script blocks, scopes each chapter's .slide rule,
applies HarmonyOS Sans + a shared type scale. Re-runnable."""
import re

def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()

def style_of(t):
    return t.split('<style>', 1)[1].split('</style>', 1)[0]

gtext = read('gray.html')
wtext = read('glow.html')

# ---- extract verbatim blocks by markers (robust to line-number shifts) ----
gray_style = style_of(gtext)
glow_style = style_of(wtext)

# gray deck inner: between <div id="deck"> and its closing </div> (before #nav)
_g = gtext.split('<div id="deck">', 1)[1].split('<div id="nav">', 1)[0]
gray_slides = _g[:_g.rfind('</div>')]

# glow: slides end at deck-close </div> before the colour panel; panel+toggle captured separately
_w = wtext.split('<div id="deck">', 1)[1].split('<div id="nav">', 1)[0]
_pstart = _w.index('<div id="panel"')
glow_slides = _w[:_pstart][:_w[:_pstart].rfind('</div>')]
glow_panel = _w[_pstart:].rstrip()
# 兜底：面板/开关内联默认隐藏（只有 JS 在黑底章节封面页才显示），防止漏到封面等页
glow_panel = (glow_panel
    .replace('<div id="panel"', '<div id="panel" style="display:none"')
    .replace('<button id="toggle"', '<button id="toggle" style="display:none"'))

# ---- scope each chapter's .slide rule so bg/padding don't collide ----
# gray: single base rule
gray_style = gray_style.replace('.slide{position:relative', '.slide.s-gray{position:relative', 1)
# glow: every .slide selector -> .slide.s-glow (base rule + descendants)
glow_style = glow_style.replace('.slide', '.slide.s-glow')

# tag the sections
gray_slides = gray_slides.replace('<section class="slide">', '<section class="slide s-gray">')
glow_slides = (glow_slides
    .replace('<section class="slide chapter-cover"', '<section class="slide s-glow chapter-cover"')
    .replace('<section class="slide" data-chapter', '<section class="slide s-glow" data-chapter'))

# ---- font swap: prepend HarmonyOS to every Inter stack (leaves JetBrains Mono / Georgia) ----
def harmony(css):
    return css.replace("font-family:'Inter'", "font-family:'HarmonyOS Sans SC','Inter'")
gray_style = harmony(gray_style)
glow_style = harmony(glow_style)

HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CANN DesignConcept 2026 · 完整汇报</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500&family=Noto+Sans+SC:wght@200;300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/IKKI2000/harmonyos-fonts@master/css/harmonyos_sans_sc.css">
<style>
/* ===== 字号规范（type scale）：正文 / 标题 / 各小一级，全 deck 统一 ===== */
:root{
  --fs-h1:clamp(20px,1.7vw,30px);   /* 页面主标题 */
  --fs-h2:clamp(15px,1.15vw,21px);  /* 区块标题 */
  --fs-h3:clamp(13px,.95vw,16px);   /* 卡片小标题 */
  --fs-body:clamp(12px,.82vw,15px); /* 正文 */
  --fs-sm:clamp(10.5px,.72vw,13px); /* 次要正文 / 说明 */
  --fs-xs:clamp(9px,.62vw,11px);    /* 标签 / 注释 / 页码 */
}
"""

# unifying layer placed LAST so it wins for shared base selectors
UNIFY = """
/* ============ 统一层（置后，覆盖各分册 base / nav / 字体）============ */
*{box-sizing:border-box;margin:0;padding:0}
/* 必须显式盖掉各分册横向用的 height/overflow/display */
html,body{width:100%;height:100%;overflow:hidden;background:#0c0a0b;color:var(--ink);
  font-family:'HarmonyOS Sans SC','Inter','Noto Sans SC',sans-serif;-webkit-font-smoothing:antialiased}
/* 整页瞬切：所有页叠在同一位置，只显示当前页（active），切换瞬时完成——物理上不可能两页同屏 */
#deck{position:fixed;inset:0;width:100vw;height:100vh;display:block;transform:none}
.slide{position:absolute!important;inset:0;width:100vw;height:100vh;overflow:hidden;font-size:var(--fs-body);visibility:hidden;opacity:0}
.slide.active{visibility:visible;opacity:1;z-index:1}
/* ===== 总览缩略图网格（内容按真实 100vw×100vh 渲染再 scale 缩小）===== */
body.overview{position:fixed;inset:0;overflow-y:auto;height:100vh;background:#15151a;padding:30px 30px 64px}
body.overview #deck{position:static;display:grid;grid-template-columns:repeat(3,1fr);gap:22px;width:auto;max-width:1480px;margin:0 auto;height:auto}
/* 缩略框：还原成静态网格项、全部可见，去内边距/flex（高度由 JS 按 scale 设）*/
body.overview .slide{position:relative!important;inset:auto;visibility:visible!important;opacity:1!important;width:auto;height:auto;padding:0!important;display:block!important;overflow:hidden;border-radius:12px;cursor:pointer;box-shadow:0 12px 34px -14px rgba(0,0,0,.6);outline:2px solid transparent;transition:outline-color .18s,transform .18s;z-index:auto}
body.overview .slide:hover{transform:translateY(-4px);outline-color:var(--accent)}
/* inner 占满真实视口尺寸 + 重建该页内部布局，JS 再 transform:scale 缩小 */
body.overview .slide-inner{position:absolute;top:0;left:0;width:100vw;height:100vh;transform-origin:top left;overflow:hidden;pointer-events:none;box-sizing:border-box}
body.overview .s-gray .slide-inner{display:flex;flex-direction:column;padding:5vh 4vw}
body.overview .s-glow .slide-inner{padding:7vh 6vw}
body.overview .s-cover .slide-inner{padding:0}
.s-gray{color:var(--ink)}
.s-glow,.s-cover{color:#fff}

/* ----- 封面（cv- 前缀，避免与各分册类名冲突）----- */
.s-cover{padding:0;background:#0c0a0b}
.cv-bg{position:absolute;inset:0;background:url("assets/cover-bg.png") center/cover no-repeat;z-index:0}
.cv-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(100deg,rgba(10,8,9,.92) 0%,rgba(10,8,9,.55) 30%,rgba(10,8,9,0) 58%)}
.cv-content{position:relative;z-index:1;height:100vh;padding:6vh 6vw;display:flex;flex-direction:column;justify-content:space-between}
.cv-top{display:flex;justify-content:space-between;align-items:flex-start}
.cv-huawei{display:flex;align-items:center;gap:.7em;font-weight:600;font-size:16px;letter-spacing:.04em}
.cv-huawei .petal{width:19px;height:19px;flex-shrink:0}
.cv-meta{font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.2em;text-transform:uppercase;opacity:.55}
.cv-center{display:flex;flex-direction:column;gap:1.8vh;max-width:60vw}
.cv-kicker{font-family:'JetBrains Mono';font-size:13px;letter-spacing:.34em;text-transform:uppercase;color:rgba(255,255,255,.6);margin-bottom:1vh}
.cv-logo{display:flex}
.cv-logo img{height:min(17vh,12vw);width:auto;display:block}
.cv-sub{font-family:'HarmonyOS Sans SC','Inter','Noto Sans SC';font-weight:300;font-size:min(3vw,5vh);line-height:1.1;letter-spacing:.005em;color:rgba(255,255,255,.92)}
.cv-lead{font-family:'HarmonyOS Sans SC','Inter','Noto Sans SC';font-weight:300;font-size:max(15px,1.2vw);line-height:1.6;color:rgba(255,255,255,.6);max-width:36ch;margin-top:1.4vh}
.cv-bot{display:flex;justify-content:space-between;align-items:flex-end}
.cv-ucd{font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.55);display:flex;align-items:center;gap:.6em}
.cv-ucd .sq{width:12px;height:12px;border:1.5px solid currentColor;display:inline-block}

/* ----- 右侧竖排导航点（鼠标移动显隐；亮/暗随当前页）----- */
.nav-dots{position:fixed;right:16px;top:50%;transform:translateY(-50%);z-index:300;display:flex;flex-direction:column;gap:7px;padding:10px 7px;border-radius:999px;background:rgba(150,150,170,.16);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);opacity:0;transition:opacity .25s}
.nav-dots.show{opacity:1}
.nav-dot{width:7px;height:7px;border-radius:50%;background:rgba(40,45,60,.28);cursor:pointer;border:0;padding:0;transition:all .25s cubic-bezier(.4,0,.2,1)}
.nav-dot:hover{background:rgba(40,45,60,.5);transform:scale(1.25)}
.nav-dot.active{background:var(--accent);height:18px;border-radius:4px}
body.on-dark .nav-dots{background:rgba(255,255,255,.1)}
body.on-dark .nav-dot{background:rgba(255,255,255,.3)}
body.on-dark .nav-dot.active{background:#fff}
/* ----- 底部控制栏：上一页/页码/下一页 ｜ 概览/全屏 ----- */
.controls{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);z-index:1000;display:flex;align-items:center;gap:8px;padding:7px 12px;border-radius:999px;background:rgba(22,25,30,.82);backdrop-filter:blur(12px) saturate(1.3);-webkit-backdrop-filter:blur(12px) saturate(1.3);color:#fff;box-shadow:0 10px 30px -12px rgba(0,0,0,.5);opacity:0;transition:opacity .25s}
.controls.show{opacity:1}
.controls button{background:transparent;color:#fff;border:0;cursor:pointer;width:32px;height:32px;border-radius:999px;display:flex;align-items:center;justify-content:center;opacity:.72;transition:opacity .15s,background .15s}
.controls button:hover:not(:disabled){opacity:1;background:rgba(255,255,255,.12)}
.controls button:disabled{opacity:.3;cursor:default}
.controls button svg{width:17px;height:17px}
.ctrl-counter{font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.1em;min-width:58px;text-align:center;opacity:.8;user-select:none}
.ctrl-sep{width:1px;height:16px;background:rgba(255,255,255,.2)}
/* glow 调色面板/开关：默认隐藏，只有 JS 在黑底章节封面页才显示（防止它挡在封面等页上）*/
#panel,#toggle{display:none}

/* ----- 字号规范落地（统一各页标题/正文层级）----- */
.brand .ttl{font-size:var(--fs-h1)!important;font-weight:800;letter-spacing:-.01em}
.subttl{font-size:var(--fs-sm)!important}
.head-r{font-size:var(--fs-xs)!important}
.body{font-size:var(--fs-body)!important}
.point .pt-title{font-size:var(--fs-h3)!important}
.point .pt-desc{font-size:var(--fs-sm)!important}
.kicker,.ch-kicker,.chrome,.shot .ph,.cmp-cap,.cmp-h .hk{font-size:var(--fs-xs)!important}
</style>
</head>
<body>
<div id="deck">
"""

COVER = """  <!-- ===== 封面 ===== -->
  <section class="slide s-cover">
    <div class="cv-bg"></div>
    <div class="cv-content">
      <div class="cv-top">
        <div class="cv-huawei"><svg class="petal" viewBox="0 0 24 24" fill="#E60012"><path d="M12 2c-1 4-3 6-6 7 3 1 5 3 6 7 1-4 3-6 6-7-3-1-5-3-6-7z"/></svg>HUAWEI</div>
        <div class="cv-meta">Ascend · Compute Architecture</div>
      </div>
      <div class="cv-center">
        <div class="cv-kicker">Design Concept · 2026</div>
        <div class="cv-logo"><img src="assets/cann-dark-logo.svg" alt="CANN"></div>
        <div class="cv-sub">DesignConcept 2026</div>
        <div class="cv-lead">华为昇腾计算架构 · 开发者体验设计概念</div>
      </div>
      <div class="cv-bot">
        <div class="cv-ucd"><span class="sq"></span>UCD CENTER</div>
        <div class="cv-meta">2026</div>
      </div>
    </div>
  </section>
"""

SCRIPT = r"""
<nav class="nav-dots" id="navDots"></nav>
<div class="controls" id="controls">
  <button id="prevBtn" title="上一页 ↑/←"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 15 12 9 18 15"/></svg></button>
  <span class="ctrl-counter" id="counter">01 / 01</span>
  <button id="nextBtn" title="下一页 ↓/→"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></button>
  <span class="ctrl-sep"></span>
  <button id="ovBtn" title="概览 O"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></button>
  <button id="fsBtn" title="全屏 F"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3M21 8V5a2 2 0 0 0-2-2h-3M16 21h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg></button>
</div>

<script src="lib/echarts.min.js"></script>
<script>
const root=document.documentElement;
const deck=document.getElementById('deck');
const slides=[...document.querySelectorAll('.slide')];
const nav=document.getElementById('nav');
let idx=0;

/* ===== glow 章节调色（仅 data-chapter 的 glow 页生效，其余页不受影响）===== */
const chapters={
  '1':{h:234,gap:57,sat:95,light:40,spread:35,cint:68,wint:58},
  '2':{h:160,gap:57,sat:95,light:40,spread:35,cint:68,wint:58}
};
/* 持久记忆：上次调好的光晕色值（localStorage），下次打开自动恢复 */
const GLOW_KEY='deck-glow-chapters';
try{const _sv=localStorage.getItem(GLOW_KEY);if(_sv){const o=JSON.parse(_sv);Object.keys(o).forEach(k=>{if(chapters[k])Object.assign(chapters[k],o[k]);});}}catch(e){}
function saveChapters(){try{localStorage.setItem(GLOW_KEY,JSON.stringify(chapters));}catch(e){}}
function curChap(){return chapters[slides[idx].dataset.chapter];}
const S={h:'s-h',gap:'s-gap',sat:'s-sat',light:'s-light',spread:'s-spread',cint:'s-cint',wint:'s-wint'};
const V={h:'v-h',gap:'v-gap',sat:'v-sat',light:'v-light',spread:'v-spread',cint:'v-cint',wint:'v-wint'};
function paintSlide(s){
  const c=chapters[s.dataset.chapter]; if(!c) return;
  s.style.setProperty('--glow-h',c.h);
  s.style.setProperty('--glow-h2',(c.h+c.gap)%360);
  s.style.setProperty('--glow-sat',c.sat+'%');
  s.style.setProperty('--glow-light',c.light+'%');
  s.style.setProperty('--glow-spread',c.spread);
  s.style.setProperty('--glow-color-int',(c.cint/100).toFixed(2));
  s.style.setProperty('--glow-white-int',(c.wint/100).toFixed(2));
}
function apply(){
  slides.forEach(paintSlide);
  saveChapters();
  const c=curChap(); if(!c) return;
  root.style.setProperty('--glow-h',c.h);
  root.style.setProperty('--glow-h2',(c.h+c.gap)%360);
  root.style.setProperty('--glow-sat',c.sat+'%');
  root.style.setProperty('--glow-light',c.light+'%');
  root.style.setProperty('--glow-spread',c.spread);
  root.style.setProperty('--glow-color-int',(c.cint/100).toFixed(2));
  root.style.setProperty('--glow-white-int',(c.wint/100).toFixed(2));
}
function syncPanel(){
  const c=curChap(); if(!c) return;
  document.getElementById('s-h').value=c.h;     document.getElementById('v-h').textContent=c.h;
  document.getElementById('s-gap').value=c.gap; document.getElementById('v-gap').textContent=c.gap+'°';
  document.getElementById('s-sat').value=c.sat;  document.getElementById('v-sat').textContent=c.sat+'%';
  document.getElementById('s-light').value=c.light; document.getElementById('v-light').textContent=c.light+'%';
  document.getElementById('s-spread').value=c.spread; document.getElementById('v-spread').textContent=c.spread+'vh';
  document.getElementById('s-cint').value=c.cint; document.getElementById('v-cint').textContent=(c.cint/100).toFixed(2);
  document.getElementById('s-wint').value=c.wint; document.getElementById('v-wint').textContent=(c.wint/100).toFixed(2);
}
function bind(key){
  const el=document.getElementById(S[key]); if(!el) return;
  el.addEventListener('input',()=>{
    const c=curChap(); if(!c) return;
    c[key]=+el.value;
    const v=document.getElementById(V[key]);
    if(key==='sat'||key==='light') v.textContent=el.value+'%';
    else if(key==='spread') v.textContent=el.value+'vh';
    else if(key==='cint'||key==='wint') v.textContent=(el.value/100).toFixed(2);
    else if(key==='gap') v.textContent=el.value+'°';
    else v.textContent=el.value;
    apply(); updTools();
  });
  el.addEventListener('change',pushHist);
}
Object.keys(S).forEach(bind);

const DEFAULTS=JSON.parse(JSON.stringify(chapters));
let history=[JSON.stringify(chapters)], hi=0;
function pushHist(){history=history.slice(0,hi+1);history.push(JSON.stringify(chapters));hi=history.length-1;updTools();}
function restoreHist(){const o=JSON.parse(history[hi]);Object.keys(o).forEach(k=>Object.assign(chapters[k],o[k]));apply();syncPanel();updTools();}
function updTools(){const u=document.getElementById('t-undo'),r=document.getElementById('t-redo'),rs=document.getElementById('t-reset');if(u)u.disabled=hi<=0;if(r)r.disabled=hi>=history.length-1;if(rs)rs.disabled=!openSnap||JSON.stringify(curChap())===openSnap;}
let openSnap=null;
const bu=document.getElementById('t-undo'); if(bu) bu.onclick=()=>{if(hi>0){hi--;restoreHist();}};
const br=document.getElementById('t-redo'); if(br) br.onclick=()=>{if(hi<history.length-1){hi++;restoreHist();}};
const bx=document.getElementById('t-reset'); if(bx) bx.onclick=()=>{if(openSnap){Object.assign(curChap(),JSON.parse(openSnap));apply();syncPanel();pushHist();}};
updTools();
document.querySelectorAll('.preset').forEach(p=>{
  p.onclick=()=>{const c=curChap(); if(!c) return; const [h,sat,light]=p.dataset.p.split(',').map(Number);Object.assign(c,{h,sat,light});apply();syncPanel();pushHist();};
});
function setPanelOpen(open){const p=document.getElementById('panel'); if(!p) return; p.classList.remove('collapsed'); p.style.display=open?'block':'none';}
document.addEventListener('click',e=>{
  const panel=document.getElementById('panel'),toggle=document.getElementById('toggle');
  if(!panel||!toggle) return;
  if(toggle.contains(e.target)){
    if(panel.style.display==='block') setPanelOpen(false);
    else { openSnap=JSON.stringify(curChap()); setPanelOpen(true); updTools(); }
    return;
  }
  if(panel.contains(e.target)) return;
  if(panel.style.display==='block') setPanelOpen(false);
});

/* ===== 整页瞬切（叠层 active，无过渡，绝不两页同屏）+ 右侧点 + 控制栏 + 总览 + 全屏 ===== */
const navDots=document.getElementById('navDots'), controls=document.getElementById('controls'), counter=document.getElementById('counter');
const prevBtn=document.getElementById('prevBtn'), nextBtn=document.getElementById('nextBtn'), ovBtn=document.getElementById('ovBtn'), fsBtn=document.getElementById('fsBtn');
const pad=n=>String(n).padStart(2,'0');
const dots=slides.map((s,i)=>{const b=document.createElement('button');b.className='nav-dot';b.title=pad(i+1)+' / '+pad(slides.length);b.onclick=()=>go(i);navDots.appendChild(b);return b;});

function show(i){
  i=Math.max(0,Math.min(slides.length-1,i));
  if(slides[idx]) slides[idx].classList.remove('active');
  idx=i; const s=slides[idx]; s.classList.add('active');
  dots.forEach((d,k)=>d.classList.toggle('active',k===idx));
  counter.textContent=pad(idx+1)+' / '+pad(slides.length);
  prevBtn.disabled=idx<=0; nextBtn.disabled=idx>=slides.length-1;
  document.body.classList.toggle('on-dark', s.classList.contains('s-cover')||s.classList.contains('s-glow'));
  const panel=document.getElementById('panel'),toggle=document.getElementById('toggle');
  if(s.dataset.chapter && s.classList.contains('chapter-cover')){ if(panel)s.appendChild(panel); if(toggle){s.appendChild(toggle);toggle.style.display='flex';} setPanelOpen(false); apply(); syncPanel(); }
  else if(toggle){ toggle.style.display='none'; setPanelOpen(false); }
}
function go(n){ if(document.body.classList.contains('overview'))return; show(n); }
function next(){go(idx+1);} function prev(){go(idx-1);}
prevBtn.onclick=prev; nextBtn.onclick=next;

/* 滚轮/触控板：整页瞬切（节流，一次一页）*/
let wlock=false;
addEventListener('wheel',e=>{
  if(document.body.classList.contains('overview'))return;
  if(wlock||Math.abs(e.deltaY)<8)return;
  wlock=true;setTimeout(()=>wlock=false,420);
  go(idx+(e.deltaY>0?1:-1));
},{passive:true});
/* 触屏上下滑 */
let ty=null;
addEventListener('touchstart',e=>{ty=e.touches[0].clientY;},{passive:true});
addEventListener('touchend',e=>{if(ty==null||document.body.classList.contains('overview')){ty=null;return;}const dy=e.changedTouches[0].clientY-ty;if(Math.abs(dy)>45)go(idx+(dy<0?1:-1));ty=null;},{passive:true});

document.addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')return;
  if(['ArrowDown','ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();next();}
  else if(['ArrowUp','ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();prev();}
  else if(e.key==='Home'){e.preventDefault();go(0);}
  else if(e.key==='End'){e.preventDefault();go(slides.length-1);}
  else if(e.key==='o'||e.key==='O'){toggleOverview();}
  else if(e.key==='f'||e.key==='F'){toggleFullscreen();}
  else if(e.key==='Escape'){ if(document.body.classList.contains('overview')) toggleOverview(); }
});

/* 全屏 */
function toggleFullscreen(){ if(!document.fullscreenElement){document.documentElement.requestFullscreen().catch(()=>{});}else{document.exitFullscreen();} }
fsBtn.onclick=toggleFullscreen;

/* 总览 Overview：每页包进 .slide-inner 缩放成缩略图，排网格 */
function applyOverviewScale(){if(!document.body.classList.contains('overview'))return;const cellW=slides[0].getBoundingClientRect().width,scale=cellW/window.innerWidth;slides.forEach(s=>{const inner=s.querySelector(':scope>.slide-inner');if(inner)inner.style.transform='scale('+scale+')';s.style.height=(window.innerHeight*scale)+'px';});}
function enterOverview(){slides.forEach(s=>{if(!s.querySelector(':scope>.slide-inner')){const w=document.createElement('div');w.className='slide-inner';while(s.firstChild)w.appendChild(s.firstChild);s.appendChild(w);}});document.body.classList.add('overview');requestAnimationFrame(applyOverviewScale);}
function exitOverview(){slides.forEach(s=>{const w=s.querySelector(':scope>.slide-inner');if(w){while(w.firstChild)s.insertBefore(w.firstChild,w);w.remove();}s.style.height='';});document.body.classList.remove('overview');show(idx);}
function toggleOverview(){ if(document.body.classList.contains('overview')){exitOverview();} else enterOverview(); }
ovBtn.onclick=toggleOverview;
document.body.addEventListener('click',e=>{if(!document.body.classList.contains('overview'))return;const sl=e.target.closest('.slide');if(sl){const i=slides.indexOf(sl);if(i>=0){exitOverview();show(i);}}});
addEventListener('resize',()=>{if(document.body.classList.contains('overview'))applyOverviewScale();});

/* 鼠标移动时显示控制栏+右侧点，2.5s 后淡出 */
let hideTimer;
function showCtrl(){controls.classList.add('show');navDots.classList.add('show');clearTimeout(hideTimer);hideTimer=setTimeout(()=>{controls.classList.remove('show');navDots.classList.remove('show');},2500);}
document.addEventListener('mousemove',showCtrl);
showCtrl();

slides.forEach(paintSlide);
show(0);

/* ===== gray 简笔头像 ===== */
const AV_SKIN={light:'#F3D2B0',tan:'#E1B188',brown:'#B97F58',pale:'#F7DEC4'};
function avatar(o){
  const skin=AV_SKIN[o.skin]||AV_SKIN.light, shirt=o.shirt||'#5B5BD6', hair=o.hair||'#33312f', bg=o.bg||'#E6EEFB';
  let h='';
  switch(o.type){
    case 'long': h=`<path d="M14 44 C12 26 16 14 32 14 C48 14 52 26 50 44 L43 44 C47 29 45 22 39 21 L25 21 C19 22 17 29 21 44Z" fill="${hair}"/>`; break;
    case 'bun': h=`<circle cx="32" cy="8.5" r="5.2" fill="${hair}"/><path d="M16 31 C16 9 48 9 48 31 C44 24 40 20 32 18 C24 20 20 24 16 31Z" fill="${hair}"/>`; break;
    case 'curly': h=`<g fill="${hair}"><circle cx="21" cy="23" r="7"/><circle cx="30" cy="16" r="7.5"/><circle cx="40" cy="19" r="7"/><circle cx="46" cy="27" r="5.6"/><circle cx="18" cy="29" r="5.6"/><circle cx="32" cy="21" r="7"/></g>`; break;
    case 'side': h=`<path d="M16 31 C16 9 48 9 48 31 C44 24 40 20 32 18 C26 19 20 22 16 31Z" fill="${hair}"/>`; break;
    default: h=`<path d="M16 31 C16 9 48 9 48 31 C44 24 40 20 32 18 C24 20 20 24 16 31Z" fill="${hair}"/>`;
  }
  const gl=o.glasses?`<g stroke="#3a3a3a" stroke-width="1.3" fill="none"><circle cx="26.6" cy="30" r="3.6"/><circle cx="37.4" cy="30" r="3.6"/><line x1="30.2" y1="30" x2="33.8" y2="30"/></g>`:'';
  return `<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">`
    +`<rect width="64" height="64" fill="${bg}"/>`
    +`<path d="M10 64 C10 51 19 45 32 45 C45 45 54 51 54 64Z" fill="${shirt}"/>`
    +`<rect x="28.6" y="39" width="6.8" height="9" rx="3.2" fill="${skin}"/>`
    +`<circle cx="32" cy="30" r="12.4" fill="${skin}"/>`
    +h
    +`<circle cx="27" cy="30" r="1.5" fill="#3a3a3a"/><circle cx="37" cy="30" r="1.5" fill="#3a3a3a"/>`
    +`<path d="M28.5 35.5 Q32 38 35.5 35.5" stroke="#a06a48" fill="none" stroke-width="1.5" stroke-linecap="round"/>`
    +gl+`</svg>`;
}
document.querySelectorAll('[data-av]').forEach(el=>{if(el.closest('.sb-role'))return;try{el.innerHTML=avatar(JSON.parse(el.getAttribute('data-av')));}catch(e){}});

/* ===== gray 用户画像B 雷达 ===== */
(function(){
  if(typeof echarts==='undefined')return;
  var el=document.getElementById('pp-radar');if(!el)return;
  var ch=echarts.init(el);
  ch.setOption({
    textStyle:{fontFamily:'HarmonyOS Sans SC, Inter, "Noto Sans SC", sans-serif'},
    color:['#3B5BDB','#E8533B'],
    radar:{center:['50%','54%'],radius:'68%',
      indicator:[{name:'C/C++ 编程'},{name:'汇编语言'},{name:'计算机体系结构'},{name:'cpu 原理'},{name:'并行计算原理'},{name:'数学结构与算法'},{name:'机器学习基础'},{name:'数学基础'}],
      axisName:{color:'#5e646e',fontSize:10},
      splitLine:{lineStyle:{color:'#d4d8df'}},axisLine:{lineStyle:{color:'#d4d8df'}},
      splitArea:{areaStyle:{color:['rgba(0,0,0,.02)','rgba(0,0,0,.04)']}}},
    series:[{type:'radar',symbol:'none',data:[
      {value:[95,70,80,72,85,78,55,75],name:'内源用户',lineStyle:{color:'#3B5BDB',width:2},areaStyle:{color:'rgba(59,91,219,.1)'}},
      {value:[88,32,46,40,50,52,42,90],name:'生态用户',lineStyle:{color:'#E8533B',width:2},areaStyle:{color:'rgba(232,83,59,.1)'}}
    ]}]
  });
  addEventListener('resize',function(){ch.resize();});
})();
</script>
</body>
</html>
"""

out = (HEAD
       + gray_style + '\n'
       + glow_style + '\n'
       + UNIFY
       + COVER
       + '\n  <!-- ===== 分析篇（gray）===== -->\n' + gray_slides + '\n'
       + '\n  <!-- ===== 设计点（glow）===== -->\n' + glow_slides + '\n'
       + '</div>\n\n'
       + '<!-- glow 调色面板（仅 glow 章节封面页挂载显示）-->\n'
       + glow_panel + '\n'
       + SCRIPT)

# decode the \uXXXX escapes that were written literally inside the r""" SCRIPT block
out = out.encode('utf-8').decode('unicode_escape') if False else out

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(out)
print('index.html written:', len(out.split(chr(10))), 'lines')
