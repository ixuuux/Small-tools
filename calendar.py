# *_* coding:utf-8 *_*
import json
import datetime
from lxml import etree
import requests
import time


def get_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.text
        return None
    except TimeoutError:
        print("请求超时", url)
        return None
    except Exception as e:
        print("未知错误", e, url, sep="\n")
        return None


def nongli(Year, Month, Day):  # 中国农历
    url = "https://www.nongli.com/plus/calendarajax2.php?Year={}&Month={}&Day={}".format(Year, Month, Day)
    html = get_info(url)
    lists = []
    if html:
        html = json.loads(html)
        lists.append(html.get("nian"))
        lists.append(html.get("yueri").replace("\u3000", ""))
        print("中国传统历法：{} {}".format(lists[0], lists[1]))


def foli(Year, Month, Day):  # 佛历，泰国采用广泛
    if Year:
        year = int(Year)
        print("佛历：{}年{}月{}日".format(year+544, Month, Day))


def zangli():  # 藏历
    url = "http://www.ptz.cc/plus/list.php?tid=78"
    html = get_info(url)
    if html:
        ele = etree.HTML(html)
        zangli = ele.xpath('//p[@class="zangli"]/text()')[0].replace("&nbsp", "")
        print("中国阴历：{}".format(zangli[5:]))


def minguo(Year, Month, Day):  # 中华民国
    print("中华民国：民国{}年{}月{}日".format(int(Year[-2:])+89, Month, Day))


def japan(Year, Month, Day):  # 日本
    print("日本年号：平成{}年{}月{}日".format(int(Year[-2:]) + 12, Month, Day))


def run():
    s = time.time()
    cur = datetime.datetime.now()
    Year = str(cur.year)
    Month = str(cur.month)
    Day = str(cur.day)
    print("本机时间：{}".format(datetime.datetime.now()))
    nongli(Year, Month, Day)
    foli(Year, Month, Day)
    zangli()
    minguo(Year, Month, Day)
    japan(Year, Month, Day)
    e = time.time()
    print(e-s)


if __name__ == '__main__':
    run()
