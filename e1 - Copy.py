

from tkinter import filedialog
from tkinter import Tk,Label,Frame,Checkbutton,Button,LEFT,BOTTOM,X,Y,E,W,Entry,Menu,TOP,SUNKEN
from tkinter import *
import os
def donothing():
    print('nothing')
    
    

root=Tk()


def video1():
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



root.geometry("500x500")

menu=Menu(root)
root.config(menu=menu)

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
insertbutt.pack(side=LEFT,padx=2,pady=2)
printexit1=Button(toolbar,text='video2',command=video1)
printexit1.pack(side=LEFT,padx=2,pady=2)
printexit2=Button(toolbar,text='video3',command=video1)
printexit2.pack(side=LEFT,padx=2,pady=2)
#printexit3=Button(toolbar,text='plot1',command=plot1)
#printexit3.pack(side=LEFT,padx=2,pady=2)


editmenu=Menu(menu)
menu.add_cascade(label='edit',menu=editmenu)
editmenu.add_command(label='New Project',command=donothing)
editmenu.add_command(label='New ',command=donothing)


toolbar.pack(side=TOP,fill=X)


status=Label(root,text='prepare to do nothing',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)


button1=Button(root,text='video_watch',bg='black',fg='white',command=video1)
button1.pack(side=LEFT,fill=X)



def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button1 = Button(master=root, text="Quit", command=_quit)
button1.pack(side=BOTTOM)


root.mainloop()

