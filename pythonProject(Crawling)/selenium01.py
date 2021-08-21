from selenium import webdriver
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus

driver = webdriver.Chrome()
url = 'https://www.naver.com'
driver.get(url)

driver.find_element_by_xpath('//input[@class="input_text"]').send_keys('인텔')
driver.find_element_by_xpath('//button[@class="btn_submit"]').click()
driver.find_element_by_xpath('//body/div[@id="wrap"]/div[@id="header_wrap"]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/a[1]').click()
driver.find_element_by_xpath('//body/div[@id="wrap"]/div[@id="container"]/div[@id="content"]/div[@id="main_pack"]/div[@id="snb"]/div[1]/div[1]/div[1]/a[2]').click()

#span
span_list = []
span_list = driver.find_elements_by_xpath('//span[@class="info"]')
span_temp = []
for i in span_list:
    span_temp.append(i.text)

#press
press_list = []
press_list = driver.find_elements_by_xpath('//a[@class="info press"]')
press_temp =[]
for i in press_list:
    press_temp.append(i.text)

#title
title_list = []
title_list = driver.find_elements_by_xpath('//a[@class="news_tit"]')
title_temp = []
for i in title_list:
    title_temp.append(i.text)

#context
context_list = []
context_list = driver.find_elements_by_xpath('//body/div[@id="wrap"]/div[@id="container"]/div[@id="content"]/div[@id="main_pack"]/section[1]/div[1]/div[2]/ul[1]/li/div[1]/div[1]/div[2]/div[1]/a[1]')
context_temp = []
for i in context_list:
    context_temp.append(i.text)

temp = [[] for j in range(len(span_temp))]

for i in range(len(press_temp)):
    temp[i].append(span_temp[i])
    temp[i].append(press_temp[i])
    temp[i].append(title_temp[i])
    temp[i].append(context_temp[i])

f = open('앰코코리아.csv', 'w', encoding='utf-8', newline ='')
csvWriter = csv.writer(f)
for i in temp:
    csvWriter.writerow(i)

f.close()
print('완료')