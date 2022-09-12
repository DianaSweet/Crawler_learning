import jieba  #分词
from matplotlib import pyplot as plt  #绘图，数据可视化
from wordcloud import WordCloud  #词云
from PIL import Image  #图片处理
import numpy as np  #矩阵运算
import sqlite3  #数据库

#准备词云所需的文字
con = sqlite3.connect("D:\The_Python\pycharm\crawler_flask\movie.db")
'''对上面的问题：
You are assuming that the current working directory is the same as the directory your script lives in. 
It is not an assumption you can make. 
Your script is opening a new database in a different directory, one that is empty.
Use an absolute path for your database file. 
You can base it on the absolute path of your script.
脚本正在打开并尝试连接另一个目录中的新数据库，该目录是空的，
因此找不到表。所以访问数据库文件时应该使用绝对路径而不是相对路径。
'''
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]
cur.close()
con.close()

#分词
cut = jieba.cut(text)
string = ' '.join(cut)

img = Image.open(r'D:\The_Python\pycharm\crawler_flask\static\assets\img\Azuma_Seren.jpg')
image_array = np.array(img)  #将图片转换成数组
wc = WordCloud(
    background_color='white',
    mask=image_array,
    font_path="msyh.ttc",  #C:\Windows\Fonts
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

#输出词云图片到文件
plt.savefig(r'D:\The_Python\pycharm\crawler_flask\static\assets\img\word.jpg', dpi=500)