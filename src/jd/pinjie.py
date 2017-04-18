#coding=utf-8
'''
Created on 2017年4月10日

@author: zww
'''
import re
html = open('C:\\Users\\zww\\Desktop\\page.txt', 'r').read()
content=re.findall(r'"guid".*?,"content":(.*?),',html)
#print(content)
#print(imgurl)
content_1 = []
file1 = open("C:\\Users\\zww\\Desktop\\pinglun.txt", "w")
h=0
for j in content:
    #print(j)
    h+=1
    j=j.strip('\"')
    if not "img" in j:
        content_1.append(j)
    #imgurl=re.findall('src=(.*)\'', j)
    #content_2=re.findall(r'"guid".*?,"content":(.*?),',j)
h=0 
for j in content_1:
    h+=1
    print(j)
    file1.write(str(j)+'\n')    
file1.close()   
print(h)
ii=0