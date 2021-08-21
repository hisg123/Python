from selenium import webdriver
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, Border, Side, PatternFill

driver = webdriver.Chrome()
url = 'https://www.naver.com'
driver.get(url)

driver.find_element_by_xpath('//input[@class="input_text"]').send_keys('인텔')
driver.find_element_by_xpath('//button[@class="btn_submit"]').click()
driver.find_element_by_xpath('//body/div[@id="wrap"]/div[@id="header_wrap"]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/a[1]').click()
driver.find_element_by_xpath('//body/div[@id="wrap"]/div[@id="container"]/div[@id="content"]/div[@id="main_pack"]/div[@id="snb"]/div[1]/div[1]/div[1]/a[2]').click()

span_list = []
span_temp = []
press_list = []
press_temp = []
title_list = []
title_temp = []
context_list = []
context_temp = []

cnt = 10
while(cnt!=0):
    #span
    span_list = driver.find_elements_by_xpath('//span[@class="info"]')
    for span in span_list:
        span_temp.append(span.text)

    #press
    press_list = driver.find_elements_by_xpath('//a[@class="info press"]')
    for press in press_list:
        press_temp.append(press.text)

    #title
    title_list = driver.find_elements_by_xpath('//a[@class="news_tit"]')
    for title in title_list:
         title_temp.append(title.text)

    #context
    context_list = driver.find_elements_by_xpath('//body/div[@id="wrap"]/div[@id="container"]/div[@id="content"]/div[@id="main_pack"]/section[1]/div[1]/div[2]/ul[1]/li/div[1]/div[1]/div[2]/div[1]/a[1]')
    for context in context_list:
        context_temp.append(context.text)

    driver.find_element_by_xpath('//i[contains(text(),"다음")]').click()
    cnt -= 1

temp = [[] for j in range(len(span_temp))]

for i in range(len(press_temp)):
    temp[i].append(span_temp[i])
    temp[i].append(press_temp[i])
    temp[i].append(title_temp[i])
    temp[i].append(context_temp[i])

# control size of row and column
write_wb = Workbook()
write_ws = write_wb.active

write_ws.column_dimensions['A'].width = 10
write_ws.column_dimensions['B'].width = 30
write_ws.column_dimensions['C'].width = 80
write_ws.column_dimensions['D'].width = 200

for i in range(1,5):
    cell = write_ws.cell(row=1, column=i)
    cell.alignment = Alignment(horizontal='center')

write_ws['A1'] = '시간'
write_ws['B1'] = '언론사'
write_ws['C1'] = '제목'
write_ws['D1'] = '내용'

for i in temp:
    write_ws.append(i)

write_wb.save('C:/Users/USER/PycharmProjects/pythonProject(Crawling)/인텔.xlsx')
