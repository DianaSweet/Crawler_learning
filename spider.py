from bs4 import BeautifulSoup #网页解析
import re   #正则表达式，进行文字匹配
import urllib.request, urllib.error #制定URL，获取网页数据
import xlwt #进行excel操作
import sqlite3  #进行SQLite数据库操作

def main():
    #1.爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)

    #保存数据
    # savepath = "豆瓣电影TOP250.xls"
    # saveData(datalist,savepath)

    dbpath = "movie.db"
    saveData2DB(datalist,dbpath)

    #askURL("https://movie.douban.com/top250?start=")

'''全局变量'''
#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串的模式）  #此处？表示只匹配一次
#影片图片的规则
findImaSrc = re.compile(r'<img.*src="(.*?)"', re.S)  #re.S表示忽略表达式中的换行符
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#影片概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):   #调用获取页面信息的函数*10次
        url = baseurl + str(i*25)
        html = askURL(url)  #保存获取到的网络原码

        #2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'): #查找符合要求的字符串，形成列表
            #print(item)  #测试：查看电影item的全部信息
            data = []  #保存一部电影的所有信息
            item = str(item)  #变为字符串

            #获取影片详情的链接
            link = re.findall(findLink, item)[0]  #re库通过正则表达式查找指定的字符串，[0]表示item中符合此正则表达式所有对象中的第一个
            data.append(link)  #添加链接

            imgSrc = re.findall(findImaSrc, item)[0]
            data.append(imgSrc)  #添加图片

            titles = re.findall(findTitle, item)  #片名可能有中英文名
            if (len(titles) == 2):  #添加标题
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace('/', '')
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')  #无数据添加为空

            rating = re.findall(findRating, item)[0]
            data.append(rating)  #添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  #添加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                data.append(inq[0].replace("。", ""))  # 添加概述
            else:
                data.append(' ')

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)  #替换<br/>
            bd = re.sub('/', '', bd)  #替换/
            data.append(bd.strip())

            datalist.append(data)   #将一部记录好的电影加入datalist

    return datalist

#得到一个指定的url的网页内容
def askURL(url):
    head = {    #模拟代理，向豆瓣发送信息。用户代理表示告诉豆瓣用户是何种类型的机器，本质告诉浏览器我们可以接受什么水平的内容
        "User-Agent":
        "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 104.0.5112.102Safari / 537.36Edg / 104.0.1293.70"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)

    return html

#3.保存数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet("douban_movieTop250", cell_overwrite_ok=True)

    col = ('电影详情链接', '图片链接', '影片中文名', '影片外文名', '评分', '评价数', '概况','相关信息')
    for i in range(0,8):
        sheet.write(0, i, col[i])  #列名
    for i in range(0,250):
        print("第%d条已输入" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1, j, data[j])

    book.save(savepath)

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'  #这里用“而不是‘，是因为电影名中可能出现’，导致sql语句读取value出错，错误提示sqlite3.OperationalError: near "s": syntax error
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,introduction,info
            )
            values(%s)'''%",".join(data)  #join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        )
    '''
    #创建数据库
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":  #当函数执行时
    #调用函数
    main()

    print("爬取完毕")