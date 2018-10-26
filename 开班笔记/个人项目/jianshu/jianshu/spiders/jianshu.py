import scrapy
from jianshu.items import JianshuItem
from scrapy.http import Request


class JianShuSpider(scrapy.Spider):
    name = 'jianshu'
    start_urls = ['https://www.jianshu.com/recommendations/collections?page=1&order_by=hot']

    def parse(self, response):
        # print(response)
        item = JianshuItem()
        info = response.xpath('.//div[@class="collection-wrap"]')
        if not info:
            return
        # print(info)
        # print(len(info))
        for i in info:
            name = i.xpath('a[1]/h4/text()').extract()[0]
            content = i.xpath('a[1]/p/text()').extract()
            article_num = i.xpath('div/a/text()').extract()[0]
            fans = i.xpath('div/text()').extract()[0]
            if content:
                content = content[0]
            else:
                content = ''
            # print(name, content, article_num, fans)
            # print('='*30)
            item['name'] = name
            item['content'] = content
            item['article_num'] = article_num
            item['fans'] = fans
            yield item

        base_url = 'https://www.jianshu.com/recommendations/collections?page={}&order_by=hot'
        urls = (base_url.format(str(i)) for i in range(1, 21))
        for url in urls:
            yield Request(url, callback=self.parse)
