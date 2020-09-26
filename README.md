# NetworkMon
Basic Ping and Port checker/poller.

Created in Python, this is a beta version. The basics seem to be working but it currently still needs more work.

To run, all you should need is Python 3 installed and then run the Run.py

Currently this is focused on running from  Windows system. There is some code in for Linux and later (much later) it will be able to run on both.

Email notifications and alerts are not currently in this version but planned for the future.

There are two parts to this program:

The "POLLER"
This runs on a PC that checks the config file to see what servers are up or down, then records the results.
This now also creates a Results.HTML file that auto refreshes itself and is a great easy way to see the results.

This mush always be running so that the results are created and updated.

The "Main"
This is a viewer that shows the results of the poller results in a clear way. You can also see the logs and add entries in the config (currently limited). This program is really for more a diagnostics type viewer and will be the main way to configure the software in the future.

### About the Configuration File

This is a text file that lives in the "Config" folder in a file called "config.txt".

The first character at the start of the line defines what the line is. Any empty lines are ignored.

:
This is a Text field only, for grouping multiple entries. You dont need to use it but it makes things easier. For example, you could use this as a header like Servers, or Switches to try and group it a little.

@
This tells the poller to Ping the IP or hostname address and then its followed by { so that you can enter in text to make it more helpful to you.

>
This tells the poller and main to Port scan the IP/Hostname and then its followed by { and the port number.

Here is an example of a config file:

```

:Switches
@127.0.0.1{My server

:Linux Server
>127.0.0.1{80{Localhost Server

:test
@192.168.1.254{Router Test

```


More documentation to follow.

