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
             [0,0,1,0,1,0,0,1],
             [0,0,0,1,0,1,0,1]])

Htemp =  [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]

def matrix():
##    p= np.zeros((2,2))
    b = Toplevel()
    b.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b.geometry(winSize)
    draw = Canvas(b,height=500, width=800,background='white')
    photo = PhotoImage(file = './11321.png')
    draw.image = photo
    image_id=draw.create_image(410, 270, image=photo, state=NORMAL)
    ####
    draw.place(x=-5,y=-6)
    line_list_all = {}
    rect_list_all = {}
    oval_list_all = {}
    H_1= np.zeros((4,8))
    for n in range(0,8):
        oval_id=draw.create_oval((n+1.5)*80-20,400,(n+1.5)*80+1+20,440,fill='skyblue')
        oval_list_all[n] = oval_id
        for m in range(0,4):
            rect_id=draw.create_rectangle((m+3.5)*80-20,230,(m+3.5)*80+20,270,fill='skyblue')
            rect_list_all[m] = rect_id
            if H[m][n] == 1:
                line_id=draw.create_line((n+1.5)*80+0.5,420,(m+3.5)*80,250,fill='skyblue',width=4)
                line_list_all = line_id


 

    m = StringVar()
    m.set('6')
    label_random = Label(b,textvariable = m,bg="palegreen", fg="green",font=(None, 50))
    label_random.place(width=80,height=75,x=705, y=150)

    
    draw.bind("<Button-1>",lambda e: xy3(e,m))
    def xy3(event,m):
        x,y = event.x, event.y            
        line_list = [item for item in draw.find_overlapping(event.x-2, event.y-2, event.x+2, event.y+2) if draw.type(item) == "line"]
        if len(line_list)==1:
            if draw.itemcget(line_list[0],"fill")=="skyblue":
            #if line_id==line_id(line_list[0],fill="skyblue"): 
                selected_object1 = line_list[0]
                coords = draw.coords(line_list[0])
                coordsy = int(((coords[0]-0.5)/80)-1.5)
                coordsx = int(((coords[2])/80)-3.5)
                print(coordsx,coordsy)
                Htemp[coordsx][coordsy]=1
                draw.itemconfig(selected_object1,fill="gold")
                tmp = m.get()
                tmp = int(tmp)
                tmp -= 1
                m.set(tmp)
            else:
                selected_object1 = line_list[0]
                draw.itemconfig(selected_object1,fill="skyblue")
                coords = draw.coords(line_list[0])
                coordsy = int(((coords[0]-0.5)/80)-1.5)
                coordsx = int(((coords[2])/80)-3.5)
                Htemp[coordsx][coordsy] = 0
                tmp = m.get()
                tmp = int(tmp)
                tmp += 1
                m.set(tmp)
            print(Htemp)    
                
    def submit():
        print('Htemp',Htemp)
        M = len(Htemp)
        N = len(Htemp[0])
        R = (N-M)/N
        girth = [0]*M
        Htmp = [k for k in Htemp]


        for x in range(M):
            print('x',x)
            all_chknodes = [x]
            level = 0
            while 1:
                new_all_chknodes = []
                new_all_bitnodes = []
                all_bitnodes = []
                print('all_chknodes',all_chknodes)
                for chk_node in all_chknodes:
                    for chk_node in all_chknodes:
                        for c in range(N):
                            if Htmp[chk_node][c] == 1:
                                Htmp[chk_node][c] = 0
                                all_bitnodes.append(c)
                                new_all_bitnodes.append(c)
                                print('bitnode',c,new_all_bitnodes)
                                print(Htmp)
                                print(c)
                    for bit_node in all_bitnodes:        
                        for r in range(M):
                            if Htmp[r][bit_node]==1:
                                Htmp[r][bit_node] = 0
                                new_all_chknodes.append(r)
                                print('checknode',r,new_all_chknodes)
                                print(Htmp)

                ##print(all_bitnodes)
                girth_found = 0
                a = 0
                for m in range(M):
                    if new_all_chknodes.count(m)>1:
                        girth_found = 1
                        break
                    for c in range(N):
                        if new_all_chknodes.count(m)>0 or new_all_bitnodes.count(c)>0:
                            a += 1
                            print('a',a)
                if a == 0:
                    print(girth[x])
                    girth[x] = 0
                    break
                for c in range(N):
                    if new_all_bitnodes.count(c)>1:
                        girth_found = 2
                        break
                level += 1
                if girth_found == 1:
                    girth[x] = 4*level
                    break
                if girth_found == 2:
                    girth[x] = 4*level-2
                    break
                else:
                    print('level',level)
                    all_chknodes = new_all_chknodes
                    all_bitnodes = new_all_bitnodes
            print('Girth = ',girth)

        if girth.count(0) < M:
            girth = [x for x in girth if x != 0]
            girth = min(girth)
        else:
            girth = 0
        print(girth)

		    
        if girth==6:
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
#-------j=correct lines--------
            score=0
            
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
image=PhotoImage(file='4pn.png')
image=image.subsample(5)
bt_1['image']=image
bt_1.image = image
bt_1.place(width=90,height=88,x=60,y=360)
