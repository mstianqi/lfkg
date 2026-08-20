from lxml import html

with open("resources/test.html", "r", encoding="utf-8") as f:
    html_text = f.read()
    document = html.fromstring(html_text)

    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list)