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
# wrong_search = wholeStringIsNum.search ('343847b30845742')
# print (wrong_search.group())

# 通配字符
# 点. 星* 匹配所有字符

nameRegex = re.compile(r'First Name:(.*)Last Name:(.*)')
name_search = nameRegex.search(' First Name: Steven Last Name: Dai')
print (name_search.group(),name_search.group(1),name_search.group(2))

#通过 re.DOTALL作为参数，可以匹配包括换行在内的所有字符
#以下代码只能打印出第一行的内容
noNewlineRegex = re.compile('.*')
word_search = noNewlineRegex.search('''Serve the publice trust.
Protect the innocent.
Uphold the law.''')
print (word_search.group())
#使用 re.DOTALL 来做全文匹配

NewlineRegex = re.compile('.*', re.DOTALL)
word_search = NewlineRegex.search('''Serve the publice trust.
Protect the innocent.
Uphold the law.''')
print (word_search.group())

# 参数re.IGNORECASE 不区分大小写的匹配

IgnoreRegex = re.compile(r'robocop', re.IGNORECASE)
robocop_search = IgnoreRegex.search('RobOCop is part man, part machine, all cop')
print (robocop_search.group())

# 使用方法sub 来替换匹配字符