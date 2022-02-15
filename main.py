from tkinter import *
import tkinter as tk
from game import Game
from tkinter import messagebox

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("305x200+0+0")
        self.title("Tic Tac Toe")
        menu = Menu(self)
        self.config(menu=menu)
#  #  File menu formation in menubar
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command = self.quit)

#  #  File menu formation in menubar
        Regimenu = Menu(menu)
        menu.add_cascade(label='Register', menu=Regimenu)
        Regimenu.add_command(label='Update',command=self.update)
        self.f1=Frame(self,borderwidth = 2, width= 290, height=195,highlightbackground="black",highlightthickness=3, relief=RIDGE)
        self.f1.place(x=4,y=4)
        self.b1=Button(self.f1,text="Start",command=lambda:{self.open()},cursor="hand2",bd=10, bg="grey", fg="red",activebackground="yellow",font="Algerian")
        self.b1.place(x=10,y=5,width=250,height=50)
        self.b1=Button(self.f1,text="How To Play",cursor="hand2",font="Algerian",bd=10, bg="grey", fg="red",activebackground="yellow")
        self.b1.place(x=10,y=65,width=250,height=50)
        self.b1=Button(self.f1,text="Quit",cursor="hand2",bd=10, bg="grey", fg="red",font="Algerian" ,activebackground="yellow",command = self.quit)
        self.b1.place(x=10,y=125,width=250,height=50)
    def update(self):
        messagebox.showinfo("Update Details","No New Update Is Out")
            
    def open(self): 
        self.app=Game(master=self)
        