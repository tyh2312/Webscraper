# Import Scrapy
import scrapy

# Create Spider class
class JapanSpider(scrapy.Spider):

    # define a name for the spider
    name = "HwzPosts"

    # specify url of page to crawl posts from
    start_urls = ["https://forums.hardwarezone.com.sg/forums/pc-gaming.382/"]

    def parse(self, response):
        for thread in response.xpath('//div[has-class("js-threadList")]/div[has-class("structItem--thread")]'):

            thread_link =  thread.css('.structItem-title a::attr(href)').get()
            
            yield response.follow("https://forums.hardwarezone.com.sg" + thread_link, self.parse_thread)
        
        next_page = response.css('a.pageNav-jump--next::attr(href)').get

        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_thread(self, response):
        topic = response.css('h1.p-title-value::text').get()
        for post in response.css('.message--post'):
            
            yield {
                'topic': topic,
                'author': post.css('.username::text').get(),
                'content': post.css('.bbWrapper::text').get(),
                
            }
        
        next_page = response.css('a.pageNav-jump--next::attr(href)').get()
        if next_page is not None:
            yield response.follow("https://forums.hardwarezone.com.sg" + next_page, self.parse_thread)