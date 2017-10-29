import re

# findall() 方法
# findall 方法返回一个列表 或者 元组

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo_search = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo_search.group())
mo_find = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print (mo_find)

# ^ 代表以什么开始  $代表以什么结束

wholeStringIsNum = re.compile(r'^\d+$')
good_search = wholeStringIsNum.search ('34384730845742')
print (good_search.group())
wrong_search = wholeStringIsNum.search ('343847b30845742')
print (wrong_search.group())