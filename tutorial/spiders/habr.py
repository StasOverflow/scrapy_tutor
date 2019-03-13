import scrapy


class QuotesSpider(scrapy.Spider):
    name = "habr"
    start_urls = ("https://habr.com/ru/company/itsumma/blog/443490/", )

    def parse(self, response):
        print('RESP IS: ', response)
        title = response.xpath('//span[contains(@class, "post__title")]/text()')
        print('TITLE IS: ', title)
