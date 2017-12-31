from bs4 import BeautifulSoup 
from selenium_infinite_html_scraper import scrape_url_to_html
import json

riddle_articles = scrape_url_to_html("https://riddles.fyi/","article", 70)
# soup = BeautifulSoup(page_content, 'html.parser')
# articles = soup.find_all('article')
riddles = [] 
index = 9
# use BeautifulSoup to get the question and answer from each article elem
for article in riddle_articles:
    article = BeautifulSoup(article, 'html.parser')
    riddle_obj = {}
    riddle_obj["ID"] = str(index)
    riddle_obj['Question'] =  article.find('h2').a.string
    riddle_obj['Answer'] = article.find_all('div', class_='su-spoiler-content')[0].string
    riddles.append(riddle_obj)
    index += 1
print(json.dumps(riddles))
print("number of riddles found:", len(riddles))
