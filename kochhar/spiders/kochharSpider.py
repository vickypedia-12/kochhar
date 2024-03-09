import scrapy
from ..items import KochharItem
import requests
import pdfplumber
import os
import io

class KochharSpider(scrapy.Spider):
    name = "kochhar"
    page_number  = 2
    start_urls = [
        "https://kochhar.com/knowledge-centre/page/1"
    ]
    
    def parse(self, response) :
        # print(response.text)
        allDivCards = response.css('div.col-xs-12.col-sm-4.col-md-3')
        for cards in allDivCards:
            url = cards.css('.language a::attr(href)').get()
            title = cards.css('.content-section h5::text, .content-section p:nth-child(3)::text').get()
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
        
        next_page = "https://kochhar.com/knowledge-centre/page/"+ str(KochharSpider.page_number) + "/"
        if KochharSpider.page_number <= 27:
            KochharSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        
        
