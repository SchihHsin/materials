# Deck 架构与多分册合并

## 单文件 deck 机制（纵向 scroll-snap）

```
html     scroll-snap-type:y mandatory; scroll-behavior:smooth
body     滚动容器：height:100%; overflow:hidden auto; scroll-snap-type:y mandatory
#deck    position:relative; display:block   （各页竖向自然堆叠）
.slide   width:100vw; height:100vh; overflow:hidden; scroll-snap-align:start; scroll-snap-stop:always
```

- **翻页 = 原生纵向滚动 + scroll-snap**：每页满屏、强制吸附——划的过程会短暂见两页，松手自动吸附到整页。**不要自己拦截滚轮做「瞬切/淡入」**——淡入会两页叠显、瞬切手感差，原生 snap 最稳，也是参考 demo 的做法。
- **当前页用 `IntersectionObserver` 判**（谁进视口 ≥55% 谁就是当前页）。别依赖「翻页函数被调用」——原生滚动不经过任何函数。`go(n)`/键盘/点导航点都走 `slides[n].scrollIntoView({behavior:'smooth',block:'start'})`。
- **底部居中控制栏 `#controls`**：`上一页 / 页码 / 下一页 ｜ 概览 / 全屏`；**要小、要透**（背景 ~`rgba(22,25,30,.42)`、按钮 26px、别抢眼）。亮/暗随当前页用 **`body.on-dark`** 切换（封面/黑底 = on-dark）。
  - ⚠️ **显隐：底部栏与右侧 `.nav-dots` 分区独立、离开即淡出**（别绑死、别用定时器）：`mousemove` 里 `controls.classList.toggle('show', e.clientY>innerHeight-120)` + `navDots.classList.toggle('show', e.clientX>innerWidth-120)` + `mouseleave` 一并隐藏。移到底部出底部栏、移到右侧出右侧点，互不联动。（旧版用 2.5s 定时器 + 两栏同步——移开残留、且只能从底部触发，已弃用。）
- **全屏**：Fullscreen API（`requestFullscreen`/`exitFullscreen`，`F` 键）；监听 `fullscreenchange` 切换按钮图标（全屏 ⛶ ↔ 退出全屏）。
- **滚动条**：细、半透、**默认隐藏，滚动时才淡入**（`body.scrolling` 类，停 700ms 淡出），亮/暗随 `body.on-dark`。⚠️ **滚动监听挂 `body` 不是 `window`**（`html{overflow-y:visible}` 让 body 当滚动容器，scroll 事件在 body 上触发）+ `wheel` 兜底，否则 `.scrolling` 永远加不上、滚动条永不出现。
- 键盘：`↑↓←→` / 空格 / PageUp-Down / Home / End / `O` 概览 / `F` 全屏 / `Esc` 退总览。
- **地址栏 `#页码` 定位（deep-link）**：翻到第 n 页时把地址同步成 `#n`，进场读 `location.hash` 跳到该页，手动改 `#n` 也能跳——方便直接打开/分享到某一页（如 `index.html#14`）。
  - `updateCurrent(i)` 末尾：`try{history.replaceState(null,'','#'+(idx+1));}catch(e){location.hash=idx+1;}`（`file://` 下 `replaceState` 可能抛错 → 回退 `location.hash`）。
  - 进场：`var n=parseInt(location.hash.slice(1),10); var i=(!isNaN(n)&&n>=1&&n<=slides.length)?n-1:0;` 然后 `slides[i].scrollIntoView({block:'start',behavior:'auto'})`（i>0 时）；配合 `history.scrollRestoration='manual'`。
  - 手动改 hash：`addEventListener('hashchange',()=>{…go(n-1)…})`。
  - ⚠️ 页码 = **整个 deck 的绝对屏序**（封面=#1，其后顺延）——不是分册内的 head-r 编号。`Start-Process`/文件关联打开会**丢掉 `#fragment`**；要带锚点打开用 `cmd /c start "" "file:///…/index.html#14"`，且已开着的同 URL 旧标签可能只是聚焦不跳转（关掉旧标签再开）。
- 页面顺序随时可调：reorder 时记得**同步页码 head-r 的 01/02…**。

### ⚠️ scroll-snap 的两个坑（都踩过）
1. **`html,body{overflow:hidden;height:100%}`（各分册横向版自带）会让 snap 失效** → 必须让滚动容器（body）`overflow-y:auto` 且带 `scroll-snap-type:y`，否则停在两页之间。统一层用 `body{overflow:hidden auto;scroll-snap-type:y mandatory}` 盖掉。
2. **进/出全屏、改窗口后不会自动重新吸附**，会停在两页之间 → 监听 `fullscreenchange`/`resize`，之后 `slides[idx].scrollIntoView({block:'start'})` 重新吸附当前页（`scrollRestoration='manual'` + 进场 `scrollTo(0,0)` 防刷新落在半页）。

### 总览 Overview（缩略图网格）
- 进入：把每页 children 包进 `.slide-inner`（`position:absolute; width:100vw;height:100vh`，并按基调重建内部布局 `display:flex/padding`，否则 `flex:1` 失父→内容塌成一团）；`body.overview` 把 `#deck` 变 `display:grid`（3 列），`.slide` 变缩略框（`overflow:hidden`）；JS 给 `.slide-inner` 加 `transform:scale(缩略框宽/视口宽)`。
- **缩略框比例 = 当前视窗比例**（不强制 16:9）：框高 JS 设为 `缩略框宽 × 视口高/视口宽`，inner 左上对齐按宽缩放 → 每页完整缩小、不裁不留缝（精确预览）。
  - ⚠️ **别强制 16:9**：页面用 `vw/vh`=窗口比例，窗口非 16:9 时强制 16:9 必然「裁边」或「留黑缝」二选一。且 `aspect-ratio:16/9` 在带 `height:100vh` 的 `.slide` 上会被忽略（失效）→ 想要固定比例只能用 `padding-top:%` 写法。
- 点缩略图跳到该页并退出；`body.overview #panel,#toggle{display:none!important}` 隐藏调色入口（否则它会浮在概览上）。

## 多分册 → 单 index.html（推荐工作流）

一份完整汇报常拆成几个源文件各自维护（如 `cover.html` / `gray.html` / `glow.html`），最后用一个 **`build_index.py`** 合成单 `index.html`。这样每册可单独预览，合并版统一翻页/字体/字号。

### 合并的三个关键

1. **按标记抽取，别用硬编码行号**（源文件会增删行）：
   ```python
   def style_of(t): return t.split('<style>',1)[1].split('</style>',1)[0]
   # deck 内部 = <div id="deck"> 与其闭合 </div>（在 <div id="nav"> 之前）之间
   inner = t.split('<div id="deck">',1)[1].split('<div id="nav">',1)[0]
   slides = inner[:inner.rfind('</div>')]
   ```
2. **作用域化每册的 `.slide` 规则**，避免各册底色/内边距互相覆盖：
   - A 册：把 `.slide{...}` 改成 `.slide.s-gray{...}`，section 加 `class="slide s-gray"`。
   - B 册：把该册 CSS 里**所有** `.slide` 替换成 `.slide.s-glow`（连 `.slide .x` 后代选择器一起），section 加 `s-glow`。
   - 然后提供一个**统一层**（拼在所有分册 CSS 之后，靠"置后 + 必要时 !important"取胜）：统一的 `*` / `html,body`（鸿蒙字体 + body 作 scroll-snap 滚动容器）/ `#deck`（竖向块流）/ `.slide`（snap 几何）/ `#controls`·`.nav-dots`（含 `body.on-dark` 变体）/ 总览 CSS / 字号 ramp 落地。⚠️ 各分册自带的横向 `#deck{display:flex}` 和 `html,body{overflow:hidden;height:100%}` 必须被统一层显式盖掉（`#deck{display:block}` + `body{overflow:hidden auto}`），否则会横排/snap 失效。
3. **脚本合一**：各册都有 `deck/slides/idx` 等会重复声明 → 只保留**一份**当前页机制（IntersectionObserver）+ `go()`(scrollIntoView) + 控制栏/键盘/总览/全屏；各册专属逻辑（图表 init、黑底调色面板）保留但**对不属于它的页面惰性**（用 `data-chapter` 判空跳过）。

### 字号 token 的坑

字号 ramp `:root` token **要写进每个会用到它的源文件**（否则单开该分册时 `var(--fs-*)` 失效）。合并版的统一层再定义一遍同值即可（重复无害）。

### 黑底光晕调色面板 + 持久记忆

黑底设计点基调可挂一个调色面板（仅**章节封面页**显示；翻页时 `go()` 用 `appendChild` 把 `#panel`/`#toggle` 挂进当前章节封面 slide）。每章一组色值存在 JS 对象 `chapters`，写到每页 inline `--glow-*` 变量（各章互不串色）。

**持久记忆**：用 `localStorage`——
```js
const GLOW_KEY='deck-glow-chapters';
try{const sv=localStorage.getItem(GLOW_KEY);if(sv){const o=JSON.parse(sv);
  Object.keys(o).forEach(k=>{if(chapters[k])Object.assign(chapters[k],o[k]);});}}catch(e){}  // 加载时恢复
function saveChapters(){try{localStorage.setItem(GLOW_KEY,JSON.stringify(chapters));}catch(e){}}
// 在 apply()（每次调色变更都会调用）里调 saveChapters() → 这次调好下次打开自动恢复
```
模板 `assets/deck-template.html` 与合并版 `build_index.py` 都已内置。注意 `localStorage` 按 origin 存：`file://` 本地可用、GitHub Pages 同域可用。

### 字体加载

鸿蒙黑体走 jsDelivr CDN 的 @font-face（其 CSS 内部用相对路径 `../fonts/`，会自动从同一 CDN 取 woff2）。需要离线就把 woff2 下载到本地 `lib/fonts/` 并改 @font-face 的 url。
