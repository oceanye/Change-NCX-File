# coding=UTF-8

import re
import glob
import os
import tkinter as tk
from tkinter import filedialog
import datetime as dt


print('NCX Tool V0.8-EVALUATION')
print('-----------------------------')
print('1.Select NCX File(s)：')




now = dt.datetime.now()
licensetime = dt.datetime(2022,12,27,1,1,1,148233)



root = tk.Tk()
root.withdraw()

Filepath1=filedialog.askopenfilenames()


file_l=Filepath1


def change_x(file_name,n):
    with open(file_name,'r',encoding='utf-8') as f:
        data0=f.readlines()

    str_data = str(data0)


    print(f'   Read: {file_name}OK')
    new_file_name = file_name.strip('.txt') +'_'+str(n)+'.txt'
    copy_function(file_name, new_file_name)



    with open(new_file_name,'w',encoding='utf-8') as f:
        for num,i in enumerate(data0):
            if num==0:
                str1=re.findall('L=(.*?) ',i)[0]
                num1=int(str1)
                i = i.replace(str1,'%i' % (num1+n))
                f.write(i)
                continue

            str0=re.findall('X:(.*?) Y',i)[0]
            num0=float(str0)
            i=i.replace(str0,'%.2f' % (num0+n))
            f.write(i)
        print(f'   File: {new_file_name} Saved')




# Copy封装成函数
def copy_function(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)
        for file in filelist:
            path = os.path.join(src, file)
            if os.path.isdir(path):
                copy_function(path, target)
            with open(path, 'rb') as rstream:
                container = rstream.read()
                path1 = os.path.join(target, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
        else:
            print('OK!')




# 另存为文件



if now < licensetime:
    n = int(input('2.Input X Value(mm):'))

    for file in file_l:
        change_x(file,n)
    print(f'3.Finish {len(file_l)} files')
    stop=input('4.Press any key Exit')

else:
    stop=input('The evaluation is expired 2022 08 27!')







