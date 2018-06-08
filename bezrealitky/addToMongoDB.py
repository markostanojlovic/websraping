#python36
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from pprint import pprint
# TODO take ad URL as argument to a script or make script to be a function 
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.bezrealitky.cz/nemovitosti-byty-domy/404359-nabidka-pronajem-bytu')
table = driver.find_element_by_xpath("//th[text()='Číslo inzerátu:']//ancestor::tbody")
keys = table.find_elements_by_xpath("//th")
data = {}
for key in keys:
    data_key = key.text
    data_value = table.find_element_by_xpath("//th[contains(text(), '" + data_key + "')]/following-sibling::td").text
    data[data_key] = data_value
    print(data_key + " : " + data_value)

pprint(data)

# connecting to a mongodb
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test_database # get a db 
collection = db.test_collection # get a collection 
insert_result = collection.insert_one(data) # insert one document 
insert_result.inserted_id
db.collection_names(include_system_collections=False) # list all collections in the db 
pprint(collection.find_one({'Číslo inzerátu:': '404359'}))