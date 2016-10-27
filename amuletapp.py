import json
from GUIAMULET import *
from threading import Thread
import subprocess
import time
from pyamf import sol
import sys
app=wx.App(False)
frame1=MyFrame2(None)
frame2=MyFrame1(None)
d=dict(sol.load('items.sol'))
d['1000 cents']='1000cents'
d['300 cents']='300cents'
d['50 cents']='50cents'
d['10 cents']='10cents'
d['100 cents']='100cents'
d['30 cents']='30cents'
keys=d.keys()
keys=sorted(keys)
m_checkList2 = wx.CheckListBox( frame2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, keys, 0 )
frame2.bSizer1.Add(m_checkList2, 1, wx.ALL|wx.EXPAND, 5 )
frame2.Layout()
frame2.m_checklist=m_checkList2
itemsarray={}
idsarray=d
for q in d:
	itemsarray[d[q]]=q
def showframe(event):
	frame2.Show()
def hideframe(event):
	frame2.Hide()
def killprocess(pid,tried=False):
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	p=subprocess.Popen(["TASKKILL","/F","/T","/pid",str(pid)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
	if not tried:
		wx.CallLater(1000,killprocess,pid,True)
def killall():
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	p=subprocess.Popen(["TASKKILL","/F","/T","/im","amulet.exe"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
def checkprocess(pid):
	global lastupdate,amuletprocess
	try:
		if (frame1.m_button2.GetLabel())=='Start':
			return
		if (amuletprocess.pid)!=pid:
			killprocess(pid)
			return
		if (time.time()-lastupdate)>30:
			killprocess(amuletprocess.pid)
			wx.CallLater(100,execspin,None)
			return
		wx.CallLater(1000,checkprocess,pid)
	except:
		wx.CallLater(1000,checkprocess,pid)
def fff(comm):
	global lastupdate,amuletprocess,itemsarray
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	amuletprocess=subprocess.Popen(comm,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
	lastupdate=time.time()
	wx.CallAfter(checkprocess,(amuletprocess.pid))
	for p in amuletprocess.stdout:
		lastupdate=time.time()
		if "GOODITEM" in p:
			p=p.strip().split("GOODITEM")[-1]
			try:
				name=itemsarray[p]
			except:
				name=p
			wx.CallAfter(frame1.m_textCtrl5.write,(name+'\n'))
			continue
		if "BADITEM" in p:
			p=p.strip().split("BADITEM")[-1]
			try:
				name=itemsarray[p]
			except:
				name=p
			wx.CallAfter(frame1.m_textCtrl4.write,(name+'\n'))
			continue
		if "ERRORREPORT" in p:
			try:
				killprocess(amuletprocess.pid)
			except:
				pass
			wx.CallAfter(execspin,None)
			break
def execspin(event):
	global idsarray
	if ((frame1.m_button2.GetLabel())=='Stop')&(event!=None):
		killall()
		frame1.m_button2.SetLabel("Start")
		return
	frame1.m_button2.SetLabel("Stop")
	lists=[]
	for p in frame2.m_checklist.GetCheckedStrings():
		lists.append(idsarray[p])
	if lists==[]:
		execspin(0)
		return
	server=frame1.m_textCtrl1.GetValue()
	Thread(target=fff,args=(['amulet.exe',server,("||".join(lists))],)).start()
def onclose(event):
	killall()
	sys.exit()
frame1.m_button2.Bind(wx.EVT_BUTTON,execspin)
frame1.m_button1.Bind(wx.EVT_BUTTON,showframe)
frame1.Bind(wx.EVT_CLOSE,onclose)
frame2.Bind(wx.EVT_CLOSE,hideframe)
frame1.Show()
app.MainLoop()
