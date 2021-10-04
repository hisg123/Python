import datetime
import os
import sys
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtWidgets import *
import PyQt5.uic
import shutil
from tqdm import tqdm
from fpdf import FPDF

#pyrcc5 -o MBC_res_rc.py MBC_res.qrc

form_class = PyQt5.uic.loadUiType("MakeBC.ui")[0]
today = datetime.datetime.today().strftime('%Y%m%d')
path = f'./image/{today}'

def SplitKrEn(string_):
    list_ = str(string_).split('/')
    return list_

def AddingMsg(message_, yPos, font, fontsize, draw):
    color = 'rgb(0, 0, 0)'
    malgun = ImageFont.truetype(font, fontsize)
    w, h = malgun.getsize(message_)
    xPos = (821 - w) / 2
    draw.text((xPos, yPos), message_, fill=color, font=malgun)

def TexttoIMG(name, position, department, location, tell, cell, email):
    width = 821
    height = 455

    image = Image.new('RGB', (width, height), (255, 255, 255))

    tempimg = Image.open("example_google.png")
    tempidback = tempimg.resize((width, height), Image.NEAREST)
    tempidback.save('tempidback.png')
    tempidback = Image.open('tempidback.png')

    image.paste(tempidback)
    draw = ImageDraw.Draw(image)

    #split KR,EN
    name_list = SplitKrEn(name)
    position_list = SplitKrEn(position)
    department_list = SplitKrEn(department)
    location_list = SplitKrEn(location)

    # adding name
    (x, y) = (0, 200)

    username = name_list[0]
    img_username = ''
    if(len(username)==3):
        for i in range(len(username)):
            if(i==0):
                img_username = username[i]
            else:
                img_username += '  ' + username[i]
        message = img_username

    elif(len(username)==2):
        for i in range(len(username)):
            if(i==0):
                img_username = username[i]
            else:
                img_username += '   ' + username[i]
        message = img_username
    else:
        message = username

    start_Ypos = y
    font = 'malgunbd.ttf'
    fontsize = 30
    AddingMsg(message, start_Ypos, font, fontsize, draw)

    #adding department | position
    message = f"{department_list[0]} | {position_list[0]}"
    start_Ypos += 50
    font = 'malgun.ttf'
    fontsize = 18
    AddingMsg(message, start_Ypos, font, fontsize, draw)

    #adding LABEL
    message = "Google Inc™"
    start_Ypos += 50
    font = 'malgunbd.ttf'
    fontsize = 18
    AddingMsg(message, start_Ypos, font, fontsize, draw)

    # adding location
    message = location_list[0]
    start_Ypos += 30
    font = 'malgun.ttf'
    fontsize = 18
    AddingMsg(message, start_Ypos, font, fontsize, draw)

    # adding tell&cell
    message = f"tel {tell} | cell {cell}"
    start_Ypos += 30
    font = 'malgun.ttf'
    fontsize = 18
    AddingMsg(message, start_Ypos, font, fontsize, draw)

    #adding email
    message = email
    start_Ypos += 30
    font = 'malgun.ttf'
    fontsize = 18
    AddingMsg(message, start_Ypos, font, fontsize, draw)

    image.save(f"{path}/{name_list[0]}_front.png")

def imageMerge():
    IMG_LIST = []
    FILE_LIST = os.listdir(path)

    for file in FILE_LIST:
        ext, ext_png = os.path.splitext(file)
        if ext[0:9] == 'mergedPDF':
            pass
        elif ext_png == '.png':
            IMG_LIST.append(file)

    TotalSize_x = 2463
    TotalSize_y = 1365
    Size_x = 821
    Size_y = 455
    Merge_image = []

    if len(IMG_LIST)%9: LEN = len(IMG_LIST)//9 + 1
    else: LEN = len(IMG_LIST)//9
    # print(LEN)

    for i in range(LEN):
        Merge_image.append(Image.new("RGB", (TotalSize_x, TotalSize_y), (255, 255, 255)))
    print(Merge_image)

    file_no = 0
    cnt = 0
    for index in range(len(IMG_LIST)):
        if cnt == 9:
            Merge_image[file_no].save(f"{path}/mergedPDF_{file_no}.png", "PNG")
            file_no += 1
            cnt = 0

        Y_idx = index//3 - 3*file_no
        # print(index, Y_idx, file_no)
        merge_area = (((index%3) * Size_x), (Y_idx * Size_y), (((index%3)+1) *Size_x), ((Y_idx+1) * Size_y))
        PasteImage = Image.open(f"{path}/{IMG_LIST[index]}")
        Merge_image[file_no].paste(PasteImage, merge_area)
        if file_no == LEN-1:
            Merge_image[file_no].save(f"{path}/mergedPDF_{file_no}.png", "PNG")
        cnt +=1

def PdfConvert(directory):
    MERGED_IMG_LIST = []
    FILE_LIST = os.listdir(path)
    for file in FILE_LIST:
        ext = os.path.splitext(file)[0]
        if ext[0:9] == 'mergedPDF':
            MERGED_IMG_LIST.append(file)

    i = 0
    for merged_image in tqdm(MERGED_IMG_LIST, desc='이미지 파일을 PDF로 저장 중입니다.', leave=False):
        pdf = FPDF(orientation='L', unit='cm', format='A4')
        pdf.add_page()

        merged_image = f'{path}/{merged_image}'
        pdf.image(merged_image, x=0, y=0, w=29.7, h=16.46)
        pdf.output(f'{directory}/{today}_{i}.pdf', 'F')
        i += 1

##오늘날짜로 폴더생성
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            shutil.rmtree(directory)
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_openfile.clicked.connect(self.openFileNamesDialog)   # 파일 올리기
        self.pushButton_savefile.clicked.connect(self.saveFileDialog)       # 저장경로 설정하기
        self.pushButton_run.clicked.connect(self.RunProgram)               # 프로그램 실행하기
        self.pushButton_close.clicked.connect(self.close)  # 취소하기

    def openFileNamesDialog(self):
        # 파일 여러개 불러오기
        files = QFileDialog.getOpenFileName(None, "Open Excel File", '.', "(*.xlsx)")[0]

        if files:
            self.lineEdit_openfile.setText(files)
            global frames
            frames = pd.read_excel(files)

    def saveFileDialog(self):
        global OutputPath
        OutputPath = QFileDialog.getExistingDirectory()
        self.lineEdit_savefile.setText(OutputPath)

    def RunProgram(self):
        createFolder(path)

        name = frames['이름']
        position = frames['직책']
        department = frames['부서']
        location = frames['위치']
        tell = frames['tell']
        cell = frames['cell']
        email = frames['email']

        for i in tqdm(range(len(name)), desc = '명함 제작중입니다.', leave= False):
            TexttoIMG(name[i], position[i], department[i], location[i], tell[i], cell[i], email[i])

        imageMerge()
        PdfConvert(path)

        try:
            PdfConvert(OutputPath)
            QMessageBox.about(self, "message", "저장경로 폴더, image 폴더 안에 PDF 파일이 생성되었습니다")

        except:
            QMessageBox.about(self, "message", "image 폴더 안에 PDF 파일이 생성되었습니다")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()