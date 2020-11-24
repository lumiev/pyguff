#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      luferov_me
#
# Created:     13.04.2020
# Copyright:   (c) luferov_me 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import string

f = 'C:\проблемные\логи'
nam_p = '20191220_jrn.log'
def putiFile (put,poisc):

    for curFold, subFold, fileNam in os.walk(put):
        p = str(curFold)#.replace("\\","\\\\",1)

        fi = str(fileNam).replace("[","").replace("]","").replace("'","")
        #print("r'{}\{}'".format(p,fi))
        if fi == '20191220_jrn.log':
            spis_ad = open(("{}\{}".format(p,fi)))
            print(spis_ad.read())


putiFile(f,nam_p)

#s = open(str(putiFile(f,nam_p)),'r')


#print(s.read())

#rg = str(putiFile(f,nam_p))
#for x in rg:
    #if x == u'jrn' :
        #print(x)


