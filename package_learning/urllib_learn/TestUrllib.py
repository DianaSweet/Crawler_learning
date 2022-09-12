#urllib.request 使用
import urllib.request

#获取一个GET请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8解码

#获取一个POST请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")  #POST收取用户发送的请求，并显示在网页中
#
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=5)  #超时处理值得关注，对超时网页针对性处理
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

#网页解析
# response = urllib.request.urlopen("http://baidu.com")
# print(response.status) #状态码获取
# print(response.getheader("Server")) #获取响应头

#防止爬虫监测

# url = "http://httpbin.org/post"
# headers = {   #关键信息是用户代理User_Agent信息
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70",
#     "X-Amzn-Trace-Id": "Root=1-630b7238-092dbc763f56c25a5f777a9d"
#   }
# data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")    #封装的对象
# response = urllib.request.urlopen(req)  #将封装的对象传输
# print(response.read().decode("utf-8"))

url = "https://www.douban.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70",
    "X-Amzn-Trace-Id": "Root=1-630b7238-092dbc763f56c25a5f777a9d"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)  #将封装的对象传输
print(response.read().decode("utf-8"))