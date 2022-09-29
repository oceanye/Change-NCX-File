import re
import glob
import os


in_path=input('待处理文件路径:')
out_path=input('保存路径:')

os.chdir(in_path)
file_l=glob.glob('*.txt')


def change_x(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        data0=f.readlines()
    print('\n')
    print(f'读取到文件: {file_name}')
    n = float(input('输入x修改值:'))
    with open(out_path+'\\'+file_name,'w',encoding='utf-8') as f:
        for num,i in enumerate(data0):
            if num==0:
                f.write(i)
                continue
            str0=re.findall('X:(.*?) Y',i)[0]
            num0=float(str0)
            i=i.replace(str0,'%.2f' % (num0+n))
            f.write(i)
        print(f'文件 {file_name} 已保存')

for file in file_l:
    change_x(file)

stop=input('任意键后退出')





