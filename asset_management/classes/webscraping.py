from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import warnings
   
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

class WebScraping:
    def get_asset_price(self, portfolio):
        browser = webdriver.Chrome(
            r'C:\Users\nicol\Desktop\Coding\Projects\Asset_Management\asset_management\chromedriver.exe')
        for key in portfolio:
            browser.get('https://www.google.com.br/')
            browser.find_element(
                By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação {}'.format(key))
            browser.find_element(
                By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
            price = browser.find_element(
                By.XPATH, '//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]').text
            price_adjusted = price.replace(',', '.')
            asset_values_list = portfolio[key]
            asset_values_list[2] = price_adjusted
        browser.close()           
        return portfolio


