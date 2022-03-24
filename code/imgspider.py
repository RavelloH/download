from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
link = input("在此输入网址:http://")
html = urlopen("https://"+link)
obj = bs(html.read(),'html.parser') #解析html
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
