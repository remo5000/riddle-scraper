from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from config import path_to_chromedriver
 
def scrape_url(url):
 
    # Load WebDriver and navigate to the page url.
    # This will open a browser window.
    driver = webdriver.Chrome(path_to_chromedriver)
    driver.get(url)
     
    urls = []
 
    # First scroll to the end of the table by sending Page Down keypresses to
    # the browser window.
    for x in range(1, 10):
        # Find the first element on the page, so we can scroll down using the
        # element object's send_keys() method
        elem = driver.find_element_by_tag_name('a')
        elem.send_keys(Keys.PAGE_DOWN)
        sleep(3)
     
    # Once the whole table has loaded, grab all the visible links.    
    articles  = driver.find_elements_by_tag_name('article')
    print(len(articles))
    #for link in visible_links:
    #    urls.append(link.get_attribute('href'))
         
    driver.quit()
           
    return urls
scrape_url("https://riddles.fyi/")
