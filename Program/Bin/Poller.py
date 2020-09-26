import os
import socket
import time
import datetime

# Configuration Settings:
HostOS = "Windows" # "Linux" currently untested for linux..
RefreshDelay = 60 #300 # in Seconds. 1min = 60, 5mins = 300, 10mins =600, 15mins=900, 20mins=1200
GenHTML = True #False 
GenHTML_Refresh_Delay = 90 #refresh built into the html file
#email_Address="Test@gmail.com"
#email_Server=""
#email_Username=""
#email_Password=""
Debugging = True # For testing True, Live set to False

#Do not change.
Todays_Date = datetime.date.today()
Total_Count = 0 # Item Counter
Down_Count = 0 # How many are down.

#More Config, Only change if you know what you are doing.
LogFile = "../Logs/" + str(Todays_Date) + ".log"
OutputFile = "../Logs/Results.txt"
ConfigFile = "../Config/config.txt"
LockFile = "../Config/Lock.File"
HTMLFile = "../Results.html"


def WriteHTML(Entry):
    fo = open(HTMLFile, "a")
    fo.write(Entry)
    fo.close()
    
    
def Welcome():
    print ("*** Welcome to the Poller ***")
    print (" **       Version 0.5     **")
    print (" Started on: " + str(datetime.datetime.now()))
    print ("")
    
def CleanFile():
    #Create File Lock Here..
    fo = open(LockFile,"w")
    fo.write("Temp Lock for refresh fix.")
    fo.close()
    #Create Output File..
    fo = open(OutputFile,"w")
    fo.write("")
    fo.close()
    #Create HTML File
    if GenHTML == True:
        fo = open(HTMLFile,"w")
        fo.write("<HTML>\n<TITLE>Network Monitor</TITLE>\n<link rel='stylesheet' href='config/w3.css'> \n")
        fo.write("<head><meta http-equiv='refresh' content='" + str(GenHTML_Refresh_Delay) + "'></head>\n<BODY>\n") 
        fo.close()
        

def WriteLogFile(Entry):
    CurrentDateTime = str(datetime.datetime.now())
    fo = open(LogFile, "a")
    fo.write(Entry + "," + CurrentDateTime + "\n")
    fo.close()
    
def WriteFile(Entry):
    fo = open(OutputFile, "a")
    fo.write(Entry + "\n")
    fo.close()


def PortTest(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pp = int(port)
    result = sock.connect_ex((ip,pp))
    PortResult = "Unknown"
    
    if result == 0:
        PortResult = " Port " + port + " is Open"
    else:
        PortResult = " Port " + port + " is Closed"
    return PortResult


def Ping(hostname):
    PingResult = "DOWN"
    if HostOS == "Windows":
        response = os.system("ping -n 4 " + hostname)  # Windows Only command
    else:
        response = os.system("ping -c 1 " + hostname)  # Unix/Linux Only command

    if response == 0:
        PingResult = "UP"
    else:
        PingResult = "DOWN"
        #CurrentDateTime = str(datetime.datetime.now())
    return PingResult


def ReadConfigFile():
    if GenHTML == True:
        WriteHTML("\n<div class='w3-container w3-orange w3-center w3-small'><p> N e t w o r k&nbsp;&nbsp;&nbsp;M o n i t o r <BR> Last Saved at : "+ str(datetime.datetime.now()) +"</p></div>\n<p></p>")
    #global LabelArrayMax
    with open(ConfigFile) as fp:
        line = fp.readline()
        global Total_Count
        global Down_Count
        Down_Count = 0
        Total_Count = 0
        if GenHTML == True:
            WriteHTML("<div class='w3-container'>")
            WriteHTML("<ul class='w3-ul w3-small w3-center'>")
        while line:
            if line[:1] == ":":
                #Header sub cat only
                line = line.replace("\n", "")
                #print (line)
                WriteFile(line)
                if GenHTML == True:
                    Title = line.replace(":","")
                    WriteHTML("<li class='w3-white w3-center'></li>\n<li class='w3-light-grey w3-center'>" + Title + "</li>\n")
                #AddSubBlank("")
                #AddSubCatWindow(line[1:])
            elif line[:1] == ">":
                #Port Scan Found
                line = line.replace(">", "")
                line = line.replace("\n", "")
                #print("Port Scan entry Found > ", line)
                ip,port,tname = line.split("{")
                #print (ip)
                PortTestResult = PortTest(ip,port)
                if "Closed" in PortTestResult:
                    print("Write to Error Log, date and time")
                    WriteLogFile(ip + "," + PortTestResult)
                    Down_Count += 1
                    if GenHTML == True:
                        WriteHTML("<li class='w3-red w3-center'>&#x274C; "+ tname +" ( "+ ip +" ) "+ PortTestResult +"</li>\n")
                else:
                    if GenHTML == True:
                        WriteHTML("<li class='w3-green w3-center'>&#x2705; "+ tname +" ( "+ ip +" ) "+ PortTestResult +"</li>\n")
                #AddPortScan(ip,port)
                Result = ">" + tname + "," + PortTestResult
                print (Result)
                #save to file....
                WriteFile(Result)
                Total_Count += 1
            elif line == "\n":
                #If nothing in the line, skip it.
                print("")
            elif line[:1] == "@":
                #IP Address (Ping only)
                line = line.replace("\n", "")
                line = line.replace("@", "")
                aip,atname = line.split("{")
                PingTest = Ping(aip)
                if PingTest == "Down":
                    print("Write to Error Log, date and time")
                    WriteLogFile(atname + "," + PingTest)
                    Down_Count += 1
                    if GenHTML == True:
                        WriteHTML("<li class='w3-red w3-center'>&#x274C; "+ atname +" ( "+ aip +" ) "+ PingTest +"</li>\n")
                #CurrentDateTime = str(datetime.datetime.now())
                Result = "@" + atname + "," + PingTest
                print (Result)
                #save to file....
                WriteFile(Result)
                if GenHTML == True:
                    WriteHTML("<li class='w3-green w3-center'>&#x2705; "+ atname +" ( "+ aip +" ) "+ PingTest +"</li>\n")
                Total_Count += 1
            line = fp.readline()
            #Delete File Lock Here..
    os.remove(LockFile)
    if GenHTML == True:
        WriteHTML("</ul></div>")
        WriteHTML("<p></p>\n<div class='w3-container w3-orange w3-center w3-xlarge'>")
        WriteHTML("<p>Total <span class='w3-badge w3-black'>"+ str(Total_Count) +"</span>")
        WriteHTML(" Up <span class='w3-badge w3-green'>"+ str(Total_Count-Down_Count) +"</span>")    
        WriteHTML(" Down <span class='w3-badge w3-red'>"+ str(Down_Count) +"</span></p>")
        WriteHTML("<p class='w3-small'>HTML Created by the Poller.</p>")
        WriteHTML(" \n</body>\n</html>\n")

# MAIN LOOP

if Debugging == True:
    Welcome()
    CleanFile()
    ReadConfigFile()
    print ("Total Hosts = " + str(Total_Count))

if Debugging == False:
    Welcome()
    CleanFile()
    while 1:
        ReadConfigFile()
        print ("--------- Waiting (Refresh Delay) --------")
        time.sleep(RefreshDelay)
        CleanFile()

