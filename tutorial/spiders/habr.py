import scrapy
from tutorial.items import ItemClass


class QuotesSpider(scrapy.Spider):
    name = "habr"
    start_urls = ("https://habr.com/ru/", )

    def parse(self, response):
        print('RESP IS: ', response)
        title_link_array = response.xpath('//a[@class="post__title_link"]/@href').extract()
        for link in title_link_array:
            yield scrapy.Request(link, self.parse_posts)

    def parse_page(self, response):
        title_link_array = response.xpath('//a[@class="post__title_link"]/@href').extract()
        for link in title_link_array:
            yield scrapy.Request(link, self.parse_posts)

    def parse_posts(self, response):
        title = response.xpath('//span[contains(@class, "post__title")]/text()').get()
        # print('TITLE IS: ', title)
        image = response.xpath('//img[contains(@alt, "banner")]/@src').get()
        description = response.xpath('//div[contains(@class, "info-desc")]/text()').extract_first()

        fields_item = ItemClass()
        fields_item['image'] = image
        fields_item['title'] = title
        fields_item['descr'] = description
        return fields_item



