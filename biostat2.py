import requests
from bs4 import BeautifulSoup
import xlsxwriter
outWorkbook=xlsxwriter.Workbook("out2.xlsx")
outSheet=outWorkbook.add_worksheet()


vgm_url = 'http://www.cazy.org/GH29_all.html#pagination_PRINC'
html_text = requests.get(vgm_url).text
#define function for stripping html tags
def cleanhtml(htmlstuff):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', htmlstuff)
  return cleantext

soup = BeautifulSoup(html_text, 'html.parser')

a=soup.select("div b")
print(a)

import re

#output of beutiful soup finder is in bs4 tags, we convert it to strings below
paragraphs = []
for x in a:
        paragraphs.append(str(x))
#function call for html stripping
j=0

while j<len(paragraphs):
  paragraphs[j]=cleanhtml(paragraphs[j])
  j+=1

i = 6
while i < 2006:
  paragraphs[i]=0
  

  
  i += 2
  
  
print('hello world')  
 
while (paragraphs.count(0)):
  paragraphs.remove(0)



print(paragraphs)



#exporting to excel 

for item in range(len(paragraphs)):
  outSheet.write(item+1,0,paragraphs[item])


a="https://pmlegacy.ncbi.nlm.nih.gov/protein/"
b="?report=fasta"

k=15




#begin selenium section for amino acids

from selenium import webdriver
from bs4 import BeautifulSoup
#DRIVER_PATH = '/path/to/chromedriver'
#driver = webdriver.Chrome("C:\Users\kevin\Downloads\chromedriver_win32\chromedriver.exe")
#driver.get('https://google.com')



chromedriver = "C:\\Users\\kevin\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome("C:\\Users\\kevin\\Downloads\\chromedriver_win32\\chromedriver.exe")


x='https://pmlegacy.ncbi.nlm.nih.gov/protein/'
y='?report=fasta'

k=20
z=1


q = [None] * 50
while k<23:
  chromedriver = "C:\\Users\\kevin\\Downloads\\chromedriver_win32\\chromedriver.exe"
  driver = webdriver.Chrome("C:\\Users\\kevin\\Downloads\\chromedriver_win32\\chromedriver.exe")
  url=x+paragraphs[k]+y
  driver.get(url)
  
  html = driver.page_source

  all_links = driver.find_element_by_tag_name('pre')

  q[z]=all_links.text
  z+=1
  k+=1


print(q)






outWorkbook.close()