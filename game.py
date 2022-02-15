from cgitb import grey
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
from tkinter import messagebox
import random

class Game(Toplevel):
    def __init__(self, master=None):
        global one,two,three,x,y
        global canvas1 ,canvas2
        Toplevel.__init__(self, master=master, width="425", height="330")
        menu = Menu(self)
        self.config(menu=menu)
#  #  File menu formation in menubar
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command = self.quit)

        self.f1=Frame(self,borderwidth = 2, width= 420, height=320,background="purple" ,highlightbackground="black",highlightthickness=3, relief=RIDGE)
        self.f1.place(x=4,y=4)
        canvas1 = Canvas(self.f1, width=150, height=150, background= "grey")
        canvas1.place(x=5, y=2)
        canvas2 = Canvas(self.f1, width=150, height=150, background= "grey")
        canvas2.place(x=250, y=2)
        
        papperimg=Image.open(r"img\papper.jpg")
        papperimg=papperimg.resize((65,65),Image.ANTIALIAS)
        self.papper=ImageTk.PhotoImage(papperimg)
        one=self.papper

        stoneimg=Image.open(r"img\stone.jpg")
        stoneimg=stoneimg.resize((65,65),Image.ANTIALIAS)
        self.stone=ImageTk.PhotoImage(stoneimg)
        two=self.stone

        scissorimg=Image.open(r"img\scissor.jpg")
        scissorimg=scissorimg.resize((65,65),Image.ANTIALIAS)
        self.scissor=ImageTk.PhotoImage(scissorimg)
        three=self.scissor
        
        vsimg=Image.open(r"img\vs.jpg")
        vsimg=vsimg.resize((80,80),Image.ANTIALIAS)
        self.vs=ImageTk.PhotoImage(vsimg)

        self.l1=Label(self.f1,image=self.vs)
        self.l1.place(x=165,y=30,width=80,height=80)
        self.x=0
        self.y=0
        self.compscore=Label(self.f1,text="Comupter : ",font="algerian 16",background="purple")
        self.compscore.place(x=5,y=165)
        self.comppoint=Label(self.f1,text=self.x,font="algerian 16",background="purple")
        self.comppoint.place(x=130,y=165)
        self.humscore=Label(self.f1,text="Human : ",font="algerian 16",background="purple")
        self.humscore.place(x=250,y=165)
        self.humpoint=Label(self.f1,text=self.y,font="algerian 16",background="purple")
        self.humpoint.place(x=335,y=165)

        self.papperb=Button(self.f1,image=self.papper,cursor="hand2",bd=10, bg="grey")
        self.papperb.place(x=160,y=210,width=90,height=90)

        self.stoneb=Button(self.f1,image=self.stone,cursor="hand2",bd=10, bg="grey")
        self.stoneb.place(x=40,y=210,width=90,height=90)

        self.scissorb=Button(self.f1,image=self.scissor,cursor="hand2",bd=10, bg="grey")
        self.scissorb.place(x=290,y=210,width=90,height=90)

        self.stoneb.bind("<ButtonRelease>", self.stonecom)
        self.papperb.bind("<ButtonRelease>", self.pappercom)
        self.scissorb.bind("<ButtonRelease>", self.scissorcom)

    def stonecom(self,event):#1=papper 2=stone 3=scissor
        if self.winfo_containing(event.x_root, event.y_root) == self.stoneb:
            canvas2.create_image(80,80, anchor=CENTER, image=two)
            ran=random.randint(1,3)
            if ran==1:
                canvas1.create_image(80,80, anchor=CENTER, image=one)
                self.x+=1
                self.comppoint.config(text=self.x)
            if ran==2:
                canvas1.create_image(80,80, anchor=CENTER, image=two)
            if ran==3:
                canvas1.create_image(80,80, anchor=CENTER, image=three)
                self.y+=1
                self.humpoint.config(text=self.y)
            #1=papper 2=stone 3=scissor
            if self.x==5:
                messagebox.showinfo("Loss", "Computer won the match")
            elif self.y==5:
                messagebox.showinfo("Winner", "You won the match")
            elif self.x==5 and self.y==5:
                messagebox.showinfo("Tie", "Its A Tie")
    def pappercom(self,event):#1=papper 2=stone 3=scissor
        if self.winfo_containing(event.x_root, event.y_root) == self.papperb:
            canvas2.create_image(80,80, anchor=CENTER, image=one)
            ran=random.randint(1,3)
            if ran==1:
                canvas1.create_image(80,80, anchor=CENTER, image=one)
                
            if ran==2:
                canvas1.create_image(80,80, anchor=CENTER, image=two)
                self.y+=1
                self.humpoint.config(text=self.y)
            if ran==3:
                canvas1.create_image(80,80, anchor=CENTER, image=three)
                self.x+=1
                self.comppoint.config(text=self.x)
            #1=papper 2=stone 3=scissor
            if (self.x==5):
                messagebox.showinfo("Loss", "Computer won the match")
            elif self.y==5:
                messagebox.showinfo("Winner", "You won the match")
            elif self.x==5 and self.y==5:
                messagebox.showinfo("Tie", "Its A Tie")
    def scissorcom(self,event):#1=papper 2=stone 3=scissor
        if self.winfo_containing(event.x_root, event.y_root) == self.scissorb:
            canvas2.create_image(80,80, anchor=CENTER, image=three)
            ran=random.randint(1,3)
            if ran==1:
                canvas1.create_image(80,80, anchor=CENTER, image=one)
                self.y+=1
                self.humpoint.config(text=self.y)
            if ran==2:
                canvas1.create_image(80,80, anchor=CENTER, image=two)
                self.x+=1
                self.comppoint.config(text=self.x)
            if ran==3:
                canvas1.create_image(80,80, anchor=CENTER, image=three)
            if self.x==5:
                messagebox.showinfo("Loss", "Computer won the match")
            elif self.y==5:
                messagebox.showinfo("Winner", "You won the match")
            elif self.x==5 and self.y==5:
                messagebox.showinfo("Tie", "Its A Tie")                
                
            #1=papper 2=stone 3=scissor

