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
  --fs-h2:clamp(15px,1.15vw,21px);  /* 区块标题 / 人名 */
  --fs-h3:clamp(13px,.95vw,16px);   /* 卡片小标题 / 中小号数字 */
  --fs-body:clamp(12px,.82vw,15px); /* 正文 */
  --fs-sm:clamp(10.5px,.72vw,13px); /* 次要正文 / 说明 */
  --fs-xs:clamp(9px,.62vw,11px);    /* 标签 / 注释 / 页码 */
}
```

**用法**：所有文字只引用 `var(--fs-*)`，不要再手写 px/vw。
**例外（bespoke 不进 ramp）**：封面超大 logo/标题、大百分比指标数字、章节序号、黑底渐变章节标题——这些是"展示数字"，按视觉单独定。

角色映射参考（来自实战）：页面标题→h1；区块标题/人名→h2；卡片标题/环形%/统计数字→h3；正文/职责/痛点/场景→body；角色行/标签/小标题→sm；字段标签/KPI 标签/页码→xs。

> 经验：一个元素该用哪档，先量它"规范前的原始 px"，落到最近的一档即可（如原 ≈11.5px → body≈12；原 ≈18px → h2≈16.6）。

## 渐变色彩系统

```css
:root{
  /* 基础冷灰主题（灰底分析篇）*/
  --paper:#E9EBEE; --card:#fff; --card-2:#F1F3F6;
  --ink:#16191e; --ink-2:#5e646e; --ink-3:#929aa6; --line:#d4d8df;
  --accent:#5B5BD6; --accent-soft:#ECECFB; --red:#E60012;

  /* 分类 / 状态渐变（120deg）*/
  --g-red:    linear-gradient(120deg,#FF5A6E,#FF6F55);  /* 状态红：同明度微色相位移 */
  --g-green:  linear-gradient(120deg,#23CFA0,#45D65A);  /* 状态绿：同明度微色相位移 */
  --g-blue:   linear-gradient(120deg,#667EEA,#764BA2);
  --g-amber:  linear-gradient(120deg,#FBBF60,#F59E0B);
  --g-purple: linear-gradient(120deg,#A78BFA,#7C3AED);
  --g-teal:   linear-gradient(120deg,#38C9D7,#4FACFE);
  --g-pink:   linear-gradient(120deg,#FF6B9D,#FF8B53);
  --g-neutral:#C4CAD4;                                  /* 中性：纯色，不渐变 */

  --dark:     #16191E;                                  /* 统一深色（实色）*/
  --g-ink:    linear-gradient(140deg,#22262F,#14171C);  /* 统一深色（渐变）：所有深色大色块用它 */
  --g-accent: linear-gradient(135deg,#5B5BD6,#7C3AED);  /* 蓝紫主渐变 */
}
```

**规则**：
- 状态色（红/绿）= **同明度 + 微微色相位移** 的渐变，**不要**做深→浅明暗变化。
- 中性色用**纯色**，不渐变。
- 所有深色大色块（指标带 / 结论条 / 阶段头 / 高亮卡）统一引用 `var(--g-ink)`，不要各自定义深色。
- 重点文字高亮：`background:linear-gradient(transparent 60%,rgba(91,91,214,.16) 0)`（紫色下划高亮底）。

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
