# Import Scrapy
import scrapy
# import logging for setting log level
import logging

# Create Spider class
class HWZoneSpider(scrapy.Spider):

    # define a name for the spider
    name = "HwzPosts"

    # specify url of page to crawl posts from
    start_urls = ["https://forums.hardwarezone.com.sg/forums/pc-gaming.382/"]

    # custom settings
    custom_settings = {
        'LOG_LEVEL': logging.WARNING
    }

    def parse(self, response):
        for thread in response.xpath("//div[@class='structItem-title']/a"):
            thread_link = thread.xpath("@href").extract()

            yield response.follow("https://forums.hardwarezone.com.sg" + thread_link[0], self.parse_thread)

        next_page = response.xpath("//a[@class='pageNav-jump pageNav-jump--next']/@href").extract()
        if next_page is not None:
            yield response.follow("https://forums.hardwarezone.com.sg" + next_page[0], self.parse)

    def parse_thread(self, response):
        title = response.xpath("//h1[@class='p-title-value']/text()").extract()
        author = response.xpath("//a[@itemprop='name']/text()").extract()
        content = response.xpath("//div[@class='bbWrapper']/text()").extract()

        for post in range(len(response.xpath("//article[@class='message message--post js-post js-inlineModContainer  ']"))):
            yield {
                'title': title[0],
                'author': author[post],
                'content':content[post],
            }

        next_page = response.xpath("//a[@class='pageNav-jump pageNav-jump--next']/@href").extract()
        if next_page is not None:
            yield response.follow("https://forums.hardwarezone.com.sg" + next_page[0], self.parse_thread)