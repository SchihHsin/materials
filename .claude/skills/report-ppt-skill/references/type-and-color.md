# 字号、色彩、字体规范

## 字体

- **主字体 = HarmonyOS Sans SC（鸿蒙黑体）**，CDN @font-face（MIT，权重 100/300/400/500/700/900）：
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/IKKI2000/harmonyos-fonts@master/css/harmonyos_sans_sc.css">
  ```
  字体栈：`'HarmonyOS Sans SC','Inter','Noto Sans SC',sans-serif`（Latin 回退 Inter）。
- **JetBrains Mono 仅用于**英文 kicker / meta 标签 / 页码这类刻意等宽的小字（配 `letter-spacing` + `text-transform:uppercase`）。
- 加载 Google Fonts 作回退：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500&family=Noto+Sans+SC:wght@200;300;400;500;700&display=swap" rel="stylesheet">
  ```

## 字号 ramp（6 档，响应式 clamp）

```css
:root{
  --fs-h1:clamp(20px,1.7vw,30px);   /* 页面主标题（每页那句结论）*/
  --fs-h2:clamp(16px,1.25vw,22px);  /* 区块标题 / 人名 */
  --fs-h3:clamp(15.5px,1.2vw,19px);  /* 卡片小标题 / 中小号数字 */
  --fs-body:clamp(15px,1.12vw,18px); /* 正文（舒适阅读档，1440 下 ~14.4px）*/
  --fs-sm:clamp(12px,.82vw,14.5px); /* 次要正文 / 说明 */
  --fs-xs:clamp(9px,.62vw,11px);    /* 标签 / 注释 / 页码 */
}
/* ⚠️ 用户画像是高密度特殊形式：在它的根容器上把 body/h3 局部冻回紧凑档，不随全局正文放大 */
.pf,.pp,.up{--fs-h3:clamp(13px,.95vw,16px);--fs-body:clamp(12px,.82vw,15px)}
```

**用法**：所有文字只引用 `var(--fs-*)`，不要再手写 px/vw。新增普通页的正文走 `--fs-body`（≈14.4px @1440，跟竞品 desc / 机会矩阵左栏一个量级）就对。
**例外（bespoke 不进 ramp）**：封面超大 logo/标题、大百分比指标数字、章节序号、黑底渐变章节标题——这些是"展示数字"，按视觉单独定。

> ⚠️ **别拿用户画像当正文基准**：画像信息密度极高、用的是局部冻小的 body（12–15），是特殊形式；普通页正文该用全局 `--fs-body`（13.5–16），不要照画像写小。**改 body 必须同时确保 `--fs-h3` ≥ `--fs-body`**（卡片小标题不能比正文小），所以这俩是一起挪的。

角色映射参考（来自实战）：页面标题→h1；区块标题/人名→h2；卡片标题/环形%/统计数字→h3；正文/职责/痛点/场景→body；角色行/标签/小标题→sm；字段标签/KPI 标签/页码→xs。

> 经验：一个元素该用哪档，先量它"规范前的原始 px"，落到最近的一档即可。

### 高密度交互模板的字号例外

- `evidence-spotlight-matrix` 的**证据承载物主体**（矩阵、表格、旅程图、流程图、截图组、架构图等）可以局部使用 `--fs-sm` 或更小的固定像素（仅限极密集矩阵 / 小节点），但浮层解释卡 `.spot-callout/.hm-callout` 的正文必须使用 `--fs-body`，标题使用 `--fs-h2`。
- `derivation-column-flow` 的竖栏标题用 `--fs-body`，条目标题用 `--fs-h3`，条目解释用 `--fs-sm`；不要为了塞更多内容把整页正文降到 xs。
- 这两个模板的数字序号（如 `/01`）属于展示性页码，可用 Condensed 字体和 bespoke 大字号，不进入正文 ramp。

## 色彩系统：纯色谱 + 渐变谱

```css
:root{
  /* 基础冷灰主题（灰底分析篇）*/
  --paper:#E9EBEE; --card:#fff; --card-2:#F1F3F6;
  --ink:#16191e; --ink-2:#5e646e; --ink-3:#929aa6; --line:#d4d8df;
  --accent:#5B5BD6; --accent-soft:#ECECFB; --red:#E60012;

  /* 纯色：小面积、清晰语义。用于标签/图标/线条/图表点/卡片局部光带。 */
  --c-red:#F05A68; --c-orange:#F47A4B; --c-amber:#F4B450; --c-yellow:#D9B52C;
  --c-lime:#91BD48; --c-green:#39B982; --c-mint:#36BFA2; --c-teal:#28A8D8;
  --c-blue:#4B8DFF; --c-indigo:#5B5BD6; --c-purple:#8D63D8; --c-pink:#D95F9D; --c-rose:#E76C88;
  --c-neutral:#9BA5B4; --c-ink:#22262F;

  /* 渐变：大面积强调面、光带、图表填充；与同名纯色保持同一色相。 */
  --g-red:linear-gradient(120deg,#FF5A6E,#FF6F55); --g-orange:linear-gradient(120deg,#FF9A55,#F47A4B);
  --g-amber:linear-gradient(120deg,#FBBF60,#F59E0B); --g-yellow:linear-gradient(120deg,#F4D35E,#D9B52C);
  --g-lime:linear-gradient(120deg,#B8DC62,#91BD48); --g-green:linear-gradient(120deg,#23CFA0,#45D65A);
  --g-mint:linear-gradient(120deg,#42D4B8,#36BFA2); --g-teal:linear-gradient(120deg,#38C9D7,#4FACFE);
  --g-blue:linear-gradient(120deg,#2F6FED,#4B8DFF); --g-indigo:linear-gradient(120deg,#6674E6,#5B5BD6);
  --g-purple:linear-gradient(120deg,#A78BFA,#7C3AED); --g-pink:linear-gradient(120deg,#FF4FA3,#FF7AC8);
  --g-rose:linear-gradient(120deg,#F37A9A,#E76C88); --g-neutral:linear-gradient(120deg,#E4E8EF,#CBD3DF);

  --dark:var(--c-ink);                                  /* 统一深色（实色）*/
  --g-ink:    linear-gradient(140deg,#22262F,#14171C);  /* 统一深色（渐变）：所有深色大色块用它 */
  --g-accent: linear-gradient(135deg,var(--c-indigo),#7C3AED); /* 蓝紫主渐变 */
}
```

### 先选纯色还是渐变

- 用 `--c-*`：小面积且需要清晰边界的元素，例如标签文字/边框、Lucide 图标、图表线和数据点、状态圆点、卡片内大图标水印、透白卡顶部光带的基色。**同一张卡的标签、图标、光带必须用同一个 `--c-*`。**
- 用 `--g-*`：大面积强调面，例如数据突出卡、进度胶囊、章节光晕、宽色带、图表面积填充、黑底设计点的渐变标题。渐变不能用作小号正文文字或细图标的 `color`。
- 用 `--g-neutral`：中性状态、默认 chip、辅助模块、非重点节点；用 `--c-neutral`：中性图标、分组标签、辅助线。
- 用 `--g-ink`：结论条、最终判断、深色阶段头、三卡页的最终卡等大块重点；用 `--c-ink`：深色图标、深色小标签、深色文字点缀。
- 同一页默认选 1 个主色 + 至多 2 个辅助色；完整色谱是可选范围，不是要求每页用全。

### 色相语义

| 色相 | 纯色 token | 常用场景 |
|---|---|---|
| 红 / 玫红 | `--c-red` / `--c-rose` | 风险、错误、告警、强烈负向情绪；不要用作普通分类色 |
| 橙 / 琥珀 / 黄 | `--c-orange` / `--c-amber` / `--c-yellow` | 注意、待确认、阶段性提醒、进行中；黄色不承载大段文字 |
| 黄绿 / 绿 / 薄荷 | `--c-lime` / `--c-green` / `--c-mint` | 完成、机会点、正向结果、增长与改善；“机会”默认优先绿或薄荷 |
| 青 / 蓝 | `--c-teal` / `--c-blue` | 信息、工具、路径、数据、探索；蓝用于主数据强调，青用于连接与辅助信息 |
| 靛 / 紫 | `--c-indigo` / `--c-purple` | 产品主调、核心主题、策略与创新；靛优先作为主 accent，紫仅在语义明确时单独使用 |
| 粉 | `--c-pink` | 用户感受、人物、社区、柔性主题；避免与红色同时承担同一类负向语义 |
| 中性 / 墨色 | `--c-neutral` / `--c-ink` | 次要分类、辅助元素、总结与最终判断 |

### 卡片颜色规则

- **3 张同类卡**：白卡 / `--g-accent` / `--g-ink`，建立事实、重点、结论三层。
- **4 张及以上同类卡**：保持透白玻璃底；默认按 `--c-indigo`、`--c-blue`、`--c-teal`、`--c-green`（第五张可用 `--c-pink`）选择有语义的纯色，驱动标签、Lucide 大图标和顶部淡光带。不要用实色满铺。
- 黄橙红只在其语义成立时加入卡片序列；它们不是“凑齐彩虹”的装饰色。
- **相近色默认不并用**：同一张卡片墙中，靛蓝 / 紫、红 / 玫红、绿 / 薄荷默认二选一；橙 / 琥珀 / 黄最多选两种。需要更多区分时，优先跨到蓝、青、绿或粉，不靠相邻色凑数。
- 状态渐变（红/绿）保持同明度、轻微色相位移，不做深到浅的明暗条。
- 重点文字高亮：`background:linear-gradient(transparent 60%,color-mix(in srgb,var(--c-indigo) 16%,transparent) 0)`。

## 玻璃折射白卡（灰底篇标志件）

```css
.glass{
  background:rgba(255,255,255,.55);
  -webkit-backdrop-filter:blur(15px) saturate(1.4); backdrop-filter:blur(15px) saturate(1.4);
  border:1px solid rgba(255,255,255,.7);
  border-radius:16px;
  box-shadow:0 10px 30px -16px rgba(30,40,70,.2), inset 0 1px 0 rgba(255,255,255,.85);
}
```
要点：半透明白 + `backdrop-filter` 让背后纹理透出 + 1px 亮边 + inset 顶部高光。大圆角（14–16px）。

## 底部大波浪纹理（灰底篇）

灰底 `.slide` 背景叠一层 SVG 波浪（`background-image` 内联 data-uri，`fill-opacity` 0.07–0.08，贴底 `background-position:bottom`，`background-size:100% 50%`）。模板里已内置，见 `assets/deck-template.html`。

## 黑底光晕（设计点篇）

黑底 `#06060a`，底部叠 `radial-gradient` 双色光斑（`mix-blend-mode:screen`）+ 一条连续白色亮带；标题用 `-webkit-background-clip:text` 的渐变字。可做"调色面板 + 一章一色"（`data-chapter` + inline `--glow-*` 变量），进阶用法见 `references/components.md` 与原 deck 的 glow 分册。
