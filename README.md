## some dependencies you need before running this program
- pip install scrapy
- pip install requests
- pip install pdfplumber

## To Start the project 
scrapy startproject kochhar
## To run the scrapy in the terminal
scrapy crawl kochhar 
## To output as JSONL format 
scrapy crawl kochhar -o output.jsonl
