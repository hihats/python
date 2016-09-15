#! env python3
# -*- encode: utf-8 -*-

import sys
import datetime
import locale
from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetch_body(url):
    html = urlopen(url)
    obj = BeautifulSoup(html.read(), "html.parser")
    return obj.body

def main():
    """ body内のclass=引数2 のテキスト取得、出力 """
    argvs = sys.argv

    bodyObj = fetch_body(argvs[1])
    class_name = argvs[2]
    res = bodyObj.find(class_=class_name).text
    d = datetime.datetime.today()
    print('[' + d.strftime("%Y-%m-%d %H:%M:%S") + ']' + res)


if __name__ == '__main__':
    main()
