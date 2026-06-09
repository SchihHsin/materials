# Deck 架构与多分册合并

## 单文件 deck 机制

```
#deck   position:fixed; display:flex; width:max-content; transition:transform .8s
.slide  width:100vw; height:100vh; flex:0 0 100vw
#nav    底部圆点；go(n) 改 translateX + 切 active；键盘 ← →
```

`go(n)` 三件事：①`deck.style.transform=translateX(-idx*100vw)`；②切 `.dot.active`；③按当前页基调切 `#nav.on-dark`（封面/黑底 = on-dark）。模板 `assets/deck-template.html` 已实现。

页面顺序随时可调：reorder 时记得**同步页码 head-r 的 01/02…**。

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
   - 然后提供一个**统一层**（拼在所有分册 CSS 之后，靠"置后 + 必要时 !important"取胜）：统一的 `*` / `html,body`（设鸿蒙字体）/ `#deck` / `.slide` 基础几何 / `#nav`（含 on-dark 变体）/ 字号 ramp 落地。
3. **脚本合一**：各册都有 `deck/slides/idx/go/nav` 会重复声明 → 只保留**一份** `go()`/nav/keydown；各册的专属逻辑（如图表 init、黑底调色面板）保留但**对不属于它的页面惰性**（用 `data-chapter` 之类判空跳过）。

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
