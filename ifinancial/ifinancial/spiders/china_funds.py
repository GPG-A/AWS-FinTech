import scrapy


class ChinaFundsSpider(scrapy.Spider):
    name = 'china-funds'
    allowed_domains = ['investing.com']
    start_urls = ['https://cn.investing.com/funds/china-funds']

## 从Inversting.com获取中国基金相关信息

    def parse(self, response):
        selectors = response.xpath('//tr')
        for selector in selectors:
            fund_name = selector.xpath('./td[2]/a/text()').get()
            fund_code = selector.xpath('./td[3]/text()').get()
            last_price = selector.xpath('./td[4]/text()').get()
            price_limit = selector.xpath('./td[5]/text()').get()
            total_assets = selector.xpath('./td[6]/text()').get()
            trans_date = selector.xpath('./td[7]/text()').get()
            if fund_name and fund_code and last_price and price_limit and total_assets and trans_date:
                print(fund_name,fund_code,last_price,price_limit,total_assets,trans_date)
