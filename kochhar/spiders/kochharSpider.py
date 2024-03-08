from typing import ItemsView
import scrapy
from datetime import datetime
from ..items import KochharItem
import requests
import pdfplumber

class kochharSpider(scrapy.Spider):
    name = 'kochhar'
    start_urls = [
        'https://kochhar.com/knowledge-centre'
    ]
    
    
    def parse(self, response) :
        allDivCards = response.css('div.col-xs-12.col-sm-4.col-md-3')
        for cards in allDivCards:
            title = cards.css('h5 a::text').get()
            url = cards.css('h5 a').xpath("@href").get()
            date = cards.css('.date::text').get()
            yield scrapy.Request(url,callback=self.parse_document, meta={'title': title,'date': date})
            
    def parse_document(self, response):
        items = KochharItem()
        title = response.meta['title']
        date = response.meta['date']
        url = response.url 
        
        response = requests.get(url)
        response.raise_for_status()
        
        
        items['Title'] = title
        items['Publication_Date'] = date
        items['URL'] = url
        
        yield items