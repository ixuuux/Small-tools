import requests

def get(url='https://httpbin.org/ip', headers=None, proxies=None, try_num=0, try_max_num=5, timeout=1):
    if try_num < try_max_num:
        if headers:
            head = headers
        else:
            head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        try:
            response = requests.get(url=url, headers=headers, proxies=proxies, timeout=timeout)
            if response.status_code == 200:
                return response
            return get(url=url, headers=head, proxies=proxies, try_num=try_num+1, try_max_num=try_max_num, timeout=timeout)
        except:
            return get(url=url, headers=head, proxies=proxies, try_num=try_num+1, try_max_num=try_max_num, timeout=timeout)
    return False


if __name__ == '__main__':
    res = get()
    print(res)
