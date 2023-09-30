import scrapy

from ancient_poetry.items import PoemsItem


class PoemsSpiderSpider(scrapy.Spider):
    name = 'poems_spider'
    allowed_domains = ['www.gushiwen.org']
    start_urls = ['http://www.gushiwen.org/']
    url = 'https://www.gushiwen.cn/'

    # 每个爬虫的自定义pipeline设置（激活）
    custom_settings = {
        'ITEM_PIPELINES': {
            'ancient_poetry.pipelines.AncientPoetryPipeline': 500,
        },
    }


    def start_requests(self):
        yield scrapy.Request(url=self.url, method='GET', callback=self.parse)

    def parse(self, response):
        item = PoemsItem()
        for x in response.xpath('//div[@class="main3"]//div[@class="left"]//div[@class="cont"]'):
            title = x.xpath('.//b/text()').get()
            item['title'] = title
            dynasty_author = x.xpath('.//p[@class="source"]/a/text()').getall()
            if len(dynasty_author) == 2:
                item['dynasty'] = dynasty_author[1]
                item['author'] = dynasty_author[0]
            content = x.xpath('.//div[@class="contson"]/text()').extract()
            item['content'] = '</br>'.join(content)
            yield item

