import bs4         # beautiful soup module for parsing html page
import requests
import os
import wget
import xlrd
import re
last_download_file_name='MOI_ZK_last_downloaded_file.txt'
old_file=True
webpage=requests.get('http://www.mvcr.cz/mvcren/article/status-of-your-application.aspx')
webpage.raise_for_status()
webpage_soup=bs4.BeautifulSoup(webpage.text, 'html.parser')
a_elem = webpage_soup.select('#content > div > ul > li > a')
file_url_path=a_elem[0].get('href')
file_url='http://www.mvcr.cz/mvcren/'+file_url_path
print file_url
# changing the current workin directory for the download destination
download_path='/home/marko/Documents/Dokumentacija-Papiri/Scripting/Python'
os.chdir(download_path)
print "Current working directory is: " + os.getcwd()
# Download the file only if it's new, different than last one downloaded
last_downloaded_file_obj=open(last_download_file_name,'r+')
old_url=last_downloaded_file_obj.read().strip()
old_file=file_url==old_url
if old_file:
    print "\nOld file. No news. \n"
    last_downloaded_file_obj.close()
else:
    print "New file, updating url in the file..."
    last_downloaded_file_obj.seek(0)
    last_downloaded_file_obj.truncate()
    last_downloaded_file_obj.write(file_url)
    last_downloaded_file_obj.close()
    download=wget.download(file_url)            # download the file from the web site
    workbook=xlrd.open_workbook(download)       # read the xls file
    print '\n'
    ZK_sheet = workbook.sheet_by_index(1)
    print "Selected workbook sheet is: "+ ZK_sheet.name
    # checking for matching cells
    print "Checking for matching patterns... \n"
    p1=re.compile('.*3809.*')
    p2=re.compile('.*07757.*')
    for cell in ZK_sheet.col_values(1):
        match_p1=p1.match(cell)
        match_p2=p2.match(cell)
        if match_p1!=None:
            print cell
        if match_p2!=None:
            print cell
    print "\nEnd of search."

