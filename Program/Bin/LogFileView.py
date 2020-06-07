from tkinter import *
import datetime

#need to add a file select here.. for now , only display todays log..


def CreateLogFileWindow():
    LogFileWindow = Tk()
    LogFileWindow.title("Log File")
    LogFileWindow.resizable(0, 1) #Remove Maximize button
    LogFileWindow.iconbitmap("../Images/network.ico")
    LogFileWindowW, LogFileWindowH = 800,500  #root.winfo_screenwidth()/2, root.winfo_screenheight()/2
    LogFileWindow.geometry("%dx%d+150+150" % (LogFileWindowW, LogFileWindowH))

    LogFileWindowScroll = Scrollbar(LogFileWindow)
    LogFileWindowScrollText = Text(LogFileWindow, height=50, width=100)
    LogFileWindowScroll.pack(side=RIGHT, fill=BOTH)
    LogFileWindowScrollText.pack(side=LEFT, fill=BOTH)
    LogFileWindowScroll.config(command=LogFileWindowScrollText.yview)
    LogFileWindowScrollText.config(yscrollcommand=LogFileWindowScroll.set)
    LogText = "\n"
    LogText = LogText + "==================---------- Error Log For Today ----------==================\n\n"
    LogText = LogText + "\n"

    try:
        Todays_Date = datetime.date.today()

        filepath = "../Logs/" + str(Todays_Date) + ".txt"

        #filepath = 'Logs/LogFile.txt'
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                LogText = LogText + line
                line = fp.readline()
    except:
        LogText = ("No Errors or No LogFile found...")
        print ("Error Opening ChangeLog.txt File !")

    LogFileWindowScrollText.insert(END, LogText)
    #mainloop()

#CreateLogFileWindow()
