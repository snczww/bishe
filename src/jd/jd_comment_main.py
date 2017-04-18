'''
Created on 2017骞�3鏈�30鏃�

@author: zww
'''
#https://item.jd.com/1993092.html
import urllib.request
import time
import re
import random

def pa(sart,end):
        i = sart
        headers = { 'Connection': 'Keep-Alive','Accept': 'text/css,*/*;q=0.1',
                   'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        while i <end:
            if i!=1550:
                s=str(i)
                url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79849&productId=1993092&score=0&sortType=5&page="+s+"&pageSize=10&isShadowSku=0"
                req = urllib.request.Request(url,headers=headers)
                response = urllib.request.urlopen(req).read()
                print(s)
                response = response.decode("gbk")
                print(response)
                time.sleep(random.uniform(0.1,2))
                file.write(response)
            i+=1

file = open("C:\\Users\\zww\\Desktop\\page.txt", "a")
pagenum=35
count=5022
while pagenum<60:
    pa(count,count+100)
    count+=100
    pagenum+=1
    time.sleep(random.uniform(60.5,200))
file.close()
html = open('C:\\Users\\zww\\Desktop\\page.txt', 'r').read()
content=re.findall(r'"guid".*?,"content":(.*?),',html)
#print(content)
#print(imgurl)
content_1 = []
file1 = open("C:\\Users\\zww\\Desktop\\pinglun.txt", "w")
h=0
for j in content:
    print(j)
    h+=1
    #if not "img" in j:
        #content_1.append(j)
    #imgurl=re.findall('src=(.*)\'', j)
    #content_2=re.findall(r'"guid".*?,"content":(.*?),',j)
    file1.write(str(j)+'\n')
file1.close()   
print(h)
ii=0


'''for h in imgurl:
    s=s.strip('\"')
    s='F:\\papic\\'+str(ii)+'.jpg'
    hi='https:'+h.strip('\"')
    
    print(hi)
    urllib.request.urlretrieve(hi,s)
    time.sleep(1)
    ii+=1'''
