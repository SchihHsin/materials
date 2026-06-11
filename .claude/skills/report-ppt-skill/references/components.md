# 组件库（骨架 + 关键 CSS）

> 通用件（**封面** / `head`（logo + 标题）/ `.card` 玻璃卡 / 胶囊指标条 / `#nav`）模板里**默认就有**，见 `assets/deck-template.html`。本文件补充其余高频组件。每页都用 `head`（logo + 结论标题 + 副标 + 页码）。

## ⭐ 选件路由（用户这么说 → 命中这个件）

> **复用本 skill 时最容易翻车的一步：识别不出用户的大白话对应哪个精调件，于是手搓一个更丑的版本。** 看到下面任一类内容/说法，**别自造排版**——直接翻到对应小节照抄骨架。用户很少说出组件的「学名」（VOC 墙 / 用户旅程…），要靠**意图**命中。

| 用户可能这么说（中英文均算） | 命中的件 | 一句话判据 |
|---|---|---|
| 几个大数字/百分比/转化率/达成率/KPI overview/metrics/数据概览/关键指标/核心数据 | **§1 渐变胶囊指标** | 3 个左右**带进度感的百分比**唱主角 → 多彩胶囊条 |
| 计划/排期/里程碑/时间线/roadmap/甘特/泳道/sprint/Q1Q2/阶段规划/什么时候上线/路线图 | **§2 甘特 roadmap** | **带时间轴的条**（谁在哪个区间做） → 浮动甘特条 |
| 用户反馈/原声/吐槽/访谈摘录/语录/VOC/voice of customer/调研摘要/客户怎么说/痛点引用/把这些话整理一下 | **§3 VOC 声音墙** | 一堆**长短不一的引用/评论**要陈列 → 瀑布流声音墙 |
| 全流程/端到端/各阶段/触点/情绪曲线/journey/journey map/全链路/操作步骤的痛点/用户怎么一步步做/流程断裂点 | **§4 用户旅程** | 内容**按阶段推进**、想看每阶段情绪/痛点 → 行旅程网格 |
| 竞品/友商/对手/同类工具/横向对比/benchmark/competitive analysis/A vs B/选型/市面方案/竞品矩阵 | **§5 竞品对照** | **2~3 个同类产品**摆开比 + 给结论 → 三卡 + 对策条 |
| 介绍某个用户/他是谁/他的日常/角色特征/职责场景痛点/persona/用户画像/用户是谁（**单人深描**） | **§6a 用户画像·形式一** | 讲清楚**一个人**的全貌 → 左栏人物 + 右侧多区 |
| 几类用户有什么不同/角色对比/各角色的敏感程度/能力维度对比/radar/雷达图/多角色对照（**多人对比**） | **§6b 用户画像·形式二** | 展示**多人在若干维度的差异** → 顶栏 + 雷达图 |
| 卡片底部补几个小数字/附加指标/标签+数值/secondary KPI | **§7 KPI 小数字组** | 嵌在别的卡**底部**，不独占一页 |
| 设计理念/方案亮点/解法/核心设计点/问题→方案/design concept/我们的答案是 | **§8 黑底设计点** | 讲**方案/主张**，要氛围感 → 黑底光晕 + 渐变标题 |

判不准时，按主体：**数字进度**→§1，**时间轴**→§2，**引用堆**→§3，**分阶段流程**→§4，**多产品比**→§5，**讲一个人**→§6a，**多人维度对比**→§6b，**讲方案**→§8。命中后翻到该节，照抄骨架 + 参考填充示例，只改文案/配色。

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

### 填充示例（三列真实内容参照）

```html
<div class="stat-grid">
  <!-- 列1：粉→橙→黄色谱，指标=编译效率差距 -->
  <div class="stat-col">
    <div class="stat-bar-area">
      <div class="stat-marks"><span>秒级</span><span class="stat-tri" style="left:92%">▼</span><span>30-60 min</span></div>
      <div class="stat-pills">
        <div class="stat-pill" style="flex:92;background:linear-gradient(90deg,#FF6B9D,#FF9340)"></div>
        <div class="stat-pill" style="flex:8;background:linear-gradient(90deg,#FF9340,#FFE040)"></div>
      </div>
    </div>
    <div class="stat-num">5000<span class="u">×</span></div>
    <div class="stat-desc">编译耗时与 CUDA 秒级编译的差距。改一行代码要全量重编，不支持增量。</div>
  </div>
  <!-- 列2：绿→青→蓝色谱，指标=调试效率损失 -->
  <div class="stat-col">
    <div class="stat-bar-area">
      <div class="stat-marks"><span>正常</span><span class="stat-tri" style="left:70%">▼</span><span>-70%</span></div>
      <div class="stat-pills">
        <div class="stat-pill" style="flex:70;background:linear-gradient(90deg,#23CFA0,#45D65A)"></div>
        <div class="stat-pill" style="flex:30;background:linear-gradient(90deg,#45D65A,#667EEA)"></div>
      </div>
    </div>
    <div class="stat-num">-70<span class="u">%</span></div>
    <div class="stat-desc">高优化模式下断点失效，调试效率损失约 70%，只能靠日志。</div>
  </div>
  <!-- 列3：蓝→紫→红色谱，指标=日志膨胀倍数 -->
  <div class="stat-col">
    <div class="stat-bar-area">
      <div class="stat-marks"><span>1×</span><span class="stat-tri" style="left:80%">▼</span><span>5×</span></div>
      <div class="stat-pills">
        <div class="stat-pill" style="flex:80;background:linear-gradient(90deg,#667EEA,#A78BFA)"></div>
        <div class="stat-pill" style="flex:20;background:linear-gradient(90deg,#A78BFA,#FF5A6E)"></div>
      </div>
    </div>
    <div class="stat-num">3-5<span class="u">×</span></div>
    <div class="stat-desc">错误日志体积比 CUDA 膨胀 3-5 倍，十几万行 16 进制难以定位。</div>
  </div>
</div>
```

## 2. 甘特 roadmap（精调模板之一）

白底**玻璃大卡** + 浮动条 + 虚线网格底纹。

### CSS 骨架

```css
.gantt{flex:0 0 auto;height:54vh;margin:auto 0;display:flex;flex-direction:column;
  border-radius:16px;position:relative;overflow:hidden}
/* 浮动条无视父 padding → 加内层容器撑出留白 */
.rm-pad{position:absolute;top:6vh;left:3.2vw;right:3.2vw;bottom:4vh}
/* 虚线网格底纹（SVG background，画在 rm-pad::before）*/
.rm-pad::before{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100'%3E%3Cpath d='M100 0 V100' stroke='%23d4d8df' stroke-width='.5' stroke-dasharray='3 5'/%3E%3C/svg%3E");
  background-size:6.25% 100%}
/* 日期标 */
.rm-date{position:absolute;top:0;transform:translateX(-50%);font-family:'JetBrains Mono';font-size:max(9px,.66vw);font-weight:500;color:var(--ink-3);white-space:nowrap}
/* Now 线 + 药丸标 + 三角 */
.rm-now-pill{position:absolute;top:1.6%;transform:translateX(-50%);font-size:max(9px,.66vw);font-weight:600;color:#fff;background:rgba(91,91,214,.92);padding:3px 11px;border-radius:9px;z-index:3}
.rm-now-line{position:absolute;top:9%;height:84%;width:2px;background:linear-gradient(rgba(91,91,214,.85),rgba(91,91,214,.35));z-index:1}
.rm-now-tri{position:absolute;top:7.2%;transform:translateX(-50%);width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:7px solid var(--accent);z-index:2}
/* 浮动条（left/width/top 均用 % 定位）*/
.rm-bar{position:absolute;height:8.5%;min-height:30px;max-height:46px;border-radius:13px;display:flex;align-items:center;justify-content:space-between;padding:0 14px;font-size:max(11px,.94vw);font-weight:500;backdrop-filter:blur(2px) saturate(130%);-webkit-backdrop-filter:blur(2px) saturate(130%);z-index:2}
.rm-bar .lbl{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rm-badge{font-size:max(9px,.74vw);font-weight:600;padding:3px 9px;border-radius:7px;white-space:nowrap;margin-left:10px;flex:none}
/* 三种条样式 */
.rm-bar.white{background:rgba(255,255,255,.6);border:1px solid rgba(255,255,255,.75);color:var(--ink);box-shadow:0 8px 22px rgba(30,40,70,.1),inset 0 1px 0 rgba(255,255,255,.8)}
.rm-bar.white .rm-badge{background:var(--dark);color:#fff}
.rm-bar.dark{background:var(--g-ink);border:1px solid rgba(255,255,255,.22);color:#fff;box-shadow:0 8px 26px rgba(20,25,35,.32),inset 0 1px 0 rgba(255,255,255,.28)}
.rm-bar.dark .rm-badge{background:rgba(255,255,255,.92);color:var(--dark)}
.rm-bar.accent{background:var(--g-accent);border:1px solid rgba(255,255,255,.34);color:#fff;box-shadow:0 10px 28px rgba(91,91,214,.3),inset 0 1px 0 rgba(255,255,255,.35)}
.rm-bar.accent .rm-badge{background:#fff;color:#5B21B6}
/* 里程碑菱形 + 标注 */
.rm-diamond{position:absolute;width:18px;height:18px;transform:rotate(45deg);background:var(--g-ink);border:1px solid rgba(255,255,255,.3);border-radius:3px;z-index:3}
.rm-ms{position:absolute;font-size:max(10px,.78vw);font-weight:500;color:var(--ink-2)}
```

### HTML 骨架

```html
<div class="body-area">
  <div class="gantt card">   <!-- .card 给玻璃质感 -->
    <div class="rm-pad">
      <!-- 日期标（按时间轴均分 left%）-->
      <div class="rm-date" style="left:6%">Q1 初</div>
      <div class="rm-date" style="left:31%">Q2 初</div>
      <div class="rm-date" style="left:56%">Q3 初</div>
      <div class="rm-date" style="left:81%">Q4 初</div>
      <!-- Now 指示线 -->
      <div class="rm-now-pill" style="left:38%">Now</div>
      <div class="rm-now-tri"  style="left:38%"></div>
      <div class="rm-now-line" style="left:38%"></div>
      <!-- 浮动条：left=开始%  width=持续%  top=泳道% -->
      <div class="rm-bar dark"  style="left:5%;width:22%;top:13%"><span class="lbl">任务A</span><span class="rm-badge">6 周</span></div>
      <div class="rm-bar white" style="left:15%;width:18%;top:27%"><span class="lbl">任务B</span><span class="rm-badge">5 周</span></div>
      <div class="rm-bar accent" style="left:35%;width:28%;top:41%"><span class="lbl">任务C（关键路径）</span><span class="rm-badge">8 周</span></div>
      <!-- 里程碑 -->
      <div class="rm-diamond" style="left:63%;top:72%"></div>
      <div class="rm-ms"      style="left:66%;top:72%">里程碑 · 发布</div>
    </div>
  </div>
</div>
```

- **泳道靠 `top` 错开**（每条约 12% 间距），**时间轴靠 `left/width`**，全用 `%` — 改窗口自适应。
- 条型语义：`dark`=已完成/主线，`white`=支撑/并行，`accent`=关键路径/重点交付。

### 填充示例（设计工作 roadmap 参照）

```html
<div class="rm-pad">
  <div class="rm-date" style="left:6%">2月</div>
  <div class="rm-date" style="left:25%">3月</div>
  <div class="rm-date" style="left:44%">4月</div>
  <div class="rm-date" style="left:63%">5月</div>
  <div class="rm-date" style="left:82%">6月</div>

  <div class="rm-now-pill" style="left:40%">Now</div>
  <div class="rm-now-tri"  style="left:40%"></div>
  <div class="rm-now-line" style="left:40%"></div>

  <div class="rm-bar dark"   style="left:5%;width:21%;top:13%"><span class="lbl">用户研究 &amp; VOC</span><span class="rm-badge">25 天</span></div>
  <div class="rm-bar white"  style="left:11%;width:14%;top:26%"><span class="lbl">竞品调研</span><span class="rm-badge">10 天</span></div>
  <div class="rm-bar white"  style="left:25%;width:16%;top:38%"><span class="lbl">设计概念定义</span><span class="rm-badge">12 天</span></div>
  <div class="rm-bar dark"   style="left:39%;width:25%;top:26%"><span class="lbl">交互式文档 &amp; 成长地图</span><span class="rm-badge">20 天</span></div>
  <div class="rm-bar accent" style="left:50%;width:26%;top:50%"><span class="lbl">Profiling 看板（关键路径）</span><span class="rm-badge">30 天</span></div>
  <div class="rm-bar accent" style="left:58%;width:28%;top:38%"><span class="lbl">算子开发向导</span><span class="rm-badge">28 天</span></div>
  <div class="rm-bar white"  style="left:70%;width:16%;top:62%"><span class="lbl">智能错误诊断</span><span class="rm-badge">12 天</span></div>
  <div class="rm-bar dark"   style="left:83%;width:14%;top:50%"><span class="lbl">联调 &amp; 灰度发布</span><span class="rm-badge">10 天</span></div>

  <div class="rm-diamond" style="left:41%;top:74%"></div>
  <div class="rm-ms"      style="left:44%;top:73.5%">设计定稿 · 转入开发</div>
</div>
```

## 3. VOC / 用户声音墙

### CSS 骨架

```css
/* ⚠️ 用 column-count 瀑布流，绝不用 flex 列（高度推挤会产生诡异间距）*/
.voc-wall{flex:1;min-height:0;column-count:4;column-gap:1.1vw}
.voc-card{break-inside:avoid;margin-bottom:1.1vw;border-radius:15px;padding:1.7vh 1.2vw;
  position:relative;display:flex;flex-direction:column;gap:.95vh}
/* 引用文字 */
.voc-q{font-size:max(12px,.86vw);line-height:1.55;color:var(--ink)}
.voc-q.boxed{background:rgba(22,30,46,.055);border-radius:9px;padding:1vh 1vw}   /* 灰块衬底 */
/* 大引号装饰 */
.qm{font-family:Georgia,serif;font-weight:700;color:var(--accent);opacity:.24}
.qm.open{font-size:42px;line-height:.72;margin-bottom:-.6vh}
/* 头像 + 署名 */
.voc-meta{display:flex;align-items:center;gap:.55vw;margin-top:1vh;padding-top:.3vh}
.voc-ava{width:40px;height:40px;border-radius:50%;flex-shrink:0;overflow:hidden;background:var(--card-2)}
.voc-ava img{width:100%;height:100%;display:block;object-fit:cover}
.voc-nm{font-weight:600;font-size:max(12px,.84vw);line-height:1.2}
.voc-rl{font-family:'JetBrains Mono';font-size:10px;color:var(--ink-3);margin-top:.2vh}
/* 卡片变体 */
.voc-card.soft{background:linear-gradient(160deg,rgba(233,236,242,.9),rgba(243,245,249,.8))!important}
.voc-card.lr{flex-direction:row;align-items:flex-start;gap:.85vw}           /* 左头像右文字 */
.voc-card.lr .voc-ava{width:44px;height:44px;flex-shrink:0;margin-top:.2vh}
.voc-card.hl{background:var(--g-ink)!important;color:#fff}                  /* 深色高亮卡 */
.voc-card.hl .voc-q,.voc-card.hl .voc-nm{color:#fff}
.voc-card.hl .voc-rl{color:rgba(255,255,255,.6)}
.voc-card.hl .qm{color:#9b8ce8;opacity:.9}
.voc-card.accent{background:var(--g-accent)!important;color:#fff}           /* accent 强调卡 */
.voc-card.accent .voc-q,.voc-card.accent .voc-nm{color:#fff}
.voc-card.accent .voc-rl{color:rgba(255,255,255,.72)}
/* 顶部深色指标带（可选，和下方浅色墙形成明暗对比）*/
.voc-top{display:grid;grid-template-columns:1.7fr 1fr 1fr 1fr;gap:1vw;flex:0 0 auto;margin-bottom:1vh}
.voc-top.t-dark{background:var(--g-ink);border-radius:14px;padding:1.8vh 1.6vw;color:#fff}
```

### HTML 骨架

```html
<div class="body-area" style="flex-direction:column">
  <!-- 可选：顶部深色指标带 -->
  <div class="voc-top t-dark">
    <div class="voc-sent"><div class="sh">核心发现</div><div>一句话总结</div></div>
    <div class="voc-stat"><div class="n">72<span class="u">%</span></div><div class="l">维度A</div></div>
    <div class="voc-stat"><div class="n">3.2<span class="u">×</span></div><div class="l">维度B</div></div>
    <div class="voc-stat"><div class="n">18<span class="u">人</span></div><div class="l">维度C</div></div>
  </div>
  <!-- 瀑布流声音墙 -->
  <div class="voc-wall">
    <!-- 普通卡 -->
    <div class="voc-card">
      <div class="voc-q">引用原声……</div>
      <div class="voc-meta">
        <div class="voc-ava"><img src="av/role-xxx.svg" alt=""></div>
        <div><div class="voc-nm">姓名 · 角色</div><div class="voc-rl">公司 · N 年</div></div>
      </div>
    </div>
    <!-- 大引号卡 -->
    <div class="voc-card">
      <div class="qm open">"</div>
      <div class="voc-q">引用原声……</div>
      <div class="voc-meta">…</div>
    </div>
    <!-- 深色高亮卡（用于最核心原声）-->
    <div class="voc-card hl">
      <div class="voc-q">最核心的那句话……</div>
      <div class="voc-meta">…</div>
    </div>
    <!-- 左头像右文字卡 -->
    <div class="voc-card lr">
      <div class="voc-ava"><img src="av/role-xxx.svg" alt=""></div>
      <div>
        <div class="voc-q">引用原声……</div>
        <div style="display:flex;gap:.5vw;align-items:center;margin-top:.8vh">
          <span class="voc-nm">姓名</span><span class="voc-rl">角色</span>
        </div>
      </div>
    </div>
    <!-- 浅灰 soft 卡 -->
    <div class="voc-card soft">
      <div class="voc-q boxed">引用原声……</div>
      <div class="voc-meta">…</div>
    </div>
  </div>
</div>
```

- **卡型多样化**是 VOC 墙的精髓：同一页混用普通/大引号/深色/左右布局，避免视觉单调。
- 头像用 **DiceBear notionists** 生成 SVG（CC0）存本地 `av/`，`beardProbability=0`，`backgroundColor` 跟页面底色。

### 填充示例（4 种卡型混排参照）

```html
<div class="voc-wall">
  <!-- 普通卡 -->
  <div class="voc-card">
    <div class="voc-q">Profiling 看板能直接点到瓶颈算子，比翻日志定位快太多了。</div>
    <div class="voc-meta">
      <div class="voc-ava"><img src="av/role-asc.svg" alt=""></div>
      <div><div class="voc-nm">陈工 · 框架开发</div><div class="voc-rl">AI 平台 · 5 年</div></div>
    </div>
  </div>
  <!-- 深色高亮卡（最核心原声）-->
  <div class="voc-card hl">
    <div class="qm open">"</div>
    <div class="voc-q">ASC 最困难的一点就是没法调试，高优化下断点全失效。</div>
    <div class="voc-meta">
      <div class="voc-ava"><img src="av/role-asc.svg" alt=""></div>
      <div><div class="voc-nm">王工 · ASC 算子开发</div><div class="voc-rl">芯片厂商 · 4 年</div></div>
    </div>
  </div>
  <!-- 左头像右文字卡 -->
  <div class="voc-card lr">
    <div class="voc-ava"><img src="av/role-research.svg" alt=""></div>
    <div>
      <div class="voc-q">学习率调不准会出现不收敛，NPU/GPU 精度对齐比想象中难。</div>
      <div style="display:flex;gap:.5vw;align-items:center;margin-top:.8vh">
        <span class="voc-nm">陈工 · 高校训练</span><span class="voc-rl">研究机构</span>
      </div>
    </div>
  </div>
  <!-- 灰块衬底卡 -->
  <div class="voc-card soft">
    <div class="voc-q boxed">如果环境能一键拉起、版本自动对齐，复现实验就不再是噩梦。</div>
    <div class="voc-meta">
      <div class="voc-ava"><img src="av/role-student.svg" alt=""></div>
      <div><div class="voc-nm">熊工 · 高校学生</div><div class="voc-rl">硕士在读</div></div>
    </div>
  </div>
  <!-- accent 强调卡（次核心，用于第二重要结论）-->
  <div class="voc-card accent">
    <div class="voc-q">很多内容只能口口相传，新人完全靠问老人。</div>
    <div class="voc-meta">
      <div class="voc-ava"><img src="av/dongguyin.svg" alt=""></div>
      <div><div class="voc-nm">董工 · 推理优化</div><div class="voc-rl">云推理 · 3 年</div></div>
    </div>
  </div>
</div>
```

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

### 填充示例（5 阶段算子开发旅程参照）

```html
<div class="body-area">
  <div style="display:flex;flex-direction:column;gap:.7vh;flex:1;min-height:0">
    <!-- 阶段行 -->
    <div class="jn-r jn-cols">
      <div class="jn-stage"><div class="s">准备接入</div><div class="e">PREPARE</div></div>
      <div class="jn-stage"><div class="s">环境搭建</div><div class="e">SETUP</div></div>
      <div class="jn-stage"><div class="s">算子开发·编译</div><div class="e">DEVELOP</div></div>
      <div class="jn-stage"><div class="s">调试定位</div><div class="e">DEBUG</div></div>
      <div class="jn-stage"><div class="s">训练·验证调优</div><div class="e">TUNE</div></div>
    </div>
    <!-- 触点行 -->
    <div class="jn-rl">触点</div>
    <div class="jn-r jn-cols">
      <div class="jn-touch">昇腾官网文档 · 选型指南（缺）</div>
      <div class="jn-touch">CANN 安装包 · MS 调试工具</div>
      <div class="jn-touch">CodeArts IDE · tbe 编译</div>
      <div class="jn-touch">MS debug · 仿真日志</div>
      <div class="jn-touch">训练监控 · TensorBoard · NPU 日志</div>
    </div>
    <!-- 情绪曲线（ECharts，可选）-->
    <div class="jn-emo"><div id="emochart"></div></div>
    <!-- 痛点行 -->
    <div class="jn-rl">痛点</div>
    <div class="jn-r jn-cols">
      <div class="jn-pain">文档分散，<b>无法快速确认算子是否支持</b></div>
      <div class="jn-pain">MS 调试配置复杂，<b>缺一键环境验证</b></div>
      <div class="jn-pain"><b>编译 30-60 分钟</b>，不支持增量</div>
      <div class="jn-pain"><b>高优化下无法打断点</b>，十几万行 16 进制日志</div>
      <div class="jn-pain"><b>NPU/GPU 精度对齐难</b>，监控分散</div>
    </div>
    <!-- 机会点行 -->
    <div class="jn-r jn-cols">
      <div class="jn-opp"><b>机会：</b>统一算子查询总表</div>
      <div class="jn-opp"><b>机会：</b>一键安装与验证脚本</div>
      <div class="jn-opp"><b>机会：</b>增量编译 + 智能去重</div>
      <div class="jn-opp"><b>机会：</b>IR 级可视化调试</div>
      <div class="jn-opp"><b>机会：</b>自动精度对齐与误差热力图</div>
    </div>
    <!-- 底部原声（可选）-->
    <div class="journey-voc">
      <div class="q">「<b>ASC 最困难的一点就是没法调试</b>」——问题集中在编译与调试两段，且互相放大</div>
      <div class="who">王工 · ASC 算子开发</div>
    </div>
  </div>
</div>
```

## 5. 竞品对照

### CSS 骨架

```css
.compare{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4vw;flex:0 0 auto}
.cmp{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}
.cmp.focus{border:2px solid var(--accent);box-shadow:0 12px 32px -12px rgba(91,91,214,.4)} /* 重点产品高亮 */
/* 文字区（order:1 在上）*/
.cmp-body{order:1;padding:2vh 1.4vw .8vh;flex:0 0 auto;display:flex;flex-direction:column;gap:1.7vh}
.cmp-h{font-family:'Inter','Noto Sans SC';font-weight:700;font-size:max(15px,1.18vw);letter-spacing:-.01em;line-height:1.3;color:var(--ink)}
.cmp-h .hk{display:block;font-family:'JetBrains Mono';font-size:10px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin-bottom:.5vh}
.cmp-desc{font-size:max(13px,.98vw);line-height:1.72;color:var(--ink-2)}
.cmp-desc b{color:var(--ink);font-weight:600;background:linear-gradient(transparent 60%,rgba(91,91,214,.16) 0)} /* 紫高亮底 */
/* 图区（order:2 沉底，margin-top:auto 让图对齐底部）*/
.cmp-img{order:2;flex:0 0 auto;padding:0 .9vw .9vw;margin-top:auto}
.cmp-img img{width:100%;height:auto;display:block;border-radius:9px;border:1px solid var(--line)}
.cmp-cap{font-family:'JetBrains Mono';font-size:11px;color:var(--ink-3);text-align:center;letter-spacing:.02em;margin-top:.7vh}
/* 底部对策深色条 */
.verdict{flex:0 0 auto;margin-top:1.6vh;display:grid;grid-template-columns:auto 1fr;gap:1.2vw;align-items:center;background:var(--g-ink);color:#fff;border-radius:12px;padding:1.8vh 1.6vw}
.verdict .vk{font-family:'Inter','Noto Sans SC';font-size:13px;font-weight:700;color:var(--ink);background:#fff;border-radius:12px;padding:6px 15px;white-space:nowrap}
.verdict .vv{font-size:max(14px,1.02vw);line-height:1.55}
.verdict .vv b{font-weight:700}
```

### HTML 骨架

```html
<div class="body-area" style="flex-direction:column">
  <div class="compare">
    <!-- 每卡：kicker + 论述（加粗+紫高亮底）+ 图沉底 -->
    <div class="cmp">
      <div class="cmp-body">
        <div class="cmp-h"><span class="hk">产品定位 kicker</span>一句话核心优势</div>
        <div class="cmp-desc">详细论述……<b>重点关键词</b>加粗后自动出现紫色高亮底。继续描述……</div>
      </div>
      <div class="cmp-img">
        <img src="cmp-productA.jpg" alt="产品A 截图">
        <div class="cmp-cap">产品A 名称</div>
      </div>
    </div>
    <div class="cmp">…</div>
    <div class="cmp">…</div>
  </div>
  <!-- 对策条（跨三卡全宽，总结我方应对策略）-->
  <div class="verdict">
    <span class="vk">对策</span>
    <span class="vv">基于以上对比，我们应该……<b>关键结论加粗</b>，补齐……</span>
  </div>
</div>
```

- **图沉卡底**（`margin-top:auto`）让三卡截图底部对齐，视觉整齐。
- `b` 标签自动加紫色高亮底（`.cmp-desc b` CSS），重点词直接 `<b>` 包即可，无需手动加样式。
- `.cmp.focus` 给「我方产品」或「最值得关注的对标」加蓝色高亮边框。
- 竞品 = **同类工具横比 + 对策结论**，通常不把自家产品列进对比卡，而是放在对策条里给结论。

### 填充示例（性能分析工具三家对比参照）

```html
<div class="body-area" style="flex-direction:column">
  <div class="compare">
    <div class="cmp">
      <div class="cmp-body">
        <div class="cmp-h"><span class="hk">Timeline 标杆</span>时间线 + 源码跳转，新手零门槛</div>
        <div class="cmp-desc">以 <b>CPU/GPU 统一时间线</b>为核心，框选即缩放、定位瓶颈算子，<b>事件→源码一键跳转</b>，配合完善教程体系，几乎零学习成本。</div>
      </div>
      <div class="cmp-img"><img src="cmp-nsight.jpg" alt="Nsight"><div class="cmp-cap">NVIDIA Nsight Systems</div></div>
    </div>
    <div class="cmp">
      <div class="cmp-body">
        <div class="cmp-h"><span class="hk">归因深度</span>逐层下钻，瓶颈归因到微架构</div>
        <div class="cmp-desc">多种分析类型，热点可<b>逐层下钻</b>，<b>微架构级瓶颈归因</b>直指根因，向导式配置让调优<b>有据可依、不靠猜测</b>。</div>
      </div>
      <div class="cmp-img"><img src="cmp-vtune.jpg" alt="VTune"><div class="cmp-cap">Intel VTune Profiler</div></div>
    </div>
    <div class="cmp">
      <div class="cmp-body">
        <div class="cmp-h"><span class="hk">开放协作</span>开源 Web 化，trace 浏览器可分享</div>
        <div class="cmp-desc">走<b>开源 + Web 化</b>路线，trace 导出 Perfetto 在浏览器查看与<b>分享</b>，天然适合<b>团队协作与远程复现</b>。</div>
      </div>
      <div class="cmp-img"><img src="cmp-rocm-tool.jpg" alt="rocprof"><div class="cmp-cap">AMD rocprof / Omnitrace</div></div>
    </div>
  </div>
  <div class="verdict">
    <span class="vk">对策</span>
    <span class="vv">CANN Profiling 看板应对标三家共性——<b>统一时间线 + 一键瓶颈定位 + Web 化可视化</b>，并补齐<b>事件→源码跳转</b>与浏览器端 trace 分享，把命令行门槛降下来。</span>
  </div>
</div>
```

## 6a. 用户画像·形式一（左栏人物 + 右侧多区）

> **触发**：「介绍某个用户」「他是谁/他的日常/职责场景痛点」「persona」—— **单人深描**，优先选此形式，无外部依赖。

### 形式一 CSS 骨架

```css
/* 整体布局：左 ~23% 人物栏 + 右侧 */
.pf-row{display:grid;grid-template-columns:.82fr 1.7fr;gap:1.8vw;align-items:start;flex:1;min-height:0}
/* 左侧人物栏 */
.pf-side{background:#EFEFF1;border-radius:16px;padding:1.7vh 1.2vw;display:flex;flex-direction:column;gap:.85vh;overflow:hidden}
.pf-portrait{width:100%;aspect-ratio:1/.86;border-radius:12px;overflow:hidden;background:#fff;flex:0 0 auto}
.pf-portrait img{width:100%;height:100%;object-fit:cover}
/* 头部信息块 */
.pf-sb{border-radius:11px;padding:.95vh .9vw;flex:0 0 auto}
.pf-sb.head{background:rgba(91,91,214,.08)}
.pf-sb.head .nm{font-family:'Inter','Noto Sans SC';font-weight:800;font-size:var(--fs-h2);color:#1a1a1a}
.pf-sb.head .rl{font-size:var(--fs-body);color:var(--accent);font-weight:600;margin-top:.1vh}
.pf-sb.white{background:#fff}
.pf-sb .sbh{font-size:var(--fs-xs);color:#999;font-weight:700;margin-bottom:.25vh}
.pf-sb .sbt{font-size:var(--fs-body);color:#333;line-height:1.5}
/* 标签 chips */
.pf-chips{display:flex;flex-wrap:wrap;gap:.4vw}
.pf-chips span{font-size:var(--fs-sm);color:var(--accent);background:rgba(91,91,214,.08);border-radius:6px;padding:.4vh .65vw}
/* 原声（margin-top:auto 贴底）*/
.pf-quote{font-size:var(--fs-body);color:#333;font-weight:600;line-height:1.5;text-decoration:underline;text-underline-offset:3px;text-decoration-color:#c2c7d0;margin-top:auto}
/* 右侧分区块 */
.pf-r{display:flex;flex-direction:column;gap:1.1vh;min-height:0}
.pf-block{display:flex;flex-direction:column;min-width:0}
.pf-h2{align-self:flex-start;display:inline-flex;align-items:center;gap:.45em;background:var(--accent);color:#fff;border-radius:20px;padding:.3vh .9vw .3vh .3vh;font-weight:700;font-size:var(--fs-h3);margin-bottom:.8vh}
.pf-h2 .ico{width:clamp(21px,1.8vw,27px);height:clamp(21px,1.8vw,27px);border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0}
/* conic 环形进度 */
.pf-ring{width:clamp(56px,5vw,72px);height:clamp(56px,5vw,72px);border-radius:50%;position:relative;flex-shrink:0}
.pf-ring::after{content:'';position:absolute;inset:23%;border-radius:50%;background:var(--card-bg,#EFEFF1)}
```

### 形式一 HTML 骨架

```html
<div class="body-area">
  <div class="pf-row">
    <!-- 左栏 -->
    <div class="pf-side">
      <div class="pf-portrait"><img src="av/role-xxx.svg" alt=""></div>
      <div class="pf-sb head"><div class="nm">张工</div><div class="rl">资深算子工程师</div></div>
      <div class="pf-chips">
        <span>5年+</span><span>C/C++</span><span>底层开发</span>
      </div>
      <div class="pf-sb white">
        <div class="sbh">核心职责</div>
        <div class="sbt">负责……一句话概括。</div>
      </div>
      <div class="pf-quote">「最核心的一句原声引用」</div>
    </div>
    <!-- 右侧 -->
    <div class="pf-r">
      <!-- 区块一：岗位特征（conic 环形）-->
      <div class="pf-block">
        <div class="pf-h2"><span class="ico"><!-- SVG icon --></span>岗位特征</div>
        <!-- 内容：conic 环形 + 标签 -->
      </div>
      <!-- 区块二：典型场景 -->
      <div class="pf-block">
        <div class="pf-h2"><span class="ico"><!-- SVG icon --></span>典型场景</div>
        <!-- mockup 截图 or 文字列表 -->
      </div>
      <!-- 区块三：核心痛点 -->
      <div class="pf-block">
        <div class="pf-h2"><span class="ico"><!-- SVG icon --></span>核心痛点</div>
        <!-- 痛点列表 -->
      </div>
    </div>
  </div>
</div>
```

### 填充示例（算子工程师画像参照）

```html
<div class="body-area">
  <div class="pf-row">
    <!-- 左栏 -->
    <div class="pf-side">
      <div class="pf-portrait"><img src="av/role-asc.svg" alt="王工"></div>
      <div class="pf-sb head"><div class="nm">王工</div><div class="rl">资深 ASC 算子工程师</div></div>
      <div class="pf-chips"><span>5年+</span><span>C/C++</span><span>CUDA 迁移</span><span>汇编基础</span></div>
      <div class="pf-sb white">
        <div class="sbh">核心职责</div>
        <div class="sbt">负责底层算子开发与优化，承接算法侧需求，保障算子可复用性与性能。</div>
      </div>
      <div class="pf-quote">「ASC 最困难的一点就是没法调试。」</div>
    </div>
    <!-- 右侧 -->
    <div class="pf-r">
      <div class="pf-block">
        <div class="pf-h2">
          <span class="ico"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><circle cx="8" cy="8" r="6"/></svg></span>岗位特征
        </div>
        <!-- conic 环形 + 标签列表 -->
        <div style="display:flex;gap:1.2vw;align-items:center">
          <div class="pf-ring" style="background:conic-gradient(var(--accent) 0 75%,#D6DAE4 0);--card-bg:#EFEFF1"></div>
          <div style="font-size:var(--fs-sm);color:#333;line-height:1.6">编译调试占用 <b>75%</b> 工作时间<br/>其余为需求评审与代码 Review</div>
        </div>
      </div>
      <div class="pf-block">
        <div class="pf-h2"><span class="ico"><!-- icon --></span>典型痛点</div>
        <div style="display:flex;flex-direction:column;gap:.6vh;font-size:var(--fs-sm);color:#333;line-height:1.5">
          <div>🔴 编译 30-60 分钟，改一行全量重编</div>
          <div>🔴 高优化模式断点失效，靠日志定位</div>
          <div>🔴 算子支持状态散落各处，手动查代码</div>
        </div>
      </div>
      <div class="pf-block">
        <div class="pf-h2"><span class="ico"><!-- icon --></span>核心期望</div>
        <div style="font-size:var(--fs-sm);color:#333;line-height:1.6">秒级增量编译、源码级断点调试、统一算子查询入口。</div>
      </div>
    </div>
  </div>
</div>
```

---

## 6b. 用户画像·形式二（顶栏 + 三栏 + ECharts 雷达）

> **触发**：「几类用户有什么不同」「各角色对 X 的敏感程度」「能力维度对比」「雷达图」—— **多人对比**，需 ECharts。

结构：
- **顶栏**：人物卡（头像+姓名+角色）/ conic 环形大图 / 期待文字块 — 三等分 grid。
- **三栏**：左=技术背景，中=ECharts 雷达（两组对比色：内源蓝 `#5B5BD6` / 生态红 `#FF5A6E`），右=痛点 & 机会。
- 雷达维度通常 5-8 个，代表用户在关键能力/需求上的强弱分布。

## 7. KPI 小数字组

紧凑的"标签 + 数字"组，常嵌在卡片底部用虚线分隔：
```css
.fkpi{margin-top:.5vh;padding-top:.5vh;border-top:1px dashed rgba(0,0,0,.15);display:flex;flex-wrap:wrap;gap:.2em .55em}
.fkpi .kl{font-size:var(--fs-xs);color:#999;font-weight:700;background:#fff;border-radius:4px;padding:.1vh .4vw}
.fkpi b{font-size:var(--fs-xs);color:var(--accent)}
```

## 8. 黑底设计点页（基调③）

### CSS 骨架

```css
.s-glow{background:#06060a;color:#fff;padding:7vh 6vw;position:relative}
/* 底部渐变光晕（颜色由 --glow-h 变量控制，可调色面板实时改）*/
.s-glow .glow{position:absolute;left:0;right:0;bottom:0;height:35vh;z-index:0;pointer-events:none}
.s-glow .glow::before,.s-glow .glow::after{content:"";position:absolute;inset:0;mix-blend-mode:screen;
  background:radial-gradient(ellipse 78% 96% at 22% 112%,hsla(var(--glow-h),95%,52%,.68) 0%,transparent 90%)}
.s-glow .glow::after{background:radial-gradient(ellipse 78% 96% at 78% 112%,hsla(var(--glow-h2),95%,52%,.52) 0%,transparent 90%)}
/* 渐变标题字 */
.h-title{position:relative;z-index:1;font-weight:700;font-size:min(4.2vw,7.2vh);line-height:1.12;
  background:linear-gradient(100deg,hsl(var(--glow-h),95%,78%),hsl(var(--glow-h2),95%,72%));
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
/* 左文右图双栏 */
.glow-inner{position:relative;z-index:1;display:grid;grid-template-columns:1fr 1fr;gap:3vw;flex:1;min-height:0;align-items:center}
/* 图位占位（玻璃拟态）*/
.shot{position:relative;border-radius:14px;overflow:hidden;background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.12);box-shadow:0 30px 80px -20px hsla(var(--glow-h),var(--glow-sat,95%),30%,.5);display:flex;align-items:center;justify-content:center;aspect-ratio:16/10}
/* 要点列表 */
.glow-points{display:flex;flex-direction:column;gap:1.6vh;margin-top:2vh}
.point{display:grid;grid-template-columns:auto 1fr;gap:.9vw;align-items:start}
.point-dot{width:8px;height:8px;border-radius:50%;background:hsl(var(--glow-h),95%,72%);margin-top:.55em;flex-shrink:0}
.point-body .pt{font-weight:700;font-size:var(--fs-h3);margin-bottom:.3vh}
.point-body .pd{font-size:var(--fs-sm);color:rgba(255,255,255,.72);line-height:1.55}
```

### HTML 骨架

```html
<section class="slide s-glow" data-chapter="1"
  style="--glow-h:234;--glow-h2:291;--glow-sat:95%;--glow-light:40%;--glow-spread:35;--glow-color-int:.68;--glow-white-int:.58">
  <div class="glow"></div>
  <div class="head">
    <div class="head-l">
      <div class="brand"><img class="logo" src="cann-dark-logo.svg" alt="CANN"><span class="ttl h-title">渐变标题即结论</span></div>
      <div class="subttl" style="color:rgba(255,255,255,.6)">副标题 · 英文补充</div>
    </div>
    <div class="head-r" style="color:rgba(255,255,255,.45)">01 / 章节名<br/>2026</div>
  </div>
  <div class="glow-inner">
    <!-- 左：文字 + 要点 -->
    <div>
      <p style="font-size:var(--fs-body);color:rgba(255,255,255,.8);line-height:1.7">正文描述……</p>
      <div class="glow-points">
        <div class="point">
          <div class="point-dot"></div>
          <div class="point-body">
            <div class="pt">要点标题</div>
            <div class="pd">补充说明……</div>
          </div>
        </div>
        <!-- 重复 × 3-4 条 -->
      </div>
    </div>
    <!-- 右：图位占位 / 截图 -->
    <div class="shot">
      <img src="screenshot.png" alt="" style="width:100%;height:100%;object-fit:cover">
    </div>
  </div>
</section>
```

- **一章一色**：每章首页（`chapter-cover`）带调色面板，其他同章页用 `data-chapter="N"` + 相同 `--glow-h` inline 变量继承颜色。
- `cann-dark-logo.svg` = 白色版 logo，专用于深色底；别用深色 logo。
- `.shot` 的 `box-shadow` 用 `hsla(var(--glow-h),...)` 让阴影颜色随光晕同步变化。

### 填充示例（「增量编译」设计点参照）

```html
<section class="slide s-glow" data-chapter="1"
  style="--glow-h:234;--glow-h2:291;--glow-sat:95%;--glow-light:40%;--glow-spread:35;--glow-color-int:.68;--glow-white-int:.58">
  <div class="glow"></div>
  <div class="head">
    <div class="head-l">
      <div class="brand"><img class="logo" src="cann-dark-logo.svg" alt="CANN">
        <span class="ttl h-title">增量编译：把 30 分钟压缩到 3 秒</span>
      </div>
      <div class="subttl" style="color:rgba(255,255,255,.6)">Design Point 01 · Incremental Build</div>
    </div>
    <div class="head-r" style="color:rgba(255,255,255,.45)">01 / 编译体验<br/>2026</div>
  </div>
  <div class="glow-inner">
    <div>
      <p style="font-size:var(--fs-body);color:rgba(255,255,255,.8);line-height:1.7;margin-bottom:2vh">
        现有 tbe 编译每次全量重编 460+ .o 文件，改一行代码等 30-60 分钟。<br>
        增量编译 + 智能依赖分析可将 <b style="color:#fff">95% 的日常改动</b>压缩到秒级响应。
      </p>
      <div class="glow-points">
        <div class="point">
          <div class="point-dot"></div>
          <div class="point-body">
            <div class="pt">依赖图感知</div>
            <div class="pd">静态分析算子依赖树，只重编真正受影响的子图，其余复用缓存。</div>
          </div>
        </div>
        <div class="point">
          <div class="point-dot"></div>
          <div class="point-body">
            <div class="pt">智能去重</div>
            <div class="pd">内容 hash 识别重复 .o，跨项目共享编译产物，节省磁盘与时间。</div>
          </div>
        </div>
        <div class="point">
          <div class="point-dot"></div>
          <div class="point-body">
            <div class="pt">IDE 实时反馈</div>
            <div class="pd">保存即触发后台编译，错误在编辑器内实时标红，无需等待完整构建。</div>
          </div>
        </div>
      </div>
    </div>
    <div class="shot"><!-- 截图或示意图 --></div>
  </div>
</section>
```
