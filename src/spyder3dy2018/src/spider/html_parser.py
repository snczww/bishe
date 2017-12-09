#coding=utf-8
'''
Created on 2016年6月6日

@author: zww
'''
from bs4 import BeautifulSoup
import re
import urllib


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile("/html/gndy/\w+/\d+/\d+.html"))
        #print links
        for link in links:
            new_url = link['href']
            #print new_url
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            #print new_full_url
            new_urls.add(new_full_url)
        return new_urls
            
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
      
        
        res_data['url']=page_url
        
        title_node = soup.find('h1')
        #print title_node
        res_data['title'] = title_node.get_text()
        #<div class="para" label-module="para">
        summary_node = soup.find('td',style="WORD-WRAP: break-word").find("a")
        res_data['summary'] = summary_node.get_text()
         
        return res_data
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='GBK')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
    



