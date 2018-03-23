#encoding:utf-8
from lxml import etree
import requests
import os
import csv

'''
定义网页URL和headers请求文件
'''
urls=['https://www.80s.tt/movie/1-0-0-0-0-0?page={}'.format(str(i)) for i in range(1,478)]
headers={'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

'''
download()方法：获取网页源码
'''
def download(url):
    html=requests.get(url,headers=headers)
    return html

'''
crawl_info()方法：使用lxml模块匹配出电影名称，放入list
'''
def crawl_info(url):
    html=download(url)
    selector=etree.HTML(html.text)
    namelist=selector.xpath('//body/div[3]/div/div[1]/div[@class="col-xlg-2 col-lg-2 col-md-3 col-sm-3 col-xs-4 list_mov"]/div[2]/h4/a/text()')
    return namelist


def crawl_link(url):
    html=download(url)
    selector=etree.HTML(html.text)
    urllist=selector.xpath('//body/div[3]/div/div[1]/div[@class="col-xlg-2 col-lg-2 col-md-3 col-sm-3 col-xs-4 list_mov"]/div[2]/h4/a/@href')
    return urllist
#write_to_file()方法：将爬取的数据存入本地csv文件
'''
def write_to_file(url):
    namelist=crawl_info(url)
    print(namelist)
    path='E:\\mivie'
    if not os.path.isdir(path):
        os.makedirs(path)
    print('正在存储！')
    with open('E:\\movie\movie.csv','a',newline='') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerows(namelist)
 '''       

if __name__=='__main__' :  
    page=0
    for url in urls:
        page=page+1
        namelist=crawl_info(url)
        urllist=crawl_link(url)
        for name in namelist,urllist:
            print(name)
    
    
    