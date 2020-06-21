import asyncio
import time

import aiohttp
import requests
from aiohttp import ClientProxyConnectionError, ClientOSError


async def test_get(url):
    conn=aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            if isinstance(url,bytes):
                url.decode('utf-8')
            async with session.get(url,timeout=15) as response:
                if response.status in [200]:
                    print("可用",response.status)
                    print(response.url, response.content,response.charset,response.read())
                else:
                    print("请求不到", response.status)
        except (ClientProxyConnectionError,ConnectionError,ConnectionRefusedError,TimeoutError,AttributeError,ClientOSError):
            print(url, response.text())

def test():
    url = 'http://www.66ip.cn/areaindex_17/{}.html'
    urls = [url.format(page) for page in range(1, 20)]
    urls = ['http://www.baidu.com'] + urls
    try:
        loop = asyncio.get_event_loop()
        tasks = [test_get(url) for url in urls]
        loop.run_until_complete(asyncio.wait(tasks))
        time.sleep(5)
    except Exception as e:
        print("测试器发生异常", e.args)


if __name__ == '__main__':
    test()













# def get(arg):
#
#     proxy={
#         'http':'http://'+arg,
#         'https':'https://'+arg,
#     }
#     print(proxy)
#     r= requests.get('http://www.baidu.com')
#     print(r.text)
#     print(r.status_code)
#     print(r.encoding)
# arg ='117.114.149.66:55443'
# get(arg)