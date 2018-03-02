# scrapy_test/simple_crawl/simple_crawl/spiders/quotes_spider.py
# Description: 
	# - Exampple of scraping static web pages 
	# - Going trough the site, listing all artist tours and checking which artists have tour in specific country
	# - Country is specified as input argument of spider 
# Start link: http://www.timba.com/tours
# What to get from a page: Date of the tour for specific country 
# Where to go next: Next artists from the list 
# 
# DESIGNING SELECTORS
# scrapy shell 'http://www.timba.com/tours'
# response.xpath("(//table[@class='striped_table']//a//@href)")
# response.xpath("//div[@class='pagination']//a[text()='Next']//@href").extract_first()

import scrapy

class TimbaTourSpider(scrapy.Spider):
    name = "timbatours"

    custom_settings = {
        'ROBOTSTXT_OBEY': 'False',
        'DOWNLOAD_DELAY': '5.0',
        'RANDOMIZE_DOWNLOAD_DELAY': 'True'
    }

    start_urls = [
        'http://www.timba.com/tours',
    ]

    def parse(self, response):
        for artist_link in response.xpath("(//table[@class='striped_table']//a//@href)"):
            yield {
                'ArtistLink': 'http://www.timba.com'+artist_link.extract()
            }

        next_page = response.xpath("//div[@class='pagination']//a[text()='Next']//@href").extract_first()
        if next_page is not None:
            next_page_url = 'http://www.timba.com' + next_page
            yield scrapy.Request(url=next_page_url, callback=self.parse)

class GetTours(scrapy.Spider):
    name = "gettours"

    import json
    from w3lib.html import remove_tags

    custom_settings = {
        'ROBOTSTXT_OBEY': 'False',
        'DOWNLOAD_DELAY': '5.0',
        'RANDOMIZE_DOWNLOAD_DELAY': 'True'
    }

    f = open('tour_links.jl')
    links = []
    for line in f:
        links.append(json.loads(line)['ArtistLink'])
    start_urls = links

    def parse(self, response):
        for concert in response.xpath("(//div[@id='tour_div']//p/strong/text())"):
            print concert.extract()




