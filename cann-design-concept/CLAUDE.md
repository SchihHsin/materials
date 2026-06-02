# CANN DesignConcept · 项目说明

> Claude 自动加载本文件。**详细迭代过程见 `DESIGN-LOG.md`**（人读 / 提炼 skill 用，Claude 不自动读，需要时主动 Read）。

## 是什么
华为 **CANN 2026 设计概念汇报 PPT**，单/多文件 HTML 横向翻页 deck，由 UCD CENTER 出品。独立于 `cann-research-ppt`（不进总览聚合页）。仓库 `SchihHsin/materials`，Pages 路径 `…/materials/cann-design-concept/<file>.html`。

## 文件
- `cover.html` 封面：用户生成的 2.5D 芯片背景图 `reference/cover-bg.png` + logo/标题
- `glow.html` 黑底光晕设计点（章节调色面板）
- `gray.html` 灰底分析篇 8 页
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

## gray.html 关键
- 冷灰配色：`--paper:#E9EBEE` `--card:#fff` `--ink:#16191e` `--accent:#5B5BD6` `--accent-soft:#ECECFB`
- **玻璃卡**（半透明 + `backdrop-filter:blur`，背后纹理透出）；accent/ink 实底块保持不透明
- **底部大波浪**：两层错位贝塞尔大色块（灰蓝 `#7e8696`/`#949bab`，opacity .07/.08，左低右高微倾斜）
- **面性渐变箭头**：实心 `➤` + accent→紫 `background-clip:text`
- **9 页**：①区块封面 ②用户研究概览 ③痛点与用户声音 ④VOC 分析(情感占比条+关键指标+masonry 声音墙：星评/头像/引号，hl/accent 实底重点卡) ⑤用户画像 ⑥全局沙盘 ⑦竞品对照(YouTube截图) ⑧用户旅程(Journey Map：阶段/触点/行为多块+多向箭头/情绪曲线/痛点/机会点) ⑨痛点→设计映射

## 能力 / 约定
- 能用 `curl` 下载网图（Wikimedia logo / **YouTube 缩略图** `img.youtube.com/vi/<id>/maxresdefault.jpg`），**不能生成 AI 图**
- 竞品分析 = 同类竞品工具对比（Nsight/VTune/rocprof，**不含 CANN**）+ 结论
- 偏好：**多步任务一次做完不打断**；**改完 push**

## 待办
- [ ] 整合成完整 deck（封面+灰底+黑底，统一翻页/索引/低功耗）
- [ ] 提炼成独立 skill 文件
