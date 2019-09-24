
from pygame import mixer
import time
mixer.init()


import random
import threading
import tkinter as tk
class mapp(tk.Tk):
    def __init__(self):
        
        self.num=0
        super().__init__()
        thread1 = threading.Thread(target = self.start)      #game starts from here
        thread1.start()
        self.title("ShOoT mE!!")
    def start(self):
        
       
        self.maxsize(800,600)                                               
        self.minsize(800,600)
     
        #self.attributes('-alpha', 0.5)
        self.configure(background="blue")                       #setting background color
        
        self.var=0
        self.pauseb=tk.Button(self,bg="blue",text='PAUSE',command=self.pause,font=("garamond", "15","bold")) #score teller
        self.pauseb.place(x=350,y=30)
        self.name=tk.Label(self,bg="blue",text='ShOoT mE!!',font=("impact", "25","italic"))
        self.name.place(x=20,y=45)
        self.canvas = tk.Canvas(self,bg="pink", width=600, height=400)                          #canvas over which image will move
        self.score=tk.Label(self,bg="blue",text='Score: {}'.format(self.var),font=("garamond", "35","bold")) #score teller
        self.score.place(x=150,y=494)
        self.canvas.place(x=90,y=90)
        self.logo=tk.PhotoImage(file='mn.png')
        self.my=self.canvas.create_image(50, 10, anchor=tk.NW, image=self.logo)        #adding monster 1 to canvas
        self.my1=self.canvas.create_image(10, 50, anchor=tk.NW, image=self.logo)        #adding monster 2 to canvas
        
        self.canvas.tag_bind(self.my,"<Button-1>", self.monster1)                       #binding monsters actions on clicking
        self.canvas.tag_bind(self.my1,"<Button-1>", self.monster2)
        #self.canvas.pack()
        t2 = threading.Thread(target = self.main)      #game starts from here
        t2.start()
    def main(self):                                         #it controls the actual play and pause
        for i in range(0,1000):
            #self.canvas.move(self.my,a,b)
            
            if self.num == 0:
                a1=random.random() * 500
                b1=random.random() * 300
                a2=random.random() * 50
                b2=random.random() * 300
            
                
                self.canvas.coords(self.my ,a1,b1)                                          #new location of monsters 1
                self.canvas.coords(self.my1 ,a2,b2)                                         # new locations of monster2
            
                self.canvas.update()
                time.sleep(0.8)
                
            else:
                time.sleep(1)
                
            
        
    def monster1(self,event):
        mixer.music.load("gun1.mp3")
        self.p1=tk.PhotoImage(file='mn2.png')
        self.canvas.itemconfig(self.my, image=self.p1)
        self.update()
        mixer.music.play()
        self.var+=1
        
        self.score.config(text='Score: {}'.format(self.var))
        time.sleep(0.5)
        self.canvas.itemconfig(self.my, image=self.logo)
    def monster2(self,event):
        mixer.music.load("gun1.mp3")
        self.p1=tk.PhotoImage(file='mn2.png')
        self.canvas.itemconfig(self.my1, image=self.p1)
        self.update()
        mixer.music.play()
        self.var+=1
        
        self.score.config(text='Score: {}'.format(self.var))
        time.sleep(0.5)
        self.canvas.itemconfig(self.my1, image=self.logo)
    def pause(self):
        self.fr=tk.Toplevel(self)
        self.withdraw()
        self.num=1
        #self.fr.pack()
        self.fr.maxsize(800,600)
        self.fr.minsize(800,600)
        self.fr.configure(bg="blue")
        self.playb=tk.Button(self.fr,bg="blue",text='PLAY',command=self.play,font=("garamond", "15","bold")) #score teller
        self.playb.place(x=150,y=80)
        #time.sleep(5465)
    def play(self):
        self.fr.withdraw()
        self.num=0
        self.deiconify()
        
        
if __name__ == "__main__": 
    app=mapp()
    app.mainloop()
