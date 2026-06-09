# CANN DesignConcept · 项目说明

> Claude 自动加载本文件。**详细迭代过程见 `DESIGN-LOG.md`**（人读 / 提炼 skill 用，Claude 不自动读，需要时主动 Read）。

## 是什么
华为 **CANN 2026 设计概念汇报 PPT**，单/多文件 HTML 横向翻页 deck，由 UCD CENTER 出品。独立于 `cann-research-ppt`（不进总览聚合页）。仓库 `SchihHsin/materials`，Pages 路径 `…/materials/cann-design-concept/<file>.html`。

## 文件
- **`index.html` 合并版完整 deck（14 页）= 封面 + gray 7 页 + glow 6 页**，统一翻页/导航/字体/字号。⚠️ **由 `build_index.py` 从三个分册自动拼装，不要手改 index.html**——改内容改分册再 `python3 build_index.py` 重生成
- `build_index.py` 拼装脚本：逐块 verbatim 抽取三分册的 CSS/slide/script → 把各册 `.slide` 作用域化（`.slide.s-gray` / `.slide.s-glow`，避免黑/灰底互相覆盖）→ 全局换 HarmonyOS Sans + 套字号 token → 合成单文件单 `#deck`/单 `go()`/单 nav；glow 调色面板逻辑保留但对非 glow 页惰性（`curChap()` 判 `data-chapter`）
- `cover.html` 封面（分册源）：2.5D 芯片背景图 `reference/cover-bg.png` + logo/标题
- `glow.html` 黑底光晕设计点（分册源，章节调色面板）
- `gray.html` 灰底分析篇 **7 页**（分册源，**当前顺序**：① 用户旅程 ② VOC 墙 ③ 关键指标概览(胶囊) ④ 用户画像·形式一 ⑤ 用户画像·形式二 ⑥ 竞品对照 ⑦ 甘特 roadmap）；页码 head-r 01–07 跟随此顺序

## 字体与字号规范（index.html，写 skill 用）
- **主字体 = HarmonyOS Sans SC（鸿蒙黑体）**，CDN @font-face `cdn.jsdelivr.net/gh/IKKI2000/harmonyos-fonts@master/css/harmonyos_sans_sc.css`（MIT，权重 100/300/400/500/700/900）；字体栈 `'HarmonyOS Sans SC','Inter','Noto Sans SC'`（Latin 回退 Inter）；**JetBrains Mono 仅保留给英文 kicker/meta/页码等刻意等宽标签**
- **字号 token（`:root`，响应式 clamp）**：`--fs-h1` 页面主标题 clamp(20,1.7vw,30) / `--fs-h2` 区块标题 clamp(15,1.15vw,21) / `--fs-h3` 卡片小标题 clamp(13,.95vw,16) / `--fs-body` 正文 clamp(12,.82vw,15) / `--fs-sm` 次要正文 clamp(10.5,.72vw,13) / `--fs-xs` 标签/注释/页码 clamp(9,.62vw,11)
- **落地**：在「统一层」（拼装后置于各册 CSS 之后）用 `!important` 把跨页通用角色绑到 token——`.brand .ttl`→h1、`.subttl`→sm、`.head-r`/`.kicker`/`.chrome`/`.cmp-cap`→xs、`.body`→body、`.point .pt-title`→h3、`.pt-desc`→sm；**超大展示数字（封面 CANN、大百分比、章节序号、glow 渐变章节标题）属 bespoke 不进 ramp**
- **用户画像两页已全量上 ramp**（`gray.html` 源里 `.pf-*`/`.pp-*` 共 34 处 font-size 已改 `var(--fs-*)`）：人名(`.pf-sb.head .nm`)→h2，**角色行(`.pf-sb.head .rl`「Senior Operator Engineer·内源团队」)→body**（规范前人名≈18px·角色≈11.5px，故人名落 h2≈16.6、角色落 body≈12 最贴近原始主次；中间试过 sm 偏小、h2 与人名同大显怪，最终 body），区块标题/环形%/统计数字→h3，正文(职责/原声/痛点/场景/期待)→body，标签/小标题/流程标题→sm，字段标签/KPI标签/分段标签→xs。⚠️ 字号 token **也写进了 `gray.html` 自己的 `:root`**（standalone 也能用），build 时统一层再覆盖一遍
- ⚠️ **`gray.html` 的字号 token 必须保留**：删了会导致 `.pf-*`/`.pp-*` 的 `var(--fs-*)` 失效
- `covers.html` 封面三程序化方案备选
- `reference/` 素材：**CANN logo 图片版 `CANNlogo.png`**（已替代手画文字 logo）、cover-bg、竞品截图（cmp-*.jpg）、`Persona.svg`/`Persona.jpg`（画像模板）、`workflow-plan-gantt(1).html`（甘特参考）、**`av/*.svg`（DiceBear notionists 开源头像，CC0，已替代手画简笔头像）**
- `lib/` 内联图表库：`echarts.min.js`（Apache-2.0）、`apexcharts.min.js`（MIT）

## 三基调（写 skill 的核心规则）
- **封面**：大图作底 + CANN logo（文字版 `C`+红`A`+`NN`）+ DesignConcept 2026 + HUAWEI（左上）+ UCD CENTER（左下）
- **灰底 = 前瞻性设计 / 分析**：冷灰 + **玻璃折射白卡** + 底部**大波浪**纹理 + 蓝紫 accent
- **纯黑底 = 问题 / 研究 / 设计点**：黑主体 + 底部**渐变光晕** + 渐变标题字，**一章一色**

## glow.html 关键
- **章节模型**：颜色按章定（`data-chapter`），每章 = 1 封面 + **2 设计点**；取当前章用 **`cur()`**（⚠️ 不是 `curCh`，曾因笔误致面板打不开）
- **设计点（CANN 工具）**：第一章 控制与可观测 = 1.1 控制流可视化 / 1.2 智能错误诊断；第二章 开发提效 = 2.1 算子开发向导 / 2.2 交互式文档+成长地图
- **光晕三层**：左右彩色光斑（`::before/::after`）+ 底部连续白带（`.glow-white`，`linear-gradient`）；视觉黑→彩→白
- **调色面板**：嵌入章节封面页内（`appendChild`，非 fixed）；图标常驻右上、面板在图标**左侧**展开、点图标开合、点外关；工具纯 icon（撤销/重做/重置，**reset = 回到打开面板前**，无变动时禁用）；`setPanelOpen` 用 `display` 控制
- 默认色：HUE 234 / GAP 57° / SAT 95% / LIGHT 40% / SPREAD 35vh / COLOR .68 / WHITE .58

## 全局图表色彩规范（gray.html，写 skill 用）
- **渐变 token**（`:root`）：分类/状态 `--g-red/green/blue/amber/purple/teal/pink`，蓝紫 `--g-accent`，**统一深色** `--g-ink`（渐变 #22262F→#14171C）、`--dark`（实色 #16191E），中性 `--g-neutral`（纯色）
- **大圆角 + 渐变**：图表色块普遍带渐变；**绿/红等状态色用同明度「微色相位移」渐变**（如绿 `#23CFA0→#45D65A`、红 `#FF5A6E→#FF6F55`，不做深浅明暗），**中性用纯色**
- **统一深色**：所有深色大色块（VOC 指标带 / 竞品结论条 / 旅程阶段头）都引用 `var(--g-ink)`，不再各自定义
- **标题 = 结论导向**：标题直接说出该页主要发现（非空泛词），副标题放英文+说明；各页统一 `.head`（CANN logo + 中文标题 + 英文副标题 + 右上页码）

## gray.html 关键（7 页）
- 冷灰配色 `--paper:#E9EBEE` `--ink:#16191e` `--accent:#5B5BD6`；**玻璃折射白卡**（半透明 + `backdrop-filter`，背后纹理透出）；底部大波浪纹理
- **头像**：统一用 **DiceBear notionists 开源头像**（`reference/av/*.svg`，CC0）；下载时 `beardProbability=0` 避免「女生长胡子」，`backgroundColor` 跟随所在页底色（如橙页 eco.svg 用 `FBEEE9`）。曾用 `avatar()` JS 手画简笔头像，已弃用
- **① 数据洞察**：渐变胶囊条（左右两段**同色谱连续衔接**：左段终点色=右段起点色）+ 超大百分比数字
- **② VOC 分析**：顶部**深色指标带**（`--g-ink`，与下方浅色墙明暗对比，无阴影）；声音墙用 **`column-count:4` 瀑布流**——卡间距全靠统一 `margin-bottom`（⚠️ **勿用 flex 列**，曾因 flex 列高度推挤/`margin-top:auto` 反复出诡异间距 bug，最终弃用）；卡型多样：大标题(boxed 灰块衬正文)/大引号(qm)/左右布局 `.lr`/普通/`.soft` 浅灰
- **③ 竞品对照**：三卡**大段论述**（重点加粗+紫高亮底）+ **图沉卡底**（`order:2`，占满宽/圆角/小 margin/不裁切）+ 产品名图下**低调注释**；`.compare` grid 三卡等高（`align-items:stretch`，图 `margin-top:auto` 贴底对齐）；底部**对策**深色条（tag 白底黑字、圆角同容器）
- **④ 用户旅程**：CANN 专属阶段（环境搭建/文档学习/算子开发/调试优化/集成发布）；6 行 = 阶段 / 触点(中性色) / 行为(mini UI 线框截图) / **情绪曲线(5 个独立格子，每格曲线段+渐变填充+虚线横纹，`flex-shrink:0` 锁高)** / 痛点(每列 2 条) / 机会点(每列 2 条)
- **⑤ 甘特 roadmap**：仿 `reference/workflow-plan-gantt(1).html`；白底**玻璃折射大卡**（`.gantt` 高 54vh、`margin:auto 0` 居中）+ 内层 `.rm-pad`（`position:absolute;inset...`，因绝对定位子元素会无视父 padding，故加内层容器撑出留白）+ **虚线 SVG 网格底纹**（画在白卡背景，实线全去）；浮动条 `.rm-bar`（`opacity:.86` + `backdrop-filter`，`max-height:46px` 限高）

## 用户画像两形式（gray.html 第 6/7 页）
- **形式一**（`.pf` 前缀，蓝 `--b:#385CFF`）：仿 `reference/Persona.svg`，左 23% 人物栏（portrait + head/标签/职责/原声）+ 右四区（岗位特征 conic 环 | 上下游协同 flow+交付物 KPI / 典型业务场景 16:9 mockup×4 / 核心痛点）
- **形式二**（`.pp` 前缀，橙 `--o:#E8533B` 扁平）：仿 `reference/Persona.jpg`(AscendC)，顶栏 pp-top（人物/环形/期待 等距）+ 三栏（含 ECharts 雷达 内源蓝/生态红）
- **左栏垂直间距坑**：`.pf-side` flex column 用统一 `gap`（块间严格等距）+ 原声 `margin-top:auto` 自适应贴底。⚠️ head 块是唯一淡蓝块且含 role 副标题，内部底部留白会让「名字离标签」视觉放大 → 收紧 head 的 `padding`+role `margin-top`，别去动 gap（gap 本就对称）

## 图表选型（重要原则）
- **手画优先**：能纯 CSS/SVG 手画的就手画（自包含、最贴主题、最轻）—— 但「能画」≠「好看」，**好看必须精心调**
- **唯一精调过、确认好看的**：① 胶囊条（数据洞察页）② 甘特浮动条。这两个可放心复用/做模板
- **deck 里其它手画件只是「能显示」、未精调、不算好看**（星评★、进度/技能条 track+fill、SVG 情绪曲线、KPI 数字）—— 要正式用前必须重新打磨，别当成「好看现成件」
- **直接用库（手画成本太高）**：雷达/桑基/热力/关系树图/大量散点/精细交互多系列 —— `lib/` 已内联 **ApexCharts**(540KB,MIT,基础图省心) + **ECharts**(1MB,Apache-2.0,最全)；配色走规范渐变 token
- 预览：`charts-gallery.html`、`charts-compare.html`（两库「好看」打平，按体积/图型选）

## 能力 / 约定
- `curl` 下载网图（Wikimedia / **YouTube 缩略图** `img.youtube.com/vi/<id>/maxresdefault.jpg`），**不能生成 AI 图**
- 竞品分析 = 同类工具对比（Nsight/VTune/rocprof，**不含 CANN**）+ 对策结论
- 偏好：**多步任务一次做完不打断**；**改完 push**

## report-ppt-skill（通用汇报 PPT skill，由本项目提炼）
内容 = README.md + SKILL.md + references/{type-and-color,components,deck-architecture,chart-selection,pitfalls}.md + assets/{deck-template.html, cover-bg.png, cann-dark-logo.svg, CANNlogo.png, persona.svg, cmp-*.jpg}。不绑死 CANN，写别的汇报材料可直接用。对外分享走 ③ 独立仓库。

⚠️ **同一份 skill 现存 3 处，其中 2 处是各自独立的 git 仓库，改完必须同步全部三处**：
1. `~/.claude/skills/report-ppt-skill/` — 用户级（跨项目通用，**不在 git**，纯本地）
2. `/Users/hsin/Documents/Coding/materials/.claude/skills/report-ppt-skill/` — 项目级，**随 `SchihHsin/materials` 仓库**（项目内可直接用）
3. `/Users/hsin/Documents/Coding/report-ppt-skill/` — **独立仓库 `SchihHsin/report-ppt-skill`（git@github.com:SchihHsin/report-ppt-skill.git，main 分支）**，可单独分发/安装

**同步规则（两个 git 仓库各自独立提交）**：任一处改动后，`cp -R` 同步到另两处；②要在 materials 仓库 commit&push，③要在它自己的仓库 commit&push（`git -C /Users/hsin/Documents/Coding/report-ppt-skill add/commit/push`），①只是本地拷贝。**别只推一个仓库就以为完事**（曾出现 ③ 落后、缺竞品/画像/dark-logo）。权威源建议以 ③ 独立仓库为准（skill 的天然主仓）。

**改 skill 的固定动作清单**（每次都走完）：① 改任一份 → ② `cp -R` 同步 A/B/C 三处 → ③ `git -C …/report-ppt-skill add&commit&push`（③ 仓库）→ ④ materials 仓库 `add&commit&push`（含 ② 内嵌份）→ ⑤ 若涉及规范/位置变化，更新本 CLAUDE.md 并随 materials 一起 push。

## 待办
- [x] 整合成完整 deck（封面 + 灰底 gray + 黑底 glow，统一翻页/索引）→ `index.html`（build_index.py 拼装）
- [x] 提炼成独立 skill 文件（含全局色彩规范 + 三基调）→ 见上「report-ppt-skill」节
