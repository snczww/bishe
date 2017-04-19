#-*- coding: utf-8 -*-
'''
Created on 2017年4月18日

@author: zww
'''
import pandas as pd

inputfile = 'C:\\Users\\zww\\Desktop\\lunwen\\chapter15\\demo\\data\\huizong.csv'
outputfile = 'D:\\源码\\python\\bishe\\src\\lianxi\\data\\haier_jd.txt'
data = pd.read_csv(inputfile, encoding = 'utf-8')
data = data[[u'评论']][data[u'品牌']==u'海尔']
data.to_csv(outputfile, index=False, header=False,encoding='utf-8')