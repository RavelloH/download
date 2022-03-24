from urllib.request import urlopen,build_opener,ProxyHandler
from bs4 import BeautifulSoup as bf
from urllib import request
import random

# UA
user_agent_list = [
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
]
# 随机UA
headers ={
    'User-Agent':random.choice(user_agent_list)
}

ip_list=[
    '209.97.171.128',
    '114.250.25.19',
    '125.120.62.26',
    '66.249.93.118',
    '1.202.113.240',
]

# IP
ip={
    'http':random.choice(ip_list)
}
link = input("在此输入网址:http://")
htmlurl = "https://"+str(link)
req = request.Request(htmlurl,headers=headers)

# 创建代理ip对象
pro_han = ProxyHandler(ip)
# 不能使用urlopen()函数，使用build_opener创建一个对象
opener = build_opener(pro_han)
# 发送请求
res = opener.open(req)
obj = bf(res.read(),'html.parser') #解析html
title = str(obj.head.title)
print("站点标题:",title,"正在查找图片")
pic_info = obj.find_all('img')
j = 0 #配置遍历
for i in pic_info:
    j += 1
    pic = str(i['src'])
    if "http" not in pic:
        if "data" in pic:
            continue
        else:
            if "//" in pic:
                print("http:"+pic) 
            else:
                if pic[0] == "/":
                    print("http://"+link+pic)    
                else:
                    print("http://"+link+"/"+pic) 
            
    else:
        print(pic)
