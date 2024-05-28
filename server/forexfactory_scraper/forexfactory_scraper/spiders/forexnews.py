import scrapy
from scrapy.utils.project import get_project_settings

class ForexNewsSpider(scrapy.Spider):
    name = "forexnews"
    allowed_domains = ["forexfactory.com"]
    start_urls = ["https://www.forexfactory.com/"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 2,
        'COOKIES_ENABLED': False,
        'RETRY_TIMES': 10,
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
        },
    }

    def parse(self, response):
        # Assuming you want to scrape all news blurbs on the home page
        news_blurbs = response.css('div.overlay__content')
        for blurb in news_blurbs:
            # Extract data from the blurb
            description = blurb.css('td.calendarspecs__specdescription::text').get()
            source = blurb.css('td.calendarspecs__specdescription a::text').get()
            speaker = blurb.css('td.calendarspecs__specdescription::text').get()
            usual_effect = blurb.css('td.calendarspecs__specdescription::text').get()
            notes = blurb.css('td.calendarspecs__specdescription::text').get()
            why_traders_care = blurb.css('td.calendarspecs__specdescription::text').get()
            acro_expand = blurb.css('td.calendarspecs__specdescription::text').get()

            yield {
                'description': description,
                'source': source,
                'speaker': speaker,
                'usual_effect': usual_effect,
                'notes': notes,
                'why_traders_care': why_traders_care,
                'acro_expand': acro_expand,
            }

        # Handle pagination if necessary
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
