#正则表达式：判断字符串是否符合一定标准的 字符串模式

import re
#创建模式对象

pat = re.compile("AA") #此处的AA是正则表达式，用于匹配其他的字符串
# m = pat.search("ABCAA") #search后的字符串是被校验的内容

# m = pat.search("CBA")

# m = pat.search("AABCAADDCCAAA") #search方法进行比对查找

#没有模式对象
# m = re.search("asd","Aasd") #前面的字符串是模板（规则），后面的字符串是被校验的对象
# print(m)

# print(re.findall("[A-Z]", "ASDaDFGAa")) #前面字符串是规则（正则表达式），后面的字符串是被校验的字符串

# print(re.findall("a", "ASDaDFGAa"))

# print(re.findall("[A-Z]+", "ASDaDFGAa"))

#sub

print(re.sub("a", "A", "abcdcasd")) #找到a，用A来替换，在第三个字符串中查找

print(re.sub("\n", "A", "abcdcasd")) #检验换行

#建议在正则表达式中，被比较的字符前面加上r，不用担心转义字符的问题
a = r"\aabd-\'" #此时，\a不会被理解为转义
print(a)