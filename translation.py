from lxml import etree
import requests
import datetime
from retrying import retry


@retry(stop_max_attempt_number=3)
def post_info(url, data, headers):  # 携带参数发起请求
    try:
        response = requests.post(url, data=data, headers=headers, timeout=2)
        if response.status_code == 200:
            return response.text
        return None
    except TimeoutError:
        print("请求超时")
        return None
    except Exception as e:
        print("未知错误", e)
        return None


def extract_info(html):  # 提取翻译结果
    if html:
        ele = etree.HTML(html)
        return ele.xpath('//ul[@id="translateResult"]/li//text()')[0].strip() \
            if ele.xpath('//ul[@id="translateResult"]/li//text()') else None
    return None


def run(keyword):
    url = "https://m.youdao.com/translate"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
                      "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Referer": "https://m.youdao.com/translate",
        "Host": "m.youdao.com"
    }
    data = {
        "inputtext": keyword,
        "type": "AUTO"
    }
    html = post_info(url, data, headers)
    return extract_info(html)


if __name__ == '__main__':
    while True:
        keyword = input("请输入要翻译的中/英文：")
        info = run(keyword)
        print("翻译结果：", info)
        with open("logging.txt", "a", encoding="utf-8") as f:  # 将历史纪录保存至本地
            f.write('输入内容："{}"，翻译结果："{}"\t\t时间:{}'.format(keyword, info, datetime.datetime.now())+"\n")
        print()
