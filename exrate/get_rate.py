from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)
url = 'http://www.xe.com/currencycharts/?from=EUR&to=CZK'  
driver.get(url)
rates_div_strong = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='rates_detail_desc']/strong[2]")))
rate = rates_div_strong.text
print(rate)
