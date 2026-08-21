from lxml import html

# XPath 基础语法：
# /               逐级选择直接子节点。
# //              在当前范围内选择任意层级的后代节点。
# .               表示当前节点，常与 .// 搭配以限定查询范围。
# [n]             选择第 n 个节点；XPath 的位置从 1 开始。
# [last()]        选择最后一个节点。
# [@attr]         选择具有 attr 属性的节点。
# [@attr='value'] 选择 attr 属性值等于 value 的节点。
# *               匹配任意名称的元素。
# @*              获取元素的所有属性。
# text()          获取元素的直接文本节点。

# 读取网页文件，并将 HTML 字符串解析成可使用 XPath 查询的节点对象。
with open("resources/xpath.html", "r", encoding="utf-8") as f:
    html_text = f.read()
    document = html.fromstring(html_text)

    # / 从根节点开始逐级查找 table，再用 text() 获取所有 th 的文本。
    th_list = document.xpath("/html/body/main/section/table/thead/tr/th/text()")
    print(th_list)

    # // 在文档任意层级查找 table，后面的 / 仍表示选择直接子节点。
    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list)

    # [2] 选择每一行中的第 2 个 th；XPath 序号从 1 开始。
    th_list = document.xpath("//table/thead/tr/th[2]/text()")
    print(th_list)

    # [@class] 只选择具有 class 属性的 td 元素。
    td_list = document.xpath("//table/tbody/tr/td[@class]/text()")
    print(td_list)

    # * 是元素通配符，表示选择 tr 下所有名称的直接子元素。
    td_list = document.xpath("//table/tbody/tr/*/text()")
    print(td_list)

    # @href 获取 a 元素的 href 属性值。
    a_list = document.xpath("//a/@href")
    print(a_list)