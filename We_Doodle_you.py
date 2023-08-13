import cv2 #for image processing
import easygui #for building UI
import numpy as np #for doing numerical operations
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt # for visualization and plotting
import os # for saving new image at specified path
import tkinter as tk # for GUI
from tkinter import * # for GUI
from PIL import ImageTk, Image # for GUI

top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    # read the image
    oriImage = cv2.imread(ImagePath)
    save1=Button(top,text="Save cartoon image",command=lambda: save(ImagePath,oriImage),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save1.pack(side=TOP,pady=50)

def save(ImagePath, ReSized6):
    newName="cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I= "Image saved by name " + newName +" at "+ path
    tk.messagebox.showinfo(title=None, message=I)

upload1=Button(top,text="Cartoonify an Image",command=lambda: upload(),padx=10,pady=5)
upload1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload1.pack(side=TOP,pady=50)

top.mainloop()





