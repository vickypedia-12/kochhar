import scrapy
from ..items import KochharItem
import requests
import pdfplumber
import os
import io


class KochharSpider(scrapy.Spider):
    name = "kochhar"
    start_urls = [
        "https://kochhar.com/knowledge-centre/"
    ]
    
    def parse(self, response) :
        # print(response.text)
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
        
        def scrapePdfFromUrl(url):
            response = requests.get(url)
            response.raise_for_status()
            text_contents = ''
            with pdfplumber.open(io.BytesIO(response.content)) as pdf:
                for page in pdf.pages:
                    text_contents += page.extract_text()
            return text_contents
        
        items['Title'] = title
        items['Publication_Date'] = date
        items['URL'] = url
        items['Content'] = scrapePdfFromUrl(url)
        
        yield items
