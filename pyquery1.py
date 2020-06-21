import requests
from pyquery import PyQuery as pq

url = 'http://i.jzj9999.com/quoteh5/'
session = requests.Session()
s = session.get(url)
# print(s.text)
doc = pq(s.text)

r= requests.get(url)
print(r.text)

# items = doc("div .quote-price-table .price-table-row").items()
# # for item in items:
# #     dic={}
# #     name = item.find('.symbol-name').text()
# #     print(name)
# #     buy_price=item.find('.symbol-price-rise').attr('href')
# #     print(buy_price)