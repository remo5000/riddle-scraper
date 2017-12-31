from bs4 import BeautifulSoup 
from selenium_infinite_html_scraper import scrape_url_to_html

page_content = scrape_url_to_html("https://riddles.fyi/", 5)
soup = BeautifulSoup(page_content, 'html.parser')
articles = soup.find_all('article')
riddles = {}
for article in articles:
    question = article.find('h2').a.string
    answer = article.find_all('div', class_='su-spoiler-content')[0].string
    riddles[question] = answer
print(riddles)
