#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 18:11
# @Author  : zww
# @Site    : 
# @File    : skjjspy.py
# @Software: PyCharm
import random
import urllib

import requests
import time
from bs4 import BeautifulSoup
import pymysql


def insert_mysql(td0,td1,td2,td3,td4,td5,td6,td7,td8,td9,td10,td11,td12,td13,td14,td15,td16,td17,td18,td19):
    db = pymysql.connect("127.0.0.1", "root", "890", "my", charset='utf8')
    cursor = db.cursor()
    a='1'
    sql="INSERT INTO shekejijin(`项目批准号`,`项目类别`,`学科分类`,`项目名称`,`立项时间`,`项目负责人`,`专业职务`,`工作单位`,`单位类别`,`所在省区市`,`所属系统`,`成果名称`,`成果形式`,`成果等级`,`结项时间`,`结项证书号`,`出版社`,`出版时间`,`作者`,`获奖情况`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (td0,td1,td2,td3,td4,td5,td6,td7,td8,td9,td10,td11,td12,td13,td14,td15,td16,td17,td18,td19)
    try:
        cursor.execute(sql)
        db.commit()
        print('插入数据成功')
        db.close()

    except Exception as e:
        print('插入数据异常', e)
        db.rollback()
        db.close()

def getagent():
    f = open('agent.cfg', 'r')
    lines = f.readlines()
    agentList = []
    for i in lines:
        agentList.append(i[:-2])
    return agentList
agentList=getagent()
def getPage(url):
    header = {
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept - Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie': 'sso_c=0; sfr=1; PHPSESSID=a1rgb3kogpiqaukv6jmh0k3mm1',
        'Upgrade - Insecure - Requests': '1',
        'Connection': 'keep - alive',
        'Host': 'fz.people.com.cn',
        'User-Agent': '\'' + agentList[random.randint(0, len(agentList) - 1)] + '\'',
    }

    # response = requests.get(url, headers=header)
    return response
# @insert_mysql
def get_vaule(td):
    print(type(td[1].text))
    print(td[1].text)
    return insert_mysql(td[0].text,td[1].text,td[2].text,td[3].text,td[4].text,td[5].text,td[6].text,td[7].text,td[8].text,td[9].text,td[10].text,td[11].text,td[12].text,td[13].text,td[14].text,td[15].text,td[16].text,td[17].text,td[18].text,td[19].text)

def get_td(tr):
    for i in range(len(tr)):
        td=tr[i].find_all('td')
        get_vaule(td)

def get_content(url):
    web_data=getPage(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    table=soup.find_all('table')[2]
    tr=table.find_all('tr')[1:]
    get_td(tr)
def loop(num):
    for i in range(1,num):

        url='http://fz.people.com.cn/skygb/sk/index.php/Index/seach?xktype=%E5%9B%BE%E4%B9%A6%E9%A6%86%E3%80%81%E6%83%85%E6%8A%A5%E4%B8%8E%E6%96%87%E7%8C%AE%E5%AD%A6&p='+str(num)
        get_content(url)
        time.sleep(4)
if __name__ == '__main__':
    loop(84)

