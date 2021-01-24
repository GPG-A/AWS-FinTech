import scrapy


class EastmoneySpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://www.eastmoney.com/']

    def parse(self, response):
        pass
