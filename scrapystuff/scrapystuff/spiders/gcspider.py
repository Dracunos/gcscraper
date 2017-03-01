import scrapy


def checklink(link):
    if link == "../":
        return False
    if link[-1] == '/' or (link[-4:] == ".txt" and link[:6] == 'morgue'):
        return True
    return False
  
def checkmorgue(morgue):
    return

class GCSpider(scrapy.Spider):
    name = "gcspider"

    start_urls = ['https://crawl.project357.org/morgue/']
    
    def parse(self, response):
    
        if response.url[-4:] == '.txt':
            print response.body
            return

        hrefs = response.css("a::attr(href)").extract()
        
        links = [response.urljoin(x) for x in hrefs if checklink(x)]
        
        for link in links:
            yield scrapy.Request(link)