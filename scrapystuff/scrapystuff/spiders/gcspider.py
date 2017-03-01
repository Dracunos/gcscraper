import scrapy


class GCSpider(scrapy.Spider):
    name = "gcspider"

    start_urls = [#'https://crawl.project357.org/morgue/',
                  'https://crawl.project357.org/morgue/Dracunos/morgue-Dracunos-20170301-043110.txt']

    def parse(self, response):

        print response.body

        #next_page_url = response.css("li.next > a::attr(href)").extract_first()
        #if next_page_url is not None:
        #    yield scrapy.Request(response.urljoin(next_page_url))