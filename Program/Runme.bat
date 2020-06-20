ECHO OFF
COLOR 1F
CLS
:MENU
CLS
ECHO.
ECHO                                             Network Monitor
ECHO                            ...............................................
ECHO                                            1  - Run the Poller
ECHO                                            2  - Run the Displayer
ECHO.
ECHO                                            20 - EXIT
ECHO.
SET /P M=".                          Type in a number and then press ENTER: "
IF %M%==1 GOTO OP1
IF %M%==2 GOTO OP2

IF %M%==20 GOTO EOF
GOTO MENU

:OP1
cd Bin
python Poller.py
Pause
GOTO MENU

:OP2
cd Bin
python Main.py
Pause
GOTO MENU

:EOF
COLOR 0F
cls