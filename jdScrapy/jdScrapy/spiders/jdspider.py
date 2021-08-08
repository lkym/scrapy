import scrapy

from jdScrapy.items import JdscrapyItem
from scrapy_splash import SplashRequest


class JdspiderSpider(scrapy.Spider):
    name = 'jdspider'
    allowed_domains = ['https://wqs.jd.com/data/coss/important/msportal_recovery.shtml?tpl=index']
    start_urls = ['https://wqs.jd.com/data/coss/important/msportal_recovery.shtml?tpl=index']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse, headers=headers, args={"wait": 5})

    def parse(self, response):
        # print("response",response)
        businessItem = response.xpath('//div[@id="recFloor"]/div[@class="floor-the-container"]/ul/li')
        # print("businessItem",businessItem)
        # print(len(businessItem))
        for item in businessItem:
            # print(item.xpath('./a/div/div/img/@src'))
            business = JdscrapyItem()
            business['b_pic'] = item.xpath('./a/div/div/img/@src').extract()
            business['b_title'] = item.xpath('./a/div/span/text()').extract()
            business['b_price'] = item.xpath('./a/div/p/span/span/text()').extract()
            # if(len(business['b_price'])):
            #     business['']
            # print(business['b_pic'])
            yield business
        pass
