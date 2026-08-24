# Materials Workspace Rules

本文件是 `/Users/hsin/Documents/Coding/materials` 的根级交接说明。它在本仓库内优先约束工作方式；案例目录中的 `CLAUDE.md`、设计记录和具体 skill 文档继续提供更细的实现细节。修改任何文件前，先检查工作树，保留用户已有改动，不使用整体回滚或整体 `git add .`。

## 工作区定位

- `materials` 是报告类网页 PPT 的**创作、试验和验收入口**。先在这里的案例 deck、参考页面和实验页验证，再把确认可复用的内容发布出去。
- 当前最重要的案例是 `cann-design-concept/`：华为昇腾 CANN 2026 DesignConcept 汇报，由 UCD CENTER 出品，独立于 `cann-research-ppt`，不进入总览聚合页。
- `cann-design-concept/` 的详细项目说明在 `CLAUDE.md`，完整设计决策和时间线在 `DESIGN-LOG.md`；需要理解历史取舍时必须读取这两份文件，不要只看生成后的 `index.html`。
- 根目录的 `index.html` 是 materials 案例索引；各案例目录内的 HTML 是独立可打开的网页 deck 或预览页。

## Report PPT Skill 发布流程

- Develop and validate report-ppt-skill changes in `materials` case decks, reference pages, and experiments first.
- Commit and push approved `materials` case, reference, and workspace-rule changes in this repository.
- After validation, transfer reusable rules, templates, and assets to `/Users/hsin/Documents/Coding/report-ppt-skill/`.
- When a release change alters user-visible behavior, templates, components, or usage guidance, update `/Users/hsin/Documents/Coding/report-ppt-skill/README.md` in the same release. Keep its changelog and quick-start sections aligned with the published skill.
- Commit and push the release repository after each approved skill change.
- Do not create or edit project-level copies under `.claude/skills/report-ppt-skill` or `.agents/skills/report-ppt-skill`.
- The Claude and Codex user-level skill paths are links to the release repository; do not edit the links directly.
- Keep case-specific materials in this repository. Only move generalized, reusable content into the release skill.
- 固定顺序：`materials` 先改和验证 → 精确同步通用内容到发布仓 → 更新发布仓 README → 分别提交并 push。不要因为发布仓已有提交就覆盖或重置；先查看差异，再和现有内容合并。
- 发布仓和 materials 都可能有其他对话产生的未提交改动。提交时只 stage 本任务明确涉及的文件；不要因为“同步”而 add 或清理无关删除。

## CANN DesignConcept 文件边界

### 源文件与生成文件

- `cann-design-concept/cover.html`：封面分册源。
- `cann-design-concept/gray.html`：灰底分析分册源，包含用户研究、竞品、旅程、画像、roadmap、能力矩阵、架构、机会矩阵、干系人图、推导流、低密度页和卡片系统示例。
- `cann-design-concept/gray2.html`：灰底 Pattern 扩展分册脚手架。新增分析型 pattern 时可先在这里试验；若要并入完整 deck，必须同步 `build_index.py` 的抽取或硬编码逻辑。
- `cann-design-concept/glow.html`：黑底光晕设计点分册，含章节调色面板。
- `cann-design-concept/build_index.py`：把封面、gray、glow 分册拼成完整单文件 deck，并作用域化 `.s-gray` / `.s-glow`、统一字体字号和 runtime。
- `cann-design-concept/index.html`：**生成文件，不是内容源**。不要直接编辑；改分册后在该目录运行 `python3 build_index.py` 重生成。当前合成版包含封面、目录、灰底分析页、卡片/色彩 pattern 和 glow 设计点，实际页数以构建后的 `<section class="slide">` 计数为准。
- 运行构建前，确认源分册已经包含另一对话或用户刚完成的页面；不要用旧 blob 或旧 index 覆盖当前用户改动。曾经出现过构建后丢失卡片和色彩页的事故，修复方式是把缺失页面回填到 `gray.html` 源，而不是长期手改 index。

### 素材边界

- deck 运行时引用的素材放在 `cann-design-concept/assets/`，例如 `CANNlogo.png`、`cann-dark-logo.svg`、`cover-bg.png`、竞品截图和 `av/*.svg`；引用路径统一写 `assets/...`，不要写 `reference/...`。
- `cann-design-concept/reference/` 是本地源参考素材，通常被 gitignore，可能含第三方或版权图片。要在 deck 中使用，先复制到 `assets/` 并确认许可/来源；不要直接把 reference 路径发布到 Pages。
- 参考资料包括 Persona、VOC、用户旅程、甘特图、层级架构、data.png、竞品页面和封面图。它们用于复刻结构和视觉判断，不代表可以把版权素材直接交付。
- 当前环境可以用 `curl` 下载 Wikimedia 原图或 YouTube 缩略图（`img.youtube.com/vi/<id>/maxresdefault.jpg`）；不能假设可以生成 AI 照片或 3D 渲染图。封面最终采用用户外部生成的 2.5D 红色芯片与数据流光背景，保留 `covers.html` 的程序化备选方案。

## 案例叙事与视觉系统

### 项目和三种基调

- 主题是“CANN 开发者体验”的 2026 设计概念汇报：研究问题 → 竞品/能力差距 → 实施规划 → 设计策略 → 黑底设计点。
- **封面**：大图作底 + CANN logo + DesignConcept 2026 + HUAWEI / UCD CENTER。用户已确认正式封面可以使用现有报告式大图，不要额外加入“封面保持克制、没有真实素材不造叙事图形”的强制限制。
- **灰底分析篇**：冷灰 `#E9EBEE`、底部大波浪、玻璃折射白卡、蓝紫 accent，用于用户研究、VOC、用户旅程、画像、竞品、能力矩阵、roadmap、架构和机会分析。
- **黑底设计篇**：纯黑主体、底部连续渐变光晕、渐变标题字，一章一色，用于问题、方案和设计点；图像、界面或路径应成为叙事主角。
- 三基调不是装饰选择，而是阅读意图选择：灰底帮助读者读清分析，黑底帮助读者感受设计方案或体验路径。

### 叙事和文案

- 页面标题必须是该页主要发现、判断或设计结论的凝练，不写空泛导航词；例如“用户研究”应改成具体发现。
- 每章只承担一个主要问题；章节之间要有承接。正文区分**证据、基于证据的推论、待验证方案**，不能把猜测写成事实。
- 重要发现必须对应设计响应、用户收益、指标/依赖，或明确“不处理”的边界；设计点应能回指发现、目标或原则。
- 方案页优先使用“设计图/示意 → 3--4 个体验点 → 用户收益、验证方式或依赖”的句法。
- 材料中的可见文案使用书面、专业、易懂的表达：例如“跑”改为“运行”，“找”改为“获取”，“兜底”改为“后备”。对话解释不受此限制。
- 标题、目录和 Tab 的文案顺序要保持整份 deck 一致；目录只建立阅读路径，不提前写完整结论。

### 目录与章节 Tab

- 目录放在封面之后，左上只写“目录”，不要堆放项目名、年份或说明小字。
- 目录卡固定为“大章节号 → 中文名 → 英文辅助名 → 1--2 个内容锚点 → 一句章节职责”。
- 章节数路由：3 / 4 / 5 章单行横排；6 章用 3×2；7 章以上先合并章节或拆为主目录 + 附录目录，不能为了塞下而缩小卡片。
- 目录数字使用 `Barlow Condensed`，字重 `300`；不要擅自改成 Bold。
- 浅底内容页右上使用横向章节 Tab，列出整份汇报的主章节，当前章节用深色胶囊高亮。不要加 `chapter-position`、页码、年份或解释小字；封面和目录不放 Tab；黑底设计点保留自身 `.chrome`。
- 当前 CANN 案例的四章为：`01 用户研究`、`02 竞品与能力`、`03 实施规划`、`04 设计策略`。干系人地图归入 Design Strategy，不新增“生态与干系人”第五章。

## 版式、字体、颜色和组件规则

### 字体和字号

- 主字体为 HarmonyOS Sans SC（鸿蒙黑体），Latin 回退 Inter / Noto Sans SC；JetBrains Mono 只用于英文 kicker、meta、页码等刻意等宽标签。
- 六档字号 token：`--fs-h1` 页面标题、`--fs-h2` 区块标题、`--fs-h3` 卡片标题、`--fs-body` 正文、`--fs-sm` 次要说明、`--fs-xs` 标签/注释/页码。正文默认使用 `--fs-body`，不要用 sm/xs 伪装正文，也不要为了塞内容缩小正文。
- 当前基准：`h1 clamp(20px,1.7vw,30px)`、`h2 clamp(15px,1.15vw,21px)`、`h3 clamp(14px,1.05vw,17px)`、`body clamp(13.5px,1vw,16px)`、`sm clamp(10.5px,.72vw,13px)`、`xs clamp(9px,.62vw,11px)`。用户画像等高密度专属形式可在 `.pf/.pp/.up` 局部冻结为紧凑档，但不要推广到普通页。
- `gray.html` 自己的 `:root` 必须保留字号 token，否则 standalone 源分册中的画像和 pattern 会失效；build 统一层会再次覆盖跨页角色。
- 超大封面 logo、章节序号、展示百分比和 glow 渐变标题属于 bespoke，不强行纳入 ramp。

### 颜色、图标和通用卡片

- 小面积语义元素使用 `--c-*` 纯色，大面积色块和光晕使用 `--g-*` 同色相渐变；全局统一深色用 `--g-ink`，不要每页另造近似深色。
- 每页通常 1 个主色 + 不超过 2 个辅色；红/橙/黄表达风险或进行中，绿/薄荷表达机会或完成。靛/紫、红/玫红、绿/薄荷等相近色不要默认同墙并排。
- 禁止 emoji 和手写通用 SVG 图标，优先使用 Lucide 线性 icon；唯一例外是用户旅程情绪曲线可使用表情脸表达人的情绪变化。标题前默认不加装饰 icon，除非用户明确要求 logo。
- 卡内标签必须随内容收缩：`display:inline-flex`、`align-self:flex-start`、`width:fit-content`、`max-width:100%`、保留内边距和胶囊圆角。不能写 `width:100%` / `display:block`，不能让 `align-items:stretch` 把标签撑成整行色条；标签过长优先精简为 1--3 个词。
- 3 张同层级卡：按事实 / 重点 / 结论使用白玻璃 / 蓝紫主题 / 深色三层，不要三张同色白卡。
- 4 张及以上：默认透白玻璃卡，使用淡色光带、语义 icon 和 `--c-*` 标签区分，不做实色满铺；阅读组固定为标签 / 两行标题 / 三行说明三轨并整体居中。
- 任何新增组件都必须使用页面根类或组件根类作用域。`.dh`、`.card`、`.head`、`.tag`、`.item` 等短类名不能裸写；迁移后用 `rg` 检查后置 style 是否污染旧页。所有 flex/grid 子项默认加 `min-height:0`，横向子项再加 `min-width:0`。
- 不用 flex 列做瀑布墙，使用 `column-count`；绝对定位子元素若需要父 padding，增加 `inset` 内层容器；固定格式元素使用稳定尺寸、`aspect-ratio` 或明确 grid track。

### 组件选择和专属约定

- 先按内容路由到已有精调组件再自定义：指标胶囊、甘特 roadmap、VOC 声音墙、用户旅程、竞品对照、三种用户画像、同层级信息卡、生态干系人地图、2×2 机会矩阵、图+文、证据聚光灯、四栏推导流、目录页等都有对应骨架。
- 胶囊条和甘特浮动条是当前确认精调好看的手绘件；其它简单手绘件只能视为可显示示例，正式复用前重新检查层级、间距、可读性，不要把 demo 当成已定稿组件。复杂雷达、桑基、热力、关系树和大量散点才使用 `lib/` 中的 ApexCharts / ECharts。
- 用户旅程优先使用独立 `user-journey-skill`。每条情绪线按格绘制；相邻格公共边界 y 值必须严格相等，不要用“前中心 → 当前中心 → 后中心”拼断线。多条序列各自连续即可，不要求彼此同高。
- 用户画像三形式：形式一适合正式深描单一核心角色；形式二适合多人能力维度/雷达对比；形式三适合工作坊或白板式单人速写。不要把一种形式当成所有画像输入的默认模板。
- 竞品分析使用 Nsight / VTune / rocprof 等同类工具对比，不把 CANN 自家产品塞进竞品卡；图片优先保留完整证据和不裁切的产品截图，结论放图下或独立深色条。
- glow 设计点每章 1 个章节封面 + 2 个设计点；当前章节为控制与可观测、开发提效。调色按章而不是按页，面板嵌入章节封面、默认收起、图标常驻右上、面板向左展开；实现函数名是 `cur()`，不要改成曾经导致面板失效的 `curCh`。

## 信息密度模型（当前为框架，未完成标定）

- `cann-design-concept/density-model-basis.md` 是模型定义和理论依据。密度模型适用于文字、数据、字段和行动为主要阅读对象的分析页；分析图解和设计展示按图像阅读角色走 A/B 细分布局。
- 内容特征：`T` 文本负荷 = 必读字形面积 / 可阅读区域；`I` 元素交互性 = `(关系边数 / 关系节点数) × (1 + 跨组边数 / 关系边数)`；`C` 对照负荷 = `(同时比较对象数 × 共同字段数) / 可阅读区域面积`；候选页渲染后另算 `V` 视觉拥挤度。
- 训练集标准化使用 `X'=(X-median_train(X))/IQR_train(X)`；连续得分 `z=beta_0+beta_T*T'+beta_I*I'+beta_C*C'`，与 `theta_1..theta_3` 比较得到 D1--D4 概率。
- D1 = 结论叙事（1 主张 + 2--3 支撑）；D2 = 标准分析（1 判断 + 1 组证据）；D3 = 结构化分析（1 判断 + 3 信号 + 4 动作）；D4 = 查阅对照（多维字段、矩阵或固定结构）。A1--A3 是灰底分析视觉页，B1--B3 是黑底设计叙事页。
- 当前 `beta`、`theta`、训练集 median/IQR、置信阈值尚未标定，不能伪装成可直接计算的固定参数。`density-preview.html`、`density-calculator-preview.html`、`density-font-routing-preview.html` 等是评审字体层级、布局路由和计算框架的 demo；模型完成标注、拟合、交叉验证并发布带版本号参数文件后，才能接入自动生成。

## Runtime、验证和安全编辑

- 新 deck 从完整 runtime 起步，必须保留 `#controls`、`#navDots`、概览、全屏、键盘、URL 页码定位、scroll-snap 和当前页同步；不能用临时文字控制条替代。
- 默认翻页是 body 纵向 `scroll-snap`；可用 `?t=fade|cut|slide-h|magic` 临时切换过渡。非默认过渡使用受控叠层，概览必须覆盖叠层状态。
- 交付前至少做：`python3 build_index.py`（如改了源分册）、`git diff --check`、HTML 结构解析、关键 marker/section 计数、CSS 裸选择器搜索、无头浏览器或本地浏览器检查溢出与对齐。浏览器打不开 `file://` 时不要绕过安全策略，可用静态检查或在允许的本地服务器上验证。
- 当前工作树经常包含来自用户或其他对话的未提交修改、删除和新增实验文件。先 `git status --short`，再按文件逐一理解；只编辑任务范围内文件，绝不 `git reset --hard`、`git checkout --` 或整体清理。
- 修改生成 deck 时必须保留源文件中的用户页面，尤其是用户旅程、画像、卡片系统、颜色校验和密度预览；不要从历史 commit 直接覆盖当前文件。

## 当前案例交接快照

- 当前 CANN deck 的目录和章节 Tab 已在 `gray.html` 源中，合成到 `index.html`；目录位于封面后，当前四章单行展示。
- 当前卡片系统示例覆盖 3 张、4 张、5+ 张同层级卡片及色彩相近性校验；低内容量结论页和密度路由/字体预览也在案例目录中。
- 当前完整 deck 的源页数量会随实验变化，不能继续相信早期文档中的“22 页 / 15 页”静态说法；以 `python3 build_index.py` 和实际 `<section class="slide">` 计数为准。
- `CLAUDE.md` 和 `DESIGN-LOG.md` 中的历史说明仍有业务价值，但其中早期“横向翻页”“7 页”等描述属于演进记录；遇到冲突时，以当前源代码、`build_index.py` 和最新提交为实现事实，以设计记录解释为什么这样演进。

## 交付前清单

1. 明确这次改动是案例专属还是可复用 skill 规则。
2. 在 `materials` 源文件中实现，保留所有已有用户改动。
3. 重建并静态/视觉检查，确认目录、Tab、卡片、字体、密度和 runtime 没有回归。
4. 更新必要的 `CLAUDE.md` / `DESIGN-LOG.md` 或案例说明；可复用变化同步发布仓 `SKILL.md`、references、assets 和 README。
5. 精确 stage、提交、push materials；发布仓单独精确 stage、提交、push。
6. 最终说明改了哪些源文件、哪些生成文件、验证结果以及未能完成的检查；不要声称已 push 未实际成功的仓库。
