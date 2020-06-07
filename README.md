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

