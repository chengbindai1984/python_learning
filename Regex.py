import re

phoneNumRegex = re.compile(r' (\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.search('My phonenumber is 415-555-4242. ')
# 正则表达式利用group()分组输出
print ('Phone number found: ' + mo.group())
print ('Phone number found: ' + mo.group(1))
print ('Phone number found: ' + mo.group(2))
print ('Phone number found: ' + mo.group(3))

# 用“？”实现 0 或者 1次匹配

batRegex = re.compile(r' Bat(wo)?man')
mo1 = batRegex.search(' The Adventures of Batman')
mo2 = batRegex.search(' The Adsafadfad of Batwoman')
mo3 = batRegex.search(' The Adsafadfad of Batwowoman')
print (mo1.group())
print (mo2.group())
# Mo是个空值
print (mo3)

# 用“*”实现0 或者 2+次匹配

batRegex = re.compile(r' Bat(wo)*man')
mom1 = batRegex.search(' The Adventures of Batman')
mom2 = batRegex.search(' The Adsafadfad of Batwoman')
mom3 = batRegex.search(' The Adsafadfad of Batwowoman')
print (mom1.group())
print (mom2.group())
# mom3 Ture
print (mom3)
print (mom3.group())

# 用“+”实现一次或者多次匹配

batRegex = re.compile(r' Bat(wo)+man')
mom1 = batRegex.search(' The Adventures of Batman')
mom2 = batRegex.search(' The Adsafadfad of Batwoman')
mom3 = batRegex.search(' The Adsafadfad of Batwowowowoman')
# mom1 空值
print (mom1)
print (mom2.group())
print (mom3.group())