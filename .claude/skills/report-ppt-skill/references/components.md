# 组件库（骨架 + 关键 CSS）

> 通用件（**封面** / `head`（logo + 标题）/ `.card` 玻璃卡 / 胶囊指标条 / `#nav`）模板里**默认就有**，见 `assets/deck-template.html`。本文件补充其余高频组件。每页都用 `head`（logo + 结论标题 + 副标 + 页码）。

## ⭐ 选件路由（用户这么说 → 命中这个件）

> **复用本 skill 时最容易翻车的一步：识别不出用户的大白话对应哪个精调件，于是手搓一个更丑的版本。** 看到下面任一类内容/说法，**别自造排版**——直接翻到对应小节照抄骨架。用户很少说出组件的「学名」（VOC 墙 / 用户旅程…），要靠**意图**命中。

| 用户可能这么说（同义触发词） | 命中的件 | 一句话判据 |
|---|---|---|
| 核心数据 / 关键指标 / 转化率·占比·达成率 / 几个大百分比 / 数据概览 / KPI 概览 | **§1 渐变胶囊指标** | 3 个左右**带进度感的百分比**唱主角 → 多彩胶囊条 |
| 用户反馈 / 用户声音 / 访谈摘录 / 原声 / 吐槽·评论·语录 / 客户怎么说 / 调研摘要 / 痛点引用 | **§3 VOC 声音墙** | 一堆**长短不一的引用/评论**要陈列 → 瀑布流声音墙 |
| 全流程 / 端到端体验 / 用户一步步怎么做 / 各阶段 / 触点 / 情绪曲线 / journey / 全链路 / 操作流程的痛点 | **§4 用户旅程** | 内容**按阶段推进**、想看每阶段情绪/痛点 → 6 行旅程网格 |
| 竞品 / 对手 / 友商 / 同类工具 / 横向对比 / 市面方案 / A vs B vs C / 选型对比 | **§5 竞品对照** | **2~3 个同类产品**摆开比 + 给结论 → 三卡 + 对策条 |
| persona / 典型用户 / 目标用户长什么样 / 角色画像 / 用户分层 / 用户是谁 | **§6 用户画像**（⚠️二选一） | 刻画**某一类人**（职责/场景/痛点 或 能力维度） |
| 计划 / 排期 / 时间线 / 路线图 / 里程碑 / Q1Q2 / 阶段规划 / 什么时候上线 / roadmap | **§2 甘特 roadmap** | **带时间轴的条**（谁在哪个区间做） → 浮动甘特条 |
| 卡片里再附几个小数字 / 补充指标 / 标签+数值 | **§7 KPI 小数字组** | 嵌在别的卡**底部**的紧凑小指标，不独占一页 |
| 设计理念 / 方案亮点 / 我们的解法 / 核心设计点 / 问题→方案 | **§8 黑底设计点**（基调③） | 讲**方案/主张**，要氛围感 → 黑底光晕 + 渐变标题 |

判不准时，按「这页主体是什么」选：**数字**→§1，**引用堆**→§3，**分阶段**→§4，**多产品比**→§5，**讲人**→§6，**时间轴**→§2，**讲方案主张**→§8。命中后照抄该节骨架，只改文案/配色，别另起炉灶。

## 0. 封面 + logo（默认件）· ⛔ 标题前不放图标

- **封面默认有**：大图作底（无图时用紫光径向渐变兜底）+ 品牌 glyph + 大标题/副标/lead + 角标。换成真素材时把 `.cv-bg` 的 background 改成 `url(图)`。
- **logo 默认有，且必须备深/浅两版**（这是常踩的坑）：
  - **深色底**（封面 `.cv-logo`、黑底设计点页）→ 用 **白色 / 反白版** logo（如 `cann-dark-logo.svg`）。⚠️ 别把深色 logo 放深色底上——会几乎看不见（只剩彩色部件），曾因此返工。
  - **浅色底**（灰底分析页 head 的 `.brand .logo`）→ 用**深色 / 彩色版** logo（如 `CANNlogo.png`）。
  - 一律用 `<img src="…">` 引用（svg/png 皆可），别手敲文字拼 logo（字形对不上真 logo）。没有现成版本就找用户要，或对单色 logo 用 `filter:brightness(0) invert(1)` 反白（会丢彩色部件，慎用）。
- **⛔ 页面标题前只放 CANN logo，或什么都不放——绝不放任何装饰性 icon。** 这是复用 skill 时最容易犯的错：head 的 `.brand` 槽**默认放 CANN logo**（`<img class="logo" src="CANNlogo.png">` / 深底 `cann-dark-logo.svg`）；用户给了别的真 logo 就换那个；都没有就**把 `<img>` 删掉留空**。**严禁**在页面标题或区块标题前顶 Lucide / 通用 SVG 小图标。
- 装饰图标**只允许存在于个别精调组件内部**（如用户画像 `.pf-h2` 自带的圈形图标，是该组件的一部分），**不是通用模式**，不要外扩到别的标题上。

## 1. 关键指标 · 多彩渐变胶囊（精调模板之一，模板默认页就是它）

三列，每列 = 刻度行 + **多段彩色胶囊条** + 极细超大数字 + 说明。胶囊是**多段拼接**：每段一个 `linear-gradient(90deg,…)`，段与段在色谱上连续衔接（左段终点色 = 右段起点色），用 `flex:占比` 控制各段宽度。
```html
<div class="stat-col">
  <div class="stat-bar-area">
    <div class="stat-marks"><span>0</span><span class="stat-tri" style="left:72%">▼</span><span>100%</span></div>
    <div class="stat-pills">
      <div class="stat-pill" style="flex:72;background:linear-gradient(90deg,#FF6B9D,#FF9340)"></div>
      <div class="stat-pill" style="flex:28;background:linear-gradient(90deg,#FF9340,#FFE040)"></div>
    </div>
  </div>
  <div class="stat-num">72<span class="u">%</span></div>
  <div class="stat-desc">说明文字……</div>
</div>
```
- `.stat-pills{display:flex;gap:5px;height:6vh}` `.stat-pill{border-radius:999px;flex-shrink:0}`
- `.stat-num` 是 **Inter 200（极细）超大数字**（`min(8.4vw,13.8vh)`），属 bespoke 展示数字，不进 ramp。
- 三列分别用不同色谱（粉→橙→黄 / 绿→青→蓝 / 蓝→紫→红），别用同一种色。⚠️ 这是用户精调过的件，直接抄别另造单色填充条。

## 2. 甘特 roadmap（精调模板之一）

白底**玻璃大卡** + 浮动条 + 虚线网格底纹。要点：
- `.gantt{position:relative;height:54vh;margin:auto 0;border-radius:16px}` 用玻璃卡样式；底纹画在白卡背景（虚线 SVG grid），**实线全去**。
- 绝对定位的浮动条无视父 padding → 加内层 `.rm-pad{position:absolute;inset:6vh 4vw 4vh}` 容器。
- 条：`.rm-bar{position:absolute;height:...;max-height:46px;border-radius:14px;opacity:.86;backdrop-filter:blur(2px) saturate(130%)}`，用 `left/width/top` 百分比定位；玻璃白条 / 深条 `var(--g-ink)` / accent 条几种。
- "Now" 竖虚线 + 顶部药丸标 + 里程碑菱形。

## 3. VOC / 用户声音墙

```css
.voc-wall{column-count:4;column-gap:1.1vw}                 /* ⚠️ 用 column-count，不是 flex 列 */
.voc-card{break-inside:avoid;margin-bottom:1.1vw;border-radius:14px}
```
- 顶部一条**深色指标带**（`var(--g-ink)`，无阴影）和下方浅色墙形成明暗对比。
- 卡型多样化：大标题(灰块衬正文)/大引号/左右布局/普通/浅灰；头像用 DiceBear。

## 4. 用户旅程（全链路）

> **适用范围比"旅程图"更广**：任何**按阶段推进的流程**都能套这个模板——用户研究旅程、产品开发流程、运维流程、算子开发六阶段、训练工程师工作流……只要内容有"阶段列 × 信息行"的结构，就命中本件。

### CSS 骨架（直接抄）

```css
/* 旅程网格容器 */
.jn-r{display:grid;gap:.5vw}
.jn-cols{grid-template-columns:repeat(5,1fr)}   /* 5 阶段 */
/* 8 阶段紧凑版 */
.jn-cols8{grid-template-columns:repeat(8,minmax(0,1fr));gap:.46vw}
.jn-cols8 .jn-stage{border-radius:9px;padding:.58vh .35vw}
.jn-cols8 .jn-stage .s{font-size:var(--fs-sm);line-height:1.15}
.jn-cols8 .jn-stage .e{font-size:12px;line-height:1.15}
.jn-cols8 .jn-touch,.jn-cols8 .jn-pain,.jn-cols8 .jn-opp{font-size:var(--fs-xs);line-height:1.24;padding:.46vh .45vw;border-radius:8px}

/* 行标（触点 / 痛点 / 机会点 等）*/
.jn-rl{display:flex;align-items:center;gap:.5em;font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);margin-top:.4vh}
.jn-rl::after{content:'';flex:1;height:1px;background:var(--line)}

/* 阶段名（深色背景）*/
.jn-stage{background:var(--g-ink);color:#fff;border-radius:10px;padding:.8vh .7vw;text-align:center}
.jn-stage .s{font-weight:700;font-size:var(--fs-body)}
.jn-stage .e{font-family:'JetBrains Mono';font-size:var(--fs-xs);opacity:.6;letter-spacing:.08em}

/* 触点（中性白卡）*/
.jn-touch{background:#fff;border:1px solid var(--line);border-radius:9px;padding:.6vh .7vw;font-size:var(--fs-sm);color:var(--ink-2);text-align:center;line-height:1.35}

/* 痛点（红）/ 机会点（绿）*/
.jn-pain,.jn-opp{background:rgba(255,255,255,.55);border:1px solid rgba(255,255,255,.7);border-radius:9px;padding:.6vh .7vw;font-size:var(--fs-sm);line-height:1.4}
.jn-pain{color:#C0344A} .jn-pain b{color:#C0344A;font-weight:700}
.jn-opp{color:var(--ink-2)} .jn-opp b{color:#1E9E6A;font-weight:700}

/* 底部引用原声（跨列全宽）*/
.journey-voc{display:grid;grid-template-columns:1fr auto;gap:1vw;align-items:center;background:rgba(255,255,255,.62);border:1px solid rgba(255,255,255,.78);border-radius:10px;padding:.75vh .95vw}
.journey-voc .q{font-size:var(--fs-sm);line-height:1.45;color:var(--ink-2)} .journey-voc .q b{color:#C0344A}
.journey-voc .who{font-size:var(--fs-xs);color:var(--ink-3);white-space:nowrap}

/* 情绪曲线格子（ECharts line chart，跨全列）*/
.jn-emo{min-height:13vh;background:rgba(255,255,255,.5);border:1px solid rgba(255,255,255,.7);border-radius:12px;overflow:hidden;position:relative}
.jn-emo #emochart{position:absolute;inset:0}
```

### HTML 骨架（5 阶段标准版）

```html
<div class="body-area">
  <div class="jn">   <!-- 或直接 display:flex;flex-direction:column;gap:.7vh -->
    <!-- 1. 阶段行（深色）-->
    <div class="jn-r jn-cols">
      <div class="jn-stage"><div class="s">阶段名</div><div class="e">PHASE</div></div>
      <!-- × N 列 -->
    </div>
    <!-- 2. 行标 + 触点行 -->
    <div class="jn-rl">触点</div>
    <div class="jn-r jn-cols">
      <div class="jn-touch">触点描述</div><!-- × N -->
    </div>
    <!-- 3. 情绪曲线（可选，需 ECharts）-->
    <div class="jn-emo"><div id="emochart"></div></div>
    <!-- 4. 行标 + 痛点行 -->
    <div class="jn-rl">痛点</div>
    <div class="jn-r jn-cols">
      <div class="jn-pain"><b>关键词：</b>描述</div><!-- × N -->
    </div>
    <!-- 5. 机会点行 -->
    <div class="jn-r jn-cols">
      <div class="jn-opp"><b>机会：</b>描述</div><!-- × N -->
    </div>
    <!-- 6. 底部原声（可选）-->
    <div class="journey-voc">
      <div class="q">「引用原声」<b>关键词</b></div>
      <div class="who">姓名 · 角色</div>
    </div>
  </div>
</div>
```

### 变体说明

| 变体 | 怎么改 |
|---|---|
| **8 阶段**（训练工程师旅程） | `jn-r jn-cols8` 替换 `jn-cols`；顶部加 `.train-kpis` 指标带（4列 grid） |
| **6 阶段**（算子开发旅程） | `grid-template-columns:repeat(6,1fr)` 内联 style 即可，不另建 class |
| **无情绪曲线** | 直接删 `.jn-emo` 行，其余不变 |
| **行内附耗时** | `.jn-touch` 里加 `<b>30-60 分钟</b> → 秒级` 格式，不影响布局 |

- 每列**阶段数可以自由调**（3-10 列），只改 `grid-template-columns`。
- 痛点用**红色**（`#C0344A`），机会点用**绿色**（`#1E9E6A`）——色义固定，别乱换。
- 底部 `.journey-voc` 是**跨列全宽**的原声引用，选用（有代表性原声时才加）。

## 5. 竞品对照

三卡等高 grid：
```css
.compare{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4vw}
.cmp{display:flex;flex-direction:column;border-radius:14px;overflow:hidden;align-items:stretch}
.cmp-body{order:1}  .cmp-img{order:2;margin-top:auto;padding:0 .9vw .9vw}  /* 图沉卡底、对齐 */
.cmp-img img{width:100%;height:auto;border-radius:9px}                     /* 不裁切 */
```
- 每卡：产品名 kicker + 大段论述（重点加粗 + 紫高亮底）+ 图在最下 + 图下低调注释。
- 底部一条**对策深色条**（`var(--g-ink)`，tag 白底黑字、圆角同容器）。
- 竞品 = 同类工具横比 + 对策结论（通常不含自家产品）。

## 6. 用户画像（两种排版 · ⚠️【二选一】）

> 形式一、形式二是**两套并列方案，不要同时放进一份 deck**。生成时按用户输入择优：
> - **形式一**（左栏人物 + 右侧四区）：单一画像**深描**、属性多（职责/上下游协同/典型场景/痛点齐全）、信息量大时用；自包含、无外部依赖。
> - **形式二**（顶栏 + 三栏 + 雷达）：偏**能力/知识维度对比**、需要雷达图、版面更图形化时用；**需 ECharts**。
> 模板默认放的是形式一。

- **形式一**（仿"左栏 + 右块"模板）：左 ~23% 人物栏（portrait + 头部"人名/角色行" + 标签 chips + 职责 + 原声）；右侧四区——岗位特征(conic 环形 %)｜上下游协同(flow + 交付物 KPI) / 典型业务场景(16:9 mockup ×4) / 核心痛点。
  - 左栏垂直分布：`display:flex;flex-direction:column;gap:.85vh` 统一间距，原声块 `margin-top:auto` 贴底自适应；头部"角色行"用 body 档（比人名 h2 小一档，主次清楚）。
- **形式二**（仿"顶栏 + 三栏"模板）：顶栏(人物 / 环形 / 期待 等距) + 三栏(含 ECharts 雷达，两组对比色)。
- conic 环形：`background:conic-gradient(var(--accent) 0 var(--p),#D6DAE4 0)`，内圈 `::after{inset:23%;background:卡底色}` 挖空，`--p` 用 inline 变量传百分比。

## 7. KPI 小数字组

紧凑的"标签 + 数字"组，常嵌在卡片底部用虚线分隔：
```css
.fkpi{margin-top:.5vh;padding-top:.5vh;border-top:1px dashed rgba(0,0,0,.15);display:flex;flex-wrap:wrap;gap:.2em .55em}
.fkpi .kl{font-size:var(--fs-xs);color:#999;font-weight:700;background:#fff;border-radius:4px;padding:.1vh .4vw}
.fkpi b{font-size:var(--fs-xs);color:var(--accent)}
```

## 8. 黑底设计点页（基调③）

```css
.s-glow{background:#06060a;color:#fff;padding:7vh 6vw}
.s-glow .glow{position:absolute;left:0;right:0;bottom:0;height:35vh;z-index:0;pointer-events:none}
.s-glow .glow::before,.s-glow .glow::after{content:"";position:absolute;inset:0;mix-blend-mode:screen;
  background:radial-gradient(ellipse 78% 96% at 22% 112%, hsla(var(--glow-h),95%,52%,.68) 0%, transparent 90%)}
.h-title{font-weight:700;font-size:min(4.2vw,7.2vh);
  background:linear-gradient(100deg,hsl(var(--glow-h),95%,78%),hsl(var(--glow-h2),95%,72%));
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
```
- 左文右图（`.inner{display:grid;grid-template-columns:1fr 1fr}`），图位用玻璃拟态边框占位。
- 进阶：`data-chapter` + 给每页写 inline `--glow-h/--glow-h2/...` 实现**一章一色**；可挂一个调色面板（仅章节封面页显示）实时改色。
- 设计点正文 `.body` 用 body 档，要点列表 `.point`（小光点 + 标题 h3 + 描述 sm）。
