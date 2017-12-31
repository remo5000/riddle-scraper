from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from config import path_to_chromedriver
 
def scrape_url_to_html(url, tag_name = "html", number_of_scrolls = 5):
 
    # Load WebDriver and navigate to the page url.
    # This will open a browser window.
    driver = webdriver.Chrome(path_to_chromedriver)
    driver.get(url)
     
    # First scroll to the end of the table by sending Page Down keypresses to
    # the browser window.
    result_set = set()
    for x in range(number_of_scrolls):
        # Add whatever content we can find using the element tag provided
        current_results = driver.find_elements_by_tag_name(tag_name)
        for res in current_results:
            result_set.add(res.get_attribute('innerHTML'))
        # Find the first element on the page, so we can scroll down using the
        # element object's send_keys() method
        elem = driver.find_element_by_tag_name('a')
        # Down, up, and down movement to faciliate loading
        elem.send_keys(Keys.END)
        elem.send_keys(Keys.HOME)
        elem.send_keys(Keys.END)
        # Wait 3 seconds for the infinitely loading page to load.
        sleep(3)
        elem.send_keys(Keys.END)
     
    driver.quit()
    return list(result_set) 
