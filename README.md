# LAB - Class 17
## Project: web-scraper
### Author: Ibraheem Areeda


### Setup
- create .env environment 
- to install all requrments : `pip install -r requirements.txt`

**run the application** by typing in the teminal `python web_scraper/scraper.py` you must be in the root of the repo


**How to use this module** 
to use scraper.py you have 2 function:
 1. get_citations_needed_count
 get_citations_needed_count(url), takes a URL as input and retrieves the webpage content using the requests library. It then uses the BeautifulSoup library to parse the HTML content of the webpage. The function searches for all occurrences of the text "citation needed" wrapped in a <span> tag and counts the number of such occurrences. Finally, it returns the count of citations needed.
  
 2. get_citations_needed_report
  get_citations_needed_report(url), performs a similar process as the first function. It retrieves the webpage content and parses it using BeautifulSoup. It searches for all occurrences of the text "citation needed" wrapped in a <span> tag. For each occurrence, it appends the parent elements' text (four levels up from the <span> tag) to a string. The function then returns the accumulated string, which represents a report of all the sections or sentences that require citations in the webpage. The report is formatted with line breaks between each section or sentence.
  
### Tests
 
 

