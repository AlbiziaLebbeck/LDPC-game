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

ans_click=0
m_start=0
print(m_start)
itr=0
ans=True



def gallager():

    
    b =Toplevel()
    b.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b.geometry(winSize)
    draw = Canvas(b,height=500, width=800,background='white')
    ####
    photo = PhotoImage(file = './soft.png')
    draw.image = photo
    image_id=draw.create_image(400, 250, image=photo, state=NORMAL)
    ####
    draw.place(x=1,y=1)

    b3 =Toplevel()
    b3.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b3.geometry(winSize)
    draw3= Canvas(b3,height=500, width=800,background='white')
    ####
    photo = PhotoImage(file = './inst_5.png')
    draw3.image = photo
    image_id=draw3.create_image(400, 250, image=photo, state=NORMAL)
    ####
    draw3.place(x=1,y=1)
    
    root.withdraw()

    def doSomething():
                    
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                    
    b.protocol('WM_DELETE_WINDOW', doSomething)

    def quit2():
        b.destroy()
        b3.destroy()
        root.deiconify()
    bt_quit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='flat',
                borderwidth=6,
                width=20,command=quit2)
    image=PhotoImage(file='home3.png')
    image=image.subsample(40)
    bt_quit['image']=image
    bt_quit.image = image
    bt_quit.place(width=50,height=50,x=740,y=440)

    bt_dict={}
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    p1c = '1-'+'P1'.translate(SUB)
    p1 = 'P1'.translate(SUB)
    p2 = 'P2'.translate(SUB)
    p2c = '1-'+'P2'.translate(SUB)
    def toggle(n):
        if bt_dict[n]['text'] == "___" :
            bt_dict[n]['text'] = p1c
            
        elif bt_dict[n]['text']==p1c:
            bt_dict[n]['text']= p1
        elif bt_dict[n]['text'] == p1:
            bt_dict[n]['text'] = p2
        elif bt_dict[n]['text'] == p2:
            bt_dict[n]['text'] = p2c
        else :
            bt_dict[n]['text'] = p1c

    def submit():
        n1 = 0

        for n in range (1,17):
            if bt_dict[n]['text']!= "___" :
                n1 =1
            
        if n1==1:
            x = (( bt_dict[1]['text']==p1 and  bt_dict[2]['text']==p2 ) or (bt_dict[1]['text']==p2 and  bt_dict[2]['text']==p1 )) and (( bt_dict[3]['text']==p1 and  bt_dict[4]['text']==p2 ) or (bt_dict[3]['text']==p2 and  bt_dict[4]['text']==p1 )) and (( bt_dict[5]['text']==p1 and  bt_dict[6]['text']==p2 ) or (bt_dict[5]['text']==p2 and  bt_dict[6]['text']==p1 ))
            y = (( bt_dict[7]['text']==p1 and  bt_dict[8]['text']==p2 ) or (bt_dict[7]['text']==p2 and  bt_dict[8]['text']==p1 )) and (( bt_dict[9]['text']==p1 and  bt_dict[10]['text']==p2 ) or (bt_dict[9]['text']==p2 and  bt_dict[10]['text']==p1 ))
            z = (( bt_dict[11]['text']==p1 and  bt_dict[12]['text']==p2 ) or (bt_dict[11]['text']==p2 and  bt_dict[12]['text']==p1 )) and (( bt_dict[13]['text']==p1 and  bt_dict[14]['text']==p2 ) or (bt_dict[13]['text']==p2 and  bt_dict[14]['text']==p1 ))
            q = (( bt_dict[15]['text']==p1 and  bt_dict[16]['text']==p2 ) or (bt_dict[15]['text']==p2 and  bt_dict[16]['text']==p1 ))

            if x == True and y == True and z == True and q == True:
                
                b.destroy()
                b3.destroy()
                
                b1 =Toplevel()
                b1.resizable(width=False,height=False)
                height=500
                width=800
                winSize = str(width)+'x'+str(height)
                b1.geometry(winSize)
                draw = Canvas(b1,height=500, width=800,background='white')
                ####
                photo = PhotoImage(file = './winall.png')
                draw.image = photo
                draw.create_image(400, 250, image=photo, state=NORMAL)
                ####
                draw.place(x=0,y=0)

                def quit21():
                        b1.destroy()
                        b3.destroy()
                        root.deiconify()
                bt_quit1 = Button(draw, compound=TOP,
                                        fg='#b7f731',
                                        relief='flat',
                                        borderwidth=6,
                                        width=20,command=quit21)
                image=PhotoImage(file='home3.png')
                image=image.subsample(40)
                bt_quit1['image']=image
                bt_quit1.image = image
                bt_quit1.place(width=50,height=50,x=740,y=440)

                def doSomething():
                    global m_start
                    m_start=0
                    b1.destroy()
                    
                    root.deiconify()
                   
                b1.protocol('WM_DELETE_WINDOW', doSomething)
                def doSomething1():
                    print('close')
                

                b.protocol('WM_DELETE_WINDOW', doSomething1)
                bt_quit.config(state="disable")
                bt_submit.config(state="disable")  

                  
##                label=ttk.Label(draw, text= str(score) , relief='ridge',font=("courier",14))
##                label.place(x=230,y=130)
                
            else :
                b1 =Toplevel()
                b1.resizable(width=False,height=False)
                height=200
                width=400
                winSize = str(width)+'x'+str(height)
                b1.geometry(winSize)
                draw = Canvas(b1,height=500, width=800,background='white')
                ####
                photo = PhotoImage(file = 'lose3.png')
                draw.image = photo
                draw.create_image(200, 100, image=photo, state=NORMAL)
                ####
                draw.place(x=0,y=0)

                  
##                label=ttk.Label(draw, text= str(score) , relief='ridge',font=("courier",14))
##                label.place(x=230,y=130)
                

                def doSomething():
                    global m_start
                    m_start=0
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                   
                b1.protocol('WM_DELETE_WINDOW', doSomething)
                def doSomething1():
                    print('close')
                

                b.protocol('WM_DELETE_WINDOW', doSomething1)
                bt_quit.config(state="disable")
                bt_submit.config(state="disable")  
                def retry1():
                    global m_start
                    m_start=0
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
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
                bt_retry.place(width=60,height=40,x=210,y=130)

#-------------bt in 1st
    for n in range (1,17):
         bt = Button(b, compound=TOP, text="___", relief='ridge',
                                    borderwidth=3, font =("courier",11),
                                    width=20, command = partial(toggle , n))
         
         bt_dict[n]=bt
    bt_dict[1].place(width=49,height=30,x= 340,y= 200)
    bt_dict[2].place(width=49,height=30,x= 415,y= 200)
    bt_dict[3].place(width=45,height=30,x= 515,y= 200)
    bt_dict[4].place(width=49,height=30,x= 576,y= 200)
    bt_dict[5].place(width=49,height=30,x= 652,y= 200)
    bt_dict[6].place(width=49,height=30,x= 723,y= 200)
    bt_dict[7].place(width=49,height=30,x= 455,y= 240)
    bt_dict[8].place(width=47,height=30,x= 557,y= 240)
    bt_dict[9].place(width=45,height=30,x= 668,y= 240)
    bt_dict[10].place(width=45,height=30,x= 730,y= 240)
    bt_dict[11].place(width=45,height=30,x= 472,y= 297)
    bt_dict[12].place(width=45,height=30,x= 560,y= 297)
    bt_dict[13].place(width=45,height=30,x= 660,y= 297)
    bt_dict[14].place(width=45,height=30,x= 725,y= 297)
    bt_dict[15].place(width=45,height=30,x= 478,y= 347)
    bt_dict[16].place(width=45,height=30,x= 625,y= 347)

    bt_submit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20 , command= submit)
    image=PhotoImage(file='submit5.png')
    image=image.subsample(2)
    bt_submit['image']=image
    bt_submit.image = image
    bt_submit.place(width=80,height=75,x=710,y=60)
        

##    bt1_1 = Button(b, compound=TOP, text="1-p1", relief='ridge',
##                                    borderwidth=3,
##                                    width=20)
##    bt1_1.place(width=52,height=30,x= 340,y= 200)
##    bt_dict[1]=bt1_1
##
##    bt1_2 = Button(b, compound=TOP, text="1-p1", relief='ridge',
##                                    borderwidth=3,
##                                    width=20)
##    bt1_2.place(width=52,height=30,x= 415,y= 200)
##    bt_dict[2]=bt1_2
##
##    bt1_3 = Button(b, compound=TOP, text="1-p1", relief='ridge',
##                                    borderwidth=3,
##                                    width=20)
##    bt1_3.place(width=45,height=30,x= 519,y= 200)
##    bt_dict[3]=bt1_3
##
##    
##    bt1_4 = Button(b, compound=TOP, text="1-p1", relief='ridge',
##                                    borderwidth=3,
##                                    width=20)
##    bt1_4.place(width=52,height=30,x= 579,y= 200)
##    bt_dict[4]=bt1_4
##
##    bt1_5 = Button(b, compound=TOP, text="1-p1", relief='ridge',
##                                    borderwidth=3,
##                                    width=20)
##    bt1_5.place(width=52,height=30,x= 579,y= 200)
##    bt_dict[5]=bt1_4

#----------------------bt in 2nd

##    oval_dict = {}
##    rect_dict = {}
##    line_dict = {}
##    label_dict_rect= defaultdict(dict)
##    label_dict_oval= defaultdict(dict)
##
##    T = [9,9,5,1,9,9,4,9]
##    P1 = np.array([k/10 for k in T])
##    P0 = 1-P1
##    for n in range(0,8):
##        oval_id = draw.create_oval((n+1.5)*80-15,240,(n+1.5)*80+1+15,270,fill='skyblue')
##        oval_dict[n] = oval_id
##        label=ttk.Label(draw, text=str(P1[n]),font = ("courier ",10),relief="groove",borderwidth=2)
##        label.place(x=(n+1.4)*80+2, y=280)
##    for m in range(0,4):
##        rect_id = draw.create_rectangle((m+3.5)*80-15,105,(m+3.5)*80+15,135,fill='light green')    
##        rect_dict[m] = rect_id
##    line_var=0
##    
##    for n in range(0,8):
##        for m in range(0,4):
##            if H[m][n]==1:
##                oval_coord = draw.coords(oval_dict[n])
##                rect_coord = draw.coords(rect_dict[m])
##                oval_node_xy = [int((oval_coord[0]+oval_coord[2])/2),int((oval_coord[1]+oval_coord[3])/2)]
##                rect_node_xy = [int((rect_coord[0]+rect_coord[2])/2),int((rect_coord[1]+rect_coord[3])/2)]
##                link1_id = draw.create_line(oval_node_xy[0], oval_node_xy[1], rect_node_xy[0], rect_node_xy[1], fill = "blue", width=4)
##                
##                line_dict[line_var]=link1_id
##                line_var=line_var+1
##                
##                draw.tag_lower(link1_id)
##                draw.tag_lower(image_id)
##
##    MaxValue=0.9
##    MinValue=0.1
##    
##
##    qij1 = np.zeros((4,8))
##    qij0 = np.zeros((4,8))
##    for m in range(0,4):
##            for n in  range(0,8):
##                qij0[m][n]=(P0[n]*H[m][n])
##                qij1[m][n]=(P1[n]*H[m][n])
##                label=ttk.Label(draw, text=str(qij1[m][n]),font = ("courier ",5))
##                label.place(x=(n+7)*17, y=340+m*28)
##
##        
##    rij0 = np.zeros((4,8))
##    rij1 = np.zeros((4,8))
##
##    for m in range(0,4):      
##                prod_term = 1
##                for k in range(0,8):
##                    if H[m][k] != 0:
##                        if qij1[m][k]>MaxValue:    
##                            qij1[m][k] = MaxValue  
##                        if qij1[m][k]<MinValue:    
##                            qij1[m][k] = MinValue  
##                        prod_term *= 1-2*qij1[m][k]
##                for n in range(0,8):
##                    if H[m][n] != 0:
##                        rij0[m][n] = 0.5 + 0.5*prod_term/(1-2*qij1[m][n])
##                        rij1[m][n] = 1 - rij0[m][n]
##                        rij1[m][n] = np.around(rij1[m][n],decimals=1)
##    for m in range(0,4):
##            for n in  range(0,8):
##                
##                label=ttk.Label(draw, text=str(rij1[m][n]),font = ("courier ",5))
##                label.place(x=(n+22)*20, y=340+m*28)
##
##    for m in range(0,4):
##        sum1 = np.sum(H[m,:])
##        for x in range (0,sum1):
##            label=Label(b, text="_",font = 10, relief='groove', borderwidth='2')
##            label.place(x=(m+3.5+0.15*x)*80-20, y=110)
##            label_dict_rect[m][x]= label    
##
##    for n in range(0,8):
##        sum2 = np.sum (H[:,n])
##        for y in range (0,sum2):
##            label=Label(b, text=" ",font = 10,relief='groove', borderwidth='2')
##            label.place(x=(n+1.5+0.15*y)*80+2, y=410)
##            label_dict_oval[n][y]= label  

    

    
    

def valid_code():
   
    b =Toplevel()
    b.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b.geometry(winSize)
    draw = Canvas(b,height=500, width=800,background='white')
    ####
    photo = PhotoImage(file = './night_sky1.png')
    draw.image = photo
    image_id=draw.create_image(400, 250, image=photo, state=NORMAL)
    ####
    draw.place(x=1,y=1)

    b3 =Toplevel()
    b3.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b3.geometry(winSize)
    draw3= Canvas(b3,height=500, width=800,background='white')
    ####
    photo = PhotoImage(file = './inst_2.png')
    draw3.image = photo
    image_id=draw3.create_image(400, 250, image=photo, state=NORMAL)
    ####
    draw3.place(x=1,y=1)

    def doSomething():
                    
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                    
    b.protocol('WM_DELETE_WINDOW', doSomething)
    root.withdraw()
    
    n1=1
    
    code = np.array([random.randint(0,1) for k in range(0,8)])
##    code= np.zeros(8)
   
    
    for n in range (0,8):
        label=ttk.Label(draw, text=str(code[n]),font = ("courier ",20),relief="groove", borderwidth=6)
        label.place(x=(n+1.5)*65+60, y=327)

    matrix = H *(code.T)
    
    for m in range (0,4):
        if np.sum(matrix[m,:])%2==0 :
             n1=n1*1
        else:
            n1=0
    def win():

        
                b1 =Toplevel()
                b1.resizable(width=False,height=False)
                height=200
                width=400
                winSize = str(width)+'x'+str(height)
                b1.geometry(winSize)

                

                def doSomething():
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                    
                b1.protocol('WM_DELETE_WINDOW', doSomething)

                def doSomething1():
                      print('close')
                

                b.protocol('WM_DELETE_WINDOW', doSomething1)
                bt_quit.config(state="disable")
                bt_submit.config(state="disable")
                bt_right.config(state="disable")
                bt_wrong.config(state="disable")
                
                draw = Canvas(b1,height=500, width=800,background='white')
                ####
                photo = PhotoImage(file = './win3.png')
                draw.image = photo
                draw.create_image(200, 100, image=photo, state=NORMAL)
                ####
                draw.place(x=0,y=0)

                
                def nextlevel_1():
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
                    root.deiconify()

                    bt_1.config(relief='ridge')
                    bt_3.config(state="normal")
                    bt_2.config(relief="ridge")
                    
                bt_next = Button(draw, compound=TOP,
                    fg='#b7f731',
                    relief='raised',
                    borderwidth=6,
                    width=20,command= nextlevel_1)
                image=PhotoImage(file='next_1.png')
                image=image.subsample(5)
                bt_next['image']=image
                bt_next.image = image
                bt_next.place(width=60,height=40,x=210,y=130)

        
    def lose():

                b1 =Toplevel()
                b1.resizable(width=False,height=False)
                height=200
                width=400
                winSize = str(width)+'x'+str(height)
                b1.geometry(winSize)
                draw = Canvas(b1,height=500, width=800,background='white')
                ####
                photo = PhotoImage(file = 'lose3.png')
                draw.image = photo
                draw.create_image(200, 100, image=photo, state=NORMAL)
                ####
                draw.place(x=0,y=0)

                  
                
                

                def doSomething():
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                   
                b1.protocol('WM_DELETE_WINDOW', doSomething)

                def doSomething1():
                    print('close')
                

                b.protocol('WM_DELETE_WINDOW', doSomething1)
                bt_quit.config(state="disable")
                bt_submit.config(state="disable")
                bt_right.config(state="disable")
                bt_wrong.config(state="disable")
                def retry1():
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
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
                bt_retry.place(width=60,height=40,x=210,y=130)


                
        
    def submit():
        global ans
        print("ans,n1",ans,n1)
        if n1==1 and ans ==True:
##            print("you win")
            win()
        elif n1==1 and ans== False:
##            print("you lose")
            lose()
        elif n1==0 and ans== False:
##            print("you win")
            win()
        else:
            lose()
    def right():
        global ans
        bt_submit.config(state="normal")
        ans= True
        print(ans)
        bt_right.config(state='disable')
        bt_wrong.config(state='normal')
    bt_right = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=right)
    image=PhotoImage(file='right_tick.png')
    image=image.subsample(10)
    bt_right['image']=image
    bt_right.image = image
    bt_right.place(width=80,height=75,x=190,y=390)

    def wrong():
        global ans
        bt_submit.config(state="normal")
        ans=False
        print(ans)
        bt_right.config(state='normal')
        bt_wrong.config(state='disable')
    bt_wrong = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=wrong)
    image=PhotoImage(file='wrong.png')
    image=image.subsample(10)
    bt_wrong['image']=image
    bt_wrong.image = image
    bt_wrong.place(width=80,height=75,x=500,y=390)
    
    def quit2():
        b.destroy()
        b3.destroy()
        root.deiconify()
    bt_quit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='flat',
                borderwidth=6,
                width=20,command=quit2)
    image=PhotoImage(file='home3.png')
    image=image.subsample(40)
    bt_quit['image']=image
    bt_quit.image = image
    bt_quit.place(width=50,height=50,x=740,y=440)

    bt_submit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=submit , state="disable")
    image=PhotoImage(file='submit5.png')
    image=image.subsample(2)
    bt_submit['image']=image
    bt_submit.image = image
    bt_submit.place(width=80,height=75,x=710,y=60)

def girth():

    H1 =  np.array([[1,1,0,0,1,1,1,0],
             [0,1,1,1,0,0,0,0],
             [0,0,1,0,1,0,0,1],
             [0,0,0,1,0,1,0,1]])

    Htemp =  [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
    
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

    b3 =Toplevel()
    b3.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b3.geometry(winSize)
    draw3= Canvas(b3,height=500, width=800,background='white')
    ####
    photo = PhotoImage(file = './inst_4.png')
    draw3.image = photo
    image_id=draw3.create_image(400, 250, image=photo, state=NORMAL)
    ####
    draw3.place(x=1,y=1)
    root.withdraw()
    line_list_all = {}
    rect_list_all = {}
    oval_list_all = {}
##    H_1= np.zeros((4,8))
    for n in range(0,8):
        oval_id=draw.create_oval((n+1.5)*80-20,400,(n+1.5)*80+1+20,440,fill='light green')
        oval_list_all[n] = oval_id
        for m in range(0,4):
            rect_id=draw.create_rectangle((m+3.5)*80-20,230,(m+3.5)*80+20,270,fill='light green')
            rect_list_all[m] = rect_id
            if H1[m][n] == 1:
                line_id=draw.create_line((n+1.5)*80+0.5,420,(m+3.5)*80,250,fill='yellow',width=4)
                line_list_all = line_id
                draw.tag_lower(line_id)
                draw.tag_lower(image_id)

 

    m = StringVar()
    
    m.set('6')
    label_random = Label(b,textvariable = m,bg="palegreen", fg="green",font=(None, 50))
    label_random.place(width=80,height=75,x=370, y=120)

    
    draw.bind("<Button-1>",lambda e: xy3(e,m))
    def xy3(event,m):
        x,y = event.x, event.y            
        line_list = [item for item in draw.find_overlapping(event.x-2, event.y-2, event.x+2, event.y+2) if draw.type(item) == "line"]
        if len(line_list)==1:
            if draw.itemcget(line_list[0],"fill")=="yellow":
            #if line_id==line_id(line_list[0],fill="skyblue"): 
                selected_object1 = line_list[0]
                coords = draw.coords(line_list[0])
                coordsy = int(((coords[0]-0.5)/80)-1.5)
                coordsx = int(((coords[2])/80)-3.5)
                print(coordsx,coordsy)
                Htemp[coordsx][coordsy]=1
                draw.itemconfig(selected_object1,fill="maroon")
                tmp = m.get()
                tmp = int(tmp)
                tmp -= 1
                m.set(tmp)
            else:
                selected_object1 = line_list[0]
                draw.itemconfig(selected_object1,fill="yellow")
                coords = draw.coords(line_list[0])
                coordsy = int(((coords[0]-0.5)/80)-1.5)
                coordsx = int(((coords[2])/80)-3.5)
                Htemp[coordsx][coordsy] = 0
                tmp = m.get()
                tmp = int(tmp)
                tmp += 1
                m.set(tmp)
            print(Htemp)    
                
    def submit(m):

        tmp = int(m.get())
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
       
        if girth==6 and tmp==0:
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
                b3.destroy()
                root.deiconify()
                
            b1.protocol('WM_DELETE_WINDOW', doSomething)

            def doSomething1():
                print('close')
                

            b.protocol('WM_DELETE_WINDOW', doSomething1)
            bt_quit.config(state="disable")
            bt_submit.config(state="disable")  
            
            draw = Canvas(b1,height=500, width=800,background='white')
            ####
            photo = PhotoImage(file = './11321_win.png')
            draw.image = photo
            draw.create_image(200, 150, image=photo, state=NORMAL)
            ####
            draw.place(x=0,y=-70)

            
            def nextlevel_1():
                    global m_start
                    m_start=0
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
                    root.deiconify()

                    bt_1.config(relief='ridge')
                    bt_3.config(relief="ridge")
                    bt_2.config(relief="ridge")
                    bt_4.config(relief="ridge")
                    bt_5.config(state="normal")
                    
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
            if tmp<0 and girth==6 :
                score = int(((girth+tmp/6)/6)*100)
            elif tmp >0 and girth!=6 :
                score = 0
            
           
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

            def doSomething1():
                print('close')
                

            b.protocol('WM_DELETE_WINDOW', doSomething1)
            bt_quit.config(state="disable")
            bt_submit.config(state="disable")        
            
            def doSomething():
                b1.destroy()
                b.destroy()
                b3.destroy()
                root.deiconify()
               
            b1.protocol('WM_DELETE_WINDOW', doSomething)

            def doSomething1():
                print('close')
                

            b.protocol('WM_DELETE_WINDOW', doSomething1)
            bt_quit.config(state="disable")
            bt_submit.config(state="disable")  
            
            def retry1():
                b1.destroy()
                b.destroy()
                b3.destroy()
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
                width=20,command=partial(submit,m))
    image=PhotoImage(file='submit5.png')
    image=image.subsample(2)
    bt_submit['image']=image
    bt_submit.image = image
    bt_submit.place(width=80,height=75,x=710,y=100)

    def quit2():
        global m_start
        global itr
        m_start=0
        itr=0
        b.destroy()
        b3.destroy()
        root.deiconify()
        
    bt_quit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='flat',
                borderwidth=6,
                width=20,command=quit2)
    image=PhotoImage(file='home3.png')
    image=image.subsample(40)
    bt_quit['image']=image
    bt_quit.image = image
    bt_quit.place(width=50,height=50,x=740,y=440)


    
    
def hard_decision():
    
    bt_3.config(state="normal")
    root.withdraw()

    code_recieved= np.array([0,0,0,1,0,0,0,1])
    code_without_error= np.array([0,0,1,1,0,0,0,1])
    Max_iteration=4
    print(m_start)
    b =Toplevel()
    b.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b.geometry(winSize)
    draw = Canvas(b,height=500, width=800,background='white')
    ####
    photo = PhotoImage(file = './2_background1.png')
    draw.image = photo
    image_id=draw.create_image(400, 250, image=photo, state=NORMAL)
    ####
    draw.place(x=1,y=1)

    b3 =Toplevel()
    b3.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b3.geometry(winSize)
    draw3= Canvas(b3,height=500, width=800,background='white')
    ####
    photo = PhotoImage(file = './inst_3.png')
    draw3.image = photo
    image_id=draw3.create_image(400, 250, image=photo, state=NORMAL)
    ####
    draw3.place(x=1,y=1)

    def doSomething():
                    
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                    
    b.protocol('WM_DELETE_WINDOW', doSomething)


    oval_dict = {}
    rect_dict = {}
    line_dict = {}

   
    
    for n in range(0,8):
        oval_id = draw.create_oval((n+1.5)*80-15,320,(n+1.5)*80+1+15,350,fill='skyblue')
        oval_dict[n] = oval_id
        label=ttk.Label(draw, text=str(code_recieved[n]),font = ("courier ",20))
        label.place(x=(n+1.5)*80+2, y=365)
    for m in range(0,4):
        rect_id = draw.create_rectangle((m+3.5)*80-15,150,(m+3.5)*80+15,180,fill='light green')    
        rect_dict[m] = rect_id
    line_var=0
    
    for n in range(0,8):
        for m in range(0,4):
            if H[m][n]==1:
                oval_coord = draw.coords(oval_dict[n])
                rect_coord = draw.coords(rect_dict[m])
                oval_node_xy = [int((oval_coord[0]+oval_coord[2])/2),int((oval_coord[1]+oval_coord[3])/2)]
                rect_node_xy = [int((rect_coord[0]+rect_coord[2])/2),int((rect_coord[1]+rect_coord[3])/2)]
                link1_id = draw.create_line(oval_node_xy[0], oval_node_xy[1], rect_node_xy[0], rect_node_xy[1], fill = "blue", width=4)
                
                line_dict[line_var]=link1_id
                line_var=line_var+1
                
                draw.tag_lower(link1_id)
                draw.tag_lower(image_id)
    
    print(m_start)

    
    button_dict = {}
    label_dict_rect= defaultdict(dict)
    label_dict_oval= defaultdict(dict)
    bt_final_dict = defaultdict(dict)
    correct_label_dict_rect = defaultdict(dict)
    correct_label_dict_oval = defaultdict(dict)

    qij = H * (code_recieved.T) 
    for m in range (0,4):
        k=0
        for n in range (0,8):
            if H[m][n]!=0:
                correct_label_dict_rect[m][k]=qij[m][n]
                k=k+1
                
    rij=np.zeros((4,8))
    s1=0
    for m in range(0,4):
        print('hello')
        vn= np.nonzero(H[m,:])
        print("vn",vn)
        length = len(vn[0])
        print(m,length)
        print(qij[m][vn])
        for k in range (0,length):
            sum1=0
            for t in range (0,length):
                if t==k:
                    s1=0
                else:
                    s1= qij[m][vn[0][t]]
                    print("s1",s1)
                sum1=sum1+s1
            if sum1%2==0:
                rij[m][vn[0][k]]=0
            else:
                print("yes")
                rij[m][vn[0][k]]=1

    print("rij",rij)

    for n in range (0,8):
        k=0
        for m in range(0,4):
            if H[m][n]!=0:
                correct_label_dict_oval[n][k]=rij[m][n]
                k=k+1
    print("correct oval label", correct_label_dict_oval)
                
    photo_msg1 = PhotoImage(file="bt_2_msg1.png")
    photo_msg1=photo_msg1.subsample(8)
    label_msg1= Label(b, image =photo_msg1, height= 70 ,width=70,relief='raised', borderwidth=4)
    label_msg1.photo=photo_msg1
    label_msg1.place(x=710, y=150)
    
    photo_msg2 = PhotoImage(file="bt_2_msg2.png")
    photo_msg2 = photo_msg2.subsample(8)
    label_msg2= Label(b, image=photo_msg2, height= 70 ,width=70,state='disabled', borderwidth=4,relief='raised')
    label_msg2.photo=photo_msg2
    label_msg2.place(x=710, y=230)

    photo_ans3 = PhotoImage(file="final_ans.png")
    photo_ans3=photo_ans3.subsample(8)
    label_ans3= Label(b, image=photo_ans3, height= 70 ,width=70, state= "disabled",borderwidth=4,relief='raised')
    label_ans3.place(x=710, y=310)
    label_ans3.photo=photo_ans3
    
    
    
    for m in range(0,4):
        sum1 = np.sum(H[m,:])
        for x in range (0,sum1):
            label=Label(b, text="_",font = 10, relief='groove', borderwidth='2')
            label.place(x=(m+3.5+0.15*x)*80-20, y=110)
            label_dict_rect[m][x]= label    

    for n in range(0,8):
        sum2 = np.sum (H[:,n])
        for y in range (0,sum2):
            label=Label(b, text=" ",font = 10,relief='groove', borderwidth='2')
            label.place(x=(n+1.5+0.15*y)*80+2, y=410)
            label_dict_oval[n][y]= label  
    
   
##    def up():
##        global m_start
####        rect_pos= draw.coords(rect_dict[m_start-1])
####        label_dict_rect[m_start-1].config(text="")
##        for k in button_dict:
##            label_dict_rect[m_start-1][k].config(text= button_dict[k]['text'])

##    def down():
##        
##        global m_start
####        rect_pos= draw.coords(rect_dict[m_start-5])
####        label_dict_oval[m_start-5].config(text="")
##        for k in button_dict:
##            label_dict_oval[m_start-5][k].config(text= button_dict[k]['text'])
        
    def left():
        global m_start
        global itr
        if itr>0 and m_start==1:
            m_start=13
            for n in range (0,8):
                bt_final_dict[itr-1][n].config(state="normal")
            itr=itr-1
              
        def count():
            global m_start
            m_start=m_start-2
        count()
        start_hard_decision()
##
##    def msg1():
##        global m_start
##        if m_start>4:
##            m_start=0
##            start_hard_decision()
##        bt_msg1.config(state="disable")
##    def msg2():
##        global m_start
##        if m_start<=4:
##            m_start=4
##            start_hard_decision()
##        bt_msg2.config(state="disable")
##        
##
##    bt_msg1 = Button(draw, compound=TOP,
##                fg='#b7f731',
##                relief='raised',
##                borderwidth=6,
##                width=20,command=msg1)
##    image=PhotoImage(file='bt_2_msg1.png')
##    image=image.subsample(8)
##    bt_msg1['image']=image
##    bt_msg1.image = image
##    bt_msg1.place(width=80,height=75,x=630,y=150)
##
##    bt_msg2 = Button(draw, compound=TOP,
##                fg='#b7f731',
##                relief='raised',
##                borderwidth=6,
##                width=20,command=msg2)
##    image=PhotoImage(file='bt_2_msg2.png')
##    image=image.subsample(8)
##    bt_msg2['image']=image
##    bt_msg2.image = image
##    bt_msg2.place(width=80,height=75,x=710,y=150)  
##            
##    bt_msg1.config(state="disable")
##    bt_msg2.config(state="disable")
        

    def start_hard_decision():
        
        
        
        global itr
        global m_start
        button_var=0
        n1=1
        m1=1
        if m_start==4:
            for k in correct_label_dict_rect :
                for n in correct_label_dict_rect[k]:
                   print("k,n",k,n)
                   print(label_dict_rect[k][n]['text'])
                   if label_dict_rect[k][n]['text']!="_" :
                        print("label is not blank")
                        if int(correct_label_dict_rect[k][n]) == int(label_dict_rect[k][n]['text']) :
                            print("one item match")
                            n1=n1*1
                        else:
                            n1=n1*0
                   else:
                            n1=n1*0
            print("n1",n1)           
            if n1==1:
                            print("yeyeyeyeyeyeyeyy")
                            label_msg2.config(state="normal")
                            photo_msg1 = PhotoImage(file="bt_2_msg1_tick.png")
                            photo_msg1= photo_msg1.subsample(8)
                            label_msg1.photo=photo_msg1
                            label_msg1['image']= photo_msg1
                            label_msg1.config(state="disabled")
                            
            else:
                            print("correct",correct_label_dict_rect)
                            print("label",label_dict_rect)
                            print('no match')
                            m_start=m_start-4
                            
            
            
        if m_start>=4:

            
                            for n in range(0,8):
                                    sum2 = np.sum (H[:,n])
                                    for y in range (0,sum2):
                                        if label_dict_oval[n][y]['text']== " ":
                                             label_dict_oval[n][y]['text']= "_"
         
                       
                       
##        if m_start<4:
##            bt_msg2.config(state="normal")
##            bt_msg1.config(state="disable")
##            
##        else:
##            bt_msg1.config(state="normal")
##            bt_msg2.config(state="disable")


        def ans(n,itr):
             global ans_click
             ans_click=1
             if bt_final_dict[itr][n]['text']==str(0):
                        bt_final_dict[itr][n]['text']=str(1)
             else:
                        bt_final_dict[itr][n]['text']=str(0)
        def print1(button_var):
                                   
                                   if m_start>=1 and m_start<=4 :
                                            
                                            
                                            if label_dict_rect[m_start-1][button_var]['text']==str(1) or label_dict_rect[m_start-1][button_var]['text']=="_":
                                                label_dict_rect[m_start-1][button_var]['text']=str(0)
                                            else:
                                                label_dict_rect[m_start-1][button_var]['text']=str(1)
                                                
                                   elif m_start>4 and m_start<=12 :
                                            print("bug")
                                            if label_dict_oval[m_start-5][button_var]['text']==str(1) or label_dict_oval[m_start-5][button_var]['text']=="_":
                                                label_dict_oval[m_start-5][button_var]['text']=str(0)
                                            
                                            else:
                                                label_dict_oval[m_start-5][button_var]['text']=str(1)
                                    
       
           
                
        def count():
            global m_start
            m_start=m_start+1
        count()
        print(m_start)

       
        bt_right.config(state="normal")
        if m_start>1:
            bt_left.config(state="normal")
        else:
            bt_left.config(state="disable")

        if m_start==5:
            bt_left.config(state="disable")
            

##        def update_msg(button_var):
##            global m_start
##            print("m_start",m_start)
##            print("button var",button_var)
##            print(button_dict)
##            print(label_dict_rect)
##            print(label_dict_rect[0][0])
##            
##            if m_start>=1 and m_start<=4 :
##                label_dict_rect[m_start-1][button_var].config(text=button_dict[button_var]['text'])
##            else :
##                label_dict_oval[m_start-5][button_var].config(text= button_dict[button_var]['text'])

                
        if m_start<=4:
##            if m_start>=1:
##                bt_up.config(state="normal")
##            bt_down.config(state="disable")
            rect_pos = draw.coords(rect_dict[m_start-1])
           
            for k in button_dict:
                print("hello")
    ##            draw.itemconfig(text_dict[k],state="hidden")
                button_dict[k].destroy()

            
            
            for k in line_dict:
                
                line_pos = draw.coords(line_dict[k])
                print(line_pos)
                if line_pos[2]==int((rect_pos[0]+rect_pos[2])/2) and line_pos[3]== int((rect_pos[1]+rect_pos[3])/2) :
                       draw.itemconfig(line_dict[k],state="normal")
                       draw.itemconfig(line_dict[k],fill="orange")
        ##               text_id= draw.create_text(int((line_pos[0]+line_pos[2])/2)-1,int((line_pos[1]+line_pos[3])/2)-1,fill="blue",width=45)

    ##                   T = Text(b, height=2, width=2)
    ##                   T.place(x= int((line_pos[0]+line_pos[2])/2)-1,y= int((line_pos[1]+line_pos[3])/2)-1)
    ##                   text_dict[text_var]=T
    ##                   print(text_dict)
    ##                   text_var=text_var+1

##                       def update_msg(button_var):
##                                    global m_start
##                                    print("m_start",m_start)
##                                    print("button var",button_var)
##                                    print(button_dict)
##                                    print(label_dict_rect)
##                                    print(label_dict_rect[0][0])
##            
##                                    if m_start>=1 and m_start<=4 :
##                                            label_dict_rect[m_start-1][button_var].config(text=button_dict[button_var]['text'])
##                                    else :
##                                            label_dict_oval[m_start-5][button_var].config(text= button_dict[button_var]['text'])
                      

                       bt = Button(b, compound=TOP, text="0/1",
                                    
                                    relief='ridge',
                                    borderwidth=3,
                                    width=20,command=partial(print1, button_var))
    ##                    image=PhotoImage(file='next_1.png')
    ##                    image=image.subsample(5)
    ##                    bt_next['image']=image
    ##                    bt_next.image = image
                       bt.place(width=30,height=30,x= int((line_pos[0]+line_pos[2])/2)-1,y= int((line_pos[1]+line_pos[3])/2)-1)
                       button_dict[button_var]= bt
                       print("bt_dict",button_dict)
                       button_var=button_var+1
                  
                   
                else:
                    draw.itemconfig(line_dict[k],state="hidden")
        if m_start>4 and m_start <=12:

##                bt_down.config(state="normal")
##                bt_up.config(state="disable")
                
                oval_pos= draw.coords(oval_dict[m_start-5])
                
                for k in button_dict:
                    print("hello")
        ##            draw.itemconfig(text_dict[k],state="hidden")
                    button_dict[k].destroy()

                for m in range(0,4):
                     if H[m][m_start-5]==1:
                            rect_pos= draw.coords(rect_dict[m])
                            for k in line_dict:
                
                                    line_pos = draw.coords(line_dict[k])
                                    print(line_pos)
                                    if line_pos[2]==int((rect_pos[0]+rect_pos[2])/2) and line_pos[3]== int((rect_pos[1]+rect_pos[3])/2) :
                                        draw.itemconfig(line_dict[k],state="normal")
                                        draw.itemconfig(line_dict[k],fill="light grey")
                     else:
                            rect_pos= draw.coords(rect_dict[m])
                            for k in line_dict:
                
                                    line_pos = draw.coords(line_dict[k])
                                    print(line_pos)
                                    if line_pos[2]==int((rect_pos[0]+rect_pos[2])/2) and line_pos[3]== int((rect_pos[1]+rect_pos[3])/2) :
                                        draw.itemconfig(line_dict[k],state="hidden")
            
                for k in line_dict:
                    
                    line_pos = draw.coords(line_dict[k])
                    print(line_pos)
                    if line_pos[0]==int((oval_pos[0]+oval_pos[2])/2) and line_pos[1]== int((oval_pos[1]+oval_pos[3])/2) :
                            draw.itemconfig(line_dict[k],state="normal")
                            draw.itemconfig(line_dict[k],fill="orange")


##                            def update_msg(button_var):
##                                    global m_start
##                                    print("m_start",m_start)
##                                    print("button var",button_var)
##                                    print(button_dict)
##                                    print(label_dict_rect)
##                                    print(label_dict_rect[0][0])
##            
##                                    if m_start>=1 and m_start<=4 :
##                                            label_dict_rect[m_start-1][button_var].config(text=button_dict[button_var]['text'])
##                                    else :
##                                            label_dict_oval[m_start-5][button_var].config(text= button_dict[button_var]['text'])
                           
                                    
                            bt = Button(b, compound=TOP, text="0/1",
                                   
                                    relief='ridge',
                                    borderwidth=3,
                                    width=25,command=partial(print1, button_var))
                            bt.place(width=30,height=30,x=int((line_pos[0]+line_pos[2])/2)-1,y= int((line_pos[1]+line_pos[3])/2)-1)
                            button_dict[button_var]= bt
                            button_var=button_var+1
                         
##                if m_start==12:

                     
                      
                     
                      

                
        if m_start>12:

                   for k in correct_label_dict_oval :
                                    for n in correct_label_dict_oval[k]:
                                           print("k,n",k,n)
                                           print(label_dict_oval[k][n]['text'])
                                           if label_dict_oval[k][n]['text']!="_" :
                                                    print("label is not blank")
                                                    if int(correct_label_dict_oval[k][n]) == int(label_dict_oval[k][n]['text']) :
                                                            print("one item match")
                                                            m1=m1*1
                                                    else:
                                                            m1=m1*0
                                           else:
                                                     m1=m1*0
                                                     
                   print("m1",m1)           
                   if m1==1:
                            print("yeyeyeyeyeyeyeyy")
                            label_ans3.config(state="normal")
                            
                            photo_msg2 = PhotoImage(file="bt_2_msg2_tick.png")
                            photo_msg2= photo_msg2.subsample(8)
                            label_msg2.photo=photo_msg2
                            label_msg2['image']= photo_msg2
                            label_msg2.config(state="disabled")

                            for k in button_dict:
                                      button_dict[k].destroy()

                            for k in line_dict:
                                      draw.itemconfig(line_dict[k],state="hidden")

                            for n in range(0,8):  
                                    bt=Button(b, relief='ridge',
                                            borderwidth=3,
                                            width=20,text="0", command = partial(ans, n,itr))
                                    bt.place(width=20,height=26, x=(n+1.5)*80+2, y= (itr*18)+455)
                            
                                    bt_final_dict[itr][n]= bt
                            if itr==0:
                                print("helloooooooo")
                                bt_right.config(state="disable")

                            
                   else:
                            print("correct",correct_label_dict_oval)
                            print("label",label_dict_oval)
                            print('no match')
                            m_start=m_start-9
                            start_hard_decision()


##                    
##                   for n in range(0,8):  
##                            bt=Button(b, relief='ridge',
##                                    borderwidth=6,
##                                    width=20,text="0", command = partial(ans, n,itr))
##                            bt.place(width=20,height=26, x=(n+1.5)*80+2, y= (itr*18)+455)
##                            
##                            bt_final_dict[itr][n]= bt
##                   if itr==0:
##                           print("helloooooooo")
##                           bt_right.config(state="disable")
##
##                   
                   print("Hello")
##                   m_start=0
                   

                   
##                   for n in range(0,8):
##                       bt_final_dict[itr][n].config(state='disable')
##                   itr=itr+1
                   
                   if itr>0:
                       bt_left.config(state="normal")
                   else:
                       bt_left.config(state="disable")
##                   bt_up.config(state="disable")
##                   bt_down.config(state="disable")
##                   start_hard_decision()
                   bt_left.config(state="disable")
                   
 #------------left------
    bt_left = Button(draw, compound=TOP,
                    fg='#b7f731',
                    relief='raised',
                    borderwidth=6,
                    width=20,command=left)
    image=PhotoImage(file='left.png')
    image=image.subsample(5)
    bt_left['image']=image
    bt_left.image = image
    bt_left.place(width=50,height=50,x=25,y=160)

    bt_right = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=start_hard_decision)
    image=PhotoImage(file='right.png')
    image=image.subsample(5)
    bt_right['image']=image
    bt_right.image = image
    bt_right.place(width=50,height=50,x=145,y=160)

#---------------------------    
##    bt_up.config(state="disable")
##    bt_down.config(state="disable")
    bt_left.config(state="disable")        
#-------------------  quit--                
    def quit2():
        global m_start
        global itr
        m_start=0
        itr=0
        b.destroy()
        b3.destroy()
        root.deiconify()
        
    bt_quit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='flat',
                borderwidth=6,
                width=20,command=quit2)
    image=PhotoImage(file='home3.png')
    image=image.subsample(40)
    bt_quit['image']=image
    bt_quit.image = image
    bt_quit.place(width=50,height=50,x=740,y=440)

    submitted_code=np.zeros(8)

   
    
    def submit():

        if bool(bt_final_dict)==True:
            global itr
            global m_start
    ##        print(text_final_dict)
            m=0
            for k in bt_final_dict :
                 m=m+1
            
            for n in range (0,8):
                print (bt_final_dict)
                if bt_final_dict[m-1][n]['state']=='disable' :
                        bt_final_dict[m-1][n].config(state='normal')
                        x = int(bt_final_dict[m-1][n]['text'])
                        submitted_code[n]=x
                        bt_final_dict[m-1][n].config(state='disable')
                else:
                        x = int(bt_final_dict[m-1][n]['text'])
                        submitted_code[n]=x

            print(submitted_code)    
            if np.array_equal(submitted_code, code_without_error)==True:

                b1 =Toplevel()
                b1.resizable(width=False,height=False)
                height=200
                width=400
                winSize = str(width)+'x'+str(height)
                b1.geometry(winSize)

                

                def doSomething():
                    global m_start
                    m_start=0
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                    
                b1.protocol('WM_DELETE_WINDOW', doSomething)

                def doSomething1():
                    print('close')
                

                b.protocol('WM_DELETE_WINDOW', doSomething1)
                bt_quit.config(state="disable")
                bt_submit.config(state="disable")  
                
                draw = Canvas(b1,height=500, width=800,background='white')
                ####
                photo = PhotoImage(file = './11321_win.png')
                draw.image = photo
                draw.create_image(200, 150, image=photo, state=NORMAL)
                ####
                draw.place(x=0,y=-70)

                
                def nextlevel_1():
                    global m_start
                    m_start=0
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
                    root.deiconify()

                    bt_1.config(relief='ridge')
                    bt_3.config(relief="ridge")
                    bt_2.config(relief="ridge")
                    bt_4.config(state="normal")
                    
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

            else:
    ##            score=0
    ##            global ans_click
    ##            if ans_click>0:
    ##                for n in range (0,8):
    ##                    if submitted_code[n]== code_without_error[n]:
    ##                        score=score+1
    ##
    ##                score_100=int(score/8*100)
    ##            else:
    ##                score_100=0

                score=0
                j=0
                correct= sum(code_without_error)
                for m in range (0,8):
                    
                        if submitted_code[m]==code_without_error[m] and code_without_error[m]==1:
                            j=j+1
                
                k=0
                for m in range (0,8):
                    
                        if submitted_code[m]!=code_without_error[m] and submitted_code[m]==1:
                            k=k+1

                if j==0 and k==0 :
                    score=0
                elif j>0 and k==0:
                    score = int(j/correct*100)
                elif j==0 and k>0:
                    score=0
                elif j>=k :
                    score = int((j-k/4)/correct*100)
                else:
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
                    global m_start
                    m_start=0
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                   
                b1.protocol('WM_DELETE_WINDOW', doSomething)

                def doSomething1():
                    print('close')
                

                b.protocol('WM_DELETE_WINDOW', doSomething1)
                bt_quit.config(state="disable")
                bt_submit.config(state="disable")  
                def retry1():
                    global m_start
                    m_start=0
                    b1.destroy()
                    b.destroy()
                    b3.destroy()
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
    bt_submit.place(width=80,height=75,x=710,y=60)

    

def quit1():
    root.destroy()
def matrix():
##    p= np.zeros((2,2))
    b =Toplevel()
    b.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b.geometry(winSize)
    draw = Canvas(b,height=500, width=800,background='white')

    def doSomething():
                    
                    b.destroy()
                    b3.destroy()
                    root.deiconify()
                    
    b.protocol('WM_DELETE_WINDOW', doSomething)

    ##-------------------------quit--
    def quit2():
        b.destroy()
        b3.destroy()
        root.deiconify()
    bt_quit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='flat',
                borderwidth=6,
                width=20,command=quit2)
    image=PhotoImage(file='home3.png')
    image=image.subsample(40)
    bt_quit['image']=image
    bt_quit.image = image
    bt_quit.place(width=50,height=50,x=740,y=440)
    ####
    photo = PhotoImage(file = './11321.png')
    draw.image = photo
    image_id=draw.create_image(410, 270, image=photo, state=NORMAL)
    ####
    draw.place(x=-5,y=-6)

    b3 =Toplevel()
    b3.resizable(width=False,height=False)
    height=500
    width=800
    winSize = str(width)+'x'+str(height)
    b3.geometry(winSize)
    draw3= Canvas(b3,height=500, width=800,background='white')
    ####
    photo = PhotoImage(file = './inst_1.png')
    draw3.image = photo
    image_id=draw3.create_image(400, 250, image=photo, state=NORMAL)
    ####
    draw3.place(x=1,y=1)
    #-----------------for checking correct----
    oval_list_all = {}
    rect_list_all = {}
    H_1= np.zeros((4,8))
    #-------------------------------------
    def delete1():
        bt_delete.configure(relief='sunken')
        draw.bind("<Button-1>",lambda e: deleteline(e))
        def deleteline(event):
            x,y = event.x, event.y            
            line_list = [item for item in draw.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1) if draw.type(item) == "line"]
            if len(line_list)>=1:
                 line_1 = line_list[0]
                 line_1_pos= draw.coords(line_1)
                 oval= [item for item in draw.find_overlapping(line_1_pos[0]-10, line_1_pos[1]-10, line_1_pos[0]+10, line_1_pos[1]+10) if draw.type(item) == "oval"]
                 rect= [item for item in draw.find_overlapping(line_1_pos[2]-10, line_1_pos[3]-10, line_1_pos[2]+10, line_1_pos[3]+10) if draw.type(item) == "rectangle"]
                 m_1=0
                 n_1=0
                 for m in range(0,4):
                     if rect_list_all[m]==rect[0]:
                         m_1=m
                 for n in range (0,8):
                     if oval_list_all[n]==oval[0]:
                         n_1=n
                 H_1[m_1][n_1]=0
                 print(H_1)
                 x=0
                 while (line_list):
##                      print("hello")
                      draw.delete(line_list[x])
                      del line_list[0]
                      
                 
            bt_delete.configure(relief='raised')
            create_newlink()
##    back=PhotoImage(file="back.png")
##    back=back.subsample(5)
##    draw.create_image(10, 10, image=back)
##    draw.attributes("-alpha", .00)
##    image=PhotoImage(file='game.png')
##    image=image.subsample(5)
##    draw['image']=image
##    draw.image = image
    bt_delete = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=delete1)
    image=PhotoImage(file='scissor_1.png')
    image=image.subsample(7)
    bt_delete['image']=image
    bt_delete.image = image
    bt_delete.place(width=75,height=60,x=50,y=290)
    
        
    def submit():
##        H_1=H
        if  np.array_equal(H, H_1)==True:
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
                b3.destroy()
                root.deiconify()
                
            b1.protocol('WM_DELETE_WINDOW', doSomething)

            def doSomething1():
                print('close')
                

            b.protocol('WM_DELETE_WINDOW', doSomething1)
            bt_quit.config(state="disable")
            bt_submit.config(state="disable")  
            
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
                b3.destroy()
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
            j=0
            
            for m in range (0,4):
                for n in range (0,8):
                    if H[m][n]==H_1[m][n] and H[m][n]==1:
                        j=j+1
            
            k=0
            for m in range (0,4):
                for n in range (0,8):
                    if H_1[m][n]!=H[m][n] and H_1[m][n]==1:
                        k=k+1

            if j==0 and k==0 :
                score=0
            elif j>0 and k==0:
                score = int(j/16*100)
            elif j==0 and k>0:
                score=0
            elif j>=k :
                score = int((j-k/4)/16*100)
            else:
                score=0
            
##            score=0
##            for m in range(0,4):
##                for n in range(0,8):
##                    if H[m][n]==H_1[m][n]:
##                        score=score+1
##            score_100 = int(score*100/32)
##            print(score_100)
            
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
                b3.destroy()
                root.deiconify()
               
            b1.protocol('WM_DELETE_WINDOW', doSomething)

            def doSomething1():
                print('close')
                

            b.protocol('WM_DELETE_WINDOW', doSomething1)
            bt_quit.config(state="disable")
            bt_submit.config(state="disable")
            
            def retry1():
                b1.destroy()
                b.destroy()
                b3.destroy()
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

    

#-------------------timer--------

##    def update_timeText():
##        # Get the current time, note you can change the format as you wish
##        current = time.strftime("%H:%M:%S")
##        # Update the timeText Label box with the current time
##        timeText.configure(text=current)
##        # Call the update_timeText() function after 1 second
##        b.after(1000, update_timeText)
##    
##    
##    # Create a timeText Label (a text box)
##    timeText = ttk.Label(draw, text="", font=("Helvetica", 15), width=14)
##    timeText.place(x=5,y=5)
##    update_timeText()
##    b.mainloop()

    

#--------------------game-------
##    label=ttk.Label(draw, text="TANNER GRAPH",font = ("courier",35), background='cyan', relief='raised')
##    label.place(x=130, y=25)   
##    
##    label=ttk.Label(draw, text="H  = ",font = ("courier ",20))
##    label.place(x=308, y=150)                
##    H =  np.array([[1,1,0,0,1,1,1,0],
##         [0,1,1,1,0,0,0,0],
##         [0,0,1,0,1,0,1,1],
##         [0,0,0,1,0,1,1,1]])
##    draw.create_line(20,250,750,250, fill='green',width=2)
##    draw.create_line(20,90,750,90, fill='green',width=2)
##     
##    draw.create_line(25*15-3,107,25*15-3,232,fill='black',width=2)
##    draw.create_line((8+22)*17+3,107,(8+22)*17+3,232,fill='black',width=2)
##    draw.create_line(25*15-3,107,(25+1)*15-3,107,fill='black',width=2)
##    draw.create_line((22+7)*17+3,107,(22+8)*17+3,107,fill='black',width=2)
##    draw.create_line(22*17-3,232,(22+1)*17-3,232,fill='black',width=2)
##    draw.create_line((22+7)*17+3,232,(22+8)*17+3,232,fill='black',width=2) 
    for n in range(0,8):
        oval_id=draw.create_oval((n+1.5)*80-20,400,(n+1.5)*80+1+20,440,fill='skyblue')
        oval_list_all[n] = oval_id
       
##                if n==0:
##                    label=ttk.Label(b, text="|",font = ("Helvetica",44),width=10)
##                    label.place(x=(n+25)*15-8, y=170+m*25)
##                label=ttk.Label(draw, text=str(H[m][n]),font = ("courier ",20))
##                label.place(x=(n+22)*17, y=108+m*28)
    for m in range(0,4):
        rect_id=draw.create_rectangle((m+3.5)*80-20,230,(m+3.5)*80+20,270,fill='skyblue')
        rect_list_all[m] = rect_id
    root.withdraw()          
    def create_newlink():
        draw.bind("<Button-1>",lambda e: xy3(e))
        
    create_newlink()
    def movenodeMotion(event,selected_object1,link_id):
        x,y = event.x,event.y
        first_node_coor = draw.coords(selected_object1)
        
        first_node_xy = [int((first_node_coor[0]+first_node_coor[2])/2),int((first_node_coor[1]+first_node_coor[3])/2)]
                 
        #link_id = draw.create_line(first_node_xy[0], first_node_xy[1], first_node_xy[0], first_node_xy[1], fill = "gray50", width=2)
##        draw.tag_lower(link_id)
##        draw.tag_lower(image_id)
        #linePos = draw.coords(lineid)
        draw.itemconfig(link_id,fill='green',width=4)
        draw.coords(link_id,x,y,first_node_xy[0], first_node_xy[1])
        draw.bind("<Button-1>",lambda e : endnodelink(e,selected_object1,link_id))
        
    def xy3(event):
        x,y = event.x, event.y            
        oval_list = [item for item in draw.find_overlapping(event.x-10, event.y-10, event.x+10, event.y+10) if draw.type(item) == "oval"]
        if len(oval_list)==1:
                 selected_object1 = oval_list[0]
                 draw.itemconfig(selected_object1,fill="gold")
                 #draw.bind("<Button-1>",lambda e : endnodelink(e,selected_object1))
                 first_node_coor = draw.coords(selected_object1)
                 first_node_xy = [int((first_node_coor[0]+first_node_coor[2])/2),int((first_node_coor[1]+first_node_coor[3])/2)]
                 link_id = draw.create_line(first_node_xy[0], first_node_xy[1], first_node_xy[0], first_node_xy[1], fill = "yellow", width=4)
                 draw.bind("<Motion>",lambda e: movenodeMotion(e,selected_object1,link_id))
    def endnodelink(event,selected_object1,link_id):
        x,y = event.x, event.y
        rect_list = [item for item in draw.find_overlapping(event.x-10, event.y-10, event.x+10, event.y+10) if draw.type(item) == "rectangle"]
        if len(rect_list)==1:
             selected_object2 = rect_list[0]
             draw.itemconfig(selected_object2,fill="pink")
             if selected_object1!=selected_object2:
                 draw.itemconfig(selected_object2,fill="pink")
                 
                 first_node_coor = draw.coords(selected_object1)
                 first_node_xy = [int((first_node_coor[0]+first_node_coor[2])/2),int((first_node_coor[1]+first_node_coor[3])/2)]
                 second_node_coor = draw.coords(selected_object2)
                 second_node_xy = [int((second_node_coor[0]+second_node_coor[2])/2),int((second_node_coor[1]+second_node_coor[3])/2)]
                 link1_id = draw.create_line(first_node_xy[0], first_node_xy[1], second_node_xy[0], second_node_xy[1], fill = "yellow", width=4)
                 m_1=0
                 n_1=0
                 for m in range(0,4):
                     if rect_list_all[m]==selected_object2:
                         m_1=m
                 for n in range (0,8):
                     if oval_list_all[n]==selected_object1:
                         n_1=n
                 H_1[m_1][n_1]=1
                 print(H_1)
                 draw.tag_lower(link1_id)
                 draw.tag_lower(image_id)
                 draw.delete(link_id)
                 create_newlink()
             draw.unbind("<Motion>")
             draw.itemconfig(selected_object1,fill="skyblue")
             draw.itemconfig(selected_object2,fill="skyblue")
        else:
            print ('test')
            draw.delete(link_id)
            draw.itemconfig(selected_object1,fill="skyblue")
            create_newlink()
            draw.unbind("<Motion>")
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

#label=ttk.Label(root, text="Welcome to LDPC game",font = ("courier",37), background='white', relief='')
#label.place(x=120, y=20)
##T = Text(root, height=1, width=15,font = ("courier",40))
##T.place(x=130, y=20)
##T.insert(END, "Welcome to LDPC game")
#-------Ist
##ttk.Style().configure("RB.TButton", background='black')
##ttk_btn = ttk.Button(text="ttk_Sample", style="RB.TButton")
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
#-----2nd
bt_2 = Button(root, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20, command=valid_code)
bt_2.config(state="disable")
image=PhotoImage(file='2_pn.png')
image=image.subsample(5)
bt_2['image']=image
bt_2.image = image
bt_2.place(width=90,height=88,x=170,y=305)
##----------3rd
bt_3 = Button(root, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20, command= hard_decision)
bt_3.config(state="disable")
image=PhotoImage(file='3pn.png')
image=image.subsample(5)
bt_3['image']=image
bt_3.image = image
bt_3.place(width=90,height=88,x=280,y=250)

##----------4th
bt_4 = Button(root, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=girth)
bt_4.config(state="disable")
image=PhotoImage(file='4pn.png')
image=image.subsample(5)
bt_4['image']=image
bt_4.image = image
bt_4.place(width=90,height=88,x=390,y=195)

##---------5th
bt_5 = Button(root, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20, command=gallager)
bt_5.config(state="disable")
image=PhotoImage(file='5pn.png')
image=image.subsample(5)
bt_5['image']=image
bt_5.image = image
bt_5.place(width=90,height=88,x=500,y=140)
##-------------------------quit--
bt_quit = Button(root, compound=TOP,
                fg='#b7f731',
                relief='groove',
                borderwidth=2,
                width=20,command=quit1)
image=PhotoImage(file='quit.png')
image=image.subsample(7)
bt_quit['image']=image
bt_quit.image = image
bt_quit.place(width=70,height=40,x=710,y=420)
####
##x,y=20,20
##draw.create_oval(x-10,y-10,x+10,y+10,fill='skyblue')

##
##def create_link():
##    draw.bind("<Button-1>",lambda e: xy3(e))
##def xy3(event):
##    x,y = event.x, event.y
##    print(x,y)
##link_id = draw.create_line(x, x, x+40, x+40, fill = "gray50", width=2)    
##    print(x,y)
##    oval_list = [item for item in self.draw.find_overlapping\
##                   (event.x-self.NodeRadius, event.y-self.NodeRadius, event.x+self.NodeRadius, event.y+self.NodeRadius) if self.draw.type(item) == "oval"]
##    if len(oval_list)==1:
##         selected_object1 = oval_list[0]
##         self.draw.itemconfig(selected_object1,fill="gold")
##         self.draw.bind("<Button-1>",lambda e : self.endnodelink(e,selected_object1))
##    else:
##         return
##    self.bt_create_node.config(state='disable')
##    self.bt_remove.config(state='disable')
##    self.bt_save_file.config(state='disable')
##    self.bt_load_file.config(state='disable')
##    self.bt_up_file.config(state='disable')
##    self.bt_move_node.config(state='disable')

##label=tkinter.Label(root, textvariable=dong)
##label.place(x=12, y=150)

##    def move_node(self):
##        self.draw.bind("<Button-1>",lambda e: self.xy_movenode(e))
##
##    def xy_movenode(self,e):
##        x,y=e.x,e.y
##        objectID = self.draw.find_overlapping(x-5,y-5,x+5,y+5)
##        nodeID = [item for item in objectID if self.draw.type(item)=='oval']
##        if len(nodeID) > 0:
##            curnode = nodeID[-1]
##            self.draw.itemconfig(curnode,fill = "gray70")
##            nodePo = self.draw.coords(curnode)
##            x = (nodePo[0]+nodePo[2])/2
##            y = (nodePo[1]+nodePo[3])/2
##
##            objectID = self.draw.find_overlapping(x-1,y-1,x+1,y+1)
##            textID = [item for item in objectID if self.draw.type(item) == 'text']
##            self.draw.itemconfig(textID,fill = "gray70")
##
##
##            objectID = self.draw.find_overlapping(nodePo[0],nodePo[1],nodePo[2],nodePo[3])
##            lineID = [item for item in objectID if self.draw.type(item) == 'line']
##            connectedLineID = []
##            for lineid in lineID:
##                linePos = self.draw.coords(lineid)
##                if linePos[0]==x and linePos[1]==y:
##                    connectedLineID.append(lineid)
##                if linePos[2]==x and linePos[3]==y:
##                    connectedLineID.append(lineid)
##            for lineid in connectedLineID:
##                self.draw.itemconfig(lineid,fill='gray70',width=2)
##
##            self.bt_create_node.config(state='disable')
##            self.bt_create_link.config(state='disable')
##            self.bt_up_file.config(state='disable')
##            self.bt_remove.config(state='disable')
##            self.bt_save_file.config(state='disable')
##            self.bt_load_file.config(state='disable')
##
##            self.draw.bind("<Motion>", self.movenodeMotion)
##            self.draw.bind("<Button-1>",self.movenode2)
##
##    def movenodeMotion(self,event):
##        x,y = event.x,event.y #ยังไม่ได้กำหนดขอบการลากเลยทำให้วาดเกินแคนวาสไปได้
##        objectID = self.draw.find_overlapping(0,0,1200,1000)
##        nodeID = [item for item in objectID if self.draw.type(item)=='oval' \
##                  and self.draw.itemcget(item,"fill")=="gray70"]
##        lineID = [item for item in objectID if self.draw.type(item) == 'line' \
##                  and self.draw.itemcget(item,"fill")=="gray70"]
##        textID = [item for item in objectID if self.draw.type(item) == 'text' \
##                  and self.draw.itemcget(item,"fill")=="gray70"]
##
##        if len(nodeID) > 0:
##            curnode = nodeID[-1]
##            nodePo = self.draw.coords(curnode)
##            prevx = (nodePo[0]+nodePo[2])/2
##            prevy = (nodePo[1]+nodePo[3])/2
##            self.draw.coords(curnode,x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius)
##
##        if len(textID) > 0:
##            curtext = textID[-1]
##            self.draw.coords(curtext,x-1,y)
##
##        for lineid in lineID:
##            linePos = self.draw.coords(lineid)
##            if linePos[0]==prevx and linePos[1]==prevy:
##                self.draw.coords(lineid,x,y,linePos[2],linePos[3])
##            if linePos[2]==prevx and linePos[3]==prevy:
##                self.draw.coords(lineid,linePos[0],linePos[1],x,y)
##
##    def movenode2(self,event):
##        x,y = event.x,event.y
##        objectID = self.draw.find_overlapping(0,0,1200,1000)
##        nodeID = [item for item in objectID if self.draw.type(item)=='oval' \
##                  and self.draw.itemcget(item,"fill")=="gray70"]
##        lineID = [item for item in objectID if self.draw.type(item) == 'line' \
##                  and self.draw.itemcget(item,"fill")=="gray70"]
##        textID = [item for item in objectID if self.draw.type(item) == 'text' \
##                  and self.draw.itemcget(item,"fill")=="gray70"]
##
##        if len(nodeID) > 0:
##            curnode = nodeID[-1]
##            nodePo = self.draw.coords(curnode)
##            prevx = (nodePo[0]+nodePo[2])/2
##            prevy = (nodePo[1]+nodePo[3])/2
##
##            self.draw.coords(curnode,x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius)
##            self.draw.itemconfig(curnode,fill='skyblue')
##        else:
##            print('Error: Node missing')
##
##            pause
##
##        if len(textID) > 0:
##            curtext = textID[-1]
##            self.draw.coords(curtext,x-1,y)
##            self.draw.itemconfig(curtext,fill='black')
##
##        for lineid in lineID:
##            linePos = self.draw.coords(lineid)
##            if linePos[0]==prevx and linePos[1]==prevy:
##                self.draw.coords(lineid,x,y,linePos[2],linePos[3])
##                self.draw.itemconfig(lineid,fill = 'gray50')
##                self.draw.tag_lower(lineid)
##
##            if linePos[2]==prevx and linePos[3]==prevy:
##                self.draw.coords(lineid,linePos[0],linePos[1],x,y)
##                self.draw.itemconfig(lineid,fill = 'gray50')
##                self.draw.tag_lower(lineid)
##
##        self.draw.unbind("<Motion>")
##        self.draw.bind("<Button-1>",lambda e: self.xy_movenode(e))
##        self.bt_create_node.config(state='enable')
##        self.bt_create_link.config(state='enable')
##        self.bt_up_file.config(state='enable')
##        self.bt_save_file.config(state='enable')
##        self.bt_load_file.config(state='enable')
##        self.bt_remove.config(state='enable')



#--------------down-----------
##    bt_down = Button(draw, compound=TOP,
##                    fg='#b7f731',
##                    relief='raised',
##                    borderwidth=6,
##                    width=20)
##    image=PhotoImage(file='down.png')
##    image=image.subsample(5)
##    bt_down['image']=image
##    bt_down.image = image
##    bt_down.place(width=50,height=50,x=85,y=220)      
###-----------up button-------
##    bt_up = Button(draw, compound=TOP,
##                    fg='#b7f731',
##                    relief='raised',
##                    borderwidth=6,
##                    width=20)
##    image=PhotoImage(file='up.png')
##    image=image.subsample(5)
##    bt_up['image']=image
##    bt_up.image = image
##    bt_up.place(width=50,height=50,x=85,y=100)
##--------------right----    
