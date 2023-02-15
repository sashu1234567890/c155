# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:16:17 2023

@author: Sashwath
"""

from tkinter import*
root = Tk()
root.title("Dictionary")
root.geometry("600x600")

label_mutable = Label(root)
label_unmutable = Label(root)
label_tkinter = Label(root)
 
dictionary = {'Mutable' : 'Values can just be changed just like list',
              'Unmutable' : 'Values can not be changed just like tuple',
              'Tkinter' : 'It is the GUI library of python'}

def mutable():
    label_mutable["text"] = dictionary['Mutable']

def unmutable():
    label_unmutable["text"] = dictionary['Unmutable']

def tkinter():
    label_tkinter["text"] = dictionary['Tkinter']
    
button_mutable = Button(root,text="Meaning of mutable" , command= mutable)  
button_mutable.place(relx=0.5,rely=0.2,anchor=CENTER)  

label_mutable.place(relx=0.5,rely=0.3,anchor=CENTER)

button_unmutable = Button(root,text="Meaning of unmutable" , command= unmutable)  
button_unmutable.place(relx=0.5,rely=0.4,anchor=CENTER)  

label_unmutable.place(relx=0.5,rely=0.5,anchor=CENTER)

button_tkinter = Button(root,text="Meaning of tkinter" , command= tkinter)  
button_tkinter.place(relx=0.5,rely=0.6,anchor=CENTER)  

label_tkinter.place(relx=0.5,rely=0.7,anchor=CENTER)
    
root.mainloop()
