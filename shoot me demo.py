from pygame import mixer
import time
mixer.init()

from tkinter import messagebox
import random
import threading
import tkinter as tk




class mapp(tk.Tk):
    def __init__(self):
        
        
        super().__init__()
        self.num=0
        #self.i=tk.PhotoImage(file="loading.gif",format="gif -index 2")
        
        thread1 = threading.Thread(target = self.start)      #game starts from here
        thread1.start()
        self.title("ShOoT mE")              #setting the title of game
    def me(self):                           #about me method
        messagebox.showinfo("ABOUT","Developer:- yash mathur\n follow me on my github account \n\nthemockingjester")
    def start(self):
        
        self.maxsize(800,550)                                               
        self.minsize(800,550)
        self.update()
        
        self.var=0                                      # score maintainer
        self.bg=tk.PhotoImage(file="background.png")   #loading background image
        self.fg=tk.PhotoImage(file="foreground.png")        #loading foreground image
        self.back=tk.Label(image=self.bg)
        self.back.place(x=0,y=0)
        self.playb=tk.Button(self,bg="slategray2",relief=tk.FLAT,text='PLAY',command=self.play,font=("garamond", "15","bold")) #play button
        self.playb.place(x=450,y=30)
        self.aboutbutton=tk.Button(self,bg="seagreen",text='ABOUT ME',command=self.me,font=("garamond", "10","bold")) #about button
        self.aboutbutton.place(x=650,y=500)
        self.pauseb=tk.Button(self,bg="slategray2",relief=tk.FLAT,text='PAUSE',command=self.pause,font=("garamond", "15","bold")) #pause button
        self.pauseb.place(x=350,y=30)
        self.name=tk.Label(self,bg="slategray2",text='ShOoT mE!!',font=("impact", "45","italic"))
        self.name.place(x=20,y=10)
        self.canvas = tk.Canvas(self, width=600, height=337, highlightthickness=0)                          #canvas over which image will move
        self.score=tk.Label(self,bg="slategray2",text='Score: {}'.format(self.var),font=("garamond", "25","bold")) #score teller
        self.score.place(x=550,y=30)
        
        self.canvas.place(x=90,y=90)        #now setting the the canvas at desired location
        self.yellowmonster=tk.PhotoImage(file='mn.png')  #loading yellow monster
        self.redmonster=tk.PhotoImage(file='red.png')      #loading red monster
        self.canvas.create_image(0, 0, image=self.fg,anchor=tk.NW)
        self.my=self.canvas.create_image(50, 10, anchor=tk.NW, image=self.yellowmonster)        #adding monster 1 to canvas
        self.my1=self.canvas.create_image(10, 50, anchor=tk.NW, image=self.yellowmonster)        #adding monster 2 to canvas
        self.my2=self.canvas.create_image(50, 10, anchor=tk.NW, image=self.redmonster)
        self.my3=self.canvas.create_image(50, 10, anchor=tk.NW, image=self.redmonster)
        self.canvas.tag_bind(self.my,"<Button-1>", self.monster1)                       #binding monsters actions on clicking
        self.canvas.tag_bind(self.my1,"<Button-1>", self.monster2)
        self.canvas.tag_bind(self.my2,"<Button-1>", self.monster3)
        self.canvas.tag_bind(self.my3,"<Button-1>", self.monster4)
        
        #self.canvas.pack()
        t2 = threading.Thread(target = self.main)      #game starts from here
        t2.start()
    def main(self):                                         #method which continuously changes the coordinates of monsters
        while True:  #running game until close
            
            
            if self.num == 0:  #checking if program is in resume condition if not so the else part runs
                a1=random.random() * 500
                
                b1=random.random() * 250
                a2=random.random() * 500
                b2=random.random() * 250
                a3=random.random() * 500
                b3=random.random() * 250
                a4=random.random() * 500
                b4=random.random() * 250
            
                
                self.canvas.coords(self.my ,a1,b1)                                          #new location of monsters 1
                self.canvas.coords(self.my1 ,a2,b2)                                         # new locations of monster2
                self.canvas.coords(self.my2 ,a3,b3)
                self.canvas.coords(self.my3 ,a4,b4)
                self.canvas.update()
                time.sleep(0.8)
                
            else:
                time.sleep(1)
                
            
        
    def monster1(self,event):
        if self.num==0:
            mixer.music.load("gun1.mp3")
            self.p1=tk.PhotoImage(file='mn2.png')
            self.canvas.itemconfig(self.my, image=self.p1)
            self.update()
            mixer.music.play()
            self.var+=1
        
            self.score.config(text='Score: {}'.format(self.var))
            time.sleep(0.5)
        self.canvas.itemconfig(self.my, image=self.yellowmonster)
    def monster2(self,event):
        if self.num==0:
            mixer.music.load("gun1.mp3")
            self.p1=tk.PhotoImage(file='mn2.png')
            self.canvas.itemconfig(self.my1, image=self.p1)
            self.update()
            mixer.music.play()
            self.var+=1
        
            self.score.config(text='Score: {}'.format(self.var))
            time.sleep(0.5)
        self.canvas.itemconfig(self.my1, image=self.yellowmonster)
    def monster3(self,event):
        if self.num==0:
            mixer.music.load("horn.mp3")
            self.p2=tk.PhotoImage(file='red2.png')
            self.canvas.itemconfig(self.my2, image=self.p2)
            self.update()
            mixer.music.play()
            messagebox.showinfo("ABOUT","Game over!!")
            self.var=0
        
            self.score.config(text='Score: {}'.format(self.var))
            time.sleep(0.5)
        self.canvas.itemconfig(self.my2, image=self.redmonster)
    def monster4(self,event):
        if self.num==0:
            mixer.music.load("horn.mp3")
            self.p2=tk.PhotoImage(file='red2.png')
            self.canvas.itemconfig(self.my3, image=self.p2)
            self.update()
            mixer.music.play()
            messagebox.showinfo("oops","Game over!!")
            self.var=0
        
            self.score.config(text='Score: {}'.format(self.var))
            time.sleep(0.5)
        self.canvas.itemconfig(self.my3, image=self.redmonster)
    def pause(self):
        
        self.num=1
        
    def play(self):
        
        self.num=0
        
        
        
if __name__ == "__main__": 
    app=mapp()
    app.mainloop()
