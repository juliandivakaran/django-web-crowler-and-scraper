from django.http import JsonResponse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mycrawler.spiders.helloworld_spider import HelloWorldSpider
from scrapy.signalmanager import dispatcher
from scrapy import signals
from .forms import URLinputForm
from django.shortcuts import render, redirect



def index(request):
    results = []

    # This will store the items in the results list
    def collect_results(item, response, spider):
        results.append(item)


    start_url = request.GET.get('url', None)
    if not start_url:
        return JsonResponse({'error': 'No url specified'}, status=400)

    # Set up a process and dispatcher to run the spider
    process = CrawlerProcess(get_project_settings())
    dispatcher.connect(collect_results, signal=signals.item_scraped)  # Connect callback

    process.crawl(HelloWorldSpider, start_url = start_url)
    process.start()  # This blocks until the spider finishes
    process.join()
    # Return the results as a JsonResponse
    if results:
        return JsonResponse(results, safe=False)  # Return the first result
    else:
        return JsonResponse({'error': 'No data found'})


def get_url(request):
    if request.method == 'POST':
        form = URLinputForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            return redirect(f'/crawl/?url={url}')
    else:
        form = URLinputForm()  # Handle GET request

    # Make sure to return the form when the request is GET or the form is invalid
    return render(request, 'index/index.html', {'form': form})


"""def get_url(request):
    if request.method == 'POST':
        form = URLinputForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            return render(request, 'index/index.html', {'url': url})
        else:
            form = URLInputForm()
        return render(request, 'index/index.html', {'form': form}) """