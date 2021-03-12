#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      luferov_me
#
# Created:     04.02.2021
# Copyright:   (c) luferov_me 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import time
import datetime

from tkinter import *
from tkinter import ttk
import pathlib

def tk_Okno(text_tk):
    window = Tk()
    window.title("Online Cashier Info")
    window.geometry('600x150')
    greeting = ttk.Label(text="Выявлена ошибка по онлайн кассе", foreground="red",
                            font = 'Arial 18' )
    greeting.pack()
    text_box = Text()
    text_box.insert("1.0", text_tk+'\n' )
    text_box.pack()

    window.after(100000, window.destroy)
    window.mainloop()



date_now = datetime.datetime.now().strftime('%d/%m/%Y')

date_n = datetime.datetime.now()
date_now = date_n.strftime('%d/%m/%Y')

duration_minutes = datetime.timedelta(minutes=30)  #Допустимое время обновления
result = date_n - duration_minutes
time_contr = result.strftime('%H:%M:%S')


put = 'Y:\\logs'       # Укажи дерикторию для поиска файлов
nam_p = 'mp_task_srv.log' # Искомый файл
poisk_str = b'RECV HTTP answer' # Строка якорь

code_201 = 'Чек создан и добавлен в очередь на обработку'
code_202 = 'Чек создан и добавлен в очередь на обработку, но еще не обработан'
code_200 = 'Чек обработан'
code_400 = 'Переданные данные содержат ошибки валидации, либо подпись не прошла проверку'
code_401 = 'Клиентский сертификат не прошел проверку'
code_409 = 'Чек с данным идентификатором уже был создан в системе'
code_503 = 'Очередь чеков на регистрацию переполнена'
code_500 = 'Путь не найден'
code_0 = 'Данные запроса некорректные и ОФД не сформировано'
onlCass_not_cod = 'OnlCass не смогу получить код ошибки из ответного сообщения'
error_Shinu = 'Возникла ошибка при отправке сообщения-запроса в Шину банка ТКБ'



info_ljg = []

def poiskFile(direct,fileN):

    path = pathlib.Path(direct)   # Проверяет наличие дериктории
    tru_dir = (path.exists()) # True   # Есть или нет путь
    #print(path.is_file()) # True  # Файл или нет

    if tru_dir == False:   # Завершение операции при отсутствии пути
        tk_Okno ('Не найдена дериктория '+put + ', проверь подключение диска')
        quit()

    for curFold, subFold, fileNam in os.walk(put):
        for file in fileNam:
            #print(file)
            if file.startswith(fileN,9):
                fi =(os.path.join(curFold,file))

                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fi)

                sdf = time.localtime(mtime)
                #print (sdf)
                prnf = time.strftime("%d/%m/%Y",sdf)
                time_mod = time.strftime("%H:%M:%S",sdf)
                #print(time_mod)

                if prnf == date_now:
                    info_ljg.append("{}\{}".format(curFold,file))


    return info_ljg

poiskFile(put,nam_p)

col_zap = (len(info_ljg))

if col_zap == 0:
    tk_Okno('Не найден файл от '+ date_now )
    quit()

iz_file = []

for i in info_ljg:

    chten = open(i, 'rb')

    for i in chten:
        if poisk_str in i:
            st1 = i
            st2 = chten.readline()

            if b'OK'  in st2:
               iz_file.append ('{} {} | RC{} | {} | OK | {}'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],code_200))
            elif b'500' in st1:
                iz_file.append ('{} {} | RC{} | {} | Code:500 | {}'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],code_500))
            elif b'{"HttpStatusMessage":"Accepted"}'  in st2:
               iz_file.append ('{} {} | RC{} | {} | Accepted'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],st2))
            elif b'"Code":409}'  in st2:
               iz_file.append ('{} {} | {} | {} | Code:409 | {}'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],code_409))
            elif b'"Code":0}'  in st2:
                iz_file.append ('{} {} | RC{} | {} | Conflict:0 | {}'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],code_0))
            elif b'"Code":202}'  in st2:
               iz_file.append ('{} {} | RC{} | {} | Code:202 | {}'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],code_202))
            elif b'"Code":400}'  in st2:
               iz_file.append ('{} {} | RC{} | {} | Code:400 | {}'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],code_400))
            elif b'"Code":401}'  in st2:
               iz_file.append ('{} {} | RC{} | {} | Code:401 | {}'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],code_401))
            elif b'"Code":503}'  in st2:
               iz_file.append ('{} {} | RC{} | {} | Code:503 | {}'.format(date_now,str(st1)[2:10],str(st1)[59:62],str(st1)[70:82],code_503))


long_iz_file = (len(iz_file)-20)
otsch =  iz_file[long_iz_file:]

time_modif = (str(otsch[19:])[13:21])

if time_modif < time_contr:
    tk_Okno('Файл сегодня создан но обновлён более 20 минут назад, в '+ time_modif )

for i in otsch:
    if u'OK' in i:
        #tk_Okno(i)
        break
    else:
        tk_Okno(i)
        break

iz_file.clear()











