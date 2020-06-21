import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Referer': 'http://i.jzj9999.com/quoteh5/',

}
url = 'http://i.jzj9999.com/quoteh5/'
session = requests.Session()
s = session.get(url, headers=headers)
html = s.text
print(html)
tree = etree.HTML(html)
name = tree.xpath('//span[@class="symbol-name y-middle"]//text()')
print(name)
# price =tree.xpath('//*[not(contains(@class,"symbol")) or *[contains(@class,"price")]//text()')
#  //*[text()="hello"]//a
price = tree.xpath('//*[starts-with(@class,"symbol-price")]//text()')
d = {
    '\ue1f2': '0',
    '\uefab': '1',
    '\ueba3': '2',
    '\uecfa': '3',
    '\uedfd': '4',
    '\ueffa': '5',
    '\uef3a': '6',
    '\ue6f5': '7',
    '\uecb2': '8',
    '\ue8ae': '9',
}
print(price)

p = ','.join(price)
print(p)
count = 0
for k, v in d.items():
    p.replace(k, v)
    count += 1
print(price)
print(count)
