from selenium import webdriver
from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True
firefox = webdriver.Firefox(options=options)


apology_url = r'https://apologygenerator.com/'

def get_apology():
    firefox.get(apology_url)
    apology_text = firefox.find_element_by_tag_name('p').get_attribute('innerHTML')
    firefox.close()
    return apology_text

