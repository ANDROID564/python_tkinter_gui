# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 22:49:35 2019

@author: TANVEER_MUSTAFA
"""

import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
import os
from tkinter import filedialog
from tkinter import Tk,Toplevel,BOTH,RAISED,Canvas,CENTER,Canvas,Label,Frame,Checkbutton,Button,LEFT,BOTTOM,X,Y,E,W,Entry,Menu,TOP,SUNKEN
from tkinter import *
import os

def stream(label):

    
    video_name = "2.avi" #This is your video file path
    video = imageio.get_reader(video_name)    
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
    
   
    
        
if __name__ == "__main__":
        root = tk.Tk()
        '''
        root.geometry("600x600")
        
        def video1():
            sub=Toplevel(root)
            sub.geometry("400x400")
            os.system('python embed_video.py')
        

        def plot1():
            os.system('python plot1.py')
        
        
        def saved_files():
            os.system('python embed_video.py')
        
        
        def browse_button():
            # Allow user to select a directory and store it in global var
            # called folder_path
            global folder_path
            filename = filedialog.askopenfilename()
            folder_path.set(filename)
            print(filename)

        
                
        menu=Menu(root)
        root.config(menu=menu)
        
        my_label =Label(root)
        my_label.pack()
        
        
        submenu=Menu(menu)
        menu.add_cascade(label='File',menu=submenu)
        submenu.add_command(label='Browse files',command=browse_button)
        submenu.add_command(label='New ',command=donothing)
        submenu.add_separator()
        submenu.add_command(label=' exit',command=donothing)
        
        editmenu=Menu(menu)
        menu.add_cascade(label='edit',menu=editmenu)
        editmenu.add_command(label='New Project',command=donothing)
        editmenu.add_command(label='New ',command=donothing)
        
        
        toolbar=Frame(root,bg='blue')
        insertbutt=Button(toolbar,text='video1',command=video1)
        insertbutt.pack(side=LEFT,padx=2,pady=2,ipadx=20)
        printexit1=Button(toolbar,text='video2',command=video1)
        printexit1.pack(side=LEFT,padx=2,pady=2,ipadx=20)
        printexit2=Button(toolbar,text='video3',command=video1)
        printexit2.pack(side=LEFT,padx=2,pady=2,ipadx=20)
        printexit3=Button(toolbar,text='plot1',command=plot1)
        printexit3.pack(side=LEFT,padx=2,pady=2,ipadx=20)
        
        
        toolbar.pack(side=TOP,fill=BOTH)
        #toolbar1=Frame(root,bg='red')
        toolbar1=Label(root,bg='red')
        
        insertbutt1=Button(toolbar1,text='video1',command=video1)
        insertbutt1.pack(side=LEFT,padx=2,pady=2,ipadx=20)
        printexit11=Button(toolbar1,text='video2',command=video1)
        printexit11.pack(side=LEFT,padx=2,pady=2,ipadx=20)
        printexit21=Button(toolbar1,text='video3',command=video1)
        printexit21.pack(side=LEFT,padx=2,pady=2,ipadx=20)
        printexit31=Button(toolbar1,text='plot1',command=plot1)
        printexit31.pack(side=LEFT,padx=2,pady=2,ipadx=20)
        
        
        
        
        
        
        status1=Label(root,text='prepare to do nothing',bd=1,relief=SUNKEN,anchor=W)
        status1.pack(side=BOTTOM,fill=BOTH)
        status=Label(root,text='prepare to do nothing',bd=2,relief=SUNKEN,anchor=W)
        status.pack(side=BOTTOM,fill=BOTH)
        
        toolbar1.pack(side=BOTTOM,fill=BOTH)
        
        
        button1=Button(root,text='video_watch',bg='black',fg='white',command=video1)
        button1.pack(fill=BOTH)
        
        '''
        my_label = tk.Label(root)
        my_label.pack()
        thread = threading.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()


     
root.mainloop()        
