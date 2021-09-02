# Import Scrapy
import scrapy

# Create Spider class
class HWZoneSpider(scrapy.Spider):

    # define a name for the spider
    name = "HwzPosts"

    # specify url of page to crawl posts from
    start_urls = ["https://forums.hardwarezone.com.sg/forums/pc-gaming.382/"]

    def parse(self, response):
        for thread in response.css('.js-threadList > .structItem--thread'):

            thread_link =  thread.css('.structItem-title a::attr(href)').get()
            
            yield response.follow("https://forums.hardwarezone.com.sg" + thread_link, self.parse_thread)
        
        next_page = response.css('a.pageNav-jump--next::attr(href)').get()
        if next_page is not None:
            yield response.follow("https://forums.hardwarezone.com.sg" + next_page, self.parse)

    def parse_thread(self, response):
        title = response.css('h1.p-title-value::text').get()
        for post in response.css('.message--post'):
            
            yield {
                'title': title,
                'content': post.css('.bbWrapper::text').get(),
                'author': post.css('.username::text').get(),
            }
        
        next_page = response.css('a.pageNav-jump--next::attr(href)').get()
        if next_page is not None:
            yield response.follow("https://forums.hardwarezone.com.sg" + next_page, self.parse_thread)