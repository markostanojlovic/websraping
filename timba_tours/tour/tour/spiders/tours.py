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
# remove_tags(response.xpath("(//div[@id='tour_div']//p/strong)")[7].extract())
# selecting name of the band:
# v1: response.xpath("(//h3[@class='box_header']/text())")[-1].extract()
# v2: response.xpath("(//div[@id='main_page']//h3[@class='box_header']/text())").extract_first()
import scrapy
import json
from w3lib.html import remove_tags

class TimbaTourSpider(scrapy.Spider):
    name = "timbatours"

    custom_settings = {
        'ROBOTSTXT_OBEY': 'False',
        'DOWNLOAD_DELAY': '0.7',
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

    custom_settings = {
        'ROBOTSTXT_OBEY': 'False',
        'DOWNLOAD_DELAY': '0.2',
        'RANDOMIZE_DOWNLOAD_DELAY': 'True'
    }

    f = open('tour_links.jl')
    links = []
    for line in f:
        links.append(json.loads(line)['ArtistLink'])
    start_urls = links

    def parse(self, response):
        search_filter = getattr(self, 'filter', None)
        for concert in response.xpath("(//div[@id='tour_div']//p/strong)"):
            info = remove_tags(concert.extract())
            band_name = response.xpath("(//div[@id='main_page']//h3[@class='box_header']/text())").extract_first()
            if search_filter.upper() in info.upper():
                yield { band_name : info }





