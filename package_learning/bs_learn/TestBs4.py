'''
Beautiful Soup4能将HTML的标签文件解析成树形结构，然后方便地获取到指定标签的对应属性。
'''

from bs4 import BeautifulSoup
import re

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser") #参量为解析文件类型

#print(bs.title)
#print(bs.a)
#print(bs.head)

#print(type(bs.head)) #返回<class 'bs4.element.Tag'>

#1.Tag 标签及其内容：只能拿到bs找到的第一个内容

#print(type(bs.title.string)) #返回<class 'bs4.element.NavigableString'>

#2.NavigableString 标签里的内容（字符串）

#print(bs.a.attrs) #返回{'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}
#获取属性

#print(type(bs)) #返回<class 'bs4.BeautifulSoup'>
#print(bs.name) #返回[document]

#3.BeautiSoup 表示整个文档

# print(bs.a.string) #返回新闻
# print(type(bs.a.string)) #返回<class 'bs4.element.Comment'#>

#4.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号


#-----------------------------

#文档的遍历

# print(bs.head.contents)
# print(bs.head.contents[1])
#获取所有Tag的节点，生成一个字典




#文档的搜索

#(1)find_all
#字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")


#正则表达式:使用search()方法来匹配内容
# t_list = bs.find_all(re.compile("a"))


#方法：传入一个函数（方法），根据函数的要求去搜索
# def name_is_exists(tag):
#     return tag.has_attr("name") #返回含name标签的内容
#
# t_list = bs.find_all(name_is_exists)



#2.kwargs参数（根据提供的参数检索）

#t_list = bs.find_all(id="head")

#t_list = bs.find_all(class_=True) #class_下划线表示含class这样的属性

#3.text参数

# t_list = bs.find_all(text="hao123")
#
# t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
#
# t_list = bs.find_all(text=re.compile("\d")) #应用正则表达式查找包含特定文本的内容（标签里的字符串）

#4.limit参数

#t_list = bs.find_all("a", limit=3) #限定输出个数

#css选择器 select()

# t_list = bs.select("title") #通过标签来查找

# t_list = bs.select(".mnav") #通过类名来查找

# t_list = bs.select("#u1") #按照id来查找

# t_list = bs.select("a[class='bri']") #通过属性来查找

# t_list = bs.select("div > div > a") #通过子标签来查找

t_list = bs.select(".mnav ~ .bri") #通过兄弟标签查找

print(t_list[0].getText())
for item in t_list:
    print(item)