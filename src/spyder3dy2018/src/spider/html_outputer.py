#coding=utf-8
'''
Created on 2016年6月6日

@author: zww
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.htm','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        
        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")
        fout.close()
    
    
    
    



