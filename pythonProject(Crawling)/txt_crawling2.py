import pandas as pd
import re

FILE_NAME = ['000FC104RFC.0000#TB4N26.00RR','000FC104RFC.0000#TB4N26.00', '000FC002KC9~0000#T3MG36~00', '000FC002KC8~0000#T3MG36~00RR', '0000C049KJW.0010#RR']

for name_index in range(len(FILE_NAME)):
    df = pd.read_csv(f'C:/Users/20605/PycharmProjects/pythonProject/RAW_DATA/{FILE_NAME[name_index]}.txt', delimiter='\t', engine='python', header=None, encoding='utf-8')
    reader = open(f'C:/Users/20605/PycharmProjects/pythonProject/RAW_DATA/{FILE_NAME[name_index]}.txt', 'r')

    df2 = pd.read_csv(reader, delimiter='\t', engine='python', header=None, encoding='utf-8')
    str = reader.read()

    #cut unecessary part
    with open(f'C:/Users/20605/PycharmProjects/pythonProject/RAW_DATA/{FILE_NAME[name_index]}.txt') as reader:
        str = reader.read()
        str = re.sub(r'=====*', '', str)
        str = re.sub(r'-----*', '', str)
        start_pattern = re.search(r' Tray| Row', str)
        end_pattern = re.search(r'Reject *:', str)
        # print(start_pattern, end_pattern)
        str = str[start_pattern.start():end_pattern.start()]

        new = re.split(r'\s|[|]', str)
        new = list(filter(None, new))

        #calculate columns
        i = 0
        while(1):
            i += 1
            if new[i] == 'Flags': break

        length = i+1

        #make rows*cols array
        array = [[] for row in range(len(new)//length)]
        i = 0
        j = 0
        cnt = 0

        while(i!=len(new)):
            array[j].append(new[i])
            i += 1
            if (i)%length == 0:
                j +=1

        new = pd.DataFrame(array)
        new.to_excel(f'C:/Users/20605/PycharmProjects/pythonProject/RESULT_DATA/{FILE_NAME[name_index]}.xlsx')
