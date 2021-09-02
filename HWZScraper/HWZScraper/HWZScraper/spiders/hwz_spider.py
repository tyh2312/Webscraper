# Import Scrapy
import scrapy

# Create Spider class
class HWZoneSpider(scrapy.Spider):

    # define a name for the spider
    name = "HwzPosts"

    # specify url of page to crawl posts from
    start_urls = ["https://forums.hardwarezone.com.sg/forums/pc-gaming.382/"]

    def parse(self, response):
        #for thread in response.css('.js-threadList > .structItem--thread'):
        for thread in response.xpath('//div[has-class("js-threadList")]/div[has-class("structItem--thread")]'):

            thread_link =  thread.css('.structItem-title a::attr(href)').get()
            #thread_link =  thread.xpath('//div[@class="structItem-title"]').get()

            yield response.follow("https://forums.hardwarezone.com.sg" + thread_link, self.parse_thread)
        
        next_page = response.css('a.pageNav-jump--next::attr(href)').get()
        #next_page = response.xpath('//a[@class="pageNav-jump pageNav-jump--next').get()
        if next_page is not None:
            yield response.follow("https://forums.hardwarezone.com.sg" + next_page, self.parse)

    def parse_thread(self, response):
        title = response.css('h1.p-title-value::text').get()
        #title = response.xpath('//h1[@class="p-title-value"].text').get()
        for post in response.css('.message--post'):
        #for post in response.xpath('//article[@class="message message--post js-post js-inlineModContainer  "]'):   
            yield {
                'title': title,
                'content': post.css('.bbWrapper::text').get(),
                #'content': post.xpath('.//article[@class="message-body js-selectToQuote').get(),
                'author': post.css('.username::text').get(),
                #'author': post.xpath('.//a[@itemprop="name"]').get(),
            }
        
        next_page = response.css('a.pageNav-jump--next::attr(href)').get()
        #next_page = response.xpath('//a[@class="pageNav-jump pageNav-jump--next').get()
        if next_page is not None:
            yield response.follow("https://forums.hardwarezone.com.sg" + next_page, self.parse_thread)