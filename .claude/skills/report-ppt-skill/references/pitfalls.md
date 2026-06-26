# 踩坑清单（都是实战翻车后总结的）

## 布局间距

- **瀑布墙别用 flex 列**：flex 列高度互相推挤、`margin-top:auto` 会吸收剩余空间导致诡异间距 → 多卡不等高墙用 **`column-count:N` + 卡片统一 `margin-bottom`**（卡片加 `break-inside:avoid`）。
- **绝对定位子元素无视父 padding**：给绝对定位内容留内边距时，父元素的 `padding` 不生效 → 加一层 `position:absolute;inset:6vh 5vw...` 的**内层容器**来撑出留白（甘特白卡的 `.rm-pad` 就是这么做的）。
- **`min-content≈0` 导致 flex 行被压扁**：行内全是绝对定位子元素时，该行 min-content 约等于 0，会被 flex 压没 → 显式 `height` + `flex-shrink:0` 锁高（情绪曲线行的教训）。
- **`gap` 本身是对称的**：flex/grid `gap` 在所有相邻项之间相等。若"看着上大下小"，多半是**某个块自身内部留白**（如带背景的标题块、两行文字块的 padding/line-height）造成的视觉差，不是 gap 不对称——去收紧那个块的内边距，别去动 gap。
- 想"前几项等距、最后一项贴底"：前面用统一 `gap`，最后一项 `margin-top:auto`（它只吃多余空间，不影响前面的等距）。
- **`.foot` / `.ucd` 是绝对定位、不占垂直空间**：所以"居中型"页（内容是个居中块、四周留白，如数据卡/甘特/2×2 矩阵/sm2 图文/竞品对照）只靠 `justify-content:center` 会偏下，固定 `padding-bottom:4.2vh`/`1.5vh` 这类猜测值**在不同页眉高度、不同窗口宽高比下都对不上**（量出来有时 0px 有时偏几十 px）。**对策**：居中型页的 `.body-area` 加 `.vc` 标记，配合 JS `balanceHeads()`——**别拿页眉高度当 padding-bottom**（直觉上"页眉占空间所以要补页眉那么多"，试过，会系统性补过头：页眉的留白已经是它自己的 `margin-bottom`，不需要重复补）；正确做法是**直接量"页眉下沿→内容顶"和"内容底→页脚上沿"两个可见空白，让它们相等**——这两个空白之差是 padding 的线性函数（斜率 -1），所以一步算出 `newPad = 当前 padding-bottom + (topGap − botGap)` 即可，不用试错。"填满型"页（旅程/VOC/画像/竞品对照等本身占满整页、不需要居中补偿的）不要加 `.vc`。⚠️ 像 `.compare`+`.verdict` 这种 `flex:0 0 auto`（不撑满高度）的内容组，`.body-area` 本身也要有 `justify-content:center` 才能居中——光加 `.vc` 不够，模板的 `.body-area` 基类已带这条，自定义页别手滑去掉。

## 翻页 / 概览

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

## 合并 / 工具

- `build_index.py` 用**标记抽取**不要硬编码行号（源文件一加 `:root` 行就全错位）。
- 多分册脚本合并时只留一份 `go()`/nav；各册专属脚本对不属于它的页要惰性跳过。
- cwd 漂移：`open xxx.html` 在子目录里跑会找不到文件 → 用绝对路径或先 `cd` 到项目根。
- 中文替换用 Read+Edit 或 Python，别用 `perl -CSD`（曾匹配不到中文）。
