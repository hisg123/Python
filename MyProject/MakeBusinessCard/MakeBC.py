import datetime
import os
import sys
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtWidgets import *
import PyQt5.uic
import shutil
from tqdm import tqdm

#pyrcc5 -o MBC_res_rc.py MBC_res.qrc

form_class = PyQt5.uic.loadUiType("MakeBC.ui")[0]
today = datetime.datetime.today().strftime('%Y%m%d')
path = f'./image/{today}'

def SplitKrEn(string_):
    list_ = str(string_).split('/')
    return list_

def TexttoIMG(name, position, department, location, tell, cell, email, dir):
    # [일반] 텍스트 이미지에 넣기
    width = 718
    height = 398

    image = Image.new('RGB', (width, height), (255, 255, 255))

    tempimg = Image.open("front_ATK.png")
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
    (x, y) = (0, 160)
    W = width

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

    color = 'rgb(0, 0, 0)'
    malgun = ImageFont.truetype('/malgunbd.ttf', 25)
    w, h = malgun.getsize(message)
    start_xPos = (W - w) / 2
    start_Ypos = y
    draw.text((start_xPos, y), message, fill=color, font=malgun)

    #adding department | position
    message = f"{department_list[0]} | {position_list[0]}"
    color = 'rgb(0, 0, 0)'
    malgun = ImageFont.truetype('/malgun.ttf', 18)
    start_Ypos += 40
    w, h = malgun.getsize(message)
    start_xPos = (W - w) / 2
    draw.text((start_xPos, start_Ypos), message, fill=color, font=malgun)

    #adding ATK_LABEL
    message = "앰코테크놀로지코리아주식회사"
    color = 'rgb(0, 0, 0)'
    malgun = ImageFont.truetype('/malgunbd.ttf', 18)
    start_Ypos += 50
    w, h = malgun.getsize(message)
    start_xPos = (W - w) / 2
    draw.text((start_xPos, start_Ypos), message, fill=color, font=malgun)

    # adding location
    message = location_list[0]
    color = 'rgb(0, 0, 0)'
    malgun = ImageFont.truetype('/malgun.ttf', 18)
    start_Ypos += 30
    w, h = malgun.getsize(message)
    start_xPos = (W - w) / 2
    draw.text((start_xPos, start_Ypos), message, fill=color, font=malgun)

    # adding tell&cell
    message = f"tel {tell} | cell {cell}"
    color = 'rgb(0, 0, 0)'
    malgun = ImageFont.truetype('/malgun.ttf', 18)
    start_Ypos += 30
    w, h = malgun.getsize(message)
    start_xPos = (W - w) / 2
    draw.text((start_xPos, start_Ypos), message, fill=color, font=malgun)

    #adding email
    message = email
    color = 'rgb(0, 0, 0)'
    malgun = ImageFont.truetype('/malgun.ttf', 18)
    start_Ypos += 30
    w, h = malgun.getsize(message)
    start_xPos = (W - w) / 2
    draw.text((start_xPos, start_Ypos), message, fill=color, font=malgun)

    image.save(f"{dir}/{name_list[0]}_front.png")
    # Save the edited image

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
        # self.pushButton_cancel.clicked.connect(self.close)  # 취소하기

    def openFileNamesDialog(self):
        # 파일 여러개 불러오기
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files = QFileDialog.getOpenFileNames(None, "Open " + " Data File", '.', "(*.xlsx)")[0][0]

        if files:
            self.lineEdit_openfile.setText(files)
            global frames
            frames = pd.read_excel(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
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
            TexttoIMG(name[i], position[i], department[i], location[i], tell[i], cell[i], email[i], path)
        try:
            for i in tqdm(range(len(name)), desc = '지정된 경로에 명함 제작중입니다.', leave= False) :
                TexttoIMG(name[i], position[i], department[i], location[i], tell[i], cell[i], email[i], OutputPath)
            QMessageBox.about(self, "message", "저장경로 폴더, image 폴더 안에 PDF 파일이 생성되었습니다")

        except:
            QMessageBox.about(self, "message", "image 폴더 안에 PDF 파일이 생성되었습니다")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()