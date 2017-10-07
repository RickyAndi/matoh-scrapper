# -*- coding: utf-8 -*-
import scrapy


class MatohsecondSpider(scrapy.Spider):
    name = 'matohsecond'
    allowed_domains = ['matohtransmalang.com']
    start_urls = ['https://matohtransmalang.com/paket-tour-wisata']

    def parse_product(self, product):
        return {
            'product_name': product.css('h4.product-name strong a::text').extract_first()
        }

    def parse(self, response):
        products = response.css('div.product-box')
        for product in products:
            yield self.parse_product(product)

        next_page_url = response.css('li > a[rel="next"]::attr(href)').extract_first()

        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)

        
