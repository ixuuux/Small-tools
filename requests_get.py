import requests

def get(url='https://httpbin.org/ip', headers=None, proxies=None, try_num=0, try_max_num=5, timeout=1):
    if try_num < try_max_num:
        try:
            response = requests.get(url=url, headers=headers, proxies=proxies, timeout=timeout)
            if response.status_code == 200:
                return response
            return get(url, try_num+1)
        except:
            return get(url, try_num+1)
    return False
