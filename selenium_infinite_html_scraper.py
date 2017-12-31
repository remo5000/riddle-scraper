from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from config import path_to_chromedriver
 
def scrape_url_to_html(url, number_of_scrolls = 30):
 
    # Load WebDriver and navigate to the page url.
    # This will open a browser window.
    driver = webdriver.Chrome(path_to_chromedriver)
    driver.get(url)
     
    # First scroll to the end of the table by sending Page Down keypresses to
    # the browser window.
    for x in range(number_of_scrolls):
        # Find the first element on the page, so we can scroll down using the
        # element object's send_keys() method
        elem = driver.find_element_by_tag_name('a')
        elem.send_keys(Keys.PAGE_DOWN)
        # Wait 3 seconds for the infinitely loading page to load.
        sleep(3)
     
    # Once the whole table has loaded, grab all the riddles 
    html_string = driver.page_source
    driver.quit()
    return html_string
