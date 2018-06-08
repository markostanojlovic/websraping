from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# credentials @ ~/bezr
cf = open('/home/redzmaja/bezr','r')
bezr_user = cf.readline().rstrip('\n')
bezr_pass = cf.readline().rstrip('\n')
cf.close()

# Chrome
# driver = webdriver.Chrome('/usr/local/bin/chromedriver')

# PHANTOMJS
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)

driver.get('https://www.bezrealitky.cz/prihlaseni')
driver.set_window_size(1920,1080) # PHANTOMJS
driver.save_screenshot('/home/redzmaja/Pictures/startpage.png') # PHANTOMJS

# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email'"))).send_keys(bezr_user) # NOT WORKING: element not visible
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password'"))).send_keys(bezr_pass)  # NOT WORKING: element not visible
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox' and @name='conditions']"))).click()  # NOT WORKING: element not visible
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox' and @name='broker']"))).click()  # NOT WORKING: element not visible
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()  # NOT WORKING: element not visible
ins = driver.find_elements_by_xpath("//input")
ins[4].send_keys(bezr_user)
ins[5].send_keys(bezr_pass)
# driver.find_element_by_xpath("/html/body/div[2]/main/section/div/div[3]/div/div[1]/form/p[1]/label/input").click()
# driver.find_element_by_xpath("/html/body/div[2]/main/section/div/div[3]/div/div[1]/form/p[2]/label/input").click()
driver.find_element_by_xpath("/html/body/div[3]/main/section/div/div[3]/div/div[1]/form/div[5]/button").click()
time.sleep(3)
driver.save_screenshot('/home/redzmaja/Pictures/loginpage.png') # PHANTOMJS

driver.get('https://www.bezrealitky.cz/')
driver.find_element_by_xpath("//a[@id='dropdownAdvertisement']").click()
driver.find_element_by_xpath("//span[@id='a-type-pronajem']").click()
driver.find_element_by_xpath("//span[text()='Typ nemovitosti:']/parent::div//a").click()
driver.find_element_by_xpath("//label[@for='a-type-byt']").click()
driver.find_element_by_xpath("//input[@id='location']").send_keys('praha')
driver.find_element_by_xpath('/html/body/div[3]/main/section[1]/div/div/form/div[1]/div/div[4]/div/button').click()
time.sleep(3)
driver.save_screenshot('/home/redzmaja/Pictures/search_basic.png') # PHANTOMJS
driver.find_element_by_xpath("//input[@id='priceTo']").send_keys('10000')
driver.find_element_by_xpath("//*[@id='search-content']/form/div/div[2]/div[1]/div[6]/div/div/a").click()
driver.find_element_by_xpath("//input[@id='disposition-garsoniera']/parent::label").click()
driver.find_element_by_xpath("//input[@id='disposition-1-kk']/parent::label").click()
driver.find_element_by_xpath("//input[@id='disposition-1-1']/parent::label").click()
driver.find_element_by_xpath("//input[@id='disposition-2-kk']/parent::label").click()
driver.find_element_by_xpath("//input[@id='disposition-2-1']/parent::label").click()
driver.find_element_by_xpath("//button[text()='Vyhledat']").click()
time.sleep(3)
number_of_ads = int(driver.find_element_by_xpath("//strong[text()='Nalezeno ']/span").text)
print("Pronadjeno oglasa: %s" %number_of_ads)
driver.save_screenshot('/home/redzmaja/Pictures/search_res_1.png') # PHANTOMJS

# get all links and put them in a file
offer_links_file = open('bezrealitky_offer_urls','a')
for i in range(0, number_of_ads/15):
    driver.find_element_by_xpath("//button[contains(text(), 'Zobrazit')]").click()
    time.sleep(20) # TODO how to adaptivly wait for page content loading?
offer_links = driver.find_elements_by_xpath("//div[@id='search-content']//div[@class='mb-20']//a[@class='product__link js-product-link']")
if len(offer_links) != number_of_ads:
    print("Error: Number of links (%d) not match number of ads (%d) ." %(len(offer_links),number_of_ads))
for elem in offer_links:
    offer_links_file.write(elem.get_attribute('href')+'\n')
offer_links_file.close()
driver.close()
