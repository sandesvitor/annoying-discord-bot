from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep


options = Options()
options.headless = True
options.executable_path = "/usr/local/bin/geckodriver"
# options.binary_path = "/usr/local/bin/geckodriver"
firefox = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")


apology_url = r'https://apologygenerator.com/'

def get_apology():
    firefox.get(apology_url)
    apology_text = firefox.find_element_by_tag_name('p').get_attribute('innerHTML')
    firefox.close()
    return apology_text

