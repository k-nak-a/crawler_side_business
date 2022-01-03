# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoocySpider(CrawlSpider):
    # クローラ名
    name = 'doocy'
    # クローリング対象ドメイン
    allowed_domains = ['doocy.jp/fukugyo']
    # クローリングの出発点となるURL
    start_urls = ['http://doocy.jp/fukugyo/']

    # クローリングをしたページのうち、リンクを辿るURLとその動作を指定
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    # クローリングしたページからの情報t輸出方法を指定
    # クローリング結果の情報はresponceオブジェクト内に格納される
    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
