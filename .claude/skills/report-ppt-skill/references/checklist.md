# 交付前质检清单（Checklist · 每页必跑）

> 复用本 skill 最常翻车的不是"组件选错"，而是**生成出来要大量手调**：字太小、文字溢出、等高对不齐、卡片/气泡越界、左右对不齐。这些几乎都来自同几个**结构性疏忽**。本清单按"每页过一遍"设计，配 `rg` / 无头截图自查。**交付前对每一页逐条过；发现问题先按本表的"正确做法"改，别靠肉眼微调凑。**

---

## A. 字号（最高频翻车点）
- [ ] **正文一律 `var(--fs-body)`**；`--fs-sm`/`--fs-xs` **只**给次要说明 / 标签 / 注释 / 页码，**绝不当正文**。
  - `rg -n 'font-size:\s*(max|clamp)\(' index.html` —— 有没有**手写小 px**（应只引 token，别 `max(11px,.8vw)` 这种）
  - "整页字都很小" → 十有八九是正文误用了 sm/xs，或**照抄了高密度件（画像/旅程）的局部小字**到了普通页
- [ ] 浏览器 100% 缩放、1440 宽下，正文 / 卡片描述 / note / caption 都能**一眼读清**
- [ ] 高密度小字（画像 `.pf/.pp/.up` 的 12–15px）只在那几个特殊件局部，**没被推广到普通页**
- [ ] 内容多 → **删减文案 / 拆两页 / 换更稀疏版式**，**绝不缩字硬塞**

## B. 溢出 / 放不下（第二高频）
- [ ] 内容**没有顶破 slide**。无头截图量（>0 即溢出）：
  ```bash
  pkill -f "Google Chrome" 2>/dev/null; sleep 1   # 多实例会打架，先清
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; ud=$(mktemp -d)
  "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
    --user-data-dir="$ud" --window-size=1600,900 --virtual-time-budget=5000 \
    --screenshot=/tmp/p.png "file://$PWD/index.html#<N>"   # 看截图底部有没有被裁
  ```
- [ ] 信息块（列表 / 便利贴墙 / 卡片网格）给 **`max-height` + `overflow:hidden/auto` 兜底**——溢出时降级（裁 / 滚），而不是把整页挤变形
- [ ] **绝不**把内容裸塞进固定高度框再靠缩字塞下

## C. flex / grid 卫生（坑最隐蔽，本轮一半的问题来自这里）
- [ ] **所有 flex 列 / grid 子项默认带 `min-height:0`（横向再带 `min-width:0`）**——否则子元素不收缩、内容一多就撑破父容器溢出。"等高对不齐 / 紫卡比白卡高 / 气泡越界 / 文字被裁"几乎都是漏了这条。
  - `rg -n 'flex:1|display:grid' index.html | head` —— 逐个确认这些元素**及其祖先链**上有 `min-height:0`
- [ ] 等高布局靠 grid 默认 `align-items:stretch`；想让某一栏吸收高度差，**只给那一栏 `flex:1`、其余 `flex:0 0 auto`**，别多处抢 `flex:1`
- [ ] 整块**别用 `flex:1` 填满超高屏**（4K/竖屏会"注水"把内容拉散）→ 用 `flex:0 1 auto`（按内容、可压缩）+ 顶对齐或居中

## D. 对齐
- [ ] **不要双层 padding**：`.slide` 已带 `padding:5vh 4vw`；主体区**别再叠一层同方向 padding**，否则主体比页眉/页脚多缩一截、左右对不齐
- [ ] 页眉（章节小标题 + 大标题）、主体、页脚的左右边都对到**同一条边线**
- [ ] 绝对定位的子元素**无视父 padding** → 要内边距就加一层 `position:absolute;inset:…` 的内层容器

## E. 图片
- [ ] 图一律 **固定 `height`(vh) + `overflow:hidden` + `object-fit:cover`**（满铺）或 `contain`（完整显示）；**禁裸 `aspect-ratio`**——内容/比例一变会撑破布局
- [ ] 截图默认 `object-position:top`；文字讲的是页面中段模块，先 `sips` 裁出对应区段单独存图，别用整图

## F. 视口比例陷阱
- [ ] 慎用 `min(Xvw, Yvh)`：16:9 屏 1vw ≈ 1.78vh，`min(7vw,10vh)` 会被 10vh 截断、字缩水 ~20%。要等比就**单用 vw 或 clamp**，别 `min(vw,vh)` 混用
- [ ] 大标题字号别超屏宽导致每行一字；长标题**手工 `<br>` 断行**，别靠自动换行

## G. 测量代替猜（铁律）
- 任何"对不齐 / 太高 / 被裁"，**用无头 Chrome 截图 + `getBoundingClientRect()` 量像素**，别肉眼猜（详见 `pitfalls.md`）。注入一段在 load 后把目标元素 `top/bottom/height/scrollHeight` 写进 `position:fixed` 黑底绿字 div、截图读数即可；数字小用 PIL crop+resize 放大。多实例打架先 `pkill -f "Google Chrome"`。

---

> 一句话纪律：**填现成槽位、别手搓几何；放不下就删/拆，别缩字；每个 flex/grid 子项都 `min-height:0`；改完逐页跑本表。**
