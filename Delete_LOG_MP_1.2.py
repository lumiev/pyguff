#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      luferov_me
#
# Created:     02.11.2020
# Copyright:   (c) luferov_me 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import io
import string
import os
import time
import datetime
import shutil



put = 'C:\\Users\luferov_me'
nam_p = ['LocalPay', 'SelfInkasTimeTrace', 'RetailTimeTrace','SQL_error']
mat_dir = "C:\ЛОГИ_ВЫГРУЗКИ_ОПЕРАЦИЙ"

if not os.path.isdir(mat_dir):
        os.mkdir(mat_dir)

info_ljg = []

def poiskFile(direct,fileN):

    for curFold, subFold, fileNam in os.walk(put):
        for file in fileNam:
            if file.startswith(fileN,0):
                fi =(os.path.join(curFold,file))
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fi)
                sdf = time.localtime(mtime)
                prnf = time.strftime("%d/%m/%Y",sdf)
                info_ljg.append("{} {}\{}".format(prnf,curFold,file))

    return info_ljg




for i in list(nam_p):
    print('     Поиск файлов: {}'.format(i))
    poiskFile(put, i)
    imya = (i)
    print('')

#poiskFile(put, nam_p)
#print(poiskFile(put, 'RetailTimeTrace'))
    for i in list(info_ljg):
        new_dir =('{}'.format(str((i)[0:10]).replace('/','')))
        #print(new_dir)
        naz_dir = ('{}\{}'.format(mat_dir,new_dir))
        #print(naz_dir)
        if not os.path.isdir(naz_dir):
            os.mkdir(naz_dir)

    for i in list(info_ljg):
        old_dir =str('{}'.format(str((i)[11:1000])))
        star_fil_name = (old_dir.find(imya,0))
        fil_name = (old_dir[star_fil_name:1000])
    ##    print(fil_name)

        new_dir =('{}'.format(str((i)[0:10]).replace('/','')))

        naz_dir = ('{}\{}'.format(mat_dir,new_dir))
        new_naz_fil = ('{}\{}'.format(naz_dir,fil_name))



        shutil.move (old_dir, new_naz_fil)

        print ('    Перенесён: {} '.format( old_dir))


        info_ljg.clear()

    print('')

print ('    Файлы перенесены')



time.sleep(10)







