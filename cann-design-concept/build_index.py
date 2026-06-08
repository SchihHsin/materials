# -*- coding: utf-8 -*-
"""Assemble cover + gray + glow into a single index.html deck.
Extracts verbatim CSS/slide/script blocks, scopes each chapter's .slide rule,
applies HarmonyOS Sans + a shared type scale. Re-runnable."""
import re

def lines(p):
    with open(p, encoding='utf-8') as f:
        return f.read().split('\n')

g = lines('gray.html')
w = lines('glow.html')

# ---- extract verbatim blocks (file line N => index N-1) ----
gray_style  = '\n'.join(g[8:573])     # lines 9..573  (inside <style>, excl tags & base? kept; scoped below)
gray_slides = '\n'.join(g[578:1146])  # lines 579..1146 (deck inner)
glow_style  = '\n'.join(w[8:175])     # lines 9..175
glow_slides = '\n'.join(w[180:281])   # lines 181..281 (deck inner)
glow_panel  = '\n'.join(w[284:306])   # lines 285..306 (#panel ... #toggle)

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
html,body{width:100%;height:100%;overflow:hidden;background:#0c0a0b;color:var(--ink);
  font-family:'HarmonyOS Sans SC','Inter','Noto Sans SC',sans-serif;-webkit-font-smoothing:antialiased}
#deck{position:fixed;inset:0;display:flex;width:max-content;height:100vh;transition:transform .8s cubic-bezier(.77,0,.175,1)}
.slide{position:relative;width:100vw;height:100vh;flex:0 0 100vw;overflow:hidden;font-size:var(--fs-body)}
.s-gray{color:var(--ink)}
.s-glow,.s-cover{color:#fff}

/* ----- 封面（cv- 前缀，避免与各分册类名冲突）----- */
.s-cover{padding:0;background:#0c0a0b}
.cv-bg{position:absolute;inset:0;background:url("reference/cover-bg.png") center/cover no-repeat;z-index:0}
.cv-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(100deg,rgba(10,8,9,.92) 0%,rgba(10,8,9,.55) 30%,rgba(10,8,9,0) 58%)}
.cv-content{position:relative;z-index:1;height:100vh;padding:6vh 6vw;display:flex;flex-direction:column;justify-content:space-between}
.cv-top{display:flex;justify-content:space-between;align-items:flex-start}
.cv-huawei{display:flex;align-items:center;gap:.7em;font-weight:600;font-size:16px;letter-spacing:.04em}
.cv-huawei .petal{width:19px;height:19px;flex-shrink:0}
.cv-meta{font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.2em;text-transform:uppercase;opacity:.55}
.cv-center{display:flex;flex-direction:column;gap:1.8vh;max-width:60vw}
.cv-kicker{font-family:'JetBrains Mono';font-size:13px;letter-spacing:.34em;text-transform:uppercase;color:rgba(255,255,255,.6);margin-bottom:1vh}
.cv-logo{font-family:'HarmonyOS Sans SC','Inter';font-weight:800;font-size:min(13vw,21vh);line-height:.88;letter-spacing:-.035em;display:flex}
.cv-logo .red{color:#E60012}
.cv-sub{font-family:'HarmonyOS Sans SC','Inter','Noto Sans SC';font-weight:300;font-size:min(3vw,5vh);line-height:1.1;letter-spacing:.005em;color:rgba(255,255,255,.92)}
.cv-lead{font-family:'HarmonyOS Sans SC','Inter','Noto Sans SC';font-weight:300;font-size:max(15px,1.2vw);line-height:1.6;color:rgba(255,255,255,.6);max-width:36ch;margin-top:1.4vh}
.cv-bot{display:flex;justify-content:space-between;align-items:flex-end}
.cv-ucd{font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.55);display:flex;align-items:center;gap:.6em}
.cv-ucd .sq{width:12px;height:12px;border:1.5px solid currentColor;display:inline-block}

/* ----- 统一翻页导航（按当前页亮/暗自动切换）----- */
#nav{position:fixed;bottom:2.6vh;left:50%;transform:translateX(-50%);z-index:200;display:flex;gap:9px;
  padding:8px 14px;border-radius:999px;background:rgba(150,150,170,.16);
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
#nav .dot{width:8px;height:8px;border-radius:50%;background:rgba(40,45,60,.32);cursor:pointer;border:0;transition:all .3s}
#nav .dot.active{background:var(--accent);width:22px;border-radius:999px}
#nav.on-dark{background:rgba(255,255,255,.08)}
#nav.on-dark .dot{background:rgba(255,255,255,.3)}
#nav.on-dark .dot.active{background:#fff}
.hint{position:fixed;bottom:2.6vh;right:2.4vw;z-index:200;font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.16em;text-transform:uppercase;color:rgba(140,140,150,.6)}

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
        <div class="cv-logo">C<span class="red">A</span>NN</div>
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
<div id="nav"></div>
<div class="hint">← → 翻页</div>

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

/* ===== nav + 翻页 ===== */
slides.forEach((s,i)=>{const b=document.createElement('button');b.className='dot';b.onclick=()=>go(i);nav.appendChild(b);});
function go(n){
  idx=Math.max(0,Math.min(slides.length-1,n));
  deck.style.transform=`translateX(${-idx*100}vw)`;
  nav.querySelectorAll('.dot').forEach((d,i)=>d.classList.toggle('active',i===idx));
  const s=slides[idx];
  nav.classList.toggle('on-dark', s.classList.contains('s-glow')||s.classList.contains('s-cover'));
  const panel=document.getElementById('panel'),toggle=document.getElementById('toggle');
  if(s.dataset.chapter){
    if(s.classList.contains('chapter-cover')){ if(panel)s.appendChild(panel); if(toggle){s.appendChild(toggle);toggle.style.display='flex';} }
    else if(toggle){ toggle.style.display='none'; }
    setPanelOpen(false); apply(); syncPanel();
  } else {
    if(toggle) toggle.style.display='none';
    setPanelOpen(false);
  }
}
addEventListener('keydown',e=>{if(e.key==='ArrowRight')go(idx+1);if(e.key==='ArrowLeft')go(idx-1);});
slides.forEach(paintSlide);
go(0);

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
