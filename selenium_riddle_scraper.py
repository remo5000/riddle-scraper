from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
def scrape_url(url):
 
    # Load WebDriver and navigate to the page url.
    # This will open a browser window.
    driver = webdriver.Chrome()
    driver.get(url)
     
    urls = []
 
    # First scroll to the end of the table by sending Page Down keypresses to
    # the browser window.
    for x in range(1, 100):
        # Find the first element on the page, so we can scroll down using the
        # element object's send_keys() method
        elem = driver.find_element_by_tag_name('a')
        elem.send_keys(Keys.PAGE_DOWN)
     
    # Once the whole table has loaded, grab all the visible links.    
    articles  = driver.find_elements_by_tag_name('article')
    print(len(articles))
    #for link in visible_links:
    #    urls.append(link.get_attribute('href'))
         
    driver.quit()
           
    return urls
scrape_url("https://riddles.fyi/")
