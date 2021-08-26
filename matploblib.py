from openpyxl import load_workbook
import pandas as pd
import re
import os

#### Input FILE_TYPE ####
SELECT_FILE_TYPE = 'E2'
##### ENTER_INPUT #######

FILE_NAME = []
MASTER_FILE_PATH = 'C:/Users/20605/PycharmProjects/pythonProject/Time To R Plotting/Master file'
DEG_FILE_PATH = 'C:/Users/20605/PycharmProjects/pythonProject/Time To R Plotting/Deg plotting'

for (path, dir, files) in os.walk(f'{DEG_FILE_PATH}'):
    for filename in files:
        ext = os.path.splitext(filename)[0]
        if ext == f'{SELECT_FILE_TYPE} DEG2':
            FILE_NAME.append(filename)

NEW = [[] for i in range(len(FILE_NAME))]
NEW_LEN = len(NEW)

for NAME_INDEX in range(len(FILE_NAME)):
    reader = open(f'{DEG_FILE_PATH}/{FILE_NAME[NAME_INDEX]}', 'r')

    str_ = reader.read()
    NEW[NAME_INDEX] = re.split(r'\s', str_)
    NEW[NAME_INDEX] = list(filter(None, NEW[NAME_INDEX]))

    # calculate columns
    i = 0
    while (1):
        i += 1
        if NEW[NAME_INDEX][i] == '-9.9999000': break

    length = i + 1

    # make rows*cols array
    array = [[] for row in range(len(NEW[NAME_INDEX]) // length)]
    i = 0
    j = 0
    cnt = 0

    while (i != len(NEW[NAME_INDEX])):
        array[j].append(NEW[NAME_INDEX][i])
        i += 1
        if (i) % length == 0:
            j += 1

    NEW[NAME_INDEX] = pd.DataFrame(array)
    if NAME_INDEX ==0:
        NEW[NAME_INDEX] = NEW[NAME_INDEX].iloc[:, [0,1]]
    else:
        NEW[NAME_INDEX] = NEW[NAME_INDEX].iloc[:, [1]]

TIME = NEW[0].iloc[:, [0]]
TIME = TIME.values.tolist()
TIME_list = pd.DataFrame(TIME, columns=['Time'])

NEW_LENGTH = len(NEW)
FINAL_NEW = pd.concat(NEW, axis=1)

FINAL_NEW_LIST = FINAL_NEW.values.tolist()

columns_name = []
for i in range(NEW_LENGTH+1):
    if i == 0: columns_name.append('Time')
    else: columns_name.append(f'#{i}')

FINAL_NEW_LIST = pd.DataFrame(FINAL_NEW_LIST, columns= columns_name)


#ExcelWriter
with pd.ExcelWriter(f'{MASTER_FILE_PATH}/Master file_{SELECT_FILE_TYPE}.xlsx', engine= "openpyxl", mode="r+", if_sheet_exists="replace") as writer:
        FINAL_NEW_LIST.to_excel(writer, sheet_name='Sheet1', index= False)

#Load_Workbook
write_wb = load_workbook(filename=f'{MASTER_FILE_PATH}/Master file_{SELECT_FILE_TYPE}.xlsx')
write_ws = write_wb['Sheet2']

write_ws_last_row = len(TIME)
for i in range(write_ws_last_row):
    write_ws['A'+ str(i+2)] = TIME[i][0]

write_wb.save(f'{MASTER_FILE_PATH}/Master file_{SELECT_FILE_TYPE}.xlsx')


