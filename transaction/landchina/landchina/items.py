# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class District(scrapy.Item):
	id=scrapy.Field()
	value=scrapy.Field()
	name=scrapy.Field()
	isParent=scrapy.Field()

class LandchinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    dis_link = scrapy.Field()

    district = scrapy.Field()
    location = scrapy.Field()
    ahref = scrapy.Field()
    former_owner = scrapy.Field()
    owner = scrapy.Field()   

    detail_flag=scrapy.Field()
    detail_num=scrapy.Field()
    detail_location=scrapy.Field()
    detail_area=scrapy.Field()
    detail_use=scrapy.Field()
    detail_class=scrapy.Field()
    detail_years=scrapy.Field()
    detail_status=scrapy.Field()
    detail_level=scrapy.Field()
    detail_method=scrapy.Field()
    detail_price=scrapy.Field()
    detail_date=scrapy.Field()
    pass
