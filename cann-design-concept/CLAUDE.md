# CANN DesignConcept · 项目说明

> Claude 自动加载本文件。**详细迭代过程见 `DESIGN-LOG.md`**（人读 / 提炼 skill 用，Claude 不自动读，需要时主动 Read）。

## 是什么
华为 **CANN 2026 设计概念汇报 PPT**，单/多文件 HTML **纵向 scroll-snap 整页翻页** deck（带概览/全屏交互），由 UCD CENTER 出品。独立于 `cann-research-ppt`（不进总览聚合页）。仓库 `SchihHsin/materials`，Pages 路径 `…/materials/cann-design-concept/<file>.html`。

## 文件
- **`index.html` 合并版完整 deck（22 页）= 封面 + gray 15 页 + glow 6 页**，统一翻页/导航/字体/字号。⚠️ **由 `build_index.py` 从三个分册自动拼装，不要手改 index.html**——改内容改分册再 `python3 build_index.py` 重生成
- `build_index.py` 拼装脚本：逐块 verbatim 抽取三分册的 CSS/slide/script → 把各册 `.slide` 作用域化（`.slide.s-gray` / `.slide.s-glow`，避免黑/灰底互相覆盖）→ 全局换 HarmonyOS Sans + 套字号 token → 合成单文件单 `#deck`/单当前页机制/单 nav；glow 调色面板逻辑保留但对非 glow 页惰性（`curChap()` 判 `data-chapter`）
- `gray2.html` 灰底 **Pattern 扩展分册**（新建）：与 gray 同基底（字号 ramp / 渐变 token / 玻璃卡 / 灰底波浪 / 横向翻页 + nav），只留封面 + 空白 pattern 起始页，供继续沉淀新分析型 pattern；`<style>`/`<script>` 末尾有注释标好新 pattern 的写入位（JS 类 pattern 并入 index 时记得同步 build_index.py 硬编码脚本）

## 翻页机制（2026-06）：纵向 scroll-snap（对齐参考 demo）
**已从横向 `translateX` 受控翻页改为纵向原生 `scroll-snap`**，`index.html`（build_index.py 统一层）与 skill 模板 `assets/deck-template.html` 同步。
- `body` 作滚动容器（`overflow:hidden auto`+`scroll-snap-type:y mandatory`），`#deck{display:block}`，`.slide{height:100vh;scroll-snap-align:start;scroll-snap-stop:always}`——划时短暂两页、松手吸附整页（不再拦截滚轮）。⚠️ 各分册自带的横向 `#deck{display:flex}` 和 `html,body{overflow:hidden;height:100%}` **必须被统一层显式盖掉**，否则横排/snap 失效。
- 当前页由 **`IntersectionObserver`（≥55%）** 判；`go()`/键盘/导航点走 `scrollIntoView`。键盘 `↑↓←→`/空格/PageUp-Down/Home/End + `O` 概览 / `F` 全屏 / `Esc` 退概览。
- **翻页过渡可切换 · 5 种**（2026-06，build_index.py + skill deck-template 同步）：脚本顶 `const TRANSITION=(URLSearchParams 取 't')||'slide'` + `CTRL=TRANSITION!=='slide'`。**`slide`(默认 scroll-snap) / `fade` / `cut`(瞬切) / `slide-h`(横向) / `magic`(神奇移动)**；**地址加 `?t=fade|cut|slide-h|magic` 即可临时切换不改代码**。非 slide 都走「受控叠层」`body.ctrl`（各页 `position:absolute` 叠一起、只 `.active` 显示、`.leaving` 退出页），每种动画用 `body[data-transition=X]` CSS（fade/cut/slide-h）；**magic = Keynote 神奇移动**：相邻两页 `data-key` 相同的元素 FLIP 位移缩放（**用 Web Animations API `el.animate`，别用同帧 transition+改值/void offsetWidth，不触发动画**），其余交叉淡化，没标 `data-key` 的页退化成淡入。⚠️ **IO 仅 slide 挂**、受控自己拦滚轮节流(620ms)、`go()`→`showSlide(i,dir)`；概览要 `body.overview.ctrl` 盖掉叠层。slide 模式一切照旧。
- 右侧竖排 `.nav-dots` + 底部居中 `#controls`（**小/透/默认隐藏**，`body.on-dark` 自适应）。**无顶部进度条**。⚠️ **显隐分区独立、离开即淡出**（2026-06 改）：`mousemove` 里 `controls.classList.toggle('show',clientY>innerHeight-120)` + `navDots.classList.toggle('show',clientX>innerWidth-120)`——移到底部出底部栏、移到右侧出右侧点，互不绑定；`mouseleave` 一并隐藏。**别用 2.5s 定时器**（会残留、且把两栏绑死）。
- **滚动条**（2026-06）：细、半透、**默认隐藏，滚动时才淡入**（`body.scrolling` 类，停 700ms 淡出）；亮/暗随 `body.on-dark`。⚠️ **滚动监听必须挂 body**（`html` 设 `overflow-y:visible`、body 才是滚动容器，事件在 body 上不在 window）+ `wheel` 兜底。
- **灰底页标题前不放 CANN logo**（2026-06 用户要求）：gray.html 各页 `.brand` 只留 `.ttl`；封面 logo 保留。
- **概览**：每页 children 包进 `.slide-inner`（按基调重建内部 flex/padding，否则 `flex:1` 失父塌成一团）→ `#deck` 变 grid 3 列；缩略框**按当前视窗比例**缩放（**不强制 16:9**——窗口非 16:9 时强制 16:9 必然裁边或留缝；且 `aspect-ratio:16/9` 在带 `height:100vh` 的 `.slide` 上失效）。`body.overview #panel,#toggle{display:none!important}` 藏调色入口。
- **全屏**：Fullscreen API，进入后图标切「退出全屏」；监听 `fullscreenchange`/`resize` → `scrollIntoView` 重新吸附当前页（修复改窗口后停两页之间）；`scrollRestoration='manual'`+进场 `scrollTo(0,0)`。
- **组件迁移必须作用域化（2026-07 事故记录）**：从 synthesis 迁移 #17/#18 时，推导页后置样式裸写了 `.dh/.dh b/.dh span`，撞上 #12「数据突出卡」已经使用的 `.dh` 网格类，导致三张数据卡变形。修法是把推导页样式全部收进 `.derive .dh...`，不是给数据卡继续补丁。以后新增/迁移组件时，凡 `.dh`、`.card`、`.head`、`.tag`、`.item` 这类通用短类名，必须挂在页面根类或组件根类下；后置 `<style>` 写完要 `rg` 检查是否有裸选择器污染旧页。
- `cover.html` 封面（分册源）：2.5D 芯片背景图 `reference/cover-bg.png` + logo/标题
- `glow.html` 黑底光晕设计点（分册源，章节调色面板）
- `gray.html` 灰底分析篇（分册源）；**2026-06 新增 3 个 pattern**（接在原 7 页后）：
  - **评分热力矩阵**（参考 `reference/mattrix.html` 逐字复刻）：`.hm-grid` 网格 + JS 渲染（`#cann-matrix`，配色/表情脸/趋势/状态点函数照抄参考）；格子极淡底 `rgba(色,.05)` + 彩色描边 + 数字按分档红/橙/绿/青/蓝 + 行首状态点。⚠️ **渲染 JS 同时写在 gray.html 脚本 和 build_index.py 硬编码脚本两处**（build 不抽取分册 script）。外层包一张 `.card` 玻璃卡。
  - **分层架构图**（参考 `reference/层级架构图.jpg`）：左竖排分层标签 + 每层若干**聚类玻璃卡**（一卡=一类、含多条目，非一条一卡）；卡高 `grid-auto-rows:auto` 自适应；范式层 mini 条目带**黑线 icon + 下方彩色光晕**（`.arc-pic::after`）。
  - **数据突出卡**（参考 `reference/data.png`）：3 张**切角方卡**（`clip-path` 切右上+左下、`aspect-ratio:1`）；⚠️ **单层玻璃**（`backdrop-filter` 直接采样背景纹理）——**别用"外层白底+内层玻璃"双层**，否则内层 backdrop 采到外层白底→发实；描边用 `::after`+`mask-composite:exclude` **只画边框环**（内部透明不加实度）；图标扁平、数字 Inter 500、小描述沉右下。
- `gray.html` 页序（2026-06，**三个用户画像连排**，共 15 页）：01 用户旅程 / 02 VOC 墙 / 03 用户研究(胶囊) / **04 画像·形式一 / 05 画像·形式二 / 06 画像·形式三** / 07 竞品对照 / 08 实施路线(甘特) / 09 能力矩阵(热力) / 10 体验架构(分层) / 11 设计目标(数据卡) / 12 用户旅程地图(复刻 Heart-of-the-Customer：人物头带+阶段chevron+Actions+Metrics大数字+情绪曲线渐变填充气泡+Functional Needs，`.cj-*`，全幅白底无 deck head) / 13 机会矩阵D / 14 干系人地图(左右版) / 15 时间分布(sm2 样板页)。head-r 与 foot 均已按此重编号
- ⚠️ **干系人地图只留左右布局版（左文案+右生态图 SVG）**：同心圆版（曾为页 13）内容与左右版基本重复，已删除，不要再加回来
- **左上角小标题(subttl) 按 4 章重新定义**（2026-06，kicker 部分 = 章节英文名，「·」后细节文字不变）：**User Research**（用户旅程/VOC/用户研究指标/三个用户画像/用户旅程地图/时间分布）/ **Competitive & Capability Analysis**（竞品对照/能力矩阵）/ **Implementation Planning**（实施路线甘特）/ **Design Strategy**（体验架构/设计目标/机会矩阵D/干系人地图）。⚠️ 不要再起「生态与干系人」这个第 5 章——干系人地图并入 Design Strategy 即可

## 字体与字号规范（index.html，写 skill 用）
- **主字体 = HarmonyOS Sans SC（鸿蒙黑体）**，CDN @font-face `cdn.jsdelivr.net/gh/IKKI2000/harmonyos-fonts@master/css/harmonyos_sans_sc.css`（MIT，权重 100/300/400/500/700/900）；字体栈 `'HarmonyOS Sans SC','Inter','Noto Sans SC'`（Latin 回退 Inter）；**JetBrains Mono 仅保留给英文 kicker/meta/页码等刻意等宽标签**
- **字号 token（`:root`，响应式 clamp）**：`--fs-h1` 页面主标题 clamp(20,1.7vw,30) / `--fs-h2` 区块标题 clamp(15,1.15vw,21) / `--fs-h3` 卡片小标题 **clamp(14,1.05vw,17)** / `--fs-body` 正文 **clamp(13.5,1vw,16)**（舒适阅读档，1440≈14.4px，跟竞品 desc/机会矩阵左栏一个量级）/ `--fs-sm` 次要正文 clamp(10.5,.72vw,13) / `--fs-xs` 标签/注释/页码 clamp(9,.62vw,11)
- ⚠️ **`--fs-body` 2026-06 从 clamp(12,.82vw,15) 提到 clamp(13.5,1vw,16)**（原来太小、新增页正文都偏小）；**`--fs-h3` 同步上调**保证 h3≥body（卡片小标题不能比正文小，这俩一起挪）。**用户画像 `.pf/.pp/.up` 根容器局部把 body/h3 冻回旧紧凑档**（`clamp(12,.82vw,15)`/`clamp(13,.95vw,16)`）——画像是高密度特殊形式、保持原样不被全局放大波及；**别再拿画像当正文基准**
- **落地**：在「统一层」（拼装后置于各册 CSS 之后）用 `!important` 把跨页通用角色绑到 token——`.brand .ttl`→h1、`.subttl`→sm、`.head-r`/`.kicker`/`.chrome`/`.cmp-cap`→xs、`.body`→body、`.point .pt-title`→h3、`.pt-desc`→sm；**超大展示数字（封面 CANN、大百分比、章节序号、glow 渐变章节标题）属 bespoke 不进 ramp**
- **用户画像两页已全量上 ramp**（`gray.html` 源里 `.pf-*`/`.pp-*` 共 34 处 font-size 已改 `var(--fs-*)`）：人名(`.pf-sb.head .nm`)→h2，**角色行(`.pf-sb.head .rl`「Senior Operator Engineer·内源团队」)→body**（规范前人名≈18px·角色≈11.5px，故人名落 h2≈16.6、角色落 body≈12 最贴近原始主次；中间试过 sm 偏小、h2 与人名同大显怪，最终 body），区块标题/环形%/统计数字→h3，正文(职责/原声/痛点/场景/期待)→body，标签/小标题/流程标题→sm，字段标签/KPI标签/分段标签→xs。⚠️ 字号 token **也写进了 `gray.html` 自己的 `:root`**（standalone 也能用），build 时统一层再覆盖一遍
- ⚠️ **`gray.html` 的字号 token 必须保留**：删了会导致 `.pf-*`/`.pp-*` 的 `var(--fs-*)` 失效
- `covers.html` 封面三程序化方案备选
- **`assets/` deck 实际用到的素材（进 git，Pages 才有图）**：`CANNlogo.png`（浅底 logo）、`cann-dark-logo.svg`（深底/封面白版 logo）、`cover-bg.png`、竞品截图 `cmp-*.jpg`、`av/*.svg`（DiceBear notionists 头像，CC0）。⚠️ **deck 引用一律走 `assets/…`**，不要再写 `reference/…`
- **`reference/` 源素材（⛔ 不进 git，已 gitignore，只存本地）**：含华为/第三方版权图（`Persona.svg/jpg` 画像模板、`VOC.jpg`、`workflow-plan-gantt(1).html`、`cann-journey-compare.html` 等参考件）。要新用某个素材时，先 `cp reference/X assets/X` 再在 deck 里引用
- `lib/` 内联图表库：`echarts.min.js`（Apache-2.0）、`apexcharts.min.js`（MIT）

## 三基调（写 skill 的核心规则）
- **封面**：大图作底 + CANN logo（文字版 `C`+红`A`+`NN`）+ DesignConcept 2026 + HUAWEI（左上）+ UCD CENTER（左下）
- **灰底 = 前瞻性设计 / 分析**：冷灰 + **玻璃折射白卡** + 底部**大波浪**纹理 + 蓝紫 accent
- **纯黑底 = 问题 / 研究 / 设计点**：黑主体 + 底部**渐变光晕** + 渐变标题字，**一章一色**

## glow.html 关键
- **章节模型**：颜色按章定（`data-chapter`），每章 = 1 封面 + **2 设计点**；取当前章用 **`cur()`**（⚠️ 不是 `curCh`，曾因笔误致面板打不开）
- **设计点（CANN 工具）**：第一章 控制与可观测 = 1.1 控制流可视化 / 1.2 智能错误诊断；第二章 开发提效 = 2.1 算子开发向导 / 2.2 交互式文档+成长地图
- **设计点页两种版式**（2026-06，图统一 **真 16:9** 匹配 1920×1080，**不裁图**；原 16:10 会裁）：**①左文右图**（默认，`.inner` 列 `0.5fr 1.5fr`+gap `2vw`，图~65%；`.h-title` 压到 `min(3.5vw,6vh)` 防标题折行，含 kicker+标题+正文+3 要点）——1.1/1.2/2.2 用；**②上下堆叠 hero 大图型**（`.inner.stack`：`.stack-head` 只 title+body 一条、**⛔无 kicker（与左上 .chrome 重复）⛔无要点**，16:9 大图 `height:100%;width:auto;margin:0 auto` 填高居中~78%）——2.1 用作样板。`.shot` 支持真 `<img>`。⚠️ **别为放大把堆叠框拉成宽幅裁 16:9**（踩过被否，几何上 16:9+文字最多并排~60%/堆叠~78%）。skill components.md §8 收两套骨架
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

## 用户画像三形式（gray.html 第 04/05/06 页，连排）
- **形式一**（`.pf` 前缀，蓝 `--b:#385CFF`）：仿 `reference/Persona.svg`，左 23% 人物栏（portrait + head/标签/职责/原声）+ 右四区（岗位特征 conic 环 | 上下游协同 flow+交付物 KPI / 典型业务场景 16:9 mockup×4 / 核心痛点）。**适用：正式深描单个核心角色**
- **形式二**（`.pp` 前缀，橙 `--o:#E8533B` 扁平）：仿 `reference/Persona.jpg`(AscendC)，顶栏 pp-top（人物/环形/期待 等距）+ 三栏（含 ECharts 雷达 内源蓝/生态红）。**适用：多角色能力维度对比**
- **形式三**（`.up` 前缀，紫栏 `linear-gradient(160deg,#6366D8,#8268E2)`）：复刻 `reference/Snipaste persona`，左紫栏档案（头像 7/5 横幅 + 信息字段 + 简介 + 特征标签便利贴）+ 右便利贴墙网格（性格滑杆/动机进度条/目标·痛点便利贴/技术圆点/兴趣胶囊 + 通栏 问题·解法）。**适用：工作坊/共创/白板式速写单人全貌**。⚠️ 等高/高屏坑：`.up` 用 `flex:0 1 auto`+顶对齐（别 flex:1 填满，4K 会注水、便利贴被拉爆）；右栏 `.up-grid` 行用 `1fr auto`（别 `1.3fr .82fr`，高屏会错位）；特征标签 `.up-notes` 用 `flex:1` 2×2 网格作弹性区吸高度差、便利贴别设固定 min-height。**调对齐用无头 Chrome 截图+getBoundingClientRect 实测，别猜**
- 三形式选用 & 触发词见 skill `references/components.md §6a/§6b/§6c`（已同步三处）
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
- **⛔ 不用 emoji，一律用线性描边 icon**（Lucide/Feather 风格：`fill=none;stroke=currentColor;stroke-width≈1.6–2;round`，跟随文字色）——emoji 随系统变样、彩色破坏冷灰+蓝紫调性、不专业；情绪/表情用线性脸（参考评分热力矩阵 `face(s)`）。**唯一例外：用户旅程「情绪曲线」可用 emoji 表情脸**（😐😕😤…，表达情绪起伏更传神）。已写进 skill SKILL.md 铁律
- **材料可见文案不口语化**：用书面/专业语（跑→运行、拍板→裁定、找→获取、兜底→后备……）；对话回复不受限
- 偏好：**多步任务一次做完不打断**；**改完 push**；**改 deck 记得连带改 skill + README + 本 CLAUDE.md**

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
