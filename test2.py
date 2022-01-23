import requests
import json
import csv

file = open("vegetable.csv","a",newline='',encoding='utf-8')
file_csv = csv.writer(file)
file_csv.writerow(["ClassFication","Name","low-price","mean-price","high-price","release-time"])

class spyderXFD():
    def __init__(self):
        self.url ="http://www.xinfadi.com.cn/getPriceData.html"
        self.headers = {
            "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
            }
        self.data = {
            "limit": 20,
            "current":"",
            "pubDateStartTime":"",
            "pubDateEndTime": "",
            "prodPcatid": "",
            "prodCatid": "",
            "prodName": ""
            }
    def post_url(self):
        res = requests.post(self.url,data =self.data,headers = self.headers)
        res_dic = json.loads(res.text)
        for i in res_dic["list"]:
            file_csv.writerow([i["prodCat"],i["prodName"],i["lowPrice"],i["avgPrice"],i["highPrice"],i["pubDate"]])
    def run(self,x):
        self.data["current"] = x#获取第x页数据
        self.post_url()


train_XFD = spyderXFD()

for i in range(10):
    if(i==0):
        train_XFD.run("")
    else:
        train_XFD.run(i)
    file_csv.writerow("")
file.close()
