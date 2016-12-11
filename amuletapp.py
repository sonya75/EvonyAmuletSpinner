import json
from GUIAMULET import *
from threading import Thread
import subprocess
import time
from pyamf import sol
import sys
from proxymanager import ProxyManager
from amulet import *
app=wx.App(False)
frame1=MyFrame2(None)
frame2=MyFrame1(None)
frame3= ProxyManager()
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
try:
	frame1.m_textCtrl600.SetValue("30")
	config=json.loads(open("amuletconfig.json",'r').read())
	if "itemlist" in config:
		if config["itemlist"]!=[]:
			frame2.m_checklist.SetCheckedStrings(config["itemlist"])
	if "server" in config:
		frame1.m_textCtrl1.SetValue(config["server"])
	if "maxconnections" in config:
		frame1.m_textCtrl41.SetValue(str(config['maxconnections']))
	if "maxchecks" in config:
		frame1.m_textCtrl6.SetValue(str(config["maxchecks"]))
	if "usebroker" in config:
		frame1.m_checkBox1.SetValue(config["usebroker"])
	if "timeout" in config:
		frame1.m_textCtrl600.SetValue(str(config["timeout"]))
	if "maxperproxy" in config:
		frame1.m_textCtrl06.SetValue(str(config['maxperproxy']))
except:
	pass
def showframe(event):
	frame2.Show()
	frame2.SetFocus()
def hideframe(event):
	frame2.Hide()
def finishhandler(p):
	global linecount
	if "GOODITEM" in p:
		p=p.strip().split("GOODITEM")[-1]
		try:
			name=itemsarray[p]
		except:
			name=p
		wx.CallAfter(frame1.m_textCtrl5.AppendText,(name+'\n'))
		return
	if "BADITEM" in p:
		linecount+=1
		if linecount>=1000:
			linecount=0
			wx.CallAfter(frame1.m_textCtrl4.SetValue,"")
		p=p.strip().split("BADITEM")[-1]
		try:
			name=itemsarray[p]
		except:
			name=p
		wx.CallAfter(frame1.m_textCtrl4.AppendText,(name+'\n'))
		return
def showmanager(event):
	frame3.Show()
	frame3.SetFocus()
def checkstop():
	if frame3.killsignal:
		wx.CallLater(1000,checkstop)
		return
	frame1.m_button2.Enable()
def onstop():
	if frame1.m_button2.GetLabel()=="Spin":
		return
	frame3.stop()
	frame1.m_button2.SetLabel("Spin")
	frame1.m_button2.Disable()
	checkstop()
def execspin(event):
	global linecount
	if frame1.m_button2.GetLabel()=="Stop":
		onstop()
		return
	linecount=0
	server=frame1.m_textCtrl1.GetValue()
	try:
		maxconnections=int(frame1.m_textCtrl41.GetValue())
		maxchecks=int(frame1.m_textCtrl6.GetValue())
		timeout=int(frame1.m_textCtrl600.GetValue())
		maxperproxy=int(frame1.m_textCtrl06.GetValue())
	except:
		return
	frame1.m_button2.SetLabel("Stop")
	frame1.m_textCtrl5.SetValue("")
	usebroker=frame1.m_checkBox1.GetValue()
	frame3.MAX_PROCESS=maxconnections
	frame3.MAX_CHECKS=maxchecks
	itemlist=frame2.m_checklist.GetCheckedStrings()
	try:
		e={'server':server,'maxconnections':maxconnections,'maxchecks':maxchecks,'usebroker':usebroker,'itemlist':itemlist,'timeout':timeout,'maxperproxy':maxperproxy}
		d=open('amuletconfig.json','w')
		json.dump(e,d)
		d.close()
	except:
		pass
	lists=[]
	for p in itemlist:
		lists.append(idsarray[p])
	if usebroker:
		t=Thread(target=frame3.startbroker)
		t.daemon=True
		t.start()
	frame3.startchecker()
	frame3.runprocess(startamulet,server,lists,timeout=timeout,totalconn=maxperproxy,callback=finishhandler)
def onclose(event):
	onstop()
	sys.exit()
frame1.m_button2.Bind(wx.EVT_BUTTON,execspin)
frame1.m_button1.Bind(wx.EVT_BUTTON,showframe)
frame1.Bind(wx.EVT_CLOSE,onclose)
frame2.Bind(wx.EVT_CLOSE,hideframe)
frame1.m_button3.Bind(wx.EVT_BUTTON,showmanager)
frame1.Show()
app.MainLoop()