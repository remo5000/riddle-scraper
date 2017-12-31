from bs4 import BeautifulSoup 
page_content = open("riddles_and_answers.html").read()
soup = BeautifulSoup(page_content, 'html.parser')
articles = soup.find_all('article')
riddles = {}
for article in articles:
    question = article.find('h2').a.string
    answer = article.find_all('div', class_='su-spoiler-content')[0].string
    riddles[question] = answer
print(riddles)
