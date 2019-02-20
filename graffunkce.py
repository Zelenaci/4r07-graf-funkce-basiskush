#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:20:55 2019

@author: spu35165
"""

import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Entry, Label, Button, filedialog
import pylab as lab


hlavni=tk.Tk()
hlavni.title("Graf funkce")

#column = sloupec, row= řádek, columnspan= přesahuje do více sloupců
generateFrame=LabelFrame(hlavni, text="Generuj graf funkce", padx=5, pady=5)
generateFrame.grid(row=0, column=0)

souborFrame=LabelFrame(hlavni, text="Generuj graf ze souboru", padx=5, pady=5)
souborFrame.grid(row=1, column=0)

osyFrame=LabelFrame(hlavni, text="Popisky os", padx=15, pady=15)
osyFrame.grid(row=2, column=0)

genGraf=LabelFrame(hlavni, text="Generuj")
genGraf.grid(row=0, column=1)

genGraf2=LabelFrame(hlavni, text="Generuj")
genGraf2.grid(row=1, column=1)

fceMin=tk.StringVar()
fceMax=tk.StringVar()

osaxVar=tk.StringVar()
osayVar=tk.StringVar()

fceVar=tk.StringVar()

souborVar=tk.StringVar()

def vyberSoubor():
    cesta= filedialog.askopenfilename(title='Vyberte soubor')    
    if cesta != '':
        souborVar.set(cesta)
    
            
def fceGraf():
    try: 
        od= float(fceMin.get())
        do= float(fceMax.get())
        x=lab.linspace(od, do, 500)
        if fceVar.get() == "sin":
            y=lab.sin(x)
        elif fceVar.get() == "log":
            y=lab.log10(x)
        elif fceVar.get() == "exp":
            y=lab.exp(x)
        lab.figure()
        lab.plot(x,y)
        lab.xlabel(osaxVar.get())
        lab.ylabel(osayVar.get())
        lab.grid(True)
        lab.show()
    except:
        pass
    
def fceSoubor():
    try:   
        cesta=souborVar.get()
        f=open(cesta,"r")
        od=[]
        do=[]
        while 1:
            radek=f.readline()
            if radek =="":
                break
            cisla=radek.split()
            od.append(float(cisla[0]))
            do.append(float(cisla[1]))
            x=lab.linspace(od, do, 500)
        if fceVar.get() == "sin":
            y=lab.sin(x)
        elif fceVar.get() == "log":
            y=lab.log10(x)
        elif fceVar.get() == "exp":
            y=lab.exp(x)
        f.close()
        lab.figure()
        lab.plot(x,y)
        lab.xlabel(osaxVar.get())
        lab.ylabel(osayVar.get())
        lab.grid(True)
        lab.show()
    except:
        pass
######    Generuj graf funkce menu   #######

Radiobutton(generateFrame, variable=fceVar, text="Sin", value="sin").grid(row=0, column=0)
Radiobutton(generateFrame, variable=fceVar, text="Log", value="log").grid(row=0, column=1)
Radiobutton(generateFrame, variable=fceVar, text="Exp", value="exp").grid(row=0, column=2)

Entry(generateFrame, textvariable=fceMin, width=10).grid(row=1, column=1, columnspan=2)
Entry(generateFrame, textvariable=fceMax, width=10).grid(row=2, column=1, columnspan=2)

Label(generateFrame, text="Od").grid(row=1, column=0) 
Label(generateFrame, text="Do").grid(row=2, column=0)

Button(genGraf, height=4, width=6,background="#00ad00", activebackground="#00d800", command=fceGraf).grid(column=2)


#####    Popisky os menu  ########

Label(osyFrame, text="osa X").grid(row=0, column=0) 

Label(osyFrame, text="osa Y").grid(row=1, column=0)

osaXEntry=Entry(osyFrame,textvariable=osaxVar, width=10).grid(row=0, column=1, columnspan=2) 

osaYEntry=Entry(osyFrame,textvariable=osayVar, width=10).grid(row=1, column=1, columnspan=2) 


#######  Generuj graf ze souboru  ##########
Button(souborFrame, text="Vyber soubor", command=vyberSoubor).grid(row=1, column=0)
Entry(souborFrame, textvariable=souborVar).grid(row=0, column=0)
Button(genGraf2, height=4, width=6,background="#00ad00", activebackground="#00d800", command=fceSoubor).grid(column=2)




hlavni.mainloop()