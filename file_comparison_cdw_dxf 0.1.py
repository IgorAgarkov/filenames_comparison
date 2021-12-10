# -*- coding: utf8 -*-

import os

cdw = r'D:\Рабочая\САМОТЕЧНОЕ ОБОРУДОВАНИЕ\КЛАПАН ПЕРЕКИДНОЙ\КД-3\чертежи гибка'
dxf = r'D:\Рабочая\САМОТЕЧНОЕ ОБОРУДОВАНИЕ\КЛАПАН ПЕРЕКИДНОЙ\КД-3\DXF'

files1 = os.listdir(cdw)
files2 = os.listdir(dxf)

files_cdw = [files1[i][:-4] for i in range(len(files1)) if files1[i][-4:].lower() == '.cdw']
files_dxf = [files2[j][:-4] for j in range(len(files2)) if files2[j][-4:].lower() == '.dxf']

# print(files_cdw)
# print(files_dxf)

flag_cdw = True
flag_dxf = True

for k in range(len(files_cdw)):
    if files_cdw[k] not in files_dxf:
        print(files_cdw[k] + '.cdw')
        flag_cdw = False
for m in range(len(files_dxf)):
    if files_dxf[m] not in files_cdw:
        print(files_dxf[m] + '.dxf')
        flag_dxf = False
if flag_cdw and flag_dxf:
    print("Имена файлов совпадают")
