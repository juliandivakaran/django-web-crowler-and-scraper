import scrapy

class HelloWorldSpider(scrapy.Spider):
    name = "helloworld"

    def start_requests(self):
        # Directly yield a request to start the crawl
        yield scrapy.Request(url='https://docs.djangoproject.com/en/5.1/intro/tutorial01/', callback=self.parse)

    def parse(self, response):
        # Debugging: log a message to confirm the spider is parsing
        self.logger.info(f"Parsing page: {response.url}")
        
        # Yield the data (Item)
        yield {"message": "Hmnbmccello Worlmd"}
