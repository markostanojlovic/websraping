import requests
from bs4 import BeautifulSoup
import os
import wget
import xlrd
import re
webpage = requests.get('http://www.mvcr.cz/clanek/informace-o-stavu-rizeni.aspx')
webpage.raise_for_status()
soup = BeautifulSoup(webpage.text, 'html.parser')
download_url = soup.select('#content > div > ul > li > a')
file_path = download_url[0].get('href')
file_url = 'http://www.mvcr.cz/' + file_path
download_path = '/home/mstan/Downloads/tp'
start_cwd = os.getcwd()
os.chdir(download_path)
download = wget.download(file_url)
workbook = xlrd.open_workbook(download)
trvale_pobyty_sheet = workbook.sheet_by_name('Trvalé pobyty')
pattern = re.compile('.*OAM-10697.*')
for cell in trvale_pobyty_sheet.col_values(1):
    if pattern.match(cell):
        print('\nCONGRATULATIONS! Your application is approved : {}'.format(cell))
os.remove(os.listdir()[0])
os.chdir(start_cwd)