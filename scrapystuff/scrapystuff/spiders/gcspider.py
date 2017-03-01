import scrapy


def checklink(link):
    if link == "../":
        return False
    if link[-1] == '/' or (link[-4:] == ".txt" and link[:6] == 'morgue'):
        return True
    return False
  

class GCSpider(scrapy.Spider):
    name = "gcspider"

    start_urls = ['https://crawl.project357.org/morgue/']
    
    def parse(self, response):
    
        if response.url[-4:] == '.txt':
            lvlline = response.body.split('\n')[2] # Line on morgue that shows character level
            endline = response.body.split('\n')[4:6] # Line on morgue that shows character level
            if "             Escaped with the Orb" in endline and "(level 1," in lvlline:
                with open("morgues.txt", "a+") as f:
                    f.write(response.url + '\n')

        hrefs = response.css("a::attr(href)").extract()
        
        links = [response.urljoin(x) for x in hrefs if checklink(x)]
        
        for link in links:
            yield scrapy.Request(link)