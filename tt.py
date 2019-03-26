from tkinter import*
from tkinter import ttk
import datetime as dt
import numpy as np
import time
import random
import os
from collections import defaultdict
#from PIL import ImageTk
from functools import partial

H =  np.array([[1,1,0,0,1,1,1,0],
             [0,1,1,1,0,0,0,0],
             [0,0,1,0,1,0,1,1],
             [0,0,0,1,0,1,1,1]])
m = 0
def matrix():
    
##    p= np.zeros((2,2))
    b = Toplevel()
    b.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b.geometry(winSize)
    draw = Canvas(b,height=500, width=800,background='white')
    photo = PhotoImage(file = './girth.png')
    draw.image = photo
    image_id=draw.create_image(410, 270, image=photo, state=NORMAL)
    ####
    draw.place(x=-5,y=-6)
    line_list_all = {}
    rect_list_all = {}
    oval_list_all = {}
    line_click_list = {}
    H_1= np.zeros((4,8))
    for n in range(0,8):
        oval_id=draw.create_oval((n+1.5)*80-20,400,(n+1.5)*80+1+20,440,fill='light green')
        oval_list_all[n] = oval_id
        for m in range(0,4):
            rect_id=draw.create_rectangle((m+3.5)*80-20,230,(m+3.5)*80+20,270,fill='light green')
            rect_list_all[m] = rect_id
            if H[m][n] == 1:
                line_id=draw.create_line((n+1.5)*80+0.5,420,(m+3.5)*80,250,fill='yellow',width=4)
                line_list_all = line_id
                draw.tag_lower(line_id)
                draw.tag_lower(image_id)
  
    
    draw.bind("<Button-1>",lambda e: xy3(e))
    
    def xy3(event):
        global m
##        while dt.configure(command!=submit):
        x,y = event.x, event.y            
        line_list = [item for item in draw.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1) if draw.type(item) == "line"]
        if len(line_list)==1:
            
            if draw.itemcget(line_list[0],"fill")=="yellow": 
                print(line_list)
                selected_object1 = line_list[0]
                print(line_list[0])
                draw.itemconfig(selected_object1,fill="maroon")
                line_click_list[m] =  selected_object1
                print(line_click_list)
                m += 1
                print(m)
            else:
                key1 = None
                selected_object1 = line_list[0]
                draw.itemconfig(selected_object1,fill="yellow")
                for key in line_click_list.keys():
                    if line_click_list[key]== selected_object1:
                        key1 = key
                del line_click_list[key1]
                print(line_click_list)
                m -= 1
                print(m)
    def submit():

        global m
        if  m==4:
            score_100 = 100
            print(score_100)
            print("you win!!")
            b1 =Toplevel()
            b1.resizable(width=False,height=False)
            height=200
            width=400
            winSize = str(width)+'x'+str(height)
            b1.geometry(winSize)

            

            def doSomething():
                b1.destroy()
                b.destroy()
                root.deiconify()
                
            b1.protocol('WM_DELETE_WINDOW', doSomething)
            
            draw = Canvas(b1,height=500, width=800,background='white')
            ####
            photo = PhotoImage(file = './11321_win.png')
            draw.image = photo
            draw.create_image(200, 150, image=photo, state=NORMAL)
            ####
            draw.place(x=0,y=-70)

            
            def nextlevel_1():
                b1.destroy()
                b.destroy()
                root.deiconify()
                bt_2.config(state="normal")
                bt_1.config(relief='ridge')
            bt_next = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command= nextlevel_1)
            image=PhotoImage(file='next_1.png')
            image=image.subsample(5)
            bt_next['image']=image
            bt_next.image = image
            bt_next.place(width=60,height=40,x=210,y=170)
            
            
        else :

           
            
            b1 =Toplevel()
            b1.resizable(width=False,height=False)
            height=200
            width=400
            winSize = str(width)+'x'+str(height)
            b1.geometry(winSize)
            draw = Canvas(b1,height=500, width=800,background='white')
            ####
            photo = PhotoImage(file = './11321_lose.png')
            draw.image = photo
            draw.create_image(200, 150, image=photo, state=NORMAL)
            ####
            draw.place(x=0,y=-70)
            
            label=ttk.Label(draw, text= str(score) , relief='ridge',font=("courier",14))
            label.place(x=230,y=130)
            
            def doSomething():
                b1.destroy()
                b.destroy()
                root.deiconify()
               
            b1.protocol('WM_DELETE_WINDOW', doSomething)
            def retry1():
                b1.destroy()
                b.destroy()
                root.deiconify()
            bt_retry = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command= retry1)
            image=PhotoImage(file='retry_4.png')
            image=image.subsample(5)
            bt_retry['image']=image
            bt_retry.image = image
            bt_retry.place(width=60,height=40,x=210,y=170)

    bt_submit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=submit)
    image=PhotoImage(file='submit5.png')
    image=image.subsample(2)
    bt_submit['image']=image
    bt_submit.image = image
    bt_submit.place(width=80,height=75,x=710,y=30)
        
root = Tk()
root.title('Low Density Parity Check Code Learning Tool \u00a9 2017')
root.resizable(width=False,height=False)
winWidth = 800
winHeight = 500
winSize = str(winWidth)+'x'+str(winHeight)
root.geometry(winSize)

tkimage=PhotoImage(file='game.png')
bg_pic=Label(root,image = tkimage)
bg_pic.place(x=0, y=0, relwidth=1, relheight=1)
bt_1 = Button(root, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=matrix)
image=PhotoImage(file='1_pn.png')
image=image.subsample(5)
bt_1['image']=image
bt_1.image = image
bt_1.place(width=90,height=88,x=60,y=360)
