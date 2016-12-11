import wx
import subprocess
import Queue
from PROXYGUI import *
from proxychecker import *
from threading import Thread
import random
class ProxyManager(MyFrame1):
	def __init__(self):
		MyFrame1.__init__(self,None)
		self.proxylist={}
		self.totalchecks=0
		self.MAX_CHECKS=100
		self.MAX_PROCESS=30
		self.totalprocess=0
		self.totalaccounts=0
		self.handlelogs=False
		self.checkingon=False
		self.checkqueue=Queue.Queue()
		self.workingproxies=Queue.Queue()
		self.workinglength=0
		self.selectedproxy=None
		self.m_button1.Bind(wx.EVT_BUTTON,self.showaddproxy)
		self.killsignal=False
		self.Bind(wx.EVT_CLOSE,self.onclose)
		self.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED,self.showlog)
	def checkstop(self):
		if (self.totalprocess>0)|(self.checkingon):
			wx.CallLater(1000,self.checkstop)
			return
		self.killsignal=False
	def stop(self):
		self.killsignal=True
		self.killbroker()
		self.checkstop()
	def showaddproxy(self,event):
		try:
			path=self.m_filePicker2.GetPath()
			a=open(path,'r').read().split('\n')
			random.shuffle(a)
			for b in a:
				if b.strip()=='':
					continue
				self.addproxy(b.strip())
		except:
			pass
	def onclose(self,event):
		self.Hide()
	def addproxy(self,proxy):
		if proxy in self.proxylist:
			return
		self.m_dataViewListCtrl4.AppendItem([proxy,"Added to checking queue","",""])
		self.proxylist[proxy]={}
		self.checkqueue.put(proxy)
	def deleteproxy(self,proxy):
		f=self.m_dataViewListCtrl4.ItemCount
		for i in range(0,f):
			if self.m_dataViewListCtrl4.GetTextValue(i,0)==proxy:
				self.m_dataViewListCtrl4.DeleteItem(i)
				self.proxylist.pop(proxy,None)
				return
#The following function can't be run in same thread.
	def startbroker(self):
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		self.ProxyBroker=subprocess.Popen(["proxy\\toto.exe"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
		for p in self.ProxyBroker.stdout:
			if self.killsignal:
				break
			p=p.strip()
			wx.CallAfter(self.addproxy,p)
	def killbroker(self):
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		try:
			subprocess.Popen(["TASKKILL","/F","/T","/pid",str(self.ProxyBroker.pid)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
		except:
			pass
#	def updateitem(self,proxy,values):
#		self.startthread(self._updateitem,(proxy,values))
	def updateitem(self,proxy,values):
		f=self.m_dataViewListCtrl4.ItemCount
		for i in range(0,f):
			if self.m_dataViewListCtrl4.GetTextValue(i,0)==proxy:
				for j in range(0,len(values)):
					wx.CallAfter(self.m_dataViewListCtrl4.SetValue,values[j],i,(j+1))
				return
	def addtocheckqueue(self,proxy):
		self.checkqueue.put(proxy)
		self.updateitem(proxy,["Added to checking queue","",""])
	def processproxy(self,value):
		self.totalchecks-=1
		if "FATALERROR101" in value:
			val=value.strip().split("FATALERROR101")[-1]
			self.deleteproxy(val)
			return
		if "FAILED259" in value:
			val=value.strip().split("FAILED259")[-1]
			if "retries" in (self.proxylist[val]):
				if self.proxylist[val]["retries"]>=5:
					self.deleteproxy(val)
					return
			else:
				self.proxylist[val]["retries"]=0
			self.proxylist[val]["retries"]+=1
			if "lastretry" not in (self.proxylist[val]):
				self.proxylist[val]["lastretry"]=5
			else:
				self.proxylist[val]["lastretry"]=(self.proxylist[val]['lastretry'])*2
			wx.CallLater((1000*60*(self.proxylist[val]['lastretry'])),self.addtocheckqueue,val)
			self.updateitem(val,["Failed","","Retrying in "+str(self.proxylist[val]["lastretry"])+" mins"])
			return
		if "SUCCESS124" in value:
			val=value.strip().split("SUCCESS124")[-1]
			val1=val.split('PROXYTYPE')[-1].strip()
			val=val.split('PROXYTYPE')[0].strip()
			if "retries" in (self.proxylist[val]):
				self.proxylist[val].pop("retries",None)
			if "lastretry" in (self.proxylist[val]):
				self.proxylist[val].pop("lastretry",None)
			self.proxylist[val]["type"]=val1
			self.workingproxies.put(val)
			self.workinglength+=1
			self.m_statusBar1.SetStatusText("Proxies in use: "+str(self.totalprocess)+", Proxies in queue: "+str(self.workinglength)+", Accounts created: "+str(self.totalaccounts))
			self.updateitem(val,["Working","",""])
		if "SCPT" in value:
			val=value.strip().split("SCPT")[-1]
			self.workingproxies.put(val)
			self.workinglength+=1
			self.m_statusBar1.SetStatusText("Proxies in use: "+str(self.totalprocess)+", Proxies in queue: "+str(self.workinglength)+", Accounts created: "+str(self.totalaccounts))
			self.updateitem(val,["Working","",""])
		if "EFAIL121" in value:
			val=value.strip().split("EFAIL121")[-1]
			wx.CallLater(300000,self.startchecker,immediate=val)
	#Thread safe version of processproxy
	def _procprox(self,value):
		wx.CallAfter(self.processproxy,value)
	def startchecker(self,immediate=None):
		self.checkingon=True
		if self.killsignal:
			if immediate!=None:
				self.addtocheckqueue(immediate)
			self.checkingon=False
			return
		if (self.totalchecks>=self.MAX_CHECKS)&(immediate==None):
			wx.CallLater(100,self.startchecker)
			return
		try:
			if immediate!=None:
				g=immediate
			else:
				g=self.checkqueue.get_nowait()
			self.startthread(checkproxy,(g,self._procprox))
			self.updateitem(g,["Checking","",""])
			self.totalchecks+=1
		except:
			pass
		if immediate==None:
			wx.CallLater(100,self.startchecker)
	def createcallback(self,proxy,callbk):
		def f(value):
			value=str(value)
			if len(value)>=3:
				if value[:3]=='8||':
					callbk(value[3:])
					return
			if len(value)>=6:
				if value[:6]=='|KILL|':
					self.totalprocess-=1
					wx.CallAfter(self.m_statusBar1.SetStatusText,("Proxies in use: "+str(self.totalprocess)+", Proxies in queue: "+str(self.workinglength)+", Accounts created: "+str(self.totalaccounts)))
					wx.CallAfter(self.processproxy,("EFAIL121"+proxy))
					wx.CallAfter(self.updatelog,proxy,"",setvalue=True)
					return
			if len(value)>=8:
				if value[:8]=='|NOKILL|':
					self.totalprocess-=1
					wx.CallAfter(self.m_statusBar1.SetStatusText,("Proxies in use: "+str(self.totalprocess)+", Proxies in queue: "+str(self.workinglength)+", Accounts created: "+str(self.totalaccounts)))
					wx.CallAfter(self.processproxy,("SCPT"+proxy))
					return
			if len(value)>=4:
				if value[:4]=="|9|9":
					self.totalaccounts+=1
					wx.CallAfter(self.m_statusBar1.SetStatusText,("Proxies in use: "+str(self.totalprocess)+", Proxies in queue: "+str(self.workinglength)+", Accounts created: "+str(self.totalaccounts)))
					return
			if "log" not in self.proxylist[proxy]:
				wx.CallAfter(self.updatelog,proxy,"",setvalue=True)
			if self.handlelogs:
				callbk(value)
			wx.CallAfter(self.updatelog,proxy,value)
			return
		return f
	def updatelog(self,proxy=None,value="",setvalue=False):
		value=str(value)
		if proxy==None:
			h=self.selectedproxy
			if h not in self.proxylist:
				return
			if "log" not in self.proxylist[h]:
				self.proxylist[h]['linecount']=0
				self.proxylist[h]['log']=""
			self.m_textCtrl23.SetValue(self.proxylist[h]["log"])
			return
		if setvalue:
			self.proxylist[proxy]['linecount']=1
			self.proxylist[proxy]["log"]=value
			self.updatelog()
			return
		self.proxylist[proxy]['linecount']+=1
		if self.proxylist[proxy]['linecount']>=100:
			self.proxylist[proxy]['linecount']=1
			self.proxylist[proxy]['log']=''
			if proxy==self.selectedproxy:
				self.m_textCtrl23.SetValue("")
		e=(self.proxylist[proxy]["log"])+value+"\n"
		self.proxylist[proxy]["log"]=e
		if proxy==self.selectedproxy:
			self.m_textCtrl23.AppendText(value+"\n")
	def showlog(self,event):
		h=self.m_dataViewListCtrl4.GetSelectedRow()
		if h==wx.NOT_FOUND:
			return
		else:
			self.selectedproxy=self.m_dataViewListCtrl4.GetTextValue(h,0)
			self.updatelog()
			return
	def runprocess(self,func,*args,**kwargs):
		if self.killsignal:
			return
		if self.totalprocess>=self.MAX_PROCESS:
			wx.CallLater(1000,self.runprocess,func,*args,**kwargs)
			return
		try:
			g=self.workingproxies.get_nowait()
			self.workinglength-=1
			wx.CallAfter(self.m_statusBar1.SetStatusText,("Proxies in use: "+str(self.totalprocess)+", Proxies in queue: "+str(self.workinglength)+", Accounts created: "+str(self.totalaccounts)))
		except:
			wx.CallLater(1000,self.runprocess,func,*args,**kwargs)
			return
		self.totalprocess+=1
		self.m_statusBar1.SetStatusText("Proxies in use: "+str(self.totalprocess)+", Proxies in queue: "+str(self.workinglength))
		self.updateitem(g,["Working","In Use","Building account. See log for details."])
		kwargs1={c:kwargs[c] for c in kwargs}
		callbk=kwargs1.pop("callback",None)
		cb=self.createcallback(g,callbk)
		self.startthread(func,args,dict(proxy=g,callback=cb,proxytype=(self.proxylist[g]['type']),checksource=self,**kwargs1))
		wx.CallLater(100,self.runprocess,func,*args,**kwargs)
	def startthread(self,func,args,kwargs={}):
		try:
			t=Thread(target=func,args=args,kwargs=kwargs)
			t.daemon=True
			t.start()
		except:
			wx.CallLater(100,self.startthread,func,args,kwargs)
