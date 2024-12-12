import scrapy

class HelloWorldSpider(scrapy.Spider):
    name = "extract"

    def start_requests(self):
        # Start from the main page
        start_url = 'https://doa.gov.lk/'

        # Initiate crawl
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        # Extract the title of the current page
        title = response.css('title::text').extract_first().strip()

        # Yield the current page's title and URL
        yield {
            'title': title,
            'url': response.url,
        }

        # Extract all links from the current page
        links = response.css('a::attr(href)').extract()

        # Follow links to other pages
        for link in links:
            absolute_url = response.urljoin(link)

            # Follow the link if it's within the same domain
            if 'doa.gov.lk' in absolute_url:
                yield scrapy.Request(url=absolute_url, callback=self.parse)
