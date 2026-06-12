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
| 干系人关系网络/谁连谁/相关方关系/角色协作/influence map/关系图（节点多、有连线） | **§9 关系网络图** | ECharts graph 力导向/环形，0 新依赖 |
| 信息架构/IA/sitemap/功能树/思维导图/组织架构/心智模型（有父子层级） | **§10 思维导图·层级树** | ECharts tree，横/纵向 |
| 用户流转/转化路径/流量分配/痛点→方案映射/从 A 到 B 的量 | **§11 桑基流向图** | ECharts sankey |
| 评分矩阵/能力打分/竞品打分/多对象×多维度热力表/scorecard | **§12 评分热力矩阵** | 手画网格 + JS 渲染（淡底+彩字+表情脸）|
| 能力架构/体验架构/产品架构/分层框架（目标→场景→…纵向分层）| **§13 分层架构图** | 左标签 + 聚类玻璃卡 |
| 几个冲击力大数字/效率提升 X%/加速 N×/关键成果/KPI 主打 | **§14 数据突出卡** | 切角玻璃方卡 + 总体说明 |

判不准时，按主体：**数字进度**→§1，**时间轴**→§2，**引用堆**→§3，**分阶段流程**→§4，**多产品比**→§5，**讲一个人**→§6a，**多人维度对比**→§6b，**讲方案**→§8，**关系网络**→§9，**层级树**→§10，**带权流向**→§11，**打分表**→§12，**分层架构**→§13，**大数字主打**→§14。命中后翻到该节，照抄骨架 + 参考填充示例，只改文案/配色。

> §9–§11 是 **ECharts 图**（已内联，0 新依赖）；§12–§14 是手画 pattern（矩阵需配套 JS）。布局型 pattern（洋葱圈 / 2×2 / 共情图 / 服务蓝图 / 亲和图）待补。

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
        <div class="voc-ava"><img src="assets/av/chen.svg" alt=""></div>
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
      <div class="voc-ava"><img src="assets/av/chen.svg" alt=""></div>
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

- **卡型多样化**是 VOC 墙的精髓：同一页混用普通/大引号/大标题/左右布局，避免视觉单调。
- 样板每卡还带**星评 `.voc-stars`**（满星 `★★★★★`，缺的用 `<span class="off">★</span>`），大标题卡用 `.voc-hd`。补充 CSS：
  ```css
  .voc-stars{display:flex;gap:2px;color:#E8A93C;font-size:13px;letter-spacing:1px} .voc-stars .off{color:var(--line)}
  .voc-hd{font-family:'Inter','Noto Sans SC';font-weight:700;font-size:max(15px,1.18vw);letter-spacing:-.01em;line-height:1.2;color:var(--ink)}
  ```
- 头像用 **DiceBear notionists** 生成 SVG（CC0）存本地 `assets/av/`，`beardProbability=0`，`backgroundColor` 跟页面底色。

### 填充示例（抄自样板 VOC 页：普通/大引号/大标题/左右/soft 混排）

```html
<div class="voc-wall">
  <!-- 普通卡 -->
  <div class="voc-card">
    <div class="voc-stars">★★★★★</div>
    <div class="voc-q">Profiling 看板能直接点到瓶颈算子，框选即缩放，比之前翻日志定位快太多了。</div>
    <div class="voc-meta"><div class="voc-ava"><img src="assets/av/chen.svg" alt=""></div><div><div class="voc-nm">陈 · 框架开发者</div><div class="voc-rl">AI 平台 · 5 年</div></div></div>
  </div>
  <!-- 大引号卡 -->
  <div class="voc-card">
    <div class="qm open">"</div>
    <div class="voc-stars">★★★★<span class="off">★</span></div>
    <div class="voc-q">成长地图让我清楚下一步该学什么，照着路线走不再瞎撞。</div>
    <div class="voc-meta"><div class="voc-ava"><img src="assets/av/liu.svg" alt=""></div><div><div class="voc-nm">刘 · 后端工程师</div><div class="voc-rl">云服务 · 2 年</div></div></div>
  </div>
  <!-- 大标题卡（灰块衬正文）-->
  <div class="voc-card head">
    <div class="qm open">"</div>
    <div class="voc-hd">文档终于连起来了</div>
    <div class="voc-stars">★★★★★</div>
    <div class="voc-q boxed">新的交互式文档把端到端示例串起来了，照着 Notebook 跑半天就通，不用再翻七八个页面。</div>
    <div class="voc-meta"><div class="voc-ava"><img src="assets/av/lin.svg" alt=""></div><div><div class="voc-nm">林 · 算法工程师</div><div class="voc-rl">互联网 · 3 年</div></div></div>
  </div>
  <!-- 左头像右文字卡 -->
  <div class="voc-card lr">
    <div class="voc-ava"><img src="assets/av/wang.svg" alt=""></div>
    <div class="lr-body">
      <div class="voc-stars">★★★★<span class="off">★</span></div>
      <div class="voc-q">算子开发向导生成骨架后，我只要填核心计算逻辑，省了大量样板代码。</div>
      <div class="lr-name"><span class="voc-nm">王 · 算子工程师</span><span class="voc-rl">芯片厂商 · 4 年</span></div>
    </div>
  </div>
  <!-- soft 浅灰卡 -->
  <div class="voc-card soft">
    <div class="voc-stars">★★★★<span class="off">★</span></div>
    <div class="voc-q">如果环境能一键拉起来、版本自动对齐，复现实验就不再是噩梦，能省下大量重装和排错的时间。</div>
    <div class="voc-meta"><div class="voc-ava"><img src="assets/av/zhao.svg" alt=""></div><div><div class="voc-nm">赵 · 学术研究者</div><div class="voc-rl">高校 · 博士在读</div></div></div>
  </div>
</div>
```

## 4. 用户旅程（全链路）

> 来自样板 `cann-design-concept`（`.jrn-*`，参照 cann-journey-compare 风格）。**适用范围比"旅程图"更广**：任何**按阶段推进的流程**都能套——用户研究旅程、产品开发流程、运维流程……只要有"阶段列 × 信息行"结构就命中。
> 结构 = `56px 行标列 + N 个阶段列` 的多行网格，逐行：① 阶段头 ② 触点 ③ 行为(手画 mini 线框) ④ 情绪曲线(逐格 SVG) ⑤ 痛点 ⑥ 机会点。行与行靠各 cell 的 `border-left/right/bottom` 拼成连续竖列。

### CSS 骨架（抄自样板）

```css
.jrn-wrap{flex:1;min-height:0;display:flex;flex-direction:column;gap:0}
.jrn-grid{display:grid;grid-template-columns:56px repeat(5,1fr);gap:0}   /* 5 阶段；改列数即改 repeat(N) */
/* 行标列 */
.jrn-rl{display:flex;flex-direction:column;justify-content:center;padding-right:9px;text-align:right}
.jrn-rn{font-size:10px;font-weight:700;color:var(--ink-2);line-height:1.4}
.jrn-re{font-size:8px;color:var(--ink-3);text-transform:uppercase;letter-spacing:.5px;margin-top:1px}
/* ① 阶段头（深色，底部彩条按阶段区分）*/
.jrn-pw{padding-right:5px;display:flex;flex-direction:column}
.jrn-ph{flex:1;border-radius:10px 10px 0 0;padding:1.1vh .85vw 1.4vh;background:var(--g-ink);position:relative;overflow:hidden}
.jrn-ph::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px}
.jpc1 .jrn-ph::after{background:#EF4444}.jpc2 .jrn-ph::after{background:#F59E0B}
.jpc3 .jrn-ph::after{background:#3B82F6}.jpc4 .jrn-ph::after{background:#10B981}
.jpc5 .jrn-ph::after{background:#8B5CF6}
.jrn-ph .pn{font-size:8.5px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:rgba(255,255,255,.28);margin-bottom:2px}
.jrn-ph .pt{font-size:max(11px,.8vw);font-weight:800;color:#fff;line-height:1.3}
.jrn-ph .ptm{font-size:8px;margin-top:.35vh;display:inline-flex;align-items:center;gap:3px;padding:1.5px 6px;border-radius:100px;background:rgba(255,255,255,.08);color:rgba(255,255,255,.5)}
/* ② 触点 */
.jrn-tw{padding-right:5px;display:flex;flex-direction:column}
.jrn-tc{flex:1;border-left:1px solid rgba(255,255,255,.6);border-right:1px solid rgba(255,255,255,.6);border-bottom:1px solid rgba(255,255,255,.6);padding:1vh .85vw;background:rgba(255,255,255,.42);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);display:flex;flex-direction:column;justify-content:center;gap:.5vh}
.jrn-touch{font-size:max(9.5px,.7vw);color:var(--ink);line-height:1.35;display:flex;align-items:baseline;gap:.4em}
.jrn-touch::before{content:"";width:4px;height:4px;border-radius:50%;background:var(--ink-3);flex-shrink:0;align-self:center}
/* ③ 行为（手画 mini 线框 + 行为描述）*/
.jrn-fw{padding-right:5px;display:flex;flex-direction:column}
.jrn-fc{flex:1;border-left:1px solid rgba(255,255,255,.6);border-right:1px solid rgba(255,255,255,.6);border-bottom:1px solid rgba(255,255,255,.6);padding:1vh .85vw;display:flex;flex-direction:column;gap:.6vh;background:rgba(255,255,255,.42);backdrop-filter:blur(15px);-webkit-backdrop-filter:blur(15px)}
.jrn-scr{border-radius:5px;overflow:hidden;border:1px solid var(--line);background:#F8F9FB;flex:0 0 auto;height:13.5vh;display:flex;flex-direction:column}
.jrn-sb{display:flex;align-items:center;gap:3px;padding:3px 5px;background:#ECEEF2;border-bottom:1px solid var(--line);flex-shrink:0}
.jrn-sd{width:4px;height:4px;border-radius:50%}
.jrn-sc{padding:4px 5px;flex:1;overflow:hidden;display:flex;flex-direction:column;gap:2px}
.jmb{height:2.5px;border-radius:2px;background:#E5E7EB}
.jrn-fl{font-size:max(9.5px,.7vw);font-weight:500;color:var(--ink);line-height:1.4}
/* ④ 情绪：逐格 SVG（jrn-grid.je 显式锁高，否则被压扁）*/
.jrn-grid.je{flex-shrink:0;height:16vh}
.jrn-ew{padding-right:5px;display:flex;flex-direction:column}
.jrn-ec{flex:1;position:relative;height:100%;border-left:1px solid rgba(255,255,255,.6);border-right:1px solid rgba(255,255,255,.6);border-bottom:1px solid rgba(255,255,255,.6);background:rgba(250,251,255,.55);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);overflow:hidden}
.jrn-ec svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.jrn-ec .d{position:absolute;width:9px;height:9px;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.2);transform:translate(-50%,-50%);left:50%;z-index:3}
.jrn-ec .e{position:absolute;font-size:13px;transform:translate(-50%,0);left:50%;z-index:3;line-height:1}
.jrn-ec .l{position:absolute;font-family:'JetBrains Mono';font-size:8px;font-weight:700;transform:translateX(-50%);left:50%;bottom:4px;z-index:3;white-space:nowrap}
/* ⑤ 痛点（红底 + 警告图标）*/
.jrn-pw2{padding-right:5px;display:flex;flex-direction:column}
.jrn-pc{flex:1;border-left:1px solid rgba(255,255,255,.6);border-right:1px solid rgba(255,255,255,.6);border-bottom:1px solid rgba(255,255,255,.6);padding:.9vh .85vw;display:flex;flex-direction:column;justify-content:center;gap:.55vh;background:linear-gradient(160deg,rgba(254,236,236,.72),rgba(255,247,240,.55));backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.jrn-pi{display:flex;gap:4px;align-items:flex-start}
.jrn-pi-icon{width:16px;height:16px;border-radius:4px;background:#FEF3C7;flex-shrink:0;margin-top:1px;display:flex;align-items:center;justify-content:center}
.jrn-pi-icon svg{width:9px;height:9px;stroke:#92400E}
.jrn-pt{font-size:max(9.5px,.7vw);color:#7F1D1D;line-height:1.45}
/* ⑥ 机会点（绿底，末行收圆角）*/
.jrn-ow{padding-right:5px;display:flex;flex-direction:column}
.jrn-oc{flex:1;border-left:1px solid rgba(255,255,255,.6);border-right:1px solid rgba(255,255,255,.6);border-bottom:1px solid rgba(255,255,255,.6);border-radius:0 0 9px 9px;padding:.9vh .85vw;display:flex;flex-direction:column;justify-content:center;gap:.55vh;background:linear-gradient(160deg,rgba(220,252,231,.72),rgba(240,253,244,.55));backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.jrn-oi{display:flex;gap:4px;align-items:flex-start}
.jrn-oi-dot{width:7px;height:7px;border-radius:50%;background:#10B981;flex-shrink:0;margin-top:3px}
.jrn-ot{font-size:max(9.5px,.7vw);color:#064E3B;line-height:1.45}
```

### HTML 骨架（每行首格 = 行标，后接 N 个阶段格）

```html
<div class="body-area"><div class="jrn-wrap">

  <!-- ① 阶段头（行标列留空）-->
  <div class="jrn-grid">
    <div></div>
    <div class="jrn-pw jpc1"><div class="jrn-ph"><div class="pn">01</div><div class="pt">环境搭建</div><div class="ptm">⏱ 2–8 hr</div></div></div>
    <div class="jrn-pw jpc2"><div class="jrn-ph"><div class="pn">02</div><div class="pt">文档学习</div><div class="ptm">⏱ 1–3 天</div></div></div>
    <!-- … jpc3/jpc4/jpc5 同理 -->
  </div>

  <!-- ② 触点 -->
  <div class="jrn-grid">
    <div class="jrn-rl"><div class="jrn-rn">触点</div><div class="jrn-re">Touch</div></div>
    <div class="jrn-tw"><div class="jrn-tc">
      <div class="jrn-touch">官网文档中心</div>
      <div class="jrn-touch">Driver/CANN 版本矩阵</div>
    </div></div>
    <!-- 每阶段一个 jrn-tw -->
  </div>

  <!-- ③ 行为：每格 = 手画 mini 浏览器线框 + 行为描述 -->
  <div class="jrn-grid">
    <div class="jrn-rl"><div class="jrn-rn">行为</div><div class="jrn-re">Action</div></div>
    <div class="jrn-fw"><div class="jrn-fc">
      <div class="jrn-scr" style="height:11vh">
        <div class="jrn-sb"><div class="jrn-sd" style="background:#FF5F57"></div><div class="jrn-sd" style="background:#FFBD2E"></div><div class="jrn-sd" style="background:#28CA41"></div></div>
        <div class="jrn-sc"><!-- 用 .jmb 小条 + 彩色块手画示意 UI(终端/IDE/看板) -->
          <div class="jmb" style="width:90%"></div><div class="jmb" style="width:70%"></div></div>
      </div>
      <div class="jrn-fl">查版本矩阵 → 装 Driver+CANN → 验证 Hello World</div>
    </div></div>
    <!-- 每阶段一个 jrn-fw，各画一张不同 mini UI -->
  </div>

  <!-- ④ 情绪：jrn-grid je 锁高；每格 SVG 曲线 + 圆点 + emoji + 标签 -->
  <div class="jrn-grid je">
    <div class="jrn-rl"><div class="jrn-rn">情绪</div><div class="jrn-re">Emotion</div></div>
    <div class="jrn-ew"><div class="jrn-ec">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none">
        <defs><linearGradient id="jeg1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F59E0B" stop-opacity=".16"/><stop offset="1" stop-color="#F59E0B" stop-opacity="0"/></linearGradient></defs>
        <line x1="0" y1="50" x2="100" y2="50" stroke="#E5E7EB" stroke-width=".8" stroke-dasharray="3,3" vector-effect="non-scaling-stroke"/>
        <polygon points="0,38 50,38 100,45 100,100 0,100" fill="url(#jeg1)"/>
        <polyline points="0,38 50,38 100,45" fill="none" stroke="#F59E0B" stroke-width="1.6" vector-effect="non-scaling-stroke"/>
      </svg>
      <div class="d" style="top:38%;background:#F59E0B"></div>
      <div class="e" style="top:calc(38% - 19px)">😐</div>
      <div class="l" style="color:#92400E">摸索中</div>
    </div></div>
    <!-- 每阶段一格；points 的 y 越大情绪越低，谷底用红 #EF4444 + 😣 -->
  </div>

  <!-- ⑤ 痛点 -->
  <div class="jrn-grid">
    <div class="jrn-rl"><div class="jrn-rn">痛点</div><div class="jrn-re">Pain</div></div>
    <div class="jrn-pw2"><div class="jrn-pc">
      <div class="jrn-pi"><div class="jrn-pi-icon"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div><div class="jrn-pt"><b>版本依赖复杂</b>，三者版本须精准匹配，一错全报</div></div>
    </div></div>
    <!-- 每阶段一个 jrn-pw2，每格 1-2 条 jrn-pi -->
  </div>

  <!-- ⑥ 机会点 -->
  <div class="jrn-grid">
    <div class="jrn-rl"><div class="jrn-rn">机会点</div><div class="jrn-re">Opps</div></div>
    <div class="jrn-ow"><div class="jrn-oc">
      <div class="jrn-oi"><div class="jrn-oi-dot"></div><div class="jrn-ot">一键环境容器，版本<b>自动匹配锁定</b></div></div>
    </div></div>
    <!-- 每阶段一个 jrn-ow -->
  </div>

</div></div>
```

### 要点

- **列数 = `.jrn-grid` 的 `repeat(N,1fr)`**，6 行必须同步改成同一列数否则错位；首列固定 `56px` 行标。
- **竖边框拼接**：每行 cell 只用 `border-left/right/bottom`（无 top），上下相邻拼成连续竖容器；阶段头 `border-radius:10px 10px 0 0`、机会点 `0 0 9px 9px` 收口。
- **情绪行必须 `.jrn-grid.je` 显式锁高**（16vh）——格内全绝对定位，不锁高会被 flex 压扁（踩过）。
- **行为行 mini UI 是手画线框**（`.jrn-scr` 内 `.jmb` 小条 + 彩色块拼）——工作量大但最贴主题；偷懒可换一句话或真截图。
- 痛点红系（`#7F1D1D`/`#FEF3C7`）、机会点绿系（`#064E3B`/`#10B981`），色义固定。

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
      <div class="pf-portrait"><img src="assets/av/chen.svg" alt=""></div>
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
      <div class="pf-portrait"><img src="assets/av/persona.svg" alt="王工"></div>
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

### CSS 骨架（抄自样板）

```css
.s-glow{background:#06060a;color:#fff;padding:7vh 6vw}
/* 三层光晕：glow(双色径向) + glow-white(底部白雾)，高度由 --glow-spread 控制 */
.s-glow .glow{position:absolute;left:0;right:0;bottom:0;height:calc(var(--glow-spread)*1vh);z-index:0;pointer-events:none}
.s-glow .glow::before,.s-glow .glow::after{content:"";position:absolute;inset:0;mix-blend-mode:screen}
.s-glow .glow::before{background:radial-gradient(ellipse 78% 96% at 22% 112%,hsla(var(--glow-h),var(--glow-sat),calc(var(--glow-light) + 12%),var(--glow-color-int)) 0%,hsla(var(--glow-h),var(--glow-sat),var(--glow-light),0) 92%)}
.s-glow .glow::after{background:radial-gradient(ellipse 78% 96% at 78% 112%,hsla(var(--glow-h2),var(--glow-sat),calc(var(--glow-light) + 12%),calc(var(--glow-color-int)*.9)) 0%,hsla(var(--glow-h2),var(--glow-sat),var(--glow-light),0) 90%)}
.s-glow .glow-white{position:absolute;left:0;right:0;bottom:0;height:calc(var(--glow-spread)*1vh);z-index:0;pointer-events:none;mix-blend-mode:screen;background:linear-gradient(to top,hsla(var(--glow-h),22%,90%,var(--glow-white-int)) 0%,hsla(var(--glow-h),30%,80%,0) 84%)}
/* 顶部角标 */
.s-glow .chrome{position:absolute;top:5vh;left:6vw;right:6vw;z-index:1;display:flex;justify-content:space-between;font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.4)}
/* 左文右图双栏 */
.s-glow .inner{position:relative;z-index:1;height:100%;display:grid;grid-template-columns:1fr 1fr;gap:4vw;align-items:center}
/* kicker 小标签 + 渐变标题 + 正文 */
.kicker{font-family:'JetBrains Mono';font-size:var(--fs-xs);letter-spacing:.24em;text-transform:uppercase;color:hsl(var(--glow-h),var(--glow-sat),72%);margin-bottom:2.4vh;display:flex;align-items:center;gap:.8em}
.kicker::before{content:"";width:28px;height:1px;background:currentColor;opacity:.7}
.h-title{font-weight:700;font-size:min(3.7vw,6.4vh);line-height:1.2;letter-spacing:-.01em;margin-bottom:1.4vh;background:linear-gradient(100deg,hsl(var(--glow-h),var(--glow-sat),80%),hsl(var(--glow-h2),var(--glow-sat),74%));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.h-title .light{font-weight:200}
.body{font-weight:300;font-size:var(--fs-body);line-height:1.75;color:rgba(255,255,255,.64);max-width:42ch;margin-bottom:3vh}
.body b{color:#fff;font-weight:600}
/* 要点列表 */
.points{display:flex;flex-direction:column;gap:1.8vh}
.point{display:grid;grid-template-columns:auto 1fr;gap:1.1em;align-items:start}
.point .dot{width:9px;height:9px;margin-top:.55em;border-radius:50%;background:hsl(var(--glow-h),var(--glow-sat),62%);box-shadow:0 0 12px 2px hsla(var(--glow-h),var(--glow-sat),60%,.7);flex-shrink:0}
.point .pt-title{font-weight:500;font-size:var(--fs-h3);color:#fff;margin-bottom:.3vh}
.point .pt-desc{font-weight:300;font-size:var(--fs-sm);line-height:1.55;color:rgba(255,255,255,.52)}
.point .pt-desc b{color:hsl(var(--glow-h),var(--glow-sat),74%);font-weight:600}
/* 右图位占位 */
.shot{position:relative;border-radius:14px;overflow:hidden;aspect-ratio:16/10;background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.12);box-shadow:0 30px 80px -20px hsla(var(--glow-h),var(--glow-sat),30%,.5);display:flex;align-items:center;justify-content:center}
.shot .ph{font-family:'JetBrains Mono';font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.3)}
```

### HTML 骨架（即样板设计点页，已填真实内容）

```html
<section class="slide s-glow" data-chapter="1"
  style="--glow-h:234;--glow-h2:291;--glow-sat:95%;--glow-light:40%;--glow-spread:35;--glow-color-int:.68;--glow-white-int:.58">
  <div class="glow-top"></div><div class="glow"></div><div class="glow-white"></div>
  <div class="chrome"><div>设计点 1.1 · CONTROL FLOW</div><div>第一章 · 控制与可观测</div></div>
  <div class="inner">
    <div>
      <div class="kicker">DESIGN POINT 1.1</div>
      <h1 class="h-title">控制流<br/><span class="light">结构化可视化</span></h1>
      <p class="body">把算子执行的控制流抽象成结构化视图——读取/计算/决策/回写，<b>一图可达，全局可见</b>。</p>
      <div class="points">
        <div class="point"><div class="dot"></div><div><div class="pt-title">执行过程全局可见</div><div class="pt-desc">各阶段一目了然，无需在代码里逐层定位</div></div></div>
        <div class="point"><div class="dot"></div><div><div class="pt-title">关键路径高亮</div><div class="pt-desc">自动标注热点算子与数据依赖关系</div></div></div>
        <div class="point"><div class="dot"></div><div><div class="pt-title">精度逻辑定位</div><div class="pt-desc">精度异常快速对应到具体算子节点</div></div></div>
      </div>
    </div>
    <div class="shot"><span class="ph">控制流可视化界面 · 16:10</span></div>
  </div>
</section>
```

### 要点

- **三层光晕**：`.glow`（双色径向，`--glow-h`/`--glow-h2`）+ `.glow-white`（底部白雾），高度由 `--glow-spread` 控制；`.glow-top` 为可选顶部叠层。
- **标题用 `.h-title`**，`<span class="light">` 包的部分变细体（200）形成主次。
- **图位用 `.shot` + `.ph` 占位文字**；有真截图就把 `<span class="ph">` 换成 `<img>`。
- **一章一色**：章节封面页（`chapter-cover`）挂调色面板，同章其他页 `data-chapter="N"` + 相同 `--glow-*` inline 变量继承。
- `cann-dark-logo.svg` = 白色版 logo，专用于深色底；别用深色 logo。

## 9. 关系网络图（ECharts graph · 干系人/角色关系）

> **命中**：干系人**关系网络**、谁连谁、相关方影响图、系统角色协作、influence map——节点多、连线表示关系、需要自动布局时用。简单分层（无连线）走手画方块即可，别上库。
> 用已内联的 **ECharts graph series**，0 新依赖。配色用样板 `PAL` 调色板，字体 `HarmonyOS Sans SC`。

```js
// 容器：<div id="netchart" style="width:100%;height:62vh"></div>
(function(){
  if(typeof echarts==='undefined')return; const el=document.getElementById('netchart'); if(!el)return;
  const PAL=['#5B5BD6','#7C3AED','#2FCB8E','#F59E0B','#4FACFE','#E6789B'];
  echarts.init(el).setOption({
    textStyle:{fontFamily:'HarmonyOS Sans SC, Inter, "Noto Sans SC", sans-serif'},
    color:PAL,
    legend:{top:0,textStyle:{color:'#5e646e',fontSize:12},icon:'roundRect',itemWidth:11,itemHeight:8},
    series:[{
      type:'graph', layout:'force',          // 也可 'circular'（环形）
      roam:false, draggable:true,
      categories:[{name:'研发侧'},{name:'平台侧'},{name:'用户侧'}],
      label:{show:true,position:'right',color:'#16191e',fontSize:12,fontWeight:500},
      labelLayout:{hideOverlap:true},
      force:{repulsion:260,edgeLength:[60,140],gravity:.08},
      lineStyle:{color:'#c4cad4',width:1.2,curveness:.08,opacity:.7},
      emphasis:{focus:'adjacency',lineStyle:{width:2.4}},
      data:[
        // symbolSize 表重要度；category 决定颜色
        {name:'算子开发',category:0,symbolSize:46,value:9},
        {name:'框架适配',category:0,symbolSize:34,value:6},
        {name:'CI/发布',category:1,symbolSize:30,value:5},
        {name:'实验平台',category:1,symbolSize:38,value:7},
        {name:'高校用户',category:2,symbolSize:30,value:5},
        {name:'生产训练',category:2,symbolSize:42,value:8}
      ],
      links:[
        {source:'算子开发',target:'框架适配'},
        {source:'框架适配',target:'实验平台'},
        {source:'实验平台',target:'CI/发布'},
        {source:'实验平台',target:'生产训练'},
        {source:'高校用户',target:'实验平台'},
        {source:'生产训练',target:'算子开发'}
      ]
    }]
  });
})();
```

- `layout:'force'` 自动力导向布局；关系是「围绕一个中心」时改 `layout:'circular',circular:{rotateLabel:true}`。
- `symbolSize` 映射重要度/影响力，`categories` 分组上色（用 PAL），`links.curveness` 给一点弧度更好看。
- 想给连线方向加箭头：`links` 里加 `symbol:['none','arrow']`。

## 10. 思维导图 / 信息架构树（ECharts tree）

> **命中**：信息架构 IA、sitemap、功能树、思维导图、组织架构、心智模型层级——**有明确父子层级**时用 ECharts tree；扁平的几个并列框走手画。

```js
// 容器：<div id="treechart" style="width:100%;height:64vh"></div>
(function(){
  if(typeof echarts==='undefined')return; const el=document.getElementById('treechart'); if(!el)return;
  echarts.init(el).setOption({
    textStyle:{fontFamily:'HarmonyOS Sans SC, Inter, "Noto Sans SC", sans-serif'},
    series:[{
      type:'tree', left:'2%', right:'18%', top:'2%', bottom:'2%',
      orient:'LR',                       // 横向左→右；纵向用 'TB'
      symbol:'circle', symbolSize:9,
      itemStyle:{color:'#5B5BD6',borderColor:'#5B5BD6'},
      lineStyle:{color:'#c4cad4',width:1.2,curveness:.5},
      label:{position:'left',align:'right',color:'#16191e',fontSize:13,fontWeight:600},
      leaves:{label:{position:'right',align:'left',color:'#5e646e',fontWeight:400}},
      expandAndCollapse:false, initialTreeDepth:-1,
      emphasis:{focus:'descendant'},
      data:[{
        name:'CANN 开发者门户',
        children:[
          {name:'入门',children:[{name:'环境搭建'},{name:'快速上手'},{name:'示例库'}]},
          {name:'算子开发',children:[{name:'Ascend C'},{name:'Tiling 指南'},{name:'调试'}]},
          {name:'训练',children:[{name:'迁移'},{name:'精度对齐'},{name:'性能调优'}]},
          {name:'参考',children:[{name:'API'},{name:'版本矩阵'}]}
        ]
      }]
    }]
  });
})();
```

- `orient:'LR'`（横向）最适合 IA/sitemap；`'TB'`（纵向）适合组织架构。
- `lineStyle.curveness:.5` 是 ECharts tree 标志性的圆角连线；根/枝节点用 accent 实心点、叶子用中性色。
- 层级深时设 `initialTreeDepth:2` + `expandAndCollapse:true` 可折叠。

## 11. 桑基流向图（ECharts sankey · 用户流转/转化/映射）

> **命中**：用户流转、转化路径、流量分配、痛点→方案映射、从 A 到 B 的「量」的流动——节点分层、连线带权重时用。抄自样板 `charts-gallery.html`。

```js
// 容器：<div id="sankeychart" style="width:100%;height:60vh"></div>
(function(){
  if(typeof echarts==='undefined')return; const el=document.getElementById('sankeychart'); if(!el)return;
  const PAL=['#5B5BD6','#7C3AED','#2FCB8E','#F59E0B','#4FACFE','#E6789B'];
  echarts.init(el).setOption({
    textStyle:{fontFamily:'HarmonyOS Sans SC, Inter, "Noto Sans SC", sans-serif'},
    color:PAL,
    series:[{
      type:'sankey', left:6, right:64, top:8, bottom:8,
      nodeWidth:12, nodeGap:10,
      label:{color:'#16191e',fontSize:12},
      lineStyle:{color:'gradient',opacity:.42},   // 连线用源/目标渐变色
      data:[
        {name:'文档碎片'},{name:'调试黑盒'},{name:'环境复杂'},
        {name:'交互式文档'},{name:'可视化 Profiling'},{name:'一键环境'}
      ],
      links:[
        {source:'文档碎片',target:'交互式文档',value:6},
        {source:'调试黑盒',target:'可视化 Profiling',value:5},
        {source:'环境复杂',target:'一键环境',value:4},
        {source:'文档碎片',target:'可视化 Profiling',value:2}
      ]
    }]
  });
})();
```

- `lineStyle.color:'gradient'` 让连线从源节点色渐变到目标节点色，是桑基最好看的设置。
- 左侧=问题/来源，右侧=方案/去向；`value` 是流量权重（决定带子粗细）。
- 节点超过两层（来源→中转→去向）直接在 `data`/`links` 里加即可，sankey 自动分层。

> 以上三个都是 **ECharts** 图（已内联 `lib/echarts.min.js`）。合并进单 deck 时遵守 `chart-selection.md` 约定：脚本放主脚本前，init 包 IIFE + `if(typeof echarts==='undefined')return` + `if(!el)return` 保护；翻页/全屏后调 `chart.resize()`。

## 12. 评分热力矩阵（行 × 列打分，参考 reference/mattrix.html）

> **命中**：能力/竞品评分矩阵、多对象 × 多维度打分、热力打分表。**手画 CSS 网格 + JS 渲染**（按分着色），不用库。
> ⚠️ 关键：cell **底色极淡**（`rgba(色,.05)`）+ 彩色描边 + **彩色数字** + **表情脸图标**——不是饱和填充。分档（0–100）：`<20红 <40橙 <60绿 <80青 ≥80蓝`。

```css
.hm-grid{display:grid;grid-template-columns:120px repeat(5,1fr);gap:8px}   /* 改列数同步改 repeat 与内联 grid-template-columns */
.hm-header{font-size:12px;font-weight:700;color:#3D4452;text-align:center;text-transform:uppercase;letter-spacing:.04em;background:#fff;border:1px solid rgba(223,223,223,.5);border-radius:12px;height:48px;display:flex;align-items:center;justify-content:center}
.hm-corner{position:relative;overflow:hidden;border-radius:12px;background:#fff;border:1px solid #EFF0F1}   /* 左上角斜线 + 行/列名 */
.hm-corner svg{position:absolute;inset:0;width:100%;height:100%}
.hm-corner .hc-col{position:absolute;top:30%;right:18%;font-size:12px;font-weight:600;color:#3D4452;text-transform:uppercase}
.hm-corner .hc-row{position:absolute;bottom:30%;left:18%;font-size:12px;font-weight:600;color:#3D4452;text-transform:uppercase}
.hm-row-label{display:flex;align-items:center;gap:10px;padding:0 8px;font-size:12px;font-weight:700;color:#1B2432;background:#fff;border:1px solid rgba(223,223,223,.5);border-radius:12px;height:48px}
.hm-row-label small{font-size:9.5px;font-weight:500;color:#A1A4AA;display:block}
.hm-cell{border-radius:12px;height:48px;display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px solid #EFF0F1}
.hm-cell .cv{font-family:'JetBrains Mono';font-size:14px;font-weight:800;display:flex;align-items:center;gap:3px}   /* 表情 + 数字 + 趋势 */
.hm-legend{display:flex;align-items:center;gap:10px;margin-top:14px;font-size:11px;color:#A1A4AA;justify-content:flex-end}
.hm-grad{height:8px;width:120px;border-radius:4px;background:linear-gradient(90deg,#FFB9B9,#FFD7B7 35%,#FFF2A5 55%,#C4F3E1 75%,#94E1C8)}
```

容器 `<div class="hm-grid" id="m1" style="grid-template-columns:150px repeat(6,1fr)"></div>` + 渲染脚本（**配色/表情/趋势/状态点函数逐字抄自 mattrix.html**）：

```js
(function(){var grid=document.getElementById('m1');if(!grid)return;
  function heat(s){return s<20?'rgba(224,33,40,.05)':s<40?'rgba(244,132,12,.05)':s<60?'rgba(5,131,88,.05)':s<80?'rgba(18,113,128,.05)':'rgba(57,121,249,.05)';}
  function bord(s){return s<20?'rgba(224,33,40,.1)':s<40?'rgba(244,132,12,.1)':s<60?'rgba(5,131,88,.1)':s<80?'rgba(18,113,128,.1)':'rgba(57,121,249,.1)';}
  function txt(s){return s<20?'#E02128':s<40?'#F4840C':s<60?'#058358':s<80?'#127180':'#3979F9';}
  function face(s){var a='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/>';
    if(s>=80)return a+'<circle cx="9" cy="9" r="1"/><circle cx="15" cy="9" r="1"/><path d="M6 15h12M6 15c3 5 9 5 12 0"/></svg>';        /* 大笑 */
    if(s>=60)return a+'<circle cx="9" cy="9" r="1"/><circle cx="15" cy="9" r="1"/><path d="M6 16c3 2 9 2 12 0"/></svg>';            /* 微笑 */
    if(s>=40)return a+'<circle cx="9" cy="9" r="1"/><circle cx="15" cy="9" r="1"/><line x1="6" y1="16" x2="18" y2="16"/></svg>';   /* 平 */
    if(s>=20)return a+'<circle cx="9" cy="9" r="1"/><circle cx="15" cy="9" r="1"/><path d="M6 17c3-2 9-2 12 0"/></svg>';            /* 难过 */
    return a+'<line x1="7" y1="8" x2="11" y2="10"/><line x1="13" y1="10" x2="17" y2="8"/><path d="M6 16c3-3 9-3 12 0"/></svg>';}     /* 哭 */
  var cols=['总分','维度A','维度B','维度C','维度D','维度E'];
  var rows=[{name:'对象一',sub:'TAG',v:[74,66,86,82,60,35]},{name:'对象二',sub:'TAG',v:[28,18,35,38,36,16]}];  // v[0]=总分(管状态点)
  var h='<div class="hm-corner"><svg viewBox="0 0 100 100" preserveAspectRatio="none"><line x1="0" y1="0" x2="100" y2="100" stroke="#EFF0F1" stroke-width="1"/></svg><span class="hc-col">维度</span><span class="hc-row">对象</span></div>';
  cols.forEach(function(c){h+='<div class="hm-header">'+c+'</div>';});
  rows.forEach(function(r){
    var dot='<div style="width:8px;height:8px;border-radius:50%;flex-shrink:0;background:'+(r.v[0]<40?'#E63838':r.v[0]<60?'#FD9A00':'#37C597')+';box-shadow:0 0 0 2px '+(r.v[0]<40?'rgba(230,56,56,.2)':r.v[0]<60?'rgba(253,154,0,.2)':'rgba(55,197,151,.2)')+'"></div>';
    h+='<div class="hm-row-label" style="background:transparent;border-color:rgba(223,223,223,.5)">'+dot+'<div><div style="font-size:12px">'+r.name+'</div><small>'+r.sub+'</small></div></div>';
    r.v.forEach(function(s){h+='<div class="hm-cell" style="background:'+heat(s)+';color:'+txt(s)+';border-color:'+bord(s)+'"><div class="cv">'+face(s)+' '+s+'</div></div>';});
  });
  grid.innerHTML=h;
})();
```

- 行标签底色 **透明**（`background:transparent`）；行首一个**状态点**（按总分 `<40红/<60橙/≥60绿`，带光晕）。
- 整张矩阵外面包一张 `.card` 玻璃卡更稳重。
- ⚠️ **合并进 build_index.py 单 deck 时，渲染脚本要同时写在分册 script 和 build_index.py 硬编码 script 两处**（build 不抽取分册 `<script>`）。

## 13. 分层架构图（左标签 + 聚类卡，参考 reference/层级架构图.jpg）

> **命中**：能力/体验/产品架构图、分层框架（目标→场景→资产→范式→理念 这类纵向分层）。纯手画。
> ⚠️ **按聚类分卡**：一层放若干张玻璃卡，**一张卡 = 一类相关内容（含多个条目）**，不是"一条内容一张卡"。卡高 `grid-auto-rows:auto` **按内容自适应**（目标层一行字就矮、范式层内容多就高）。

```css
.arc{margin:auto 0;width:100%;display:grid;gap:.9vw;grid-auto-rows:auto}     /* auto = 各层按内容高度自适应 */
.arc-row{display:grid;grid-template-columns:74px 1fr;gap:1vw;align-items:stretch}
.arc-lbl{display:flex;flex-direction:column;justify-content:center;gap:.3vh}  /* 左侧分层标签：中文 + 英文 */
.arc-lbl .zh{font-weight:800;font-size:var(--fs-sm);color:var(--ink)}
.arc-lbl .en{font-family:'JetBrains Mono';font-size:9px;letter-spacing:.1em;color:var(--ink-3);text-transform:uppercase}
.arc-cells{display:flex;gap:.9vw;align-items:stretch}                         /* 一层的若干聚类卡；用 inline flex:N 配不等宽 */
.arc-band{flex:1;min-width:0;background:rgba(255,255,255,.5);border:1px solid rgba(255,255,255,.7);border-radius:14px;padding:1vw;display:flex;flex-direction:column;justify-content:center;gap:1vw;box-shadow:0 6px 18px -14px rgba(30,40,70,.18)}
.arc-vision{justify-content:center;align-items:center;text-align:center;font-weight:700;font-size:var(--fs-h3)}  /* 目标层：单卡居中陈述，别用深底深字 */
.arc-vision b{background:linear-gradient(100deg,#5B5BD6,#7C3AED);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.arc-h{font-weight:800;font-size:var(--fs-sm);color:var(--ink);display:flex;align-items:baseline;gap:.5em}   /* 聚类卡标题 + 英文 small */
.arc-h small{font-family:'JetBrains Mono';font-size:9px;color:var(--ink-3);text-transform:uppercase}
.arc-chips{display:flex;gap:.5vw .9vw;flex-wrap:wrap;align-items:center}     /* 场景层：图标 chips */
.arc-chip{display:flex;align-items:center;gap:.42vw;font-size:var(--fs-sm);font-weight:600;color:var(--ink)}
.arc-ic{width:26px;height:26px;border-radius:7px;flex-shrink:0;display:flex;align-items:center;justify-content:center}  /* 彩色底块（inline background:var(--g-blue)…）*/
.arc-ic svg{width:15px;height:15px;stroke:#fff}
.arc-list{font-size:var(--fs-sm);color:var(--ink-2);line-height:1.62}        /* 资产层：长列表文本 */
.arc-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:1.1vw}         /* 理念层：3 列 */
.arc-band.ctr{align-items:center}                                            /* 居中聚类卡 */
.arc-band.ctr .arc-h{justify-content:center} .arc-band.ctr .arc-chips{justify-content:center}
/* 范式层 mini 条目：黑线 icon + 下方彩色光晕 */
.arc-mini{display:flex;flex-direction:column;align-items:center;text-align:center;gap:.4vh}
.arc-pic{position:relative;width:32px;height:32px;display:flex;align-items:center;justify-content:center}
.arc-pic svg{width:24px;height:24px;stroke:#16191e;fill:none;position:relative;z-index:1}     /* 黑色线性图标 */
.arc-pic::after{content:"";position:absolute;left:50%;bottom:1px;transform:translateX(-50%);width:26px;height:10px;border-radius:50%;background:var(--glow,rgba(91,91,214,.55));filter:blur(6px);z-index:0}  /* 彩色光晕 */
.arc-mini .mt{font-weight:700;font-size:var(--fs-sm);color:var(--ink)} .arc-mini .md{font-size:var(--fs-xs);color:var(--ink-2);line-height:1.4}
```

HTML：`.arc` 内每层一个 `.arc-row`（左 `.arc-lbl` + 右 `.arc-cells`）；`.arc-cells` 里放 1~N 张 `.arc-band`，每张 band 内是一个聚类（标题 `.arc-h` + 内容 chips/list/grid/cols）。范式层每个 `.arc-mini` = `.arc-pic`(图标+光晕) + `.mt` + `.md`。

## 14. 数据突出卡（切角玻璃卡 + 总体说明，参考 reference/data.png）

> **命中**：3 个左右**冲击力大数字**（效率提升 X%、加速 N×…），每个配图标 + 短标题 + 小描述，上面一段**总体说明**。
> ⚠️ **两个致命坑**：
> 1. **必须单层玻璃**——卡片直接 `backdrop-filter` 采样背景纹理。**别用"外层白底 + 内层玻璃"双层做描边**，否则内层 backdrop 采到外层白底 → 卡片发实、不透（反复踩）。
> 2. **切角用 `clip-path` 会裁掉 `border`/`box-shadow`** → 渐变描边改用 **`::after` + `mask-composite:exclude` 只画边框环**（内部透明、不加实度）。

```css
.dh-wrap{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:4.2vh}
.dh-lead{font-size:clamp(15px,1.05vw,18px);color:var(--ink-2);line-height:1.7;text-align:center;max-width:1000px;margin:0 auto}   /* 总体说明，宽度=卡片行宽 */
.dh{display:grid;grid-template-columns:repeat(3,1fr);gap:2vw;max-width:1000px;margin:0 auto}
/* 单层玻璃卡：切右上+左下角、近正方、内容三段分布（图标上 / 数字组中 / 描述右下）*/
.dh-card{position:relative;aspect-ratio:1;overflow:hidden;clip-path:polygon(0 0,calc(100% - 44px) 0,100% 44px,100% 100%,44px 100%,0 calc(100% - 44px));padding:2.6vh 1.7vw;display:flex;flex-direction:column;align-items:flex-start;justify-content:space-between;text-align:left;background:rgba(255,255,255,.4);backdrop-filter:blur(15px) saturate(1.5);-webkit-backdrop-filter:blur(15px) saturate(1.5)}
.dh-card::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.32),rgba(255,255,255,0) 14%);pointer-events:none;z-index:1}  /* 顶部细高光 */
.dh-card::after{content:"";position:absolute;inset:0;clip-path:polygon(0 0,calc(100% - 44px) 0,100% 44px,100% 100%,44px 100%,0 calc(100% - 44px));padding:1.3px;background:linear-gradient(150deg,rgba(255,255,255,.85),rgba(255,255,255,.25) 55%,rgba(255,255,255,.5));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;z-index:2}  /* 渐变描边环 */
.dh-card>*{position:relative;z-index:3}
.dh-ic{width:44px;height:44px;border-radius:11px;display:flex;align-items:center;justify-content:center;background:rgba(91,91,214,.12);color:var(--accent)}  /* 扁平图标（无白底无阴影）*/
.dh-ic svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:2}
.dh-num{font-family:'Inter';font-weight:500;font-size:min(5.4vw,9vh);line-height:1;letter-spacing:-.02em;background:linear-gradient(120deg,#5B5BD6,#8B3DEE);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}  /* 大但不粗：Inter 500 */
.dh-num .u{font-size:.36em;font-weight:600;margin-left:.04em}   /* % / × 小上标 */
.dh-t{font-weight:700;font-size:var(--fs-h3);color:var(--ink);margin-top:.3vh}
.dh-d{font-size:var(--fs-sm);color:var(--ink-3);line-height:1.4;align-self:flex-end;text-align:right;white-space:nowrap}  /* 小描述沉右下、灰色、单行 */
```

HTML：`.dh-wrap` = `.dh-lead`(总体说明) + `.dh`(3 张 `.dh-card`)；每张 card = `.dh-ic` + `.dh-main`(`.dh-num`+`.dh-t`) + `.dh-d`。
- 倒角大小调 `clip-path` 的 `44px`（`::after` 同步）；要更透降 `.dh-card` 背景 `.4`。
- 说明是**总体一段**（不是每数字一条），且 `max-width` 跟卡片行一致。
