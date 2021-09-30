import sys
import PyQt5.uic
import time
from selenium import webdriver
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import win32com.client
import os
import getpass

form_class = PyQt5.uic.loadUiType("test.ui")[0]

#
HRD_ID = "hisg1201"
HRD_PW = "h108109h!@#"

#
OJT_ID = "hisg1201"
OJT_PW = "h108109h"

#
PMS_ID = "20605"
PMS_PW = "H108109h!@#"

today_Mon = datetime.today().strftime('%m')
YEAR, WEEK, DAY = datetime.now().isocalendar()
path = "./testui"

def CaculateMealTime():
    hour = int(datetime.now().time().strftime('%H'))
    if hour >= 0 and hour <= 8: return "조식"
    if hour >= 9 and hour <= 12: return "중식"
    if hour >= 13 and hour <= 18: return "석식"
    if hour >= 19 and hour <= 24: return "야식"

def SearchMonthBtn(month):
    month_btn_dict = {"02": 1, "01": 2, "12": 3, "11": 4, "10": 5, "09": 6, "08": 7}
    return month_btn_dict[month]

def MealBring(day):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options= options)
    url = f"https://intranet.amkor.co.kr/app/service/carte/view/detail?plant=S&year=2021&week={WEEK}"
    driver.get(url)

    br_k_food = driver.find_element_by_xpath(f"//tbody/tr[2]/td[{day+2}]").text
    br_j_food = driver.find_element_by_xpath(f"//tbody/tr[3]/td[{day+1}]").text
    br_i_food = driver.find_element_by_xpath(f"//tbody/tr[4]/td[{day+1}]").text
    br_p_food = driver.find_element_by_xpath(f"//tbody/tr[5]/td[{day+1}]").text

    lu_k_food = driver.find_element_by_xpath(f"//tbody/tr[6]/td[{day + 2}]").text
    lu_j_food = driver.find_element_by_xpath(f"//tbody/tr[7]/td[{day + 1}]").text
    lu_i_food = driver.find_element_by_xpath(f"//tbody/tr[8]/td[{day + 1}]").text
    lu_p_food = driver.find_element_by_xpath(f"//tbody/tr[9]/td[{day + 1}]").text

    di_k_food = driver.find_element_by_xpath(f"//tbody/tr[10]/td[{day + 2}]").text
    di_j_food = driver.find_element_by_xpath(f"//tbody/tr[11]/td[{day + 1}]").text
    di_i_food = driver.find_element_by_xpath(f"//tbody/tr[12]/td[{day + 1}]").text
    di_p_food = driver.find_element_by_xpath(f"//tbody/tr[13]/td[{day + 1}]").text

    ni_k_food = driver.find_element_by_xpath(f"//tbody/tr[14]/td[{day + 2}]").text
    ni_j_food = driver.find_element_by_xpath(f"//tbody/tr[15]/td[{day + 1}]").text
    ni_i_food = driver.find_element_by_xpath(f"//tbody/tr[16]/td[{day + 1}]").text
    ni_p_food = driver.find_element_by_xpath(f"//tbody/tr[17]/td[{day + 1}]").text

    driver.quit()
    return br_k_food, br_j_food, br_i_food, br_p_food, \
           lu_k_food, lu_j_food, lu_i_food, lu_p_food, \
           di_k_food, di_j_food, di_i_food, di_p_food,\
           ni_k_food, ni_j_food, ni_i_food, ni_p_food

def ClosePopUp(CPdriver):
    # Close pop-up window
    main = CPdriver.window_handles
    for handle in main:
        if handle != main[0]:
            CPdriver.switch_to.window(handle)
            CPdriver.close()

def SetDefaultMealType(handler):
    # Set Default MealType
    mealtime = CaculateMealTime()
    handler.comboBox_mealtype.setCurrentText(mealtime)
    if mealtime == "조식":
        handler.label_k.setText(BR_k_food)
        handler.label_j.setText(BR_j_food)
        handler.label_c.setText(BR_i_food)
        handler.label_p.setText(BR_p_food)

        handler.label_k.setFont(QtGui.QFont("Arial", 8))
        handler.label_j.setFont(QtGui.QFont("Arial", 8))
        handler.label_c.setFont(QtGui.QFont("Arial", 6))
        handler.label_p.setFont(QtGui.QFont("Arial", 6))

    if mealtime == "중식":
        handler.label_k.setText(LU_k_food)
        handler.label_j.setText(LU_j_food)
        handler.label_c.setText(LU_i_food)
        handler.label_p.setText(LU_p_food)

        handler.label_k.setFont(QtGui.QFont("Arial", 8))
        handler.label_j.setFont(QtGui.QFont("Arial", 8))
        handler.label_c.setFont(QtGui.QFont("Arial", 6))
        handler.label_p.setFont(QtGui.QFont("Arial", 6))

    if mealtime == "석식":
        handler.label_k.setText(DI_k_food)
        handler.label_j.setText(DI_j_food)
        handler.label_c.setText(DI_i_food)
        handler.label_p.setText(DI_p_food)

        handler.label_k.setFont(QtGui.QFont("Arial", 8))
        handler.label_j.setFont(QtGui.QFont("Arial", 8))
        handler.label_c.setFont(QtGui.QFont("Arial", 6))
        handler.label_p.setFont(QtGui.QFont("Arial", 6))

    if mealtime == "야식":
        handler.label_k.setText(NI_k_food)
        handler.label_j.setText(NI_j_food)
        handler.label_c.setText(NI_i_food)
        handler.label_p.setText(NI_p_food)

        handler.label_k.setFont(QtGui.QFont("Arial", 8))
        handler.label_j.setFont(QtGui.QFont("Arial", 8))
        handler.label_c.setFont(QtGui.QFont("Arial", 6))
        handler.label_p.setFont(QtGui.QFont("Arial", 6))

#UI이벤트 처리
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_HRD_net.clicked.connect(self.ConnectHRDnet)   # Connect HRD_net
        self.pushButton_OJT.clicked.connect(self.ConnectOJT) # Connect OJT
        self.pushButton_AmkorIntranet.clicked.connect(self.ConnectAmkorIntranet) # Connect AmkorIntranet
        self.pushButton_AmkorPMS.clicked.connect(self.ConnectAmkorPMS)  # Connect AmkorPMS
        # self.pushButton_Setting.clicked.connect(self.SettingAutoLogin)
        self.comboBox_mealtype.currentTextChanged.connect(self.ConnectMealType)


        global BR_k_food, BR_j_food, BR_i_food, BR_p_food,\
            LU_k_food, LU_j_food, LU_i_food, LU_p_food, \
            DI_k_food, DI_j_food, DI_i_food, DI_p_food,\
            NI_k_food, NI_j_food, NI_i_food, NI_p_food

        BR_k_food, BR_j_food, BR_i_food, BR_p_food, \
        LU_k_food, LU_j_food, LU_i_food, LU_p_food, \
        DI_k_food, DI_j_food, DI_i_food, DI_p_food, \
        NI_k_food, NI_j_food, NI_i_food, NI_p_food = MealBring(DAY)

        SetDefaultMealType(self)

    # def SettingAutoLogin(self):
    #     pwd = getpass.getpass(prompt='Password: ')
    #     df = pd.read_excel('AutoSetting.xlsx', Password= pwd)
    #     print(df)

    def ConnectMealType(self):
        mealtime = self.comboBox_mealtype.currentText()
        if mealtime == "조식":
            self.label_k.setText(BR_k_food)
            self.label_j.setText(BR_j_food)
            self.label_c.setText(BR_i_food)
            self.label_p.setText(BR_p_food)

            self.label_k.setFont(QtGui.QFont("Arial",8))
            self.label_j.setFont(QtGui.QFont("Arial", 8))
            self.label_c.setFont(QtGui.QFont("Arial", 6))
            self.label_p.setFont(QtGui.QFont("Arial", 6))

        if mealtime == "중식":
            self.label_k.setText(LU_k_food)
            self.label_j.setText(LU_j_food)
            self.label_c.setText(LU_i_food)
            self.label_p.setText(LU_p_food)

            self.label_k.setFont(QtGui.QFont("Arial",8))
            self.label_j.setFont(QtGui.QFont("Arial", 8))
            self.label_c.setFont(QtGui.QFont("Arial", 6))
            self.label_p.setFont(QtGui.QFont("Arial", 6))

        if mealtime == "석식":
            self.label_k.setText(DI_k_food)
            self.label_j.setText(DI_j_food)
            self.label_c.setText(DI_i_food)
            self.label_p.setText(DI_p_food)

            self.label_k.setFont(QtGui.QFont("Arial",8))
            self.label_j.setFont(QtGui.QFont("Arial", 8))
            self.label_c.setFont(QtGui.QFont("Arial", 6))
            self.label_p.setFont(QtGui.QFont("Arial", 6))

        if mealtime == "야식":
            self.label_k.setText(NI_k_food)
            self.label_j.setText(NI_j_food)
            self.label_c.setText(NI_i_food)
            self.label_p.setText(NI_p_food)

            self.label_k.setFont(QtGui.QFont("Arial",8))
            self.label_j.setFont(QtGui.QFont("Arial", 8))
            self.label_c.setFont(QtGui.QFont("Arial", 6))
            self.label_p.setFont(QtGui.QFont("Arial", 6))

    def ConnectHRDnet(self):
        driver = webdriver.Chrome()
        url = "https://www.hrd.go.kr/hrdp/pa/ppaho/PPAHO0100T.do"
        driver.get(url)
        driver.find_element_by_xpath("//input[@id='userloginId']").send_keys(HRD_ID)
        driver.find_element_by_xpath("//input[@id='userloginPwd']").send_keys(HRD_PW)
        driver.find_element_by_xpath("//button[@id='loginBtn']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='qnaQ']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(text(),'학습활동서 작성')]").click()
        driver.find_element_by_xpath(f"//tbody/tr[{SearchMonthBtn(today_Mon)}]/td[4]/button[1]").click()

    def ConnectOJT(self):
        driver = webdriver.Chrome()
        url = "https://biz.amkor.co.kr/ojt/ojt_login.jsp"
        driver.get(url)
        driver.find_element_by_xpath("//input[@name='inputId']").send_keys(OJT_ID)
        driver.find_element_by_xpath("//input[@name='inputPwd']").send_keys(OJT_PW)
        driver.find_element_by_xpath("//img[@src='../img/ojt-img/btn.png']").click()
        driver.find_element_by_xpath("//input[@value='클릭']").click()
        driver.find_element_by_xpath("//input[@value='편집']").click()

    def ConnectAmkorIntranet(self):
        driver = webdriver.Chrome()
        url = "https://intranet.amkor.co.kr/index.jsp"
        driver.get(url)

        driver.find_element_by_xpath("//input[@name='input_id']").send_keys(OJT_ID)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(OJT_PW)
        driver.find_element_by_xpath("//input[@type='image']").click()

        ClosePopUp(driver)

    def ConnectAmkorPMS(self):
        driver = webdriver.Chrome()
        url = "https://pms.amkor.co.kr"
        driver.get(url)

        driver.find_element_by_xpath("//input[@name='loginId']").send_keys(PMS_ID)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(PMS_PW)
        driver.find_element_by_xpath("//a[contains(text(),'로그인')]").click()

        ClosePopUp(driver)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()