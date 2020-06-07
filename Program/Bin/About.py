from tkinter import *


def ButtonClick():
    print("Closed About Window.")
    #AboutWindow.destroy()
    #About_Window.hide()
    
    
    
def Create_About_Window():
    AboutWindow = Tk()
    AboutWindow.title("About")
    AboutWindow.geometry("500x400")
    AboutWindow.resizable(0,0) #Remove Maximize button
    #AboutImage = PhotoImage(file="Network-Broadcasting-icon.gif")
    AboutWindow.iconbitmap("../Images/network.ico")

    About_Lbl_1 = Label(AboutWindow, text="", font=(None, 20))
    About_Lbl_2 = Label(AboutWindow, text="", font=(None, 20))
    About_Lbl_3 = Label(AboutWindow, text="", font=(None, 20))
    #About_Lbl_4 = Label(AboutWindow, image=AboutImage)
    About_Lbl_5 = Label(AboutWindow, text="Network Monitor", font=(None,20))
    About_Lbl_6 = Label(AboutWindow, text="Created By Alex Garwood", font=(None, 10))
    About_Lbl_7 = Label(AboutWindow, text="Version 0.5 Alpha", font=(None, 12))
    About_Lbl_8 = Label(AboutWindow, text=" ", font=(None, 10))
    About_Button = Button(AboutWindow, text="Close", command=AboutWindow.destroy)
    
    #About_Lbl_4.place(x=0,y=0)
    About_Lbl_1.pack()
    #About_Lbl_4.pack()

    About_Lbl_2.pack()
    About_Lbl_5.pack()
    About_Lbl_6.pack()
    About_Lbl_3.pack()
    About_Lbl_7.pack()
    About_Lbl_8.pack()
    About_Button.pack()

    #mainloop()

#Only uncomment when testing and just running this file
#About_Window = Create_About_Window()
    
#Create_About_Window()
#print ("About Closed After event")


