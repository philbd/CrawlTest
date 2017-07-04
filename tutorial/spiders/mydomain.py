# -*- coding: utf-8 -*-
import scrapy


class MydomainSpider(scrapy.Spider):
    name = 'mydomain'
    allowed_domains = ['commandcontrolservices.com']
    start_urls = ['http://commandcontrolservices.com/']

    def parse(self, response):
        pass
