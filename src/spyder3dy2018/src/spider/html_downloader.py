#coding=utf-8
'''
Created on 2016年6月6日

@author: zww
'''
import urllib.request


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None :
            return None
        response = urllib.request.urlopen(url)
        #print response.read()
        
        if response.getcode() != 200:
            return None
        
        return response.read()
    



