from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class guiTopology():
    def __init__(self,onoGUI):
#------ Constants for node radius
        self.NodeRadius = 10
#------ Frame for Status -----------------------------------#     
        style_obj = ttk.Style()
        style_obj.configure('mystyle1.TFrame',background='linen')

        self.frame_status = ttk.Frame(onoGUI.frame_network_topology,
                                      style='mystyle1.TFrame')
        self.frame_status['relief']='flat'
        self.frame_status['borderwidth']=1
        self.frame_status.place(height=30,width=onoGUI.winWidth,x=5,y=2)

#------ Frame for Command Buttons -----------------------------------#
        style_obj.configure('mystyle2.TFrame',background='ivory')
        self.frame_button = ttk.Frame(onoGUI.frame_network_topology,style='mystyle2.TFrame')
        self.frame_button['relief']='groove'
        self.frame_button['borderwidth']=2
        self.frame_button.place(height=600,width=125,x=5,y=32)
#------ Canvas -----------------------------------#        
        self.draw = Canvas(onoGUI.frame_network_topology,height=(0.9*onoGUI.winHeight)-10,
                           width=((7*onoGUI.winWidth)/8)-30, background='wheat')
        self.draw.place(x=132,y=32)
        #------ Command buttons
        self.bt_create_node = ttk.Button(self.frame_button,text='Create Node',
                                         compound=TOP,command=self.create_node)
        image5 = PhotoImage(file='node2.png')
        image5 = image5.subsample(6)
        self.bt_create_node['image'] = image5
        self.bt_create_node.image = image5
        self.bt_create_node.place(width=120,height=75,x=0,y=0)

        self.bt_create_link = ttk.Button(self.frame_button,text='Create Link',
                                         compound=TOP,command = self.create_link,style='P1style.TButton')
        image=PhotoImage(file='link.png')
        image=image.subsample(5)
        self.bt_create_link['image']=image
        self.bt_create_link.image = image
        self.bt_create_link.place(width=120,height=75,x=0,y=77)

        self.bt_move_node = ttk.Button(self.frame_button,text='Move Node/Link',
                                       compound=TOP,command=self.move_node)
        image6=PhotoImage(file='move2.png')
        image6=image6.subsample(5)
        self.bt_move_node['image']=image6
        self.bt_move_node.image = image6
        self.bt_move_node.place(width=120,height=75,x=0,y=154)

        self.bt_remove=ttk.Button(self.frame_button,text='Remove Node/Link',
                                  compound=TOP,command=self.remove_node_link)
        image1=PhotoImage(file='trash.png')
        image1=image1.subsample(12)
        self.bt_remove['image']=image1
        self.bt_remove.image = image1
        self.bt_remove.place(width=120,height=75,x=0,y=231)

        self.bt_up_file=ttk.Button(self.frame_button,text='Update',compound=TOP,
                                   command=self.update_topology,style='P1style.TButton')
        image3=PhotoImage(file='social_graph.png')
        image3=image3.subsample(10)
        self.bt_up_file['image']=image3
        self.bt_up_file.image = image3
        self.bt_up_file.place(width=120,height=75,x=0,y=308)

        #------ Frame for Load & Save Buttons -----------------------------------#
        self.frame_button_saveload = ttk.Labelframe(onoGUI.frame_network_topology,
                                                    text='Save&Load')
        self.frame_button_saveload['relief']='sunken'
        self.frame_button_saveload['borderwidth']=4
        self.frame_button_saveload.place(height=90, width=125,x=5,y=420)


        self.bt_save_file=ttk.Button(self.frame_button_saveload,text='Save',compound=TOP,
                                     command=self.save_topology)
        image3=PhotoImage(file='save4.png')
        image3=image3.subsample(8)
        self.bt_save_file['image']=image3
        self.bt_save_file.image = image3
        self.bt_save_file.place(width=55,height=55,x=2,y=5)


        self.bt_load_file=ttk.Button(self.frame_button_saveload,text='load',compound=TOP,
                                     command= self.load_topology)
        image2=PhotoImage(file='load4.png')
        image2=image2.subsample(8)
        self.bt_load_file['image']=image2
        self.bt_load_file.image = image2
        self.bt_load_file.place(width=55,height=55,x=58,y=5)
        self.load_update()
    #------------------createnode-------------------------------#
    def create_node(self):
        self.draw.bind("<Button-1>",lambda e: self.xy2(e))

    def xy2(self,event):
        x,y = event.x,event.y
        oval_list = [item for item in self.draw.find_overlapping(event.x-self.NodeRadius,event.y-self.NodeRadius,
                    event.x+self.NodeRadius, event.y+self.NodeRadius) if self.draw.type(item) == "oval"]
        line_list = [item for item in self.draw.find_overlapping(event.x-self.NodeRadius,event.y-self.NodeRadius,
                    event.x+self.NodeRadius, event.y+self.NodeRadius) if self.draw.type(item) == "line"]
        if oval_list==[] and line_list==[]:
            self.draw.create_oval(x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius,fill='skyblue')
            print('New node created at',x,y)
        else:
            print('Create Node: please click another place')

    #-----------------------createlink--------------------------#
    def create_link(self):
        self.draw.bind("<Button-1>",lambda e: self.xy3(e))

    def xy3(self,event):
        x,y = event.x, event.y
        oval_list = [item for item in self.draw.find_overlapping\
                       (event.x-self.NodeRadius, event.y-self.NodeRadius, event.x+self.NodeRadius, event.y+self.NodeRadius) if self.draw.type(item) == "oval"]
        if len(oval_list)==1:
             selected_object1 = oval_list[0]
             self.draw.itemconfig(selected_object1,fill="gold")
             self.draw.bind("<Button-1>",lambda e : self.endnodelink(e,selected_object1))
        else:
             return
        self.bt_create_node.config(state='disable')
        self.bt_remove.config(state='disable')
        self.bt_save_file.config(state='disable')
        self.bt_load_file.config(state='disable')
        self.bt_up_file.config(state='disable')
        self.bt_move_node.config(state='disable')

    def endnodelink(self,event,selected_object1):
        x,y = event.x, event.y
        oval_list = [item for item in \
                       self.draw.find_overlapping\
                       (event.x-5, event.y-5, event.x+5, event.y+5) if self.draw.type(item) == "oval"]
        if len(oval_list):
             selected_object2 = oval_list[0]
             if selected_object1!=selected_object2:
                 self.draw.itemconfig(selected_object2,fill="gold")
                 first_node_coor = self.draw.coords(selected_object1)
                 first_node_xy = [int((first_node_coor[0]+first_node_coor[2])/2),int((first_node_coor[1]+first_node_coor[3])/2)]
                 second_node_coor = self.draw.coords(selected_object2)
                 second_node_xy = [int((second_node_coor[0]+second_node_coor[2])/2),int((second_node_coor[1]+second_node_coor[3])/2)]
                 objectID = self.draw.find_overlapping(0,0,1200,1000)
                 All_linkID = [item for item in objectID if self.draw.type(item) == 'line']
                 link_existed = False
                 for lineid in All_linkID:
                     linePos = self.draw.coords(lineid)
                     if first_node_xy[0]==linePos[0] and first_node_xy[1]==linePos[1] and \
                        second_node_xy[0]==linePos[2] and second_node_xy[1]==linePos[3]:
                         link_existed = True
                         break
                     if first_node_xy[0]==linePos[2] and first_node_xy[1]==linePos[3] and \
                        second_node_xy[0]==linePos[0] and second_node_xy[1]==linePos[1]:
                         link_existed = True
                         break
                 if link_existed == False:
                     link_id = self.draw.create_line(first_node_xy[0], first_node_xy[1], second_node_xy[0], second_node_xy[1], fill = "gray50", width=2)

             else:
                 print('Click on the same node')
             self.draw.itemconfig(selected_object1,fill="skyblue")
             self.draw.itemconfig(selected_object2,fill="skyblue")
        else:
            self.draw.itemconfig(selected_object1,fill="skyblue")

        self.draw.bind("<Button-1>",lambda e: self.xy3(e))
        self.bt_create_node.config(state='normal')
        self.bt_remove.config(state='normal')
        self.bt_save_file.config(state='normal')
        self.bt_load_file.config(state='normal')
        self.bt_move_node.config(state='normal')
        self.bt_up_file.config(state='normal')
    #------- Move node
    def move_node(self):
        self.draw.bind("<Button-1>",lambda e: self.xy_movenode(e))

    def xy_movenode(self,e):
        x,y=e.x,e.y
        objectID = self.draw.find_overlapping(x-5,y-5,x+5,y+5)
        nodeID = [item for item in objectID if self.draw.type(item)=='oval']
        if len(nodeID) > 0:
            curnode = nodeID[-1]
            self.draw.itemconfig(curnode,fill = "gray70")
            nodePo = self.draw.coords(curnode)
            x = (nodePo[0]+nodePo[2])/2
            y = (nodePo[1]+nodePo[3])/2

            objectID = self.draw.find_overlapping(x-1,y-1,x+1,y+1)
            textID = [item for item in objectID if self.draw.type(item) == 'text']
            self.draw.itemconfig(textID,fill = "gray70")


            objectID = self.draw.find_overlapping(nodePo[0],nodePo[1],nodePo[2],nodePo[3])
            lineID = [item for item in objectID if self.draw.type(item) == 'line']
            connectedLineID = []
            for lineid in lineID:
                linePos = self.draw.coords(lineid)
                if linePos[0]==x and linePos[1]==y:
                    connectedLineID.append(lineid)
                if linePos[2]==x and linePos[3]==y:
                    connectedLineID.append(lineid)
            for lineid in connectedLineID:
                self.draw.itemconfig(lineid,fill='gray70',width=2)

            self.bt_create_node.config(state='disable')
            self.bt_create_link.config(state='disable')
            self.bt_up_file.config(state='disable')
            self.bt_remove.config(state='disable')
            self.bt_save_file.config(state='disable')
            self.bt_load_file.config(state='disable')

            self.draw.bind("<Motion>", self.movenodeMotion)
            self.draw.bind("<Button-1>",self.movenode2)

    def movenodeMotion(self,event):
        x,y = event.x,event.y #ยังไม่ได้กำหนดขอบการลากเลยทำให้วาดเกินแคนวาสไปได้
        objectID = self.draw.find_overlapping(0,0,1200,1000)
        nodeID = [item for item in objectID if self.draw.type(item)=='oval' \
                  and self.draw.itemcget(item,"fill")=="gray70"]
        lineID = [item for item in objectID if self.draw.type(item) == 'line' \
                  and self.draw.itemcget(item,"fill")=="gray70"]
        textID = [item for item in objectID if self.draw.type(item) == 'text' \
                  and self.draw.itemcget(item,"fill")=="gray70"]

        if len(nodeID) > 0:
            curnode = nodeID[-1]
            nodePo = self.draw.coords(curnode)
            prevx = (nodePo[0]+nodePo[2])/2
            prevy = (nodePo[1]+nodePo[3])/2
            self.draw.coords(curnode,x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius)

        if len(textID) > 0:
            curtext = textID[-1]
            self.draw.coords(curtext,x-1,y)

        for lineid in lineID:
            linePos = self.draw.coords(lineid)
            if linePos[0]==prevx and linePos[1]==prevy:
                self.draw.coords(lineid,x,y,linePos[2],linePos[3])
            if linePos[2]==prevx and linePos[3]==prevy:
                self.draw.coords(lineid,linePos[0],linePos[1],x,y)

    def movenode2(self,event):
        x,y = event.x,event.y
        objectID = self.draw.find_overlapping(0,0,1200,1000)
        nodeID = [item for item in objectID if self.draw.type(item)=='oval' \
                  and self.draw.itemcget(item,"fill")=="gray70"]
        lineID = [item for item in objectID if self.draw.type(item) == 'line' \
                  and self.draw.itemcget(item,"fill")=="gray70"]
        textID = [item for item in objectID if self.draw.type(item) == 'text' \
                  and self.draw.itemcget(item,"fill")=="gray70"]

        if len(nodeID) > 0:
            curnode = nodeID[-1]
            nodePo = self.draw.coords(curnode)
            prevx = (nodePo[0]+nodePo[2])/2
            prevy = (nodePo[1]+nodePo[3])/2

            self.draw.coords(curnode,x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius)
            self.draw.itemconfig(curnode,fill='skyblue')
        else:
            print('Error: Node missing')

            pause

        if len(textID) > 0:
            curtext = textID[-1]
            self.draw.coords(curtext,x-1,y)
            self.draw.itemconfig(curtext,fill='black')

        for lineid in lineID:
            linePos = self.draw.coords(lineid)
            if linePos[0]==prevx and linePos[1]==prevy:
                self.draw.coords(lineid,x,y,linePos[2],linePos[3])
                self.draw.itemconfig(lineid,fill = 'gray50')
                self.draw.tag_lower(lineid)

            if linePos[2]==prevx and linePos[3]==prevy:
                self.draw.coords(lineid,linePos[0],linePos[1],x,y)
                self.draw.itemconfig(lineid,fill = 'gray50')
                self.draw.tag_lower(lineid)

        self.draw.unbind("<Motion>")
        self.draw.bind("<Button-1>",lambda e: self.xy_movenode(e))
        self.bt_create_node.config(state='enable')
        self.bt_create_link.config(state='enable')
        self.bt_up_file.config(state='enable')
        self.bt_save_file.config(state='enable')
        self.bt_load_file.config(state='enable')
        self.bt_remove.config(state='enable')
    #----------remove------------------#
    def remove_node_link(self):
        self.draw.bind("<Button-1>",self.xy_remove)

    def xy_remove(self,e):
        x,y=e.x,e.y
        objectID = self.draw.find_overlapping(x-5,y-5,x+5,y+5)
        nodeID = [item for item in objectID if self.draw.type(item)=='oval']
        lineID = [item for item in objectID if self.draw.type(item) == 'line']
        if len(lineID) > 0:
            curline = lineID[-1]
            self.draw.delete(curline)

        if len(nodeID) > 0  :
            curnode = nodeID[-1]
            curnodePo = self.draw.coords(curnode)
            x = (curnodePo[0]+curnodePo[2])/2
            y = (curnodePo[1]+curnodePo[3])/2
            objectID = self.draw.find_overlapping(x-1,y-1,x+1,y+1)
            textID = [item for item in objectID if self.draw.type(item) == 'text']
    # delete links adjacent to node
            objectID = self.draw.find_overlapping(0,0,1200,1000)
            lineID = [item for item in objectID if self.draw.type(item) == 'line']
            for lineid in lineID:
                linePos = self.draw.coords(lineid)
                if linePos[0]==x and linePos[1]==y:
                    self.draw.delete(lineid)
                if linePos[2]==x and linePos[3]==y:
                    self.draw.delete(lineid)

            if len(textID)>0:
                curtext = textID[-1]
                self.draw.delete(curtext)
            self.draw.delete(curnode)
    #----------------save/load topology----------------------------#
    def update_topology(self):
        f = open('node_location.txt', 'w')
        objectID = self.draw.find_overlapping(0,0,1200,1000)
        nodeID = [item for item in objectID if self.draw.type(item) == 'oval']
        #print(nodeID)
        node = 1;
        nodeList = {};

        for n in nodeID:
            NodePosition = self.draw.coords(n)
            NodePosX = (NodePosition[0]+NodePosition[2])/2
            NodePosY = (NodePosition[1]+NodePosition[3])/2
            nodeList[node] = [NodePosX,NodePosY]
            node += 1;
        #print(nodeList)

        for m in range(1,len(nodeList)):
            for n in range(1,len(nodeList)):
                if nodeList[n][1] > nodeList[n+1][1]:
                    nodeList[n],nodeList[n+1] = nodeList[n+1],nodeList[n];
        print(nodeList)

        for n in range(1,len(nodeList)+1):
            f.write('{}\t{}\t{}\n'.format(n,nodeList[n][0],nodeList[n][1]))
        f.close()

        objectID = self.draw.find_overlapping(0,0,1200,1000)
        linkID = [item for item in objectID if self.draw.type(item) == 'line']
        nodeID = [item for item in objectID if self.draw.type(item) == 'oval']
        Nolink = 1;
        AdjacencyMatrix = {};
        AdjacencyMatrix = AdjacencyMatrix.fromkeys(nodeList.keys(),[])

        for link in linkID:
            linePos = self.draw.coords(link)
            TwoEndNodePos = [i for i in linePos] #[x1,y1,x2,y2]
            n1 = 0
            n2 = 0
            for k,v in nodeList.items():
                #print(v[0],TwoEndNodePos[0],TwoEndNodePos[2])
                if v[0] == TwoEndNodePos[0] and v[1] == TwoEndNodePos[1]:
                    n1 = k
                    #print(n1)
                if v[0] == TwoEndNodePos[2] and v[1] == TwoEndNodePos[3]:
                    n2 = k
                    #print(n2)
            if n1 != 0 and n2 != 0:
                A = AdjacencyMatrix[n1]
                A = A + [n2]
                AdjacencyMatrix[n1] = A
                A = AdjacencyMatrix[n2]
                A = A + [n1]
                AdjacencyMatrix[n2] = A
            else:
                print('error1')
                break
        print(AdjacencyMatrix)
        f = open('adjacency_matrix.txt', 'w')
        for node, adjNodes in AdjacencyMatrix.items():
            f.write('{}\t'.format(node))
            for node in adjNodes:
                f.write('{}\t'.format(node))
            f.write('\n')
        f.close()

        f = open('topology.txt', 'w')
        number_of_nodes = len(nodeList)

        for n1 in range(1,number_of_nodes+1):
            adjNodes = AdjacencyMatrix[n1]
            #print(n1,adjNodes)
            for n2 in range(1,number_of_nodes+1):
                if n2 in adjNodes:
                    f.write('1')
                elif n1==n2:
                    f.write('2')
                else:
                    f.write('0')
                if n2==number_of_nodes:
                    f.write('\n')
                else:
                    f.write('\t')
        f.close()
        self.load_update()

    def load_update(self):
        self.draw.delete('all')
        f = open('node_location.txt', 'r')
        nodePosList = {};
        n = 1
        for text in f.readlines():
            myNodeInfo = text.strip().split('\t')
            nodeid = int(myNodeInfo[0])
            x = float(myNodeInfo[1])
            y = float(myNodeInfo[2])
            nodePosList[n] = [int(x), int(y)]
            n = n + 1
            self.draw.create_oval(x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius,fill='skyblue')
            self.draw.create_text(x-1,y,text=str(nodeid))

        print(nodePosList)
        f = open('adjacency_matrix.txt', 'r')
        for text in f.readlines():
            node_adjNodes = text.strip().split('\t')
            #print('node_adjNodes',node_adjNodes)
            n1 = int(node_adjNodes[0])
            for node in node_adjNodes[1:]:
                n2 = int(node)
                #print(n2)
                if n1 < n2:
                    pos_n1 = nodePosList[n1]
                    pos_n2 = nodePosList[n2]
                    lineID = self.draw.create_line(pos_n1[0],pos_n1[1],pos_n2[0],pos_n2[1],fill='gray50', width = 2)
                    self.draw.tag_lower(lineID)

    #----------------save/load topology in directory----------------------------#
    def save_topology(self):
        name= asksaveasfilename(filetypes =(("Text File", "*.txt"),("All Files","*.*")))
        #print('name',type(name))
        f = open(name+'.nodelocation.txt', 'w')
        objectID = self.draw.find_overlapping(0,0,1200,1000)
        nodeID = [item for item in objectID if self.draw.type(item) == 'oval']
        #print(nodeID)
        node = 1;
        nodeList = {};

        for n in nodeID:
            NodePosition = self.draw.coords(n)
            NodePosX = (NodePosition[0]+NodePosition[2])/2
            NodePosY = (NodePosition[1]+NodePosition[3])/2
            nodeList[node] = [NodePosX,NodePosY]
            node += 1;
        print(nodeList)

        for m in range(1,len(nodeList)):
            for n in range(1,len(nodeList)):
                if nodeList[n][1] > nodeList[n+1][1]:
                    nodeList[n],nodeList[n+1] = nodeList[n+1],nodeList[n];
        #print(nodeList)

        for n in range(1,len(nodeList)+1):
            f.write('{}\t{}\t{}\n'.format(n,nodeList[n][0],nodeList[n][1]))
        f.close()

        objectID = self.draw.find_overlapping(0,0,1200,1000)
        linkID = [item for item in objectID if self.draw.type(item) == 'line']
        nodeID = [item for item in objectID if self.draw.type(item) == 'oval']
        Nolink = 1;
        AdjacencyMatrix = {};
        AdjacencyMatrix = AdjacencyMatrix.fromkeys(nodeList.keys(),[])

        for link in linkID:
            linePos = self.draw.coords(link)
            TwoEndNodePos = [i for i in linePos] #[x1,y1,x2,y2]
            n1 = 0
            n2 = 0
            for k,v in nodeList.items():
                #print(v[0],TwoEndNodePos[0],TwoEndNodePos[2])
                if v[0] == TwoEndNodePos[0] and v[1] == TwoEndNodePos[1]:
                    n1 = k
                    #print(n1)
                if v[0] == TwoEndNodePos[2] and v[1] == TwoEndNodePos[3]:
                    n2 = k
                    #print(n2)
            if n1 != 0 and n2 != 0:
                A = AdjacencyMatrix[n1]
                A = A + [n2]
                AdjacencyMatrix[n1] = A
                A = AdjacencyMatrix[n2]
                A = A + [n1]
                AdjacencyMatrix[n2] = A
            else:
                print('error1')
                break
        print(AdjacencyMatrix)
        f = open(name+'.adjacency_matrix.txt', 'w')
        for node, adjNodes in AdjacencyMatrix.items():
            f.write('{}\t'.format(node))
            for node in adjNodes:
                f.write('{}\t'.format(node))
            f.write('\n')
        f.close()

        f = open(name+'.topology.txt', 'w')
        number_of_nodes = len(nodeList)

        for n1 in range(1,number_of_nodes+1):
            adjNodes = AdjacencyMatrix[n1]
            #print(n1,adjNodes)
            for n2 in range(1,number_of_nodes+1):
                if n2 in adjNodes:
                    f.write('1')
                elif n1==n2:
                    f.write('2')
                else:
                    f.write('0')
                if n2==number_of_nodes:
                    f.write('\n')
                else:
                    f.write('\t')
        f.close()
        self.update_topology()

    def load_topology(self):
        self.draw.delete('all')
        name = filedialog.askopenfilename(title='Please choose file ',filetypes =(("Text File", "*.txt"),("All Files","*.*")))
        if '.txt' not in name:
            return
        a=[]
        b=[]
        index=0
        while index < len(name):
                index = name.find('.', index)
                if index == -1:
                    break

                #print('. found at', index)
                b.append(index)
                index += 1


        print(name[0:b[-2]])


        if 'nodelocation' in name:
    ##        print('nantanach')
            f = open(name, 'r')
            nodePosList = {};
            n = 1
            for text in f.readlines():
                myNodeInfo = text.strip().split('\t')
                nodeid = int(myNodeInfo[0])
                x = float(myNodeInfo[1])
                y = float(myNodeInfo[2])
                nodePosList[n] = [int(x), int(y)]
                n = n + 1
                self.draw.create_oval(x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius,fill='skyblue')
                self.draw.create_text(x-1,y,text=str(nodeid))
        ##    load_topology2(nodePosList)
            print(nodePosList)
            f = open(name[0:b[-2]]+'.adjacency_matrix.txt', 'r')
            for text in f.readlines():
                node_adjNodes = text.strip().split('\t')
                print('node_adjNodes',node_adjNodes)
                n1 = int(node_adjNodes[0])
                for node in node_adjNodes[1:]:
                    n2 = int(node)
                    #print(n2)
                    if n1 < n2:
                        pos_n1 = nodePosList[n1]
                        pos_n2 = nodePosList[n2]
                        lineID = self.draw.create_line(pos_n1[0],pos_n1[1],pos_n2[0],pos_n2[1],fill='gray50', width = 2)
                        self.draw.tag_lower(lineID)
        elif 'adjacency_matrix' in name:
            f = open(name[0:b[-2]]+'.nodelocation.txt', 'r')
            nodePosList = {};
            n = 1
            for text in f.readlines():
                myNodeInfo = text.strip().split('\t')
                nodeid = int(myNodeInfo[0])
                x = float(myNodeInfo[1])
                y = float(myNodeInfo[2])
                nodePosList[n] = [int(x), int(y)]
                n = n + 1
                self.draw.create_oval(x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius,fill='skyblue')
                self.draw.create_text(x-1,y,text=str(nodeid))
            f = open(name, 'r')
            for text in f.readlines():
                node_adjNodes = text.strip().split('\t')
                print('node_adjNodes',node_adjNodes)
                n1 = int(node_adjNodes[0])
                for node in node_adjNodes[1:]:
                    n2 = int(node)
                    #print(n2)
                    if n1 < n2:
                        pos_n1 = nodePosList[n1]
                        pos_n2 = nodePosList[n2]
                        lineID = self.draw.create_line(pos_n1[0],pos_n1[1],pos_n2[0],pos_n2[1],fill='gray50', width = 2)
                        self.draw.tag_lower(lineID)

        elif 'topology' in name:
            f = open(name[0:b[-2]]+'.nodelocation.txt', 'r')
            nodePosList = {};
            n = 1
            for text in f.readlines():
                myNodeInfo = text.strip().split('\t')
                nodeid = int(myNodeInfo[0])
                x = float(myNodeInfo[1])
                y = float(myNodeInfo[2])
                nodePosList[n] = [int(x), int(y)]
                n = n + 1
                self.draw.create_oval(x-self.NodeRadius,y-self.NodeRadius,x+self.NodeRadius,y+self.NodeRadius,fill='skyblue')
                self.draw.create_text(x-1,y,text=str(nodeid))
            f = open(name[0:b[-2]]+'.adjacency_matrix.txt', 'r')
            for text in f.readlines():
                node_adjNodes = text.strip().split('\t')
                print('node_adjNodes',node_adjNodes)
                n1 = int(node_adjNodes[0])
                for node in node_adjNodes[1:]:
                    n2 = int(node)
                    #print(n2)
                    if n1 < n2:
                        pos_n1 = nodePosList[n1]
                        pos_n2 = nodePosList[n2]
                        lineID = self.draw.create_line(pos_n1[0],pos_n1[1],pos_n2[0],pos_n2[1],fill='gray50', width = 2)
                        self.draw.tag_lower(lineID)

        self.update_topology()
        return
        

