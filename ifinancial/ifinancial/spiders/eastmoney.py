import scrapy
import re

class EastmoneySpider(scrapy.Spider):
    # 思考如何设置日志级别 import logging
    name = 'eastmoney'
    allowed_domains = ['fund.eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/HBJJ_pjsyl.html']

    # 货币型基金收益
    def parse(self, response):
        datadate = response.xpath('/html/body/div[9]/div/div[5]/text()[2]').get().strip()
        print("数据日期：" + datadate)
        selectors = response.xpath('//tr')
        for selector in selectors:
            fund_name = selector.xpath('./td[5]/nobr/a/text()').get()
            fund_code = selector.xpath('./td[4]/text()').get()
            # 七日年化收益
            income_7 = selector.xpath('./td[7]/text()').get()
            create_date = selector.xpath('./td[13]/text()').get()
            fund_manager = selector.xpath('./td[14]/a/text()').get()
            if fund_name and fund_code and create_date and fund_manager:
                print(fund_name,fund_code,income_7,create_date,fund_manager)

            # 基金净值
                ## 开放式基金：股票型、混合型、债券型、指数型、QDII、ETF、LOF、FOF
                ## 货币基金
                ## 场内基金

            # 基金行情
                ## 净值估算
                ## 交易行情
               
            # 基金评级
                ## 上海证券 招商证券 济安金信

            # 基金排行
                ## 开放式基金：股票型、混合型、债券型、指数型、QDII、ETF、LOF、FOF
                ## 货币基金
                ## 场内基金
                ## 基金定投
            
            # 新发基金
                ## 在售
                ## 新成立
            
            ## 基金信息