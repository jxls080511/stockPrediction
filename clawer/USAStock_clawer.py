# -*- coding: utf-8 -*- #
import re
import requests
import urllib
import time
import os
from bs4 import BeautifulSoup
import re

def get_encoding(text):
    try:
        return re.search('charset=\"?([^\"]+)"',text).group(1)
    except:
        return None


def clawer_page(url):
    try:
        response = requests.get(url)
        text=response.text
        encoding=get_encoding(text)
        if(encoding is not None):
            response.encoding=encoding
        text=response.text
        return text
    except:
        print('error')
        return None

    


if __name__ == '__main__':
    for i in range(8):
        url='http://data.tsci.com.cn/US/USCODE.aspx?M=3&First=All&Sid=&uhu=df&P='+str(i)
        page=clawer_page(url)
        out=open('D:\\programing\\Python\\MLHomework\\美股数据\\美国证券交易所'+str(i),'w',encoding='utf-8')
        out.write(page)
        out.close()
        print(i)
        