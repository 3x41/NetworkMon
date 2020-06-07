from tkinter import *

from tkinter import messagebox

import os
import socket
import timeit
import time
#import thread
import threading
import datetime

#My custom py files imported

import LogFileView
import Add_Title
import About
global LabelCounter


#Varible configuration (work in progress)
LabelArrayMax = 1000
LabelWidth = 50
WindowSizeHeight = "500"
WindowSizeWidth = "600" #if this increases then the LabelWidth also needs to increase




w = [None] * LabelArrayMax #1000 #size of array, max of labels.
firstrun = True

AutoRefresh = False

LabelCounter = 0

#Set window up for the program
Window = Tk()
Window.title("Network Monitor (Alpha)")
Window.geometry(WindowSizeWidth+"x"+WindowSizeHeight)
Window.iconbitmap("../Images/network.ico")
#Window.iconbitmap("Network-Broadcasting-icon.png")


#w, h = 600,300  #root.winfo_screenwidth()/2, root.winfo_screenheight()/2
#Window.geometry("%dx%d+150+150" % (w,h))

Window.resizable(0,1) #Remove Maximize button, only allow y resize


 
# Gets both half the screen width/height and window width/height
#positionRight = int(Window.winfo_screenwidth()/2 - windowWidth/2)
#positionDown = 0 #int(Window.winfo_screenheight()/2 - windowHeight/2)

def WriteLogFile(Entry):
    # Open a file
    fo = open("../Logs/LogFile.txt", "a")
    fo.write(Entry + "\n");

    # Close opend file
    fo.close()

def AddSubBlank(Title):
    global LabelCounter
    LabelCounter = LabelCounter + 1
    global w
    w[LabelCounter] = Label(frame, text=Title, bg="white", fg="white", anchor=W, font="-size 15", width=LabelWidth)
    w[LabelCounter].pack(fill=X)


def AddSubCatWindow(Title):
    global LabelCounter
    LabelCounter = LabelCounter + 1
    global w
    w[LabelCounter] = Label(frame, text=Title, bg="black", fg="white", anchor=W, font="-size 15", width=LabelWidth)
    w[LabelCounter].pack(fill=X)
    #w[LabelCounter].bind("<Button-1>", exitapp)


def AddPortScan(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pp = int(port)
    result = sock.connect_ex((ip,pp))
    global LabelCounter
    global w
    LabelCounter = LabelCounter + 1
    if result == 0:
        #global w
        w[LabelCounter] = Label(frame, text=ip + " Port " + port + " is Open", bg="green", fg="black")
        w[LabelCounter].pack(fill=X)
        #w.config(bg="blue")
        #w.destroy()

    else:
        #global w
        w[LabelCounter] = Label(frame, text=ip + " Port " + port + " is Closed", bg="red", fg="white")
        w[LabelCounter].pack(fill=X)
        CurrentDateTime = str(datetime.datetime.now())
        WriteLogFile(CurrentDateTime + " ~ Closed Port Detected ~ " + ip + " Port " + port + " ")


def AddToWindow(hostname):
    response = os.system("ping -n 1 " + hostname)  # Windows Only command
    #response = os.system("ping -c 1 " + hostname)  # Unix/Linux Only command

    # ggg = ping("aht.org.uk")
    global LabelCounter
    global w
    LabelCounter = LabelCounter + 1
    if response == 0:
        #global w
        w[LabelCounter] = Label(frame, text=hostname + " is Up", bg="green", fg="black")
        w[LabelCounter].pack(fill=X)
        #w.config(bg="blue")
        #w.destroy()

    else:
        #global w
        w[LabelCounter] = Label(frame, text=hostname + " is Down", bg="red", fg="white")
        w[LabelCounter].pack(fill=X)
        CurrentDateTime = str(datetime.datetime.now())
        WriteLogFile(CurrentDateTime + " ~ No Ping Detected ~ " + hostname + " ")




def ThreadRefresh():
    global AutoRefresh
    while AutoRefresh == True:
        time.sleep(60)              #Thread Sleep, may need adjusting if many file entries.
        print("Thread Ran")
        if AutoRefresh == True:
            ClearLabels()
            ReadConfigFile()
    print("Thread Stopped")







def BeginThread(event=None):
    print("Exit..")
    global AutoRefresh
    if AutoRefresh == False:
        W_Button_1['relief']=SUNKEN
        W_Button_1['text'] = " Auto Refresh (ON) "
        #global AutoRefresh
        AutoRefresh = True

        threading.Thread(target=ThreadRefresh).start()
        #ReadConfigFile()
    else:
        W_Button_1['relief'] = RAISED
        W_Button_1['text'] = " Auto Refresh (OFF) "
        #global AutoRefresh
        AutoRefresh = False

    #w.pack_forget()
    #Window.destroy()

    #time.sleep(5)

    #AddPingCheck()

def ClearLabels():
    global LabelCounter
    Total = LabelCounter +1
    for num in range(1,Total):
        w[num].destroy()
        #global LabelCounter
        LabelCounter = 0
        #w[num].pack_forget()



#Setup the parts for the window
#hwtext = Label(Window, text="Hello and welcome to the program..")
#hwtext.pack()


W_Button_1 = Button(Window,text=" Auto Refresh (OFF) ", command=BeginThread)
W_Button_1.pack(fill=X)




def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


canvas = Canvas(Window,borderwidth=5, background="#fffff0")
#canvas.pack(side=LEFT, fill='y')
canvas.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(Window, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = Frame(canvas, background="#889988")
canvas.create_window((10,10), window=frame, anchor='nw')

def ReadConfigFile():
    filepath = '../Config/config.txt'
    #global LabelArrayMax
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if LabelCounter == LabelArrayMax-1:
                print("MAX ARRAY !!")
            else:
                if line[:1] == ":":
                #Header
                    #line = fp.readline()
                    print ("HEADER")
                    line = line.replace("\n", "")
                    AddSubBlank("")
                    AddSubCatWindow(line[1:])
                elif line[:1] == ">":
                    line = line.replace(">", "")
                    line = line.replace("\n", "")
                    print("Port Scan entry Found > ", line)
                    ip,port = line.split(":")
                    print (ip)
                    AddPortScan(ip,port)

                elif line == "\n":
                    print("nothing in line")
                elif line[:1] == "@":
                    line = line.replace("@", "")
                    line = line.replace("\n", "")
                    AddToWindow(line)
                else:
                    print ("---")
                    #line = line.replace("\n", "")
                    #AddToWindow(line)


            ##print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            ##cnt += 1
    print(LabelCounter)


#def AddPingCheck():
#    AddSubCatWindow("Switches")
#    AddToWindow("191.9.200.35")
#    AddToWindow("aht.org.uk")
#    AddToWindow("127.0.0.1")
#    AddToWindow("127.0.0.1")
#    AddToWindow("127.0.0.1")
#    AddToWindow("127.0.0.1")
#    AddToWindow("127.0.0.1") #30
#    print(LabelCounter)
#    global firstrun#
#
#    if firstrun == False:
#        time.sleep(10)
#        print ("go..")
#        exitapp()
#    else:
# firstrun = True

#def PortScan():
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    result = sock.connect_ex(('127.0.0.1', 80))
#    if result == 0:
#        print "Port is open"
#    else:
#        print "Port is not open"



ReadConfigFile()
# AddPingCheck() #old no longer used...

# PortScan()




# hhh = socket.gethostbyname("csas205")
print("WIDTH = ")
print (frame.winfo_geometry())
print (frame.size())




def test():
    print("Menu Click")
    #textarea.CreateAboutWindow()

    #import textarea  # import another Py file.
    #os.system('python textarea.py')
    #root.deiconify()
    #root.new_window()


def ShowLogWindow():
    print("LogFile Click")
    LogFileView.CreateLogFileWindow()
    #os.system('python LogFileView.py')

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
    #threading.Thread(target=About.Create_About_Window).start()
    #About.Create_About_Window()
    #About_Window.show()
    About_Window = About.Create_About_Window()
    #About_Window.show()

def EditConfig():
    os.system("notepad.exe Config/config.txt")
    #windows only at the mo.


menu = Menu(Window)
Window.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Program", menu=filemenu)
#filemenu.add_command(label="Settings / Options", command=test)
#filemenu.add_command(label="Configuration", command=test)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=Window.destroy)

logmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Logs", menu=logmenu)
logmenu.add_command(label="Show Log File", command=ShowLogWindow)

Checksmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Configuration", menu=Checksmenu)
Checksmenu.add_command(label="Add Header", command=AddTitle)
Checksmenu.add_command(label="Add Ping Check", command=AddPing)
Checksmenu.add_command(label="Add Port Check", command=AddPort)
Checksmenu.add_command(label="Manual Edit Config", command=EditConfig)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
#helpmenu.add_command(label="Manual", command=test)
helpmenu.add_command(label="About...", command=AboutWindow)



# Main window loop
Window.mainloop()



#try:
#   thread.start_new_thread(Window.mainloop())
#except:
#   print "Error: unable to start thread"#
#
#while 1:
#   pass
