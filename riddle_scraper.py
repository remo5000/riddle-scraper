from bs4 import BeautifulSoup 
page_content = open("riddles_and_answers.html").read()
soup = BeautifulSoup(page_content, 'html.parser')
