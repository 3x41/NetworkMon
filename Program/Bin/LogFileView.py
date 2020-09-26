from tkinter import filedialog

from tkinter import *
import datetime

#need to add a file select here.. for now , only display todays log..


def OpenLogFile():
    SelectedFile =  filedialog.askopenfilename(initialdir = "..\Logs",title = "Select file",filetypes = (("Log files","*.log"),("all files","*.*")))
    print (SelectedFile)
    OpenFile(SelectedFile)


def CloseWindows():
    exit()
    


LogFileWindow = Tk()
LogFileWindow.title("Log File")
LogFileWindow.resizable(0,0) #Remove Maximize button
LogFileWindow.iconbitmap("../Images/network.ico")
LogFileWindowW, LogFileWindowH = 665,440  #root.winfo_screenwidth()/2, root.winfo_screenheight()/2
LogFileWindow.geometry("%dx%d+150+150" % (LogFileWindowW, LogFileWindowH))


    
LogFileSelectFileDrop = Button(LogFileWindow,text="Select Log File",command=OpenLogFile)
LogFileSelectClose = Button(LogFileWindow,text="Close Window",command=CloseWindows)
LogFileWindowScroll = Scrollbar(LogFileWindow)
LogFileWindowScrollText = Text(LogFileWindow) #


LogFileSelectFileDrop.grid(row=0, column=0,sticky="we")
LogFileWindowScroll.grid(row=1, column=1,sticky="ns")
LogFileWindowScrollText.grid(row=1, column=0)
LogFileSelectClose.grid(row=2, column=0,sticky="we")

LogFileWindowScroll.config(command=LogFileWindowScrollText.yview)
LogFileWindowScrollText.config(yscrollcommand=LogFileWindowScroll.set)
LogText = "\n"
LogText = LogText + "==================---------- Error Log For Today ----------==================\n\n"
LogText = LogText + "\n"





def OpenFile(FileName):
    try:
        LogText = ""
        LogFileWindowScrollText.delete(1.0,END)
        
        if FileName=="":
            Todays_Date = datetime.date.today()
            FileName = "../Logs/" + str(Todays_Date) + ".log"
        
        with open(FileName) as fp:
            line = fp.readline()
            while line:
                LogText = LogText + line
                line = fp.readline()
        LogFileWindowScrollText.insert(END,LogText)
        #LogFileWindowScrollText
        print(LogText)
    except:
        LogText = ("No Errors or No LogFile found...")
        print ("Error Opening File !")



LogFileWindowScrollText.insert(END, LogText)
OpenFile("")


mainloop()
