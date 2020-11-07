#!/usr/bin/python

import sys
import os
import pathlib
import subprocess

from os import listdir
from tkinter import messagebox
from os.path import isfile, join


assert (len(sys.argv) >= 2),"Número de parametros tem de ser maior que zero!"


parametro = str(sys.argv[4])
entrada = str(sys.argv[5])
ficheiro_ou_pasta = str(sys.argv[6])
saida = str(sys.argv[7])



try:
   path = pathlib.Path(saida)
   os.makedirs(saida) 
except:
   pass

if ( parametro == "-i" ):
   cmd = ['C:\\Program Files\\Portugal Identity Card\\pteidguiV2.exe', 'signAdvanced', '-d', saida, entrada]
   head_tail = os.path.split(entrada) 
   ficheiros = os.path.splitext(head_tail[1])
   ficheiro = ficheiros[0]

   try:
      p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
      p.wait()	  
      os.rename(r'' + saida + ficheiro + '_signed.pdf',r'' + saida + ficheiro + '.pdf')     
   except:
      pass
      #messagebox.showinfo("Erro a correr o comando", cmd)

#Se o parametro for -d vai processar todos os ficheiros pdf que se encontram dentro da pasta
if ( parametro == "-d" ):
    os.chdir(entrada)
	
    cmd = ['C:\\Program Files\\Portugal Identity Card\\pteidguiV2.exe', 'signAdvanced', '-d', saida]
    ficheiros = [f for f in listdir(entrada) if isfile(join(entrada, f))]    
    cmd.extend(ficheiros)    
    #messagebox.showinfo("comando a executar", str(cmd))
    try:      
      p = subprocess.Popen(cmd, stdout=subprocess.PIPE)      
      p.wait()	  
      for f in listdir(entrada):
         if isfile(f):
            ficheiros = os.path.splitext(f)
            ficheiro = ficheiros[0]
            os.rename(r'' + saida + ficheiro + '_signed.pdf',r'' + saida + ficheiro + '.pdf')
    except:
      pass  
      #messagebox.showinfo("Erro a correr o comando", cmd)
