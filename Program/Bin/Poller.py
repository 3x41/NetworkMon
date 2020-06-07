from tkinter import *
import os
import socket
import time
import datetime

# Configuration Settings:
HostOS = "Windows" # "Linux"
RefreshDelay = 60 # in Seconds. 1min = 60, 5mins = , 10mins, 15mins, 20mins


#More Config, Only change if you know what you are doing.
OutputFile = "Logs/Results.txt"
ConfigFile = "Config/config.txt"
Debugging = True #For testing True, Live set to False

Todays_Date = datetime.date.today()
LogFile = "Logs/" + str(Todays_Date) + ".txt"
cnt = 0

def Welcome():
    print ("*** Welcome to the Poller ***")
    print (" **       Version 0.2     **")
    print ("")
    
def CleanFile():
    fo = open(OutputFile,"w")
    fo.write("")
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
        response = os.system("ping -n 1 " + hostname)  # Windows Only command
    else:
        response = os.system("ping -c 1 " + hostname)  # Unix/Linux Only command

    if response == 0:
        PingResult = "UP"
    else:
        PingResult = "DOWN"
        CurrentDateTime = str(datetime.datetime.now())
    return PingResult


def ReadConfigFile():
    
    #global LabelArrayMax
    with open(ConfigFile) as fp:
        line = fp.readline()
        global cnt
        cnt = 0
        while line:
            if line[:1] == ":":
                #Header sub cat only
                line = line.replace("\n", "")
                #print (line)
                WriteFile(line)
                #AddSubBlank("")
                #AddSubCatWindow(line[1:])
            elif line[:1] == ">":
                #Port Scan Found
                line = line.replace(">", "")
                line = line.replace("\n", "")
                #print("Port Scan entry Found > ", line)
                ip,port = line.split(":")
                #print (ip)
                PortTestResult = PortTest(ip,port)
                if "Closed" in PortTestResult:
                    print("Write to Error Log, date and time")
                    WriteLogFile(ip + "," + PortTestResult)
                #AddPortScan(ip,port)
                Result = ip + "," + PortTestResult
                print (Result)
                #save to file....
                WriteFile(Result)
                cnt += 1
            elif line == "\n":
                #If nothing in the line, skip it.
                print("")
            elif line[:1] == "@":
                #IP Address (Ping only)
                line = line.replace("\n", "")
                line = line.replace("@", "")
                #ip = line.split(":")
                PingTest = Ping(line)
                if PingTest == "Down":
                    print("Write to Error Log, date and time")
                    WriteLogFile(line + "," + PingTest)
                #CurrentDateTime = str(datetime.datetime.now())
                Result = line + "," + PingTest
                print (Result)
                #save to file....
                WriteFile(Result)
                cnt += 1
            line = fp.readline()

if Debugging == True:
    Welcome()
    CleanFile()
    ReadConfigFile()
    print ("Total Hosts = " + str(cnt))

if Debugging == False:
    Welcome()
    CleanFile()
    while 1:
        ReadConfigFile()
        time.sleep(RefreshDelay)

