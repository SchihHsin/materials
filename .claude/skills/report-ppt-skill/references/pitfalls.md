# 踩坑清单（都是实战翻车后总结的）

## 布局间距

- **瀑布墙别用 flex 列**：flex 列高度互相推挤、`margin-top:auto` 会吸收剩余空间导致诡异间距 → 多卡不等高墙用 **`column-count:N` + 卡片统一 `margin-bottom`**（卡片加 `break-inside:avoid`）。
- **绝对定位子元素无视父 padding**：给绝对定位内容留内边距时，父元素的 `padding` 不生效 → 加一层 `position:absolute;inset:6vh 5vw...` 的**内层容器**来撑出留白（甘特白卡的 `.rm-pad` 就是这么做的）。
- **`min-content≈0` 导致 flex 行被压扁**：行内全是绝对定位子元素时，该行 min-content 约等于 0，会被 flex 压没 → 显式 `height` + `flex-shrink:0` 锁高（情绪曲线行的教训）。
- **`gap` 本身是对称的**：flex/grid `gap` 在所有相邻项之间相等。若"看着上大下小"，多半是**某个块自身内部留白**（如带背景的标题块、两行文字块的 padding/line-height）造成的视觉差，不是 gap 不对称——去收紧那个块的内边距，别去动 gap。
- 想"前几项等距、最后一项贴底"：前面用统一 `gap`，最后一项 `margin-top:auto`（它只吃多余空间，不影响前面的等距）。
- **`.foot` / `.ucd` 是绝对定位、不占垂直空间**：所以"居中型"页（内容是个居中块、四周留白，如数据卡/甘特/2×2 矩阵/sm2 图文/竞品对照）只靠 `justify-content:center` 会偏下，固定 `padding-bottom:4.2vh`/`1.5vh` 这类猜测值**在不同页眉高度、不同窗口宽高比下都对不上**（量出来有时 0px 有时偏几十 px）。**对策**：居中型页的 `.body-area` 加 `.vc` 标记，配合 JS `balanceHeads()`——**别拿页眉高度当 padding-bottom**（直觉上"页眉占空间所以要补页眉那么多"，试过，会系统性补过头：页眉的留白已经是它自己的 `margin-bottom`，不需要重复补）；正确做法是**直接量"页眉下沿→内容顶"和"内容底→页脚上沿"两个可见空白，让它们相等**——这两个空白之差是 padding 的线性函数（斜率 -1），所以一步算出 `newPad = 当前 padding-bottom + (topGap − botGap)` 即可，不用试错。"填满型"页（旅程/VOC/画像/竞品对照等本身占满整页、不需要居中补偿的）不要加 `.vc`。⚠️ 像 `.compare`+`.verdict` 这种 `flex:0 0 auto`（不撑满高度）的内容组，`.body-area` 本身也要有 `justify-content:center` 才能居中——光加 `.vc` 不够，模板的 `.body-area` 基类已带这条，自定义页别手滑去掉。

## 翻页 / 概览

- **总览页（按 O）悬浮缩略图显示页码**（好用的小功能）：纯 CSS counter——`body.overview #deck{counter-reset:slideno}` + `body.overview .slide{counter-increment:slideno}` + `body.overview .slide:hover::after{content:counter(slideno);position:absolute;bottom:7px;right:8px;...;opacity:0→1}`（默认隐藏、hover 浮出；`z-index` 要高于缩放的 `.slide-inner`，否则被盖住）。页码与翻页器一致、不用 JS。
- **`body.ctrl{overflow:hidden}`（受控叠层翻页模式 fade/cut/slide-h/magic）会一直锁住 body 滚动**：进总览 `enterOverview()` 只加了 `.overview` 类，没摘掉 `.ctrl`；如果总览缩略图网格高度超过一屏，`body.overview.ctrl` 这条规则必须**显式把 `overflow` 改回 `hidden auto`**，否则总览页在这几种翻页模式下会出现"滚不动、看不到后面的缩略图"——默认 `slide` 模式不受影响（body 本来就能滚），只有切到非默认翻页模式才会踩到，容易被漏测。

## 字号

- 别给每个组件随手写 px/vw → 全部走 6 档 ramp（见 `type-and-color.md`）。判断该用哪档：量"原始 px"落最近档。
- 同一元素改大小时，先想清楚它在层级里是"标题/正文/次要/标签"哪一类，对应到档位；别为了"大一点"直接跳两档（如角色副标题跳到和人名同档 h2 会显怪）。

## 头像 / 图片

- **DiceBear 开源头像**（notionists，CC0）替代手画简笔头像：`https://api.dicebear.com/9.x/notionists/svg?seed=X&beardProbability=0&backgroundColor=YYY`，`curl` 下载到本地。**必须带 `beardProbability=0`**，否则会出现"女生长胡子"。
- 头像 `backgroundColor` 要**跟随所在页底色**（橙页用暖底如 `FBEEE9`，别用绿底）。
- **不能生成 AI 图**：背景大图让用户给，或 `curl` 网图。
- 竞品/产品截图：`width:100%;height:auto` 不裁切 + 圆角 + 小 padding；三卡等高用 `align-items:stretch`，图 `order:2;margin-top:auto` 沉到卡底对齐。

## SVG

- **SVG 里的文字是矢量轮廓**，提取不出文字内容，只能拿到 rect/ellipse 布局。照着 SVG 模板复刻时，文案要另外问用户/自己写，别指望从 SVG 读。

## 内容

- **标题必须是结论**，不是栏目名。每页问自己"这页到底想说什么发现"，把那句话放标题；空泛词、过度否定的措辞都要改。

## 嵌入复用（iframe 嵌精调原件，别手搓重画）

> 背景：要把另一份**已精调好的报告/图表页**的内容搬进 deck 时，第一反应常是「照着重画一遍」——几乎必被打回：手搓版**内容更少、更丑**，还丢交互。正解是 **iframe 嵌原件 + 注入 `embedfix` 只露目标元素**。

- **判断顺序**：① 原报告/原图已有现成的 → iframe 嵌；② skill 有精调件 → 套；③ 都没有才手搓（且先提方案）。**别用 `var(--fs-*)` 自己拼组件去复刻别人已经做好的东西。**
- **embedfix 套路**：`cp` 原文件成副本 → 注入一段 `<style id="embedfix">`+`<script>`：读 URL 参数（`?sec=ID` / `?tp=ID` 等）→ 给 `<html>/<body>` 加 `.embed` 类隐藏 topnav/页脚/侧栏 → 沿目标元素的**祖先链**把所有旁支兄弟 `display:none`、只留这一条 DOM → 必要时 `removeAttribute('hidden')`+清 inline `display:none`（异步渲染的内容用 `setInterval` 重试）。deck 页 `.body-area` 里放 `<iframe src="副本.html?sec=...">`。⚠ 原文件改了，副本要**重新 cp + 注入**。⚠ 副本若比原文件深一级目录，**图片相对路径 `const IMG` 要改**（`../` → `../../`），否则截图全 404。
- **🔴 别让 iframe 先闪一下原始页（FOUC）**：embedfix 跑在 `setInterval` 里，原页会先整页渲染、几百 ms 后才被裁剪——中间露馅。修法：在 `<head>` 里（body 绘制前）同步给 `<html>` 加 `embed-wait` 类 + `html.embed-wait body{opacity:0}`，在 embedfix **首次成功**处 `classList.remove('embed-wait')` 淡入，并 `setTimeout(reveal,3000)` 兜底。⚠ 揭显**必须**挂在 embedfix 成功点，只靠兜底超时会黑屏数秒（比闪烁更糟）。
- **🔴 多 iframe 要懒加载**：deck 里几十个 iframe 一次性并发加载极慢。把 `src` 改 `data-src`，写 `lazyFrames(center)` 只给当前页及相邻 ±1 注入 `src`，在翻页函数 `updateCurrent(idx)` 里调用。相邻预载让顺序翻页时下一页已就绪。
- **鼠标在 iframe 上滚不动页**：deck 靠 `wheel` 翻页，但 wheel 被 iframe 吃掉不冒泡 → 每个 embed 末尾加脚本把 wheel `postMessage({__deckWheel:dy})` 给父页，父页监听后复用翻页逻辑（可做 edge-aware：iframe 内未到顶/底先滚自身，到边才翻页）。
- **嵌入页常见错位**：原页 `body` 若有 `padding-left`（TOC 侧栏留位）等，embedfix 要 `body.embed{padding:0!important}` 复位，否则内容整体偏右下。

## 缩放适配（fit-to-fit 的宽窄陷阱）

- **🔴「内容变窄 / 变小」先查 `fit()` 缩放**：常见写法 `if(fh>vh) transform:scale((vh)/fh)` 把楼层「缩到刚好装下高度」，配 `transform-origin:top center` → **整体等比缩小并水平居中 → 两侧留缝、内容变窄**（视口越矮缩得越狠）。对**宽幅内容**（横向 grid、宽表、并排卡）这是错的：宁可**铺满宽度**（矮了底部留白没关系），也别为塞高度而缩小变窄 → 给这类楼层的缩放加 `id!=='宽幅页'` 排除，或改成只按宽度适配。
- **嵌入/内容应与题目同宽 + 上下居中**：正文（iframe 或卡片）要**和大标题左对齐、和右上角页码小字右对齐**（即与 `.head` 同宽，把容器 padding 归 0），并垂直居中（容器 `display:flex;flex-direction:column;justify-content:center;height:100vh`）。常见毛病：内容比题目窄、且顶对齐「太靠上」。

## CSS grid 易踩

- **🔴 百分比列 + `gap` 会溢出被裁**：`grid-template-columns:64% 36%` + `column-gap:18px` = 100%+18px，超出容器、右侧内容溢出被父级 `overflow:hidden`（如 iframe）裁掉（**圆角被切**就是这症状）→ **百分比改 `fr` 单位**（`64fr 36fr`，fr 自动扣掉 gap、不溢出）。记住：卡片右边/圆角被切先查是不是「百分比+gap 溢出」。
- **🔴 `display:grid!important` 会顶掉 JS 给兄弟设的 inline `display:none`**：若用 `.card{display:grid!important}` 广谱命中，被 JS 隐藏的相邻卡会一起冒出来 → grid（及任何 `display:…!important`）只 scope 到**目标元素的专属类**（如 `.xxx.solo`），别落到广谱选择器。
- **左栏两卡被右侧高卡撑开、间距忽大忽小**：A 在 row2、B 在 row3、右侧 C 跨 row2/4 时，C 比左栏高 → 多出的高度被等分进 row2/row3，把 A、B 推开 → 用一个 flex 容器把左栏两卡**裹成一列**（固定 gap），空隙只留到底部。
- **同行卡片 demo 顶部对不齐**：题目/描述长短不一会让下方 demo 起始高度参差 → 内容**顶部对齐**（`justify-content:flex-start`）+ 给题目、描述设 `min-height`（统一占位），demo 顶部就齐了；别用 `justify-content:center`（会让序号/标题上下参差）。

## 配色 / 视觉主次

- **🔴 满屏单一 accent = AI 味重**：6 张卡的标签、icon、强调字全是同一个蓝紫 → 颜色多、没主次。**铁律：装饰性元素（类别标签、icon、出处）用中性灰，颜色只留给「有含义」的功能元素**（如 依据/做法/指标 三类标签各一色）。这样颜色都承载意义、主次自然出来。
- **别用「左描边 accent 条」的卡片**（左边一条竖色条）——很套路、AI 味重。改用 **1px 整框 + 柔阴影**，或 **白底 + 角落径向光晕**（`background:radial-gradient(125% 95% at 0% 0%, rgba(accent,.2), transparent 52%), #fff`，光晕做背景层、文字自然浮在上、无 z-index 问题）。
- **同一页卡片统一用透白玻璃卡**（`rgba(255,255,255,.55)`+`backdrop-filter:blur(15px) saturate(1.4)`+白边+柔阴影+inset 高光），别一处玻璃一处实底。
- **小图形直接画在玻璃卡上**，别再给它套个白底小框（卡片本身就是底）。
- **不常见的专业词换成常见的**：专业没问题，但「结构性缺口」这种不常见、观众反应不过来 → 换「系统性短板」等常见说法；术语（canonical 等）配中文通用译法 +（英文）。

## 配图（别生搬通用 icon）

- **「太多文字、不好读」的页**：拆成**左文字 + 右 demo/示意**，文字密度立降。demo 用**内容相关的小 mockup**：浏览器框（`正文 0 字`/`404`）、版本号徽章列、`原因：N/A` 兜底页、平台覆盖对照（红✕/绿✓ 芯片）、清单（☑ + 指标映射）、渠道/公式图、下降柱、尖峰线…——比堆文字直观得多。
- **概念页配图，别放通用线性 icon**（用户会说「只是个 icon，我以为有图」）：画**真·小 SVG 概念图**——对照=天平、价值链=漏斗、检索=放大镜→文档、知识 gap=时间轴、多渠道=三路汇一、可复现=循环↻+✓。一眼说明这页在讲什么。
- icon 当**淡水印**（`opacity:.06`、放大铺角落、`z-index:0` 压文字下层）也行，但那是「装饰」不是「配图」；用户要 demo 时别用水印糊弄。

## 合并 / 工具

- `build_index.py` 用**标记抽取**不要硬编码行号（源文件一加 `:root` 行就全错位）。
- 多分册脚本合并时只留一份 `go()`/nav；各册专属脚本对不属于它的页要惰性跳过。
- cwd 漂移：`open xxx.html` 在子目录里跑会找不到文件 → 用绝对路径或先 `cd` 到项目根。
- 中文替换用 Read+Edit 或 Python，别用 `perl -CSD`（曾匹配不到中文）。
