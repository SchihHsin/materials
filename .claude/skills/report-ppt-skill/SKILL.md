---
name: report-ppt-skill
description: 生成"产品 / 设计 / 研究汇报"风格的单文件网页 PPT（横向翻页 deck）。三基调——① 封面：大图作底 + 产品 logo + 标题；② 灰底分析篇：冷灰 + 玻璃折射白卡 + 底部大波浪 + 蓝紫 accent（承载数据洞察 / VOC / 竞品 / 用户旅程 / 用户画像 / 甘特 roadmap）；③ 黑底设计点：纯黑 + 底部渐变光晕 + 渐变标题字（承载问题 / 方案 / 设计点，可一章一色）。统一鸿蒙黑体 + 六档字号 ramp + 渐变色彩 token + 手画优先图表。当用户要做"设计概念汇报 / 研究汇报 / 产品方案汇报 / 数据分析汇报 / 用户研究 PPT / 竞品分析 PPT / roadmap"等偏分析与方案的网页 PPT 时使用。
---

# Report PPT Skill（汇报材料网页 PPT）

> 来源：本 skill 由 CANN DesignConcept 2026 汇报 deck 提炼，面向"分析 + 方案"型汇报材料。区别于 `guizang-ppt-skill`（杂志风 / 瑞士风、偏分享演讲）——本 skill 偏**企业内部产品/设计/研究汇报**，信息密度更高、有成体系的组件（胶囊指标、甘特、用户画像、竞品对照、旅程图）。

## 这个 Skill 做什么

生成**单文件 HTML** 的横向翻页 deck（也可多分册各自成文件，最后用 `build_index.py` 模式合并成一个 `index.html`）。核心 = **三基调 + 一套设计 token（字号 ramp / 渐变色彩 / 玻璃卡 / 鸿蒙字体）+ 一组可复用组件**。

- 翻页：`#deck` 横向 `translateX`，`.slide` 占满 `100vw/100vh`，键盘 ← →，底部 `#nav` 圆点。
- 自包含：纯 HTML/CSS/SVG，外链仅字体 CDN + 可选图表库；可离线（库 inline 到 `lib/`）。
- 不能生成 AI 图：背景大图需用户提供，或 `curl` 下载网图（Wikimedia / YouTube 缩略图 `img.youtube.com/vi/<id>/maxresdefault.jpg`）。

## 三基调（先选基调，再填内容）

| 基调 | 底色 / 氛围 | 承载内容 | 关键视觉 |
|---|---|---|---|
| **① 封面** | 大图作底 + 深色侧向叠加 | 标题页 / 章节封 | kicker（等宽小字）+ 超大 logo/标题 + 副标 + lead；品牌左上、出品方左下 |
| **② 灰底分析篇** | 冷灰 `#E9EBEE` + 底部大波浪 | 数据 / VOC / 竞品 / 旅程 / 画像 / 甘特 | **玻璃折射白卡** + 蓝紫 accent + 渐变色块 |
| **③ 黑底设计点** | 纯黑 `#06060a` + 底部渐变光晕 | 问题 / 方案 / 设计点 | **渐变标题字** + 一章一色（可调色面板）+ 玻璃拟态图位 |

> 一份完整汇报常按 **封面 → 灰底分析（现状/洞察）→ 黑底设计点（方案）→ 灰底 roadmap（甘特）** 串。

## 工作流

1. **澄清（动手前必做）**：主题 / 受众 / 章节大纲 / 有无现成素材（背景图、截图、数据）/ 需要哪几类页面（数据洞察？竞品？画像？旅程？甘特？）。结构定错后期翻修代价高。
2. **选基调 + 起模板**：复制 `assets/deck-template.html` 为起点（已含字体、token、base、nav、示例页）。
3. **按需取组件**：从 `references/components.md` 拷对应组件骨架（胶囊条 / 甘特 / VOC 墙 / 旅程 / 竞品 / 画像 / KPI）。
4. **套规范**：字号只用 ramp（`references/type-and-color.md`），颜色只用渐变 token，深色大色块统一 `--g-ink`。
5. **图表**：能手画就手画（胶囊/甘特是精调模板）；复杂图（雷达/桑基/热力/关系树）才上 ECharts/ApexCharts（`references/chart-selection.md`）。
6. **多分册合并**（可选）：每个基调一个源文件，跑 `build_index.py` 合成单 `index.html`（机制见 `references/deck-architecture.md`）。
7. **交付**：浏览器 `open` 自检；每次改完 **git push**（用户偏好）。

## 铁律（最容易翻车的几条）

- **标题 = 结论导向**：每页标题直接说出该页的「主要发现 / 结论」，不要写空泛词（❌「用户研究」→ ✅「文档、调试、环境是三大核心障碍」）。英文+说明放副标题。
- **字号只用 6 档 ramp**（h1/h2/h3/body/sm/xs），别再随手写 `max(13px,.9vw)`。超大展示数字（封面大字、大百分比、章节序号）属 bespoke，不进 ramp。
- **颜色只用渐变 token**：状态色（红/绿）用「同明度·微色相位移」渐变，不做深浅明暗；中性用纯色；深色大块统一 `var(--g-ink)`。
- **列布局间距别用 flex 列**做瀑布墙（高度推挤 + `margin-top:auto` 会出诡异间距 bug）→ 用 `column-count`。
- **绝对定位子元素无视父 padding** → 需要内边距时加一层 `position:absolute;inset:...` 的内层容器。
- **logo 用图片、且分深/浅两版按底色选**：深色底（封面 / 黑底页）用白/反白版，浅色底（灰底页 head）用深色/彩色版；**别把深色 logo 放深色底**（看不见），也别手敲文字拼 logo。详见 `components.md §0`。
- 详见 `references/pitfalls.md`。

## 参考文件

- `assets/deck-template.html` — 可用单文件 deck 起手（**7 个样例页全是真·精调件、覆盖三基调**：① 封面 ② 关键指标(多彩渐变胶囊·精调①) ③ 竞品对照(三卡+对策条) ④ 用户画像·形式一 ⑤ 甘特 roadmap(精调②) ⑥ 黑底章节封面(调色面板·持久记忆) ⑦ 黑底设计点；自带真实素材 `cover-bg.png`/`cann-dark-logo.svg`(深色封面用白版 logo)/`CANNlogo.png`(浅色页用深版 logo)/`persona.svg`/`cmp-*.jpg`）。**新材料从这里开始拷**，删改样例页 + 从 `components.md` 取更多组件。⚠️ 用户画像形式一/二是**两套方案二选一**，按输入择优（详见 components.md §5）
- `references/type-and-color.md` — 字号 ramp（6 token）+ 渐变色彩系统 + 玻璃卡公式 + 鸿蒙字体加载
- `references/components.md` — 组件骨架：胶囊条 / 甘特 / VOC 墙 / 用户旅程 / 竞品对照 / 用户画像两形式 / KPI / glass card / head
- `references/deck-architecture.md` — 单文件 deck 机制 + 多分册 `build_index.py` 合并模式
- `references/chart-selection.md` — 手画优先原则 + ECharts/ApexCharts 选型
- `references/pitfalls.md` — 踩坑清单（间距 / 头像 / SVG / 甘特 / 合并）
