#!usr/bin/python
#coding=utf-8
import  re
# urllib模块提供了读取Web页面数据的接口
import  urllib
# 定义一个获取网页的函数
def getHtml(url):
# 打开一个url地址
    page =urllib.urlopen(url)
    html = page.read() 
    return html
def getImg(html):
    reg = reg = r'src="(.*?\.jpg)" size'
    imgre =re.compile(reg)
    imgerlist = re.findall(imgre,html)
    x=0
    for imgurl in imgerlist:
        urllib.urlretrieve(imgurl,'D:\E\%s.jpg' % x)
        x+=1
html =  getHtml("https://tieba.baidu.com/p/5081322513")
print getImg(html)