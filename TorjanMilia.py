#author = mberr!
#team  = Loli4
import time,os,sys
from time import sleep as jd
m = '\x1b[1;31m'
p = '\x1b[1;37m'
i = '\x1b[1;32m'
banner = '''==welome to sc torjanmilia
==author==1999Dilan==
== gak punya team solo==
==no wa gw 089691551748==
==blog masih gak ada==
== lgi mikir nih=== '''.format(m,p,m,p,m,p,m,p,m,p,m,p,m,p,m,p,m,p)


def menu():
  os.system('clear')
  print(banner)
  print('{}[{}>>>>>>{}]{} gunakan dengan baik ini bukan mainan ok '.format(m,p,m,p))
  print('{}[{}>>>>>>{}]{} masukan ip andressnya..'.format(m,p,m,p))
  cor = str(input('{}[{}>>>>>>{}]{} ip anderss nya .= >> '.format(m,p,m,p)))
  print('sabar dulu..')
  time.sleep(2)
  print(m + '[' + p +'>>>>>' + m +']' + p + 'sedang memproses ip>> '+ i + cor )
  time.sleep(2)
  load()
def load():
        a = 0

        while a<=1000: #MEMBUAT HITUNGAN BIASA
             sys.stdout.write('torjan terkirim ke ip target..'+str(a)+'%  ')
             sys.stdout.flush()
             a=a+1 #NILAI A DITAMBAH 1
             jd(4.0)  #Waktu Jeda
        done()
def done():
  time.sleep(3)
  print('\n{}[{}>>>>>>{}]{}komputer target sudah down'.format(m,p,m,p))
if __name__ == '__main__':
  menu()
    