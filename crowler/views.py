from django.http import JsonResponse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mycrawler.spiders.helloworld_spider import HelloWorldSpider
from scrapy.signalmanager import dispatcher
from scrapy import signals

def index(request):
    results = []

    # This will store the items in the results list
    def collect_results(item, response, spider):
        results.append(item)


    # Set up a process and dispatcher to run the spider
    process = CrawlerProcess(get_project_settings())
    dispatcher.connect(collect_results, signal=signals.item_scraped)  # Connect callback

    process.crawl(HelloWorldSpider)
    process.start()  # This blocks until the spider finishes
    process.join()
    # Return the results as a JsonResponse
    if results:
        return JsonResponse(results, safe=False)  # Return the first result
    else:
        return JsonResponse({'error': 'No data found'})
