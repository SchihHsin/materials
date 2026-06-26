# report-ppt-skill

一个用于 **Claude Code / Claude Agent** 的 Skill：生成「产品 / 设计 / 研究汇报」风格的**单文件网页 PPT**（纵向 scroll-snap 整页翻页 deck，带概览 / 全屏 / 多种翻页过渡）。偏企业内部的分析 + 方案型汇报，信息密度高、组件成体系。

> 由「CANN DesignConcept 2026」汇报 deck 提炼而成。

## 三基调

| 基调 | 氛围 | 承载内容 |
|---|---|---|
| ① 封面 | 大图作底 + 深色叠加 | 标题页 / 章节封 |
| ② 灰底分析篇 | 冷灰 + 玻璃折射白卡 + 底部大波浪 + 蓝紫 accent | 数据洞察 / VOC / 竞品 / 用户旅程 / 用户画像 / 甘特 roadmap |
| ③ 黑底设计点 | 纯黑 + 底部渐变光晕 + 渐变标题字 | 问题 / 方案 / 设计点（可一章一色，带调色面板） |

## 设计规范速览

- **字体**：HarmonyOS Sans SC（鸿蒙黑体，CDN @font-face），等宽标签用 JetBrains Mono。
- **字号**：6 档 ramp token `--fs-h1/h2/h3/body/sm/xs`，正文/标题分级统一，超大展示数字除外。
- **颜色**：渐变 token；状态色（红/绿）用同明度·微色相位移；深色大块统一 `--g-ink`。
- **玻璃折射白卡**：半透明 + `backdrop-filter` + 亮边 + inset 高光。
- **标题=结论导向**：每页标题直接说出主要发现，不写空泛栏目名。
- **logo 分深/浅两版按底色选**：深色底用白/反白版，浅色底用深色/彩色版。

详见 `references/`：`type-and-color.md` · `components.md` · `deck-architecture.md` · `chart-selection.md` · `pitfalls.md` · **`checklist.md`（交付前每页必跑的质检清单）**。

## 翻页过渡（5 种，可切换）

默认上下滑动，另有 4 种可选。**地址加 `?t=xxx` 即时切换，不用改代码**（也可改脚本顶 `TRANSITION` 常量改默认）：

| `?t=` | 效果 |
|---|---|
| `slide`（默认） | 上下滑动 · 原生 scroll-snap |
| `fade` | 淡入淡出 |
| `cut` | 瞬切硬切（PPT 式） |
| `slide-h` | 横向滑动（带前进 / 后退方向） |
| `magic` | **Keynote 式神奇移动** |

- 例：`index.html?t=magic`、`index.html?t=fade`。
- **magic（神奇移动）需配合**：在**相邻两页给同一个东西标相同 `data-key`**（如 logo / 标题 / 某张卡），翻页时该元素会从旧位置 / 大小平滑飞到新位置（FLIP）；没标 `data-key` 的页自动退化成淡入。
- 架构：除默认 slide 外都走「受控叠层」`body.ctrl`，加新过渡只需多写一段 CSS。详见 `deck-architecture.md`。

## 安装

作为 Claude Code Skill 使用——把整个目录放到 skills 目录即可：

```bash
# 用户级（所有项目可用）
git clone git@github.com:SchihHsin/report-ppt-skill.git ~/.claude/skills/report-ppt-skill

# 或 项目级（仅该项目）
git clone git@github.com:SchihHsin/report-ppt-skill.git <项目>/.claude/skills/report-ppt-skill
```

之后让 Claude「做一份 XX 汇报 / 研究 / 竞品分析 / 数据分析 PPT」即可命中。

## 用法

1. 复制 `assets/deck-template.html` 作为起点（已含字体、token、base、导航 + **8 个精调样例页**覆盖三基调）。
2. 删改样例页，从 `references/components.md` 取更多组件骨架。
3. 浏览器打开自检（试不同翻页过渡加 `?t=fade|cut|slide-h|magic`）。

样例页：① 封面 ② 关键指标(多彩渐变胶囊) ③ 竞品对照 ④ 用户画像·形式一 ⑤ 甘特 roadmap ⑥ 黑底章节封面(调色面板·localStorage 持久记忆) ⑦ 黑底设计点·版式①左文右图 ⑧ 黑底设计点·版式②上下堆叠 hero。

> ⚠️ 用户画像有**三套形式（一/二/三），按内容三选一**：正式深描单人→形式一、多角色雷达对比→形式二、白板便利贴速写单人→形式三（详见 `components.md §6a/§6b/§6c`）。
> ⚠️ 黑底设计点有**两种版式**：①左文右图（要点多）/ ②上下堆叠 hero（大图为主），见 `components.md §8`。

## 目录结构

```
SKILL.md                  主文件（三基调 / 工作流 / 铁律 / 索引）
references/               规范与组件骨架
assets/
  deck-template.html      7 页起手模板
  cover-bg.png · cann-dark-logo.svg · CANNlogo.png · persona.svg · cmp-*.jpg   示例素材
```

## 关于示例素材

`assets/` 里的封面图、CANN logo、竞品截图等**仅作排版示例**，用于演示组件效果。**套用到你自己的材料时请替换成自己的素材**；其中第三方产品截图、品牌 logo 版权归各自所有，请勿直接商用或再分发。

## 更新日志

### 2026-06 — 加交付前质检清单，治"生成出来要大量手调"
- 新增 `references/checklist.md`：**每页必跑的质检清单**（字号误用 sm/xs、内容溢出 slide、flex/grid 子项漏 `min-height:0`、双层 padding 对不齐、图片裸 `aspect-ratio` 撑破、`min(vw,vh)` 视口比例陷阱、测量代替猜），配 `rg` + 无头截图自查。工作流加"交付前逐页跑 checklist"为关键步。
- 铁律新增 **flex/grid 子项默认 `min-height:0`（横向 `min-width:0`）**——"等高对不齐 / 某栏更高 / 卡片气泡越界 / 文字被裁"几乎都是漏这条。
- 对照 `guizang-ppt-skill` 的稳健做法提炼：填现成槽位别手搓几何、放不下就删/拆别缩字、图片固定 height+overflow+object-fit、溢出降级而非顶破。

### 2026-06 — 翻页过渡扩到 5 种 + 设计点页两版式

- **翻页过渡 5 种可切换**（`?t=slide|fade|cut|slide-h|magic`，默认 slide）：翻页引擎从 fade-only 泛化为「受控叠层」`body.ctrl` + `data-transition`；`fade`/`cut`/`slide-h` 用 CSS，`magic`（Keynote 神奇移动）用 Web Animations API 对相邻两页 `data-key` 相同的元素做 FLIP 位移缩放。详见上「翻页过渡」节 + `deck-architecture.md`。
- **黑底设计点页两版式**（`components.md §8`）：① 左文右图（图~65%，含 kicker+标题+正文+3 要点）/ ② 上下堆叠 hero（大图型~78%，只标题+正文）；图统一真 16:9（匹配 1920×1080，不裁），`.body` 正文细体 + `<b>` 加粗提亮主次。
- **灰底「图 / 表 + 一段文字」通用版式**（`components.md §14`）：左 sm2 文案（结论 h2 + 段落 + 黑底结论条）+ 右图 / 占位，由内容形态直接触发的默认范式。
- `.body-area{padding-bottom}`：给绝对定位的 `.foot`/`.ucd` 留位，避免居中卡贴页尾（见 `pitfalls.md`）。

### 2026-06-12 — 新增 3 个分析 pattern + 控制栏显隐重做

- `components.md` 新增 **§12 评分热力矩阵**（行×列打分，淡底+彩字+表情脸+状态点，含渲染 JS，复刻 mattrix 参考）、**§13 分层架构图**（左标签 + 按聚类分卡，卡高自适应，范式层黑线图标+彩色光晕）、**§14 数据突出卡**（切角玻璃方卡 + 总体说明）；路由表同步加 3 行。
- §14 沉淀两个踩坑：① 切角玻璃卡**必须单层**（双层会让内层 backdrop 采到外层白底发实）；② `clip-path` 裁掉 border → 渐变描边改用 `::after`+`mask-composite:exclude` 只画边框环。
- **控制栏显隐重做**（`deck-template.html` + `deck-architecture.md`）：底部栏与右侧导航点**分区独立、离开即淡出**（移到底部/右侧分别触发，`mouseleave` 隐藏），弃用旧的 2.5s 定时器 + 两栏同步（残留、只能底部触发）。

### 2026-06-10 — 提升典型 pattern 命中率

复用本 skill 时，VOC 墙 / 用户旅程 / 竞品对照等精调件常**识别不出来**（用户说大白话、不说组件学名），导致 Claude 手搓更丑的版面。

- `references/components.md` 顶部新增 **「选件路由表」**：每个 pattern 列出用户**常说的各种说法/同义触发词**（如「这些吐槽/原声/访谈摘录」→ VOC 墙，「各阶段体验/全链路/情绪曲线」→ 用户旅程），按**意图**命中而非组件名。
- `SKILL.md`：工作流加「逐页先过路由表再取件」步骤；铁律加「先路由再动手，命中精调件就照抄、别另造」。
- 修掉 `components.md` 的重号（原有两个 `## 2.`），组件统一编号 §1–§8。

### 2026-06-10 — 翻页与交互大改

deck 从「横向 `translateX` 受控翻页」改为 **纵向原生 `scroll-snap` 整页翻页**，并补齐概览/全屏交互。`assets/deck-template.html` 与 `build_index.py`（合并版）已同步。

- **纵向 scroll-snap 翻页**：`body` 作滚动容器（`overflow:hidden auto` + `scroll-snap-type:y mandatory`），`.slide` 满屏 + `scroll-snap-align:start;scroll-snap-stop:always`——划动过程短暂见两页、松手自动吸附到整页（不再拦截滚轮做瞬切/淡入）。当前页改由 **`IntersectionObserver`（≥55%）** 判定，`go()`/键盘/导航点统一走 `scrollIntoView`。
- **键盘**：`↑↓←→` / 空格 / PageUp-Down / Home / End 全支持翻页；`O` 概览、`F` 全屏、`Esc` 退概览。
- **右侧竖排 `.nav-dots`** + **底部居中控制栏 `#controls`**：控制栏**小而透**、**默认隐藏**，鼠标移到屏幕底部才出现、2.5s 淡出；亮/暗随当前页 `body.on-dark` 自适应。**移除顶部进度条**。
- **概览 Overview**：缩略图网格按 **当前视窗比例** 缩放（不强制 16:9——窗口非 16:9 时强制 16:9 必然裁边或留缝），每页完整缩小、不裁不留缝；点缩略图跳页。
- **全屏**：Fullscreen API（`F`），**进入后按钮图标切换为「退出全屏」**；监听 `fullscreenchange`/`resize` 重新吸附当前页（修复改窗口后停在两页之间）。
- 黑底设计点章节封面的**调色面板**保留，默认 `display:none`、仅在章节封面页出现，`localStorage` 持久记忆；概览中隐藏。
- 踩坑记录见 `references/deck-architecture.md`（scroll-snap 两个坑、`aspect-ratio` 在带 `height:100vh` 元素上失效等）。

## License

代码与模板：MIT。示例素材不在此列（见上）。
