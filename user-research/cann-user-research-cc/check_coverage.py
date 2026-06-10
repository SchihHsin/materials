#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_coverage.py — 逐条核对研究报告源文（doc.txt）的内容单元是否在 PPT（index.html）中有呈现。

用法:
    python3 check_coverage.py                          # 默认 doc.txt + index.html + ignore.txt
    python3 check_coverage.py doc.txt index.html -o coverage_report.md --ignore ignore.txt

豁免清单（ignore.txt）:
    每行一个片段，归一化后对内容单元做子串匹配，命中即跳过（计为「豁免」）。
    用于登记纯结构性标题（「第一部分」「2.1」等）与人工确认过的有意取舍，
    跑完一轮后把确认项补进清单，剩下的才是真缺口。

机制:
  1. 把 doc.txt 解析成「内容单元」：标题 / 表格行 / 列表项 / 引语 / 段落，
     ASCII 框图（``` 围栏内）剥掉制表符后同样按行解析——画像卡、干系人图、BP 详情都在里面。
  2. 提取 index.html 的可见文本（剥 <style>，保留 <script>——雷达图的中文标签在 JS 里）。
  3. 每个单元按标点切成子句，子句再切成 6-gram 字符片段做包含匹配（归一化：去空白/标点/全半角统一）。
     单元得分 = 各子句 gram 命中率均值 → ≥0.55 已呈现 / ≥0.25 部分呈现 / 其余 缺失。
  4. 关键数字（460、30-60、70%、5000、6.75、20.1% …）单独做精确比对。
  5. 输出 coverage_report.md（按源文章节分组），stdout 打印汇总；存在「缺失」时退出码为 1，
     方便外层循环「补内容 → 重跑」直到通过。

给 codex 的建议用法:
    循环执行本脚本，针对报告中【缺失】与【部分】条目，把对应内容补进 index.html
    （新增 slide 或扩充现有 slide 文案），直到退出码为 0 或剩余条目均为有意取舍并人工确认。
"""
import argparse, html, os, re, sys, unicodedata
from collections import OrderedDict

# ---------- 归一化 ----------
_PUNCS = r'[\s　，。、；：！？「」『』“”‘’（）()【】《》〈〉<>·…—\-—\|/\\.,;:!?\'"`~*#>\[\]＋+＝=～〜]'

def normalize(s: str) -> str:
    s = unicodedata.normalize('NFKC', s)
    s = re.sub(_PUNCS, '', s)
    s = s.lower()
    # 语义等价：3-5 倍 / 3-5x / 3-5× 视为同一写法
    return s.replace('倍', '×').replace('x', '×')

# ---------- HTML 可见文本 ----------
def html_text(path: str) -> str:
    raw = open(path, encoding='utf-8').read()
    raw = re.sub(r'<style\b.*?</style>', ' ', raw, flags=re.S | re.I)
    raw = re.sub(r'<!--.*?-->', ' ', raw, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', raw)
    return html.unescape(txt)

# ---------- doc 解析成内容单元 ----------
BOX_CHARS = '│┃┆┇┊┋╎╏┌┐└┘├┤┬┴┼─━═║╔╗╚╝╠╣╦╩╬▲▼▶◀➤＞•·‣箭▸'
SKIP_RE = re.compile(r'^[\s%s>\-=_*~`.#0-9┄┈]*$' % re.escape(BOX_CHARS))

def parse_units(path: str):
    """返回 [(section, line_no, unit_text)]"""
    units, section = [], '（开头）'
    in_fence = False
    for i, line in enumerate(open(path, encoding='utf-8'), 1):
        raw = line.rstrip('\n')
        if raw.strip().startswith('```'):
            in_fence = not in_fence
            continue
        s = raw
        if in_fence:                                # 框图：剥制表符后按普通行处理
            s = re.sub('[%s]' % re.escape(BOX_CHARS), ' ', s)
        s = s.strip()
        if not s or SKIP_RE.match(s):
            continue
        m = re.match(r'^(#{1,6})\s*(.+)$', s)
        if m and not in_fence:
            section = m.group(2).strip()
            units.append((section, i, m.group(2).strip()))
            continue
        if re.match(r'^\|[\s:\-|]+\|$', s):          # 表格分隔行
            continue
        if s.startswith('|'):                        # 表格行 → 各 cell 拼接
            cells = [c.strip(' *') for c in s.strip('|').split('|') if c.strip(' *-')]
            if cells:
                units.append((section, i, ' · '.join(cells)))
            continue
        s = re.sub(r'^[>\-•*\d.\s]+', '', s)         # 引语/列表/序号前缀
        s = s.replace('**', '').replace('<br>', ' ').replace('<br/>', ' ')
        s = re.sub(r'【|】', ' ', s)
        if len(normalize(s)) >= 6:
            units.append((section, i, s.strip()))
    # 去重（doc 里同一引语出现多次）
    seen, out = set(), []
    for sec, ln, t in units:
        k = normalize(t)
        if k in seen:
            continue
        seen.add(k)
        out.append((sec, ln, t))
    return out

# ---------- 匹配 ----------
def unit_score(text: str, hay: str) -> float:
    clauses = [c for c in re.split(r'[，。；：、！？,;:!?…]|<br\s*/?>', text) if len(normalize(c)) >= 5]
    if not clauses:
        n = normalize(text)
        return 1.0 if n and n in hay else 0.0
    scores = []
    for c in clauses:
        n = normalize(c)
        grams = [n[j:j + 6] for j in range(len(n) - 5)] or [n]
        hit = sum(1 for g in grams if g in hay)
        scores.append(hit / len(grams))
    return sum(scores) / len(scores)

NUM_RE = re.compile(r'\d+(?:\.\d+)?(?:[%×xX倍]|分钟|小时|天|周|个月|年|人|条|份|行|步|张)?')
KEY_NUMS = ['800k', '172', '155', '8小时', '6.75', '70%', '30-60', '460', '5000',
            '20.1%', '31/155', '3-5倍', '2000', '5%-10%', '100-500', '128k',
            '3-6个月', '2-3个月', '1-2周', '1-3天', '600-700', '54', '73', '26',
            '2万元', '24万元', '2周', '15天', '28t', '800w', '2-3小时',
            '1-2天', '2-4周', '1个月', '3个月', '15份', '18个', '15小时']

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('doc', nargs='?', default='doc.txt')
    ap.add_argument('html', nargs='?', default='index.html')
    ap.add_argument('-o', '--out', default='coverage_report.md')
    ap.add_argument('--ignore', default='ignore.txt',
                    help='豁免清单：每行一个归一化后做子串匹配的片段，# 开头为注释')
    a = ap.parse_args()

    ignores = []
    if os.path.exists(a.ignore):
        for line in open(a.ignore, encoding='utf-8'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            n = normalize(line)
            if n:
                ignores.append(n)

    hay = normalize(html_text(a.html))
    units = parse_units(a.doc)

    groups = OrderedDict()
    stats = {'已呈现': 0, '部分呈现': 0, '缺失': 0, '豁免': 0}
    for sec, ln, text in units:
        nt = normalize(text)
        if any(p in nt for p in ignores):
            stats['豁免'] += 1
            continue
        sc = unit_score(text, hay)
        verdict = '已呈现' if sc >= 0.55 else ('部分呈现' if sc >= 0.25 else '缺失')
        stats[verdict] += 1
        groups.setdefault(sec, []).append((verdict, sc, ln, text))

    # 关键数字
    num_rows = []
    for k in KEY_NUMS:
        num_rows.append((k, '✓' if normalize(k) in hay else '✗ 缺失'))

    total = sum(stats.values())
    judged = total - stats['豁免'] or 1
    with open(a.out, 'w', encoding='utf-8') as f:
        f.write('# 内容覆盖核对报告\n\n')
        f.write(f'源文 `{a.doc}` 共解析出 **{total}** 个内容单元（去重后），'
                f'其中 {stats["豁免"]} 个命中豁免清单 `{a.ignore}` 不计入核对。\n\n')
        f.write(f'| 已呈现 | 部分呈现 | 缺失 | 豁免 |\n|---|---|---|---|\n'
                f'| {stats["已呈现"]} ({stats["已呈现"]/judged:.0%}) '
                f'| {stats["部分呈现"]} ({stats["部分呈现"]/judged:.0%}) '
                f'| {stats["缺失"]} ({stats["缺失"]/judged:.0%}) '
                f'| {stats["豁免"]} |\n\n')
        f.write('## 关键数字核对\n\n| 数字 | 状态 |\n|---|---|\n')
        for k, v in num_rows:
            f.write(f'| {k} | {v} |\n')
        f.write('\n## 逐条明细（缺失 与 部分呈现 优先列出）\n\n')
        for sec, items in groups.items():
            bad = [it for it in items if it[0] != '已呈现']
            if not bad:
                continue
            f.write(f'### {sec}\n\n')
            for verdict, sc, ln, text in sorted(items, key=lambda x: x[1]):
                if verdict == '已呈现':
                    continue
                mark = '❌' if verdict == '缺失' else '⚠️'
                f.write(f'- {mark} **[{verdict} {sc:.2f}] L{ln}**：{text[:120]}\n')
            f.write('\n')
        f.write('## 已呈现章节（仅计数）\n\n')
        for sec, items in groups.items():
            ok = sum(1 for it in items if it[0] == '已呈现')
            f.write(f'- {sec}：{ok}/{len(items)}\n')

    missing_nums = sum(1 for _, v in num_rows if v.startswith('✗'))
    print(f'共 {total} 单元 → 已呈现 {stats["已呈现"]} · 部分 {stats["部分呈现"]} · 缺失 {stats["缺失"]}'
          f'；关键数字缺失 {missing_nums}/{len(KEY_NUMS)}')
    print(f'明细见 {a.out}')
    sys.exit(1 if (stats['缺失'] > 0 or missing_nums > 0) else 0)

if __name__ == '__main__':
    main()
