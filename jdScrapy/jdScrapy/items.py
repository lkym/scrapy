# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    b_pic = scrapy.Field()    # 商品图片
    b_title = scrapy.Field()  # 商品标题
    b_price = scrapy.Field()  # 商品图片
    b_tag = scrapy.Field()    # 商品标签
    b_plus_price = scrapy.Field()   # 商品会员价
    pass
