#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,getopt
from datetime import datetime

def main(argv):

   bIncrementa = False
   bDecrementa = False
   valpha = 0 
   alphain = ''
   pos = 0
   pos2 = 0 

   try:
       opts, args = getopt.getopt(sys.argv[1:],"hidp:v:",["help","incrementa","decrementa","posicao=","valor=","alpha="])
   except getopt.GetoptError as err:
       print('0: rot -h <help> -i <incrementa> -d <decrementa> -p <posicao> -v <valor> -a <alpha>')
       print(err)
       usage()
       sys.exit(2)
       
   for opt,arg in opts:
       if opt == '-h':
          print('rot -h <help> -i <incrementa> -d <decrementa> -p <posicao> -v <valor> -a <alpha>')
          sys.exit()
       elif opt in ('-i', '--incrementa'):
          bIncrementa = True 
          bDecrementa = False
       elif opt in ('-d', '--decrementa'):
          bDecrementa = True
          bIncrementa = False
       elif opt in ('-p', '--posicao'):
          bIncrementa = False
          bDecrementa = False
          pos2 = int(arg)
       elif opt in ('-v', '--valor'):
          alphain = arg
       elif opt in ('-a', '--alpha'):
           valpha = int(arg)




   alpha1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   alpha2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   alpha3=['0','1','2','3','4','5','6','7','8','9',]
   alpha4=[':',';','<','=','>','?','@']

   alpha5 = alpha3 + alpha4

   if valpha == 0:
       alpha = alpha1 + alpha1 + alpha2 + alpha2
   else:
       alpha = alpha5 + alpha1 + alpha5 + alpha2 + alpha5

   #now = datetime.now()
   #agora = str(now.year) + str(now.month) + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) 

   #print(now)
   #print(agora)
   #print(alpha)
   #print(alphain)

   alphaout = ""

   if len(sys.argv)>=2:
      for dig in alphain:
          if dig in alpha:
              pos = alpha.index(dig) + pos2 
              alphaout = alphaout + alpha[pos]
          else:
              alphaout = alphaout + dig

          if bIncrementa == True:
             pos2 = pos2 + 1
          elif bDecrementa == True:
             pos2 = pos2 - 1  
   
   
      linha =  "******************************************************************"
      print 
      print
      print(linha)
      print("* O resultado é: "+ alphaout)
      print(linha)
      print 
      print


if __name__ == "__main__":
   main(sys.argv) 
   #main(sys.argv[1:])

