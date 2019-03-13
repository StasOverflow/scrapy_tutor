import scrapy
from tutorial.items import ItemClass


class QuotesSpider(scrapy.Spider):
    name = "habr"
    start_urls = ("https://habr.com/ru/company/itsumma/blog/443490/", )

    def parse(self, response):
        # print('RESP IS: ', response)
        title = response.xpath('//span[contains(@class, "post__title")]/text()').get()
        # print('TITLE IS: ', title)
        image = response.xpath('//img[contains(@alt, "banner")]/@src').get()
        description = response.xpath('//div[contains(@class, "info-desc")]/text()').extract_first()

        fields_item = ItemClass()
        fields_item['image'] = image
        fields_item['title'] = title
        fields_item['descr'] = description

        return fields_item



