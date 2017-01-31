# EvonyAmuletSpinnet

Its a amulet spinner(spins amulet and registers those accounts only when it finds the items that you want) app for Evony based on pyEvony.

There are two ways to run this app, one is to use python directly to run it or use the executable file in the release folder.

# Using python to run it:-

You will need to install python 2.7.x(the latest one is 2.7.13, but using any python 2.7 version will work). This app requires two python modules to run, pyamf and wxPython-Phoniex. The first one you can directly install using pip:-

`` pip install pyamf ``

The second one, you can download the wheel file from here:- https://wxpython.org/Phoenix/snapshot-builds/ . Download the proper one for your system and install it. Then you can run the app by running amuletapp.py

# Using the executable file to run it:-

The executable is located in the amulet.rar file in the release folder. Extract the rar file and run amuletapp.exe.

# Proper settings for running the app:-

This app uses thousands of proxies to create accounts, spins amulet in each 4 times and whenever gets the items that you chose from the items list, it saves those accounts. In the app there is an option to select which items you want. Note that, not all the items that appear there are available in the amulet. Also certain items are available in the amulet only during promos.

It shows the emails of the accounts which gets the items that you want in the right text box and also saves the emaillist in a file named emaillog.txt in the same folder. It used to show the list of all the items that you get from spinning the amulet. But that list growed so fast that it used to crash the app. So it just shows blank on the left textbox now.

It has an in-built proxy scraper, named proxybroker. You can enable it by checking the chekbox beside the label "Use Proxybroker". You can also load your own list of proxies. Click the Proxy-Manager button and there is an option to load proxies there. Gatherproxy.com is a good site to get a lot of free proxies. Also I have included a tool named uProxy which is also a pretty good proxy scraper. Its located in the proxytools folder.

To run this app properly, you need a good computer and a good internet connection. A good setting for running the app will be:-

```
Maximum number of proxies to be used:- 20000
Maximum number of proxies to be checked simultaneously:- 1000
Maximum number of connections per proxy:- 3
Timeout:- 20
```

**To run this app its very important to have a lot of working proxies. So you should a lot of proxies in the proxy manager before starting the app. You can easily scraper over 20-30k proxies from gatherproxy.com and using the tool I mentioned.**
