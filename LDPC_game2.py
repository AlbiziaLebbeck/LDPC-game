from tkinter import*
from tkinter import ttk
import datetime as dt
import numpy as np
import time
import os
from collections import defaultdict
#from PIL import ImageTk

H =  np.array([[1,1,0,0,1,1,1,0],
             [0,1,1,1,0,0,0,0],
             [0,0,1,0,1,0,1,1],
             [0,0,0,1,0,1,1,1]])


m_start=0
print(m_start)
itr=0
def hard_decision():
    bt_2.config(state="normal")
    root.withdraw()

    code_recieved= np.array([1,0,1,1,0,1,0,1])
    code_without_error= np.array([0,0,0,0,0,0,0,0])
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


    oval_dict = {}
    rect_dict = {}
    line_dict = {}

   
    
    for n in range(0,8):
        oval_id = draw.create_oval((n+1.5)*80-20,320,(n+1.5)*80+1+20,360,fill='skyblue')
        oval_dict[n] = oval_id
        label=ttk.Label(draw, text=str(code_recieved[n]),font = ("courier ",15))
        label.place(x=(n+1.5)*80+2, y=365)
    for m in range(0,4):
        rect_id = draw.create_rectangle((m+3.5)*80-20,150,(m+3.5)*80+20,190,fill='skyblue')    
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

    
    text_dict = {}
    label_dict_rect={}
    label_dict_oval={}
    text_final_dict = defaultdict(dict)

    
    
    
    for m in range(0,4):
        label=Label(b, text=" ",font = 10)
        label.place(x=(m+3.5)*80-20, y=110)
        label_dict_rect[m]= label    

    for n in range(0,8):
        label=Label(b, text=" ",font = 10)
        label.place(x=(n+1.5)*80+2, y=410)
        label_dict_oval[n]= label  
    
   
    def up():
        global m_start
##        rect_pos= draw.coords(rect_dict[m_start-1])
        label_dict_rect[m_start-1].config(text="")
        for k in text_dict:
            label_dict_rect[m_start-1].config(text= label_dict_rect[m_start-1]["text"]+text_dict[k].get("1.0","end-1c")+" ")
    def down():
        
        global m_start
##        rect_pos= draw.coords(rect_dict[m_start-5])
        label_dict_oval[m_start-5].config(text="")
        for k in text_dict:
            label_dict_oval[m_start-5].config(text= label_dict_oval[m_start-5]["text"]+text_dict[k].get("1.0","end-1c")+" ")
        
    def left():
        global m_start
        global itr
        if itr>0 and m_start==1:
            m_start=13
            for n in range (0,8):
                text_final_dict[itr-1][n].configure(state="normal")
            itr=itr-1
              
        def count():
            global m_start
            m_start=m_start-2
        count()
        start_hard_decision()

       
            
            
        

    def start_hard_decision():
        
        

        global itr
        global m_start
        text_var=0

       
                
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

        
        if m_start<=4:
            if m_start>=1:
                bt_up.config(state="normal")
            bt_down.config(state="disable")
            rect_pos= draw.coords(rect_dict[m_start-1])
           
            for k in text_dict:
                print("hello")
    ##            draw.itemconfig(text_dict[k],state="hidden")
                text_dict[k].destroy()
                
            
            for k in line_dict:
                
                line_pos = draw.coords(line_dict[k])
                print(line_pos)
                if line_pos[2]==int((rect_pos[0]+rect_pos[2])/2) and line_pos[3]== int((rect_pos[1]+rect_pos[3])/2) :
                   draw.itemconfig(line_dict[k],state="normal")
                   draw.itemconfig(line_dict[k],fill="yellow")
    ##               text_id= draw.create_text(int((line_pos[0]+line_pos[2])/2)-1,int((line_pos[1]+line_pos[3])/2)-1,fill="blue",width=45)

                   T = Text(b, height=2, width=2)
                   T.place(x= int((line_pos[0]+line_pos[2])/2)-1,y= int((line_pos[1]+line_pos[3])/2)-1)
                   text_dict[text_var]=T
                   print(text_dict)
                   text_var=text_var+1

##                    bt_next = Button(b, compound=TOP, text="0/1"
##                                fg='#b7f731',
##                                relief='raised',
##                                borderwidth=6,
##                                width=20)
##                    image=PhotoImage(file='next_1.png')
##                    image=image.subsample(5)
##                    bt_next['image']=image
##                    bt_next.image = image
##                    bt_next.place(width=60,height=40,x= int((line_pos[0]+line_pos[2])/2)-1,y= int((line_pos[1]+line_pos[3])/2)-1)
##
##                  
                   
                else:
                    draw.itemconfig(line_dict[k],state="hidden")
        if m_start>4 and m_start <=12:

                bt_down.config(state="normal")
                bt_up.config(state="disable")
                
                oval_pos= draw.coords(oval_dict[m_start-5])
                
                for k in text_dict:
                    print("hello")
        ##            draw.itemconfig(text_dict[k],state="hidden")
                    text_dict[k].destroy()

                for m in range(0,4):
                     if H[m][m_start-5]==1:
                            rect_pos= draw.coords(rect_dict[m])
                            for k in line_dict:
                
                                    line_pos = draw.coords(line_dict[k])
                                    print(line_pos)
                                    if line_pos[2]==int((rect_pos[0]+rect_pos[2])/2) and line_pos[3]== int((rect_pos[1]+rect_pos[3])/2) :
                                        draw.itemconfig(line_dict[k],state="normal")
                                        draw.itemconfig(line_dict[k],fill="sky blue")
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
                       draw.itemconfig(line_dict[k],fill="yellow")
        ##               text_id= draw.create_text(int((line_pos[0]+line_pos[2])/2)-1,int((line_pos[1]+line_pos[3])/2)-1,fill="blue",width=45)

                       T = Text(b, height=2, width=2)
                       T.place(x= int((line_pos[0]+line_pos[2])/2)-1,y= int((line_pos[1]+line_pos[3])/2)-1)
                       text_dict[text_var]=T
                       print(text_dict)
                       text_var=text_var+1
                       
##                    else:
##                        draw.itemconfig(line_dict[k],state="hidden")

                
                if m_start==12:
                      for n in range(0,8):  
                            text=Text(b, height=1,width=1)
                            text.place(x=(n+1.5)*80+2, y= (itr*18)+460)
                            text_final_dict[itr][n]= text
                      if itr==0:
                           bt_right.config(state="disable")

                
        if m_start>12:
                   
                   print("Hello")
                   m_start=0
                   start_hard_decision()

                   
                   for n in range(0,8):
                       text_final_dict[itr][n].configure(state='disabled')
                   itr=itr+1
                   
                   if itr>0:
                       bt_left.config(state="normal")
                   else:
                       bt_left.config(state="disable")
##                   bt_up.config(state="disable")
                   bt_down.config(state="disable")
       
                   
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
#--------------down-----------
    bt_down = Button(draw, compound=TOP,
                    fg='#b7f731',
                    relief='raised',
                    borderwidth=6,
                    width=20,command=down)
    image=PhotoImage(file='down.png')
    image=image.subsample(5)
    bt_down['image']=image
    bt_down.image = image
    bt_down.place(width=50,height=50,x=85,y=220)      
#-----------up button-------
    bt_up = Button(draw, compound=TOP,
                    fg='#b7f731',
                    relief='raised',
                    borderwidth=6,
                    width=20,command=up)
    image=PhotoImage(file='up.png')
    image=image.subsample(5)
    bt_up['image']=image
    bt_up.image = image
    bt_up.place(width=50,height=50,x=85,y=100)
#--------------right----    
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
    bt_up.config(state="disable")
    bt_down.config(state="disable")
    bt_left.config(state="disable")        
#-------------------  quit--                
    def quit2():
        global m_start
        global itr
        m_start=0
        itr=0
        b.destroy()
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
        global itr
        global m_start
        print(text_final_dict)
        m=0
        for k in text_final_dict :
             m=m+1
        
        for n in range (0,8):
            if text_final_dict[m-1][n]['state']=='disabled' :
                    text_final_dict[m-1][n].configure(state='normal')
                    x = int(text_final_dict[m-1][n].get("1.0","end-1c"))
                    submitted_code[n]=x
                    text_final_dict[m-1][n].configure(state='disabled')
            else:
                    x = int(text_final_dict[m-1][n].get("1.0","end-1c"))
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
                b1.destroy()
                b.destroy()
                root.deiconify()
                
            b1.protocol('WM_DELETE_WINDOW', doSomething)
            
            draw = Canvas(b1,height=500, width=800,background='white')
            ####
            photo = PhotoImage(file = './win2.png')
            draw.image = photo
            draw.create_image(200, 150, image=photo, state=NORMAL)
            ####
            draw.place(x=0,y=0)

            
            def nextlevel_1():
                b1.destroy()
                b.destroy()
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
            bt_next.place(width=60,height=40,x=210,y=140)

        else:

            b1 =Toplevel()
            b1.resizable(width=False,height=False)
            height=200
            width=400
            winSize = str(width)+'x'+str(height)
            b1.geometry(winSize)
            draw = Canvas(b1,height=500, width=800,background='white')
            ####
            photo = PhotoImage(file = './lose2.png')
            draw.image = photo
            draw.create_image(200, 150, image=photo, state=NORMAL)
            ####
            draw.place(x=0,y=0)

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
            bt_retry.place(width=60,height=40,x=230,y=120)

            
            
                
        
    bt_submit = Button(draw, compound=TOP,
                fg='#b7f731',
                relief='raised',
                borderwidth=6,
                width=20,command=submit)
    image=PhotoImage(file='submit5.png')
    image=image.subsample(2)
    bt_submit['image']=image
    bt_submit.image = image
    bt_submit.place(width=80,height=75,x=710,y=80)

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

    ##-------------------------quit--
    def quit2():
        b.destroy()
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
        H_1=H
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
            bt_next.place(width=60,height=40,x=240,y=170)
            
            
        else :
            score=0
            for m in range(0,4):
                for n in range(0,8):
                    if H[m][n]==H_1[m][n]:
                        score=score+1
            score_100 = int(score*100/32)
            print(score_100)
            
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
            
            label=ttk.Label(draw, text= str(score_100) , relief='ridge',font=("courier",14))
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
root.title('Low Density Parity Check Code learning tool')
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
                width=20, command=hard_decision)
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
                width=20)
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
                width=20)
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
                width=20)
bt_5.config(state="disable")
image=PhotoImage(file='5pn.png')
image=image.subsample(5)
bt_5['image']=image
bt_5.image = image
bt_5.place(width=90,height=88,x=500,y=140)
##-------------------------quit--
bt_quit = Button(root, compound=TOP,
                fg='#b7f731',
                relief='flat',
                borderwidth=6,
                width=20,command=quit1)
image=PhotoImage(file='quit.png')
image=image.subsample(5)
bt_quit['image']=image
bt_quit.image = image
bt_quit.place(width=50,height=50,x=740,y=440)
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
