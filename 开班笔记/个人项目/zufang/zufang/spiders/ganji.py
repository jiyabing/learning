import scrapy
from itertools import zip_longest
from zufang.items import ZufangItem


class GanJiSpider(scrapy.Spider ):
    name = 'zufang'
    start_urls = ['http://wh.ganji.com/fang1/']

    def parse(self, response):
        # print(response)
        zf = ZufangItem()
        title_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        lease_type_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[@class='first js-huxing']/text()").extract()
        address = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[3]/span")
        address_list = []
        for i in address:
            ads = ''.join(i.xpath('string(.)').extract()[0].split())
            # print(ads)
            address_list.append(ads)
        # print(address_list)
        price_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        # print(len(title_list))
        # print(len(lease_type_list))
        # print(len(address_list))
        # print(len(price_list))
        for i, j, x, y in zip(title_list, lease_type_list, address_list, price_list):
            zf['title'] = i
            zf['lease_type'] = j
            zf['address'] = x
            zf['price'] = y
            yield zf
            # print(zf)
