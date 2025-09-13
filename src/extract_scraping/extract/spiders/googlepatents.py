import scrapy


class GooglepatentsSpider(scrapy.Spider):
    name = 'googlepatents'
    allowed_domains = ['patents.google.com']
    start_urls = ['http://patents.google.com/']

    def parse(self, response):
        pass
