from bs4 import BeautifulSoup 
from selenium_infinite_html_scraper import scrape_url_to_html

riddle_articles = scrape_url_to_html("https://riddles.fyi/","article", 14)
# soup = BeautifulSoup(page_content, 'html.parser')
# articles = soup.find_all('article')
riddles = {}
for article in riddle_articles:
    article = BeautifulSoup(article, 'html.parser')
    question = article.find('h2').a.string
    answer = article.find_all('div', class_='su-spoiler-content')[0].string
    riddles[question] = answer
print(riddles)
print("number of riddles found:", len(riddles))
