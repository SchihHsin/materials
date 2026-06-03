# CANN DesignConcept · 项目说明

> Claude 自动加载本文件。**详细迭代过程见 `DESIGN-LOG.md`**（人读 / 提炼 skill 用，Claude 不自动读，需要时主动 Read）。

## 是什么
华为 **CANN 2026 设计概念汇报 PPT**，单/多文件 HTML 横向翻页 deck，由 UCD CENTER 出品。独立于 `cann-research-ppt`（不进总览聚合页）。仓库 `SchihHsin/materials`，Pages 路径 `…/materials/cann-design-concept/<file>.html`。

## 文件
- `cover.html` 封面：用户生成的 2.5D 芯片背景图 `reference/cover-bg.png` + logo/标题
- `glow.html` 黑底光晕设计点（章节调色面板）
- `gray.html` 灰底分析篇 **4 页**（数据洞察 / VOC / 竞品 / 旅程）
- `covers.html` 封面三程序化方案备选
- `reference/` 素材：CANN logo、cover-bg、竞品截图（cmp-*.jpg）

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

## gray.html 关键（4 页）
- 冷灰配色 `--paper:#E9EBEE` `--ink:#16191e` `--accent:#5B5BD6`；**玻璃折射白卡**（半透明 + `backdrop-filter`，背后纹理透出）；底部大波浪纹理
- **简笔头像**：`avatar()` JS 按 `data-av`（`type`短/长/丸子/卷/侧分 · `shirt` · `skin` · `hair` · `glasses` · `bg`）即时绘制 SVG，发型须贴头（外顶 ~y11-14，发际沿头圆 `C44 24 40 20 32 18`，否则浮高脱节）
- **① 数据洞察**：渐变胶囊条（左右两段**同色谱连续衔接**：左段终点色=右段起点色）+ 超大百分比数字
- **② VOC 分析**：顶部**深色指标带**（`--g-ink`，与下方浅色墙明暗对比，无阴影）；声音墙用 **`column-count:4` 瀑布流**——卡间距全靠统一 `margin-bottom`（⚠️ **勿用 flex 列**，曾因 flex 列高度推挤/`margin-top:auto` 反复出诡异间距 bug，最终弃用）；卡型多样：大标题(boxed 灰块衬正文)/大引号(qm)/左右布局 `.lr`/普通/`.soft` 浅灰
- **③ 竞品对照**：三卡**大段论述**（重点加粗+紫高亮底）+ **图沉卡底**（`order:2`，占满宽/圆角/小 margin/不裁切）+ 产品名图下**低调注释**；`.compare` grid 三卡等高（`align-items:stretch`，图 `margin-top:auto` 贴底对齐）；底部**对策**深色条（tag 白底黑字、圆角同容器）
- **④ 用户旅程**：CANN 专属阶段（环境搭建/文档学习/算子开发/调试优化/集成发布）；6 行 = 阶段 / 触点(中性色) / 行为(mini UI 线框截图) / **情绪曲线(5 个独立格子，每格曲线段+渐变填充+虚线横纹，`flex-shrink:0` 锁高)** / 痛点(每列 2 条) / 机会点(每列 2 条)

## 图表选型（重要原则）
- **能手画就手画优先**：占比(胶囊条/环形SVG/进度)、排行(横条/KPI大数字)、简单趋势(SVG折线面积)、星级、甘特 —— 全用纯 CSS/SVG 手画（自包含、最贴主题色、最轻）
- **手画不动才用库**：雷达/桑基/热力/关系树图/大量散点/精细交互多系列 —— 用 `lib/` 已内联的库：基础图用 **ApexCharts**(540KB,MIT,省心)、复杂图用 **ECharts**(1MB,Apache-2.0,最全)；配色一律用规范渐变 token
- 预览：`charts-gallery.html`(ECharts 12 种)、`charts-compare.html`(ECharts vs ApexCharts)；结论：两库「好看」打平，按体积/图型选

## 能力 / 约定
- `curl` 下载网图（Wikimedia / **YouTube 缩略图** `img.youtube.com/vi/<id>/maxresdefault.jpg`），**不能生成 AI 图**
- 竞品分析 = 同类工具对比（Nsight/VTune/rocprof，**不含 CANN**）+ 对策结论
- 偏好：**多步任务一次做完不打断**；**改完 push**

## 待办
- [ ] 整合成完整 deck（封面 + 灰底 gray + 黑底 glow，统一翻页/索引）
- [ ] 提炼成独立 skill 文件（含上述全局色彩规范 + 三基调）
