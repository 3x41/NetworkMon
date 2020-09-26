from tkinter import *

#from tkinter import messagebox
#messagebox.showinfo("Title", "a Tk MessageBox")

import os
#import socket
#import timeit
import time
import threading
#import datetime

#My custom py files imported

#import LogFileView
import Add_Title
from About import About_Window #New class method, working 
global LabelCounter


#Varible configuration (work in progress)
LabelArrayMax = 1000
LabelWidth = 50
WindowSizeHeight = "500"
WindowSizeWidth = "600" #if this increases then the LabelWidth also needs to increase





w = [None] * LabelArrayMax #1000 #size of array, max of labels.
firstrun = True

AutoRefresh = False
View_Results = 0 # 0=All, 1=Failed Only, 2=Passed Only
LabelCounter = 0

#Stats of Results
Status_Total = 0
Status_Failed = 0
Status_Passed = 0

#Set window up for the program
Window = Tk()
Window.title("Network Monitor GUI (Alpha)")
Window.geometry(WindowSizeWidth+"x"+WindowSizeHeight)
Window.iconbitmap("../Images/network.ico")
Window.resizable(0,1) #Remove Maximize button, only allow y resize


    
def AddSubBlank(Title):
    global LabelCounter
    LabelCounter = LabelCounter + 1
    global w
    w[LabelCounter] = Label(frame, text=Title, bg="#EEEEEE", fg="white", anchor=W, font="-size 2", width=LabelWidth)
    w[LabelCounter].pack(fill=X)

def AddSubCatWindow(Title):
    global LabelCounter
    LabelCounter = LabelCounter + 1
    global w
    w[LabelCounter] = Label(frame, text=Title, bg="black", fg="white", anchor=W, font="-size 15", width=LabelWidth)
    w[LabelCounter].pack(fill=X)

def AddPortScan(ip,port):
    global LabelCounter, Status_Total, Status_Failed, Status_Passed
    global w
    LabelCounter = LabelCounter + 1
    Status_Total = Status_Total + 1
    if "Closed" not in port:
        if View_Results == 0 or View_Results == 2:
            w[LabelCounter] = Label(frame, text="‼  " + ip + " " + port + " ", bg="green", fg="black")
            w[LabelCounter].pack(fill=X)
            Status_Passed = Status_Passed + 1
    else:
        if View_Results == 0 or View_Results == 1:
            w[LabelCounter] = Label(frame, text="‼  " + ip + " " + port + " ", bg="red", fg="white")
            w[LabelCounter].pack(fill=X)
            Status_Failed = Status_Failed + 1

def AddToWindow(ipaddr,ipstats):
    global LabelCounter, Status_Total, Status_Failed, Status_Passed
    global w
    LabelCounter = LabelCounter + 1
    Status_Total = Status_Total + 1
    if "DOWN" not in ipstats:
        if View_Results == 0 or View_Results == 2:
            w[LabelCounter] = Label(frame, text="√  " + ipaddr + "", bg="green", fg="black")
            w[LabelCounter].pack(fill=X)
            Status_Passed = Status_Passed + 1
    else:
        if View_Results == 0 or View_Results == 1:
            w[LabelCounter] = Label(frame, text="‼  " + ipaddr + "", bg="red", fg="white")
            w[LabelCounter].pack(fill=X)
            Status_Failed = Status_Failed + 1

def ThreadRefresh():
    global AutoRefresh
    while AutoRefresh == True:
        time.sleep(60)              #Thread Sleep, may need adjusting if many file entries.
        print("Thread Ran")
        if AutoRefresh == True:
            if os.path.exists("../Config/Lock.File"):
                #Can not refresh as the file is being updated.
                print("Lock Found")
            else:
                ClearLabels()
                ReadConfigFile()
    print("Thread Stopped")

def BeginThread(event=None):
    print("Thread Start...")
    global AutoRefresh
    if AutoRefresh == False:
        #W_Button_1['relief']=SUNKEN
        #W_Button_1['text'] = " Auto Refresh (ON) "
        #global AutoRefresh
        AutoRefresh = True

        threading.Thread(target=ThreadRefresh).start()
        #ReadConfigFile()
    else:
        #W_Button_1['relief'] = RAISED
        #W_Button_1['text'] = " Auto Refresh (OFF) "
        #global AutoRefresh
        AutoRefresh = False

def ClearLabels():
    global Status_Failed, Status_Passed, Status_Total
    Status_Total = 0
    Status_Failed = 0
    Status_Passed = 0
    global LabelCounter
    Total = LabelCounter +1
    for num in range(1,Total):
        w[num].destroy()
        #global LabelCounter
        LabelCounter = 0

#new button bar under menu..
#W_Button_1 = Button(Window,text=" Auto Refresh (OFF) ", command=BeginThread)
#W_Button_1.pack()

lbl_Status = Label(Window, text="---", font="-size 15", bg="#FB9214")
lbl_Status.pack(pady=10)



def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

canvas = Canvas(Window,borderwidth=5, background="#EEEEEE")
canvas.pack(side="left", fill="both", expand=True)
scrollbar = Scrollbar(Window, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill='y')
canvas.configure(yscrollcommand = scrollbar.set)
# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = Frame(canvas, background="#EEEEEE")
canvas.create_window((10,10), window=frame, anchor='nw')

def mouse_wheel(event):
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        #print("Mouse Wheel Down")
        canvas.yview_moveto( 1 )
    if event.num == 4 or event.delta == 120:
        #print("Mouse Wheel Up")
        canvas.yview_moveto( 0 )
    
def ReadConfigFile():
    filepath = '../Logs/Results.txt'
    #global LabelArrayMax
    with open(filepath) as fp:
        line = fp.readline()
        #cnt = 1
        while line:
            if LabelCounter == LabelArrayMax-1:
                print("MAX ARRAY !!")
            else:
                if line[:1] == ":":
                #Header
                    line = line.replace("\n", "")
                    AddSubBlank("")
                    AddSubCatWindow(line[1:])
                elif line[:1] == ">":
                    #Port
                    line = line.replace(">", "")
                    line = line.replace("\n", "")
                    ip,port = line.split(",")
                    AddPortScan(ip,port)
                elif line == "\n":
                    print("")
                    #print("nothing in line")
                elif line[:1] == "@":
                    line = line.replace("@", "")
                    line = line.replace("\n", "")
                    ipaddr,ipstats = line.split(",")
                    AddToWindow(ipaddr,ipstats)
                else:
                    print ("---")

            line = fp.readline()
    #print(LabelCounter)
    lbl_Status['text'] = "\t" + str(Status_Total) + "  Total\t\t" + str(Status_Failed) + "  Failed\t\t" + str(Status_Passed) + "  Passed\t"



ReadConfigFile()

def ShowLogWindow():
    print("LogFile Click")
    #import LogFileView
    os.system("python LogFileView.py")
    #LogFileView.CreateLogFileWindow()

def AddTitle():
    Title_Window = Add_Title.Add_Title_Main_WindowFun()
    ClearLabels()
    ReadConfigFile()

def AddPing():
    Add_Title.Add_Ping_Main_Window()
    ClearLabels()
    ReadConfigFile()

def AddPort():
    Add_Title.Add_Port_Main_Window()
    ClearLabels()
    ReadConfigFile()

def AboutWindow():
    About_Window()

def EditConfig():
    os.system("start notepad.exe ../Config/config.txt")
    #windows only at the mo.

def View_All():
    global View_Results
    View_Results = 0
    ClearLabels()
    ReadConfigFile()

def View_Failed():
    global View_Results
    View_Results = 1
    ClearLabels()
    ReadConfigFile()

def View_Passed():
    global View_Results
    View_Results = 2
    ClearLabels()
    ReadConfigFile()

def View_Auto():
    BeginThread()
    
    #global AutoRefresh
    #if AutoRefresh == False:
    #    AutoRefresh = True
    #else:
    #    AutoRefresh = False
    #print (AutoRefresh) # For Debugging only..       
        
menu = Menu(Window)
Window.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Program", menu=filemenu)
#filemenu.add_command(label="Settings / Options", command=test)
#filemenu.add_command(label="Configuration", command=test)
#filemenu.add_separator()
filemenu.add_command(label="About...", command=AboutWindow)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Window.destroy)

logmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Logs", menu=logmenu)
logmenu.add_command(label="Show Log File", command=ShowLogWindow)

Checksmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Configuration", menu=Checksmenu)
Checksmenu.add_command(label="Add Header", command=AddTitle)
#Checksmenu.add_command(label="Add Ping Check", command=AddPing)
#Checksmenu.add_command(label="Add Port Check", command=AddPort)
Checksmenu.add_separator()
Checksmenu.add_command(label="Manual Edit Config", command=EditConfig)

viewmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Show All", command=View_All)
viewmenu.add_command(label="Show Only Failed (Red)", command=View_Failed)
viewmenu.add_command(label="Show Only Passed (Green)", command=View_Passed)
viewmenu.add_separator()
viewmenu.add_checkbutton(label="Auto Refresh", command=View_Auto) #Default is OFF (FALSE)

Refreshmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Refresh", command=View_All)
#menu.add_cascade(label="Refresh", menu=ReFreshmenu)
#Refreshmenu.add_command(label="Show All", command=View_All)

# with Windows OS
Window.bind("<MouseWheel>", mouse_wheel)
# with Linux OS
#root.bind("<Button-4>", mouse_wheel)
#root.bind("<Button-5>", mouse_wheel)


# Main window loop
Window.mainloop()

