# *_* coding:utf-8 *_*
import random
import time
import datetime
from lxml import etree
import requests

session = requests.Session()


def get_weather(city):
    url = "https://www.tianqi.com/{}/".format(city)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/67.0.3396.62 Safari/537.36"
    }
    try:
        response = session.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except TimeoutError:
        print("请求超时")
        return None
    except Exception as e:
        print("未知错误", e)
        return None


def parsing(html):
    if html:
        ele = etree.HTML(html)
        try:
            yield {
                "city": ele.xpath('//dd[@class="name"]/h2/text()')[0],
                "date": ele.xpath('//dd[@class="week"]/text()')[0].replace("\u3000", "  "),
                "now": ele.xpath('//dd[@class="weather"]/p[@class="now"]/b/text()')[0]+"℃",
                "today": "  ".join(ele.xpath('//dd[@class="weather"]/span//text()')),
                "shidu": " | ".join(ele.xpath('//dd[@class="shidu"]//text()')),
                "kongqi": " | ".join(ele.xpath('//dd[@class="kongqi"]//text()'))
            }
        except IndexError:
            print("未查询到")


def run():
    while True:
        city = input("请输入城市的全拼(直接回车查询本地天气)：")
        s = time.time()
        html = get_weather([city if city else None][0])
        for i in parsing(html):
            _ = "-+=*@"[random.randint(0, 4)]
            print(_ * 30)
            print("{} | {}\n体感温度：{} | {}\n{}\n{}".format(i.get("city"),
                                                                        i.get("date"), i.get("now"), i.get("today"),
                                                                        i.get("shidu"), i.get("kongqi")))
            print(_ * 30)
            e = time.time()
            print("用时{:.5f}秒".format(e-s))
            with open("logging.txt", "a", encoding="utf-8") as f:  # 将查询历史保存至本地
                f.write("{}\n{} | {}\n体感温度：{} | {}\n{}\n{}\n{}\n{}\n用时{:.5f}秒\n".format(_*30,i.get("city"),
                                                                        i.get("date"), i.get("now"), i.get("today"),
                                                                        i.get("shidu"), i.get("kongqi"),
                                                                        _*30, datetime.datetime.now(), (e-s))+"\n")
        print("查询时间:{}".format(datetime.datetime.now()))
        print()


if __name__ == '__main__':
    run()

