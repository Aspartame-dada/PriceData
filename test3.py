# @Time:2021/12/1710:05
# @Author:中意灬
# @File:新发地.py
# @ps:tutu qqnum:2117472285
import csv
from  concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
with open('北京新发地菜价.csv',mode='w', encoding='utf-8',newline='') as f:
    wirter = csv.writer(f)#创建一个写入的对象
    wirter.writerow(['菜名', '最低价(元)', '最高价(元)', '平均价(元)', '产地','发布日期'])
    def get_one_page(pageNo):
        data={
            "limit":20,
            "current":pageNo,
        }
        url="http://www.xinfadi.com.cn/getPriceData.html"
        resp=requests.post(url,data=data)
        html=resp.json()
        list=html['list']
        # print(list)
        for i in list:
            if i['place']=='':
                i['place']='产地不详'
            wirter.writerow([i['prodName'],i['lowPrice'],i['highPrice'],i['avgPrice'],i['place'],i['pubDate']])
    if __name__ == '__main__':
        # get_one_page(1)
        with ThreadPoolExecutor(10000) as t:#创建10000个线程
            for i in range(1,20448):#所有页数
                t.submit(get_one_page,pageNo=i)
        print('over!')
        print('点赞不白嫖（狗头）')

