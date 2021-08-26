from pywinauto import application, WindowSpecification, findwindows, mouse, timings
from pywinauto.keyboard import send_keys
import pandas as pd

if __name__ == '__main__':
    timings.Timings.fast()
    app = application.Application()
    app.start('C://Users//20605//Desktop//CIMitarReport//Amkor.CIMitarReport.exe', timeout=60)
    app.CIMitarReport.child_window(auto_id='pb_login').click()

    ##Waiting until login
    LOGON_CNT = 0
    while(LOGON_CNT == 0):
        try:
            info = findwindows.find_element(title='CIMitarReport 3')
            LOGON_CNT +=1

        except:
            print("CIMitarReport 3 is loading, please wait...")

    app = application.Application(backend='uia').connect(title='CIMitarReport 3')
    app.CIMitarReport_3.child_window(auto_id='YieldReport')
    app.CIMitarReport_3.menu_select("ATK->REPORT->YIELD REPORT")

    ##Customer input
    YieldReport = app.CIMitarReport_3.child_window(auto_id='YieldReport')
    CmbCustomer = YieldReport.child_window(auto_id='cmbCustomer')
    CmbCustomer.click_input()
    CmbCustomer.select("[531] NVIDIA INT")
    YieldReport.child_window(auto_id='btnDeviceSearch').click_input()

    ##Device_Search_btn Click
    YieldReport.child_window(auto_id='gridDeviceList').child_window(class_name='WindowsForms10.BUTTON.app.0.13965fa_r7_ad1').click_input()

    ##Set DateTime
    YieldReport.child_window(auto_id='panel7').child_window(auto_id='dateTimeStart').click_input()
    send_keys("{TAB}""{VK_RIGHT}""{VK_RIGHT}""18""25")

    ##device serach_btn
    YieldReport.child_window(auto_id='btnLotSearch').click_input()

    ##lot process list search_btn
    YieldReport.child_window(auto_id='gridLotList').child_window(class_name='WindowsForms10.BUTTON.app.0.13965fa_r7_ad1').click_input()

    ##click add_btn
    YieldReport.maximize()
    YieldReport.child_window(auto_id='btnDetailSearch').click_input()

    ##cmbReportFormat Select
    CmbReportFormat = YieldReport.child_window(auto_id='cmbReportFormat')
    CmbReportFormat.click_input()
    CmbReportFormat.select("NVIDIA_AST")

    #All Bin_select
    YieldReport.child_window(auto_id='chkAllBin').click_input()

    #Select All Lot Process File List
    YieldReport.child_window(auto_id='gridDetailLotList').child_window(class_name='WindowsForms10.BUTTON.app.0.13965fa_r7_ad1').click_input()

    #Excel btn click
    YieldReport.child_window(auto_id='cmdExcel').click_input()

    #Save_File
    send_keys("C:\\Users\\20605\\PycharmProjects\\pythonProject\\CIMITAR_REPORT\\test_file.xlsx""{ENTER}""{TAB}""{ENTER}")
    XLSX_FILE = "C:\\Users\\20605\\PycharmProjects\\pythonProject\\CIMITAR_REPORT\\test_file.xlsx"

    ##Waiting until saving Excel
    SAVE_FIN = 0
    while (SAVE_FIN == 0):
        try:
            df = pd.read_excel(XLSX_FILE)
            SAVE_FIN += 1

        except: pass

    print(df.head(10))

    exit()