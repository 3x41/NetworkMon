# NetworkMon
Basic Ping and Port checker / poller.

Created in Python, this is an alpha version. The basics seem to be working but it currently needs a lot more work.

To run, all you should need is Python 3 installed and then run the Run.py

Currently this is focused on running from  Windows system. There is some code in for Linux and later (much later) it will be able to run on both.

There are two parts to this program:

The "POLLER"
This runs on a PC that checks the config file to see what servers are up or down, then records the results.

The "Main"
This is a viewer that shows the results of the poller results in a clear way. You can also see the logs and add entries in the config.

### About the Configuration File

This is a text file that lives in the "Config" folder in a file called "config.txt".

The first character at the start of the line defines what the line is. Any empty lines are ignored.

:
This is a Text field only, for grouping multiple entries. You dont need to use it but it makes things easier.

@
This tells the poller and main to Ping the IP or hostname address.

>
This tells the poller and main to Port scan the IP/Hostname and then its followed by : and the port number.

Here is an example of a config file:

```

:Switches
@127.0.0.1

:Linux Server
>127.0.0.1:80

:test
@192.168.1.254

```


More documentation to follow.

