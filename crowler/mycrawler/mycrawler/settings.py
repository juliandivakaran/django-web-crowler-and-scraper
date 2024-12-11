import os
import sys
import django

# Set up Django integration
sys.path.append(os.path.dirname(os.path.abspath('../../mysite')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

# Scrapy settings for mycrawler project
BOT_NAME = "mycrawler"

SPIDER_MODULES = ["mycrawler.spiders"]
NEWSPIDER_MODULE = "mycrawler.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "mycrawler (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "mycrawler.pipelines.DjangoPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60

# Set logging level
LOG_LEVEL = 'INFO'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
