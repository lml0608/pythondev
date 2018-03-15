
from lxml import etree

html = etree.parse("helle.html")

# result = etree.tostring(html,pretty_print=True)
# print(result)

print(type(html))

#result = html.xpath('//li')

# print(result)
#
# print(len(result))
#
# print(type(result))
#
# print(type(result[0]))

result = html.xpath('//li/@class')

print(result)