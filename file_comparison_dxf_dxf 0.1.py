# -*- coding: utf8 -*-

import os

dxf1 = r'D:\Рабочая\Заказы\Заявка №448 2021.08.27\DXF'
dxf2 = r'D:\Рабочая\САМОТЕЧНОЕ ОБОРУДОВАНИЕ\ЗАДВИЖКИ\УЗР-300\DXF!'

files1 = os.listdir(dxf1)
files2 = os.listdir(dxf2)

files_dxf1 = [files1[i][:-4] for i in range(len(files1)) if files1[i][-4:].lower() == '.dxf']
files_dxf2 = [files2[j][:-4] for j in range(len(files2)) if files2[j][-4:].lower() == '.dxf']

flag = True

for k in range(len(files_dxf1)):
    if files_dxf1[k] in files_dxf2:
        print(files_dxf1[k] + '.dxf')
        flag = False

if flag:
    print("Одноимённых файлов нет")








