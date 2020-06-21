import requests
from pyquery import PyQuery as pq


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    return r.text

def craw_daili66(page_count=4):
    url = 'http://www.66ip.cn/{}.html'
    urls = [url.format(page) for page in range(1, page_count)]
    for url in urls:
        print('Crawl', url)
        html = get_page(url)
        if html:
            print(html)
            doc = pq(html)
            trs = doc('.containerbox  table tr:get(0)').items()
            for tr in trs:
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                yield ':'.join([ip, port])


# for i in craw_daili66(page_count=4):
#     print(i)
def get1():
    html=requests.get('http://www.66ip.cn/1.html').text
    # print(html)
    doc = pq(html)
    trs = doc('.containerbox  table tr:get(0)').items()
    print(trs)
    # for tr in trs:
    #     ip = tr.find('td:nth-child(1)').text()
    #     port = tr.find('td:nth-child(2)').text()
    #     yield ':'.join([ip, port])

if __name__ == '__main__':
    html=requests.get('http://www.66ip.cn/1.html').text
    # print(html)
    doc = pq(html)
    trs = doc('.containerbox  table tr:gt(0)').items()
    for tr in trs:
        ip = tr.find('td:nth-child(1)').text()
        port = tr.find('td:nth-child(2)').text()
        aa= ':'.join([ip, port])
        print(aa)