from tkinter import *
from tkinter import messagebox


def AddToConfigFile(EntryToAdd):
    # Open a file
    fof = open("../Config/config.txt", "a")
    fof.write(EntryToAdd);

    # Close opend file
    fof.close()

global Add_Title_Txt_Input #header
global Add_Ping_Txt_Input
global Add_Port_Txt_Input

global WindowDestroy
WindowDestroy = False #default no.


def senddetails():
    Txt_BuildLine = "\n:" + str(Add_Title_Txt_Input.get())
    AddToConfigFile(Txt_BuildLine)
    global WindowDestroy
    WindowDestroy = True
    messagebox.showinfo("Saved", "Header has been saved to the config file. ")
    #Close Window somehow...
    #Add_Title_Main_Window.exit
    #.quit()
    #Add_Title_Main_Window.destroy()
    print (tk)
    #.destroy()
    


def Add_Title_Main_WindowFun():
    global WindowDestroy
    WindowDestroy = False
    Add_Title_Main_Window = Tk()
    Add_Title_Main_Window.title("Setup Hosts to Monitor")
    Add_Title_Main_Window.resizable(0, 0) #Remove Maximize button
    Add_Title_Main_Window.iconbitmap("../Images/network.ico")
    GUI_HostsWindowW, GUI_HostsWindowH = 500,130  #root.winfo_screenwidth()/2, root.winfo_screenheight()/2
    Add_Title_Main_Window.geometry("%dx%d+150+150" % (GUI_HostsWindowW, GUI_HostsWindowH))

    #tempdd = Radiobutton(Add_Title_Main_Window,text="Python",padx=20,variable="w",value=1).pack(anchor=W)

    Add_Title_Label1 = Label(Add_Title_Main_Window, text="Add Item to the Config File", relief=FLAT)
    Add_Title_Label1.pack(fill=X)

    Add_Title_Label2 = Label(Add_Title_Main_Window, text="")
    Add_Title_Label2.pack(fill=X)

    #Lb1 = Listbox(Add_Title_Main_Window,height=3)
    #Lb1.insert(1, "Header Name")
    #Lb1.insert(2, "Ping")
    #Lb1.insert(3, "Port Check")
    #Lb1.pack(fill=X)

    Add_Title_Label3 = Label(Add_Title_Main_Window, text="Enter in a Header", relief=FLAT)
    Add_Title_Label3.pack()

    global Add_Title_Txt_Input
    Add_Title_Txt_Input = Entry(Add_Title_Main_Window,width=50, justify=CENTER)
    #Txt_input1 = Entry(Add_Title_Main_Window, width=50, justify=CENTER)
    Add_Title_Txt_Input.pack()

    Add_Title_Label4 = Label(Add_Title_Main_Window, text="")
    Add_Title_Label4.pack(fill=X)

    Add_Title_Button1 = Button(Add_Title_Main_Window, text=" Add Header ",command=senddetails)
    Add_Title_Button1.pack(fill=X)
    #mainloop()

    
def send_ping_details():
    Txt_BuildLine = "\n@" + str(Add_Ping_Txt_Input.get())
    AddToConfigFile(Txt_BuildLine)
    messagebox.showinfo("Saved", "Ping Check has been saved to the config file.")
    #Close Window somehow...
   



def Add_Ping_Main_Window():
    Add_Ping_Main_Window = Tk()
    Add_Ping_Main_Window.title("Setup Hosts to Monitor")
    Add_Ping_Main_Window.resizable(0, 0)  # Remove Maximize button
    Add_Ping_Main_Window.iconbitmap("../Images/network.ico")
    GUI_HostsWindowW, GUI_HostsWindowH = 500, 130  # root.winfo_screenwidth()/2, root.winfo_screenheight()/2
    Add_Ping_Main_Window.geometry("%dx%d+150+150" % (GUI_HostsWindowW, GUI_HostsWindowH))

    Add_Title_Label1 = Label(Add_Ping_Main_Window, text="Add Item to the Config File", relief=FLAT)
    Add_Title_Label1.pack(fill=X)

    Add_Title_Label2 = Label(Add_Ping_Main_Window, text="")
    Add_Title_Label2.pack(fill=X)

    Add_Title_Label3 = Label(Add_Ping_Main_Window, text="Enter IP / Hostname To Ping Check", relief=FLAT)
    Add_Title_Label3.pack()

    global Add_Ping_Txt_Input
    Add_Ping_Txt_Input = Entry(Add_Ping_Main_Window, width=50, justify=CENTER)
    # Txt_input1 = Entry(Add_Title_Main_Window, width=50, justify=CENTER)
    Add_Ping_Txt_Input.pack()

    Add_Title_Label4 = Label(Add_Ping_Main_Window, text="")
    Add_Title_Label4.pack(fill=X)

    Add_Title_Button1 = Button(Add_Ping_Main_Window, text=" Add Ping Check ", command=send_ping_details)
    Add_Title_Button1.pack(fill=X)

    #mainloop()


#Port Adding..
def send_port_details():
    #Add_Port_Txt_Input
    Txt_BuildLine = "\n>" + str(Add_Ping_Txt_Input.get() + ":" + str(Add_Port_Txt_Input.get()))
    AddToConfigFile(Txt_BuildLine)
    messagebox.showinfo("Saved", "Port Check has been saved to the config file.")
    # Close Window somehow...

def Add_Port_Main_Window():
    Add_Port_Main_Window = Tk()
    Add_Port_Main_Window.title("Setup Hosts to Monitor")
    Add_Port_Main_Window.resizable(0, 0)  # Remove Maximize button
    Add_Port_Main_Window.iconbitmap("../Images/network.ico")
    GUI_HostsWindowW, GUI_HostsWindowH = 500, 170  # root.winfo_screenwidth()/2, root.winfo_screenheight()/2
    Add_Port_Main_Window.geometry("%dx%d+150+150" % (GUI_HostsWindowW, GUI_HostsWindowH))

    Add_Title_Label1 = Label(Add_Port_Main_Window, text="Add Item to the Config File", relief=FLAT)
    Add_Title_Label1.pack(fill=X)

    Add_Title_Label2 = Label(Add_Port_Main_Window, text="")
    Add_Title_Label2.pack(fill=X)

    Add_Title_Label3 = Label(Add_Port_Main_Window, text="Enter IP / Hostname To Port Check", relief=FLAT)
    Add_Title_Label3.pack()

    global Add_Ping_Txt_Input
    Add_Ping_Txt_Input = Entry(Add_Port_Main_Window, width=50, justify=CENTER)
    # Txt_input1 = Entry(Add_Title_Main_Window, width=50, justify=CENTER)
    Add_Ping_Txt_Input.pack()

    Add_Title_Label4 = Label(Add_Port_Main_Window, text="Enter Port Number")
    Add_Title_Label4.pack(fill=X)

    global Add_Port_Txt_Input
    Add_Port_Txt_Input = Entry(Add_Port_Main_Window, width=50, justify=CENTER)
    # Txt_input1 = Entry(Add_Title_Main_Window, width=50, justify=CENTER)
    Add_Port_Txt_Input.pack()

    Add_Title_Label5 = Label(Add_Port_Main_Window, text="")
    Add_Title_Label5.pack(fill=X)

    Add_Title_Button1 = Button(Add_Port_Main_Window, text=" Add Port Check ", command=send_port_details)
    Add_Title_Button1.pack(fill=X)

    #mainloop()


if WindowDestroy==True:
    print ("KILL ")

#Add_Port_Main_Window()

    # label3 = Label(Add_Title_Main_Window, text="Enter Hostname or IP", relief=FLAT)
    # label3.pack()
    #
    # txt3 = Entry(Add_Title_Main_Window, width=50, justify=CENTER)
    # txt3.pack()
    # W_Button_2 = Button(Add_Title_Main_Window, text=" Add Ping Check ")
    # W_Button_2.pack(fill=X)
    #
    #
    #
    # label4 = Label(Add_Title_Main_Window, text="Enter Hostname or IP", relief=FLAT)
    # label4.pack()
    #
    # txt4 = Entry(Add_Title_Main_Window, width=50, justify=CENTER)
    # txt4.pack()
    #
    #
    # label5 = Label(Add_Title_Main_Window, text="Enter Port Number", relief=FLAT)
    # label5.pack()
    #
    # txt5 = Entry(Add_Title_Main_Window, width=50, justify=CENTER)
    # txt5.pack()
    #
    # W_Button_4 = Button(Add_Title_Main_Window, text=" Add Port Check ")
    # W_Button_4.pack(fill=X)



    #Add_Title_Main_Window.Label(Add_Title_Main_Window, text="Choose a number:").grid(column=1, row=0)  # 1
    #number = tk.StringVar()  # 2
    #numberChosen = ttk.Combobox(win, width=12, textvariable=number)  # 3
    #numberChosen['values'] = (1, 2, 4, 42, 100)  # 4
    #numberChosen.grid(column=1, row=1)  # 5
   # numberChosen.current(0)  # 6


    #phone = StringVar()
    #home = GUI_HostsWindow.Radiobutton(GUI_HostsWindow, text='Home', variable=phone, value='home')
    #office = GUI_HostsWindow.Radiobutton(GUI_HostsWindow, text='Office', variable=phone, value='office')
    #cell = GUI_HostsWindow.Radiobutton(GUI_HostsWindow, text='Mobile', variable=phone, value='cell')

    #username = StringVar()
    #name = GUI_HostsWindow.Entry(GUI_HostsWindow, textvariable=username)


    #try:
    #    filepath = 'LogFile.txt'
    #    with open(filepath) as fp:
    #        line = fp.readline()
    #        while line:
    #            LogText = LogText + line
    #            line = fp.readline()
    #except:
    #    LogText = ("No Errors or No LogFile.txt found...")
    #    print ("Error Opening ChangeLog.txt File !")






#CreateGUI_HostsWindow()





#:Switches
#127.0.0.1
#>192.168.0.2:80
