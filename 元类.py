import asyncio
import time
import aiohttp as aiohttp
import requests
from aiohttp import ClientProxyConnectionError, ClientOSError
from pyquery import PyQuery as pq
'''
attrs= {'__module__': '__main__',
        '__qualname__': 'Crawler',
        'get_proxy': <function Crawler.get_proxy at 0x000001F828A85A60>,
        'craw_daili66': <function Crawler.craw_daili66 at 0x000001F828A85E18>,
        '_Crawlfunc_': ['craw_daili66'],
        '_Crawlfunccount_': 1
    }
'''
class Proxymetaclass(type):
    def __new__(cls, name, bases,attrs):
        count=0
        attrs['_Crawlfunc_']=[]
        for k,v in attrs.items():
            print(k,v)
            if 'craw_' in k:
                attrs['_Crawlfunc_'].append(k)
                count+=1
        attrs['_Crawlfunccount_']=count
        print('attrs is',attrs)
        return type.__new__(cls,name,bases,attrs)

class Crawler(object,metaclass=Proxymetaclass):
    def get_proxy(self,callback):
        proxys=[]
        for proxy in eval('self.{}()'.format(callback)):
            proxys.append(proxy)
        # print(proxys)
        return proxys

    def get_page(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }
        r = requests.get(url, headers=headers)
        return r.text

    def craw_daili66(self,page_count=4):
        url='http://www.66ip.cn/areaindex_1/{}.html'
        urls=[url.format(page) for page in range(1,page_count)]
        for url in urls:
            print('Crawl',url)
            html=self.get_page(url)
            if html:
                doc=pq(html)
                trs=doc('.containerbox  table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port =tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip,port])
        # yield '0.0.0.0'
        # yield '1.1.1.1'

async def test_single_proxy(proxy):
    conn=aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            if isinstance(proxy,bytes):
                proxy.decode('utf-8')
            real_proxy='http://'+proxy
            print("正在测试代理",proxy)
            url='http://www.baidu.com'
            async with session.get(url,proxy=real_proxy,timeout=15) as response:
                if response.status in [200]:
                    print("代理可用",proxy)
                else:
                    print("请求响应不合法", proxy)
        except (ClientProxyConnectionError,ConnectionError,ConnectionRefusedError,TimeoutError,AttributeError,ClientOSError):
            print("请求失败", proxy)






def get_proxys():
    crawler=Crawler()
    for callback_label in range(crawler._Crawlfunccount_):
        callback=crawler._Crawlfunc_[callback_label]
        proxys=crawler.get_proxy(callback)
        # for proxy in proxys:
        #     print(proxy)
        return proxys


for proxy in get_proxys():
    print(proxy)


def test():
    proxys=[i for i in get_proxys()]
    print(proxys)

    try:
        loop = asyncio.get_event_loop()
        for i in range(0, len(proxys), 100):
            test_proxys = proxys[i:i + 100]
            print('test_proxys',test_proxys)
            tasks = [test_single_proxy(proxy) for proxy in test_proxys]
            loop.run_until_complete(asyncio.wait(tasks))
            time.sleep(5)
    except Exception as e:
        print("测试器发生异常", e.args)

if __name__ == '__main__':
    test()

# print(type(metaclass))
# counts=(dir(metaclass))
# for i in enumerate(counts):
#     print(i)