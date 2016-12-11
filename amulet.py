from evony import *
import time
import os
import sys
import random
from threading import Thread
import Queue
import string
from actionfactory.builder import *
from actionfactory.quest import *
from actionfactory.items import *
import hashlib
def createacc(server,itemsarray,proxy=None,proxytype='HTTP',useclient=None,callback=None,timeout=30):
	try:
		if proxy.count(':')!=1:
			proxyhost=''
			proxyport=0
			useproxy=False
		else:
			useproxy=True
			proxyhost=proxy.split(':')[0]
			proxyport=int(proxy.split(':')[-1])
		if useclient==None:
			x=Client(server,setproxy=useproxy,proxyhost=proxyhost,proxyport=proxyport,proxytype=proxytype,callback=callback,timeout=timeout)
		else:
			x=useclient
		y=x.registernewplayer()
		callback("|9|9")
		builder=Builder(x)
		castleid=y['data']['player']['castles'][0]['id']
		quest=Quest(x,castleid)
		x.client.sendmessage('common.addToFavorites',{})
		res=x.responsehandler('common.addToFavorites')
		builder.createbuilding(castleid,0,1)
		quest.completequest(1)
		quest.completequest(226)
		items=Item(x,castleid)
#		quest.completequest(535)
		result=[]
		v=items.useitem('player.box.gambling.3')
		result.append(v['data']['itemBeans'][0])
		quest.completequest(223)
		v=items.useitem('player.box.gambling.3')
		result.append(v['data']['itemBeans'][0])
		v=items.useitem('player.box.gambling.3')
		result.append(v['data']['itemBeans'][0])
		v=items.useitem('player.box.gambling.3')
		result.append(v['data']['itemBeans'][0])
		alreadyreg=False
		filestr=''
		for p in result:
			itemname=p['id']
			if p['id']=='player.box.gambling.medal.10':
				itemname=str(p['count'])+'cents'
#			callback("8||BADITEM"+itemname)
			if itemname not in itemsarray:
				continue
			if alreadyreg:
				filestr+=("   "+itemname)
				callback("8||GOODITEM"+itemname)
				continue
			email=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
			pwd='aaaaaa'
			pwd=(hashlib.sha1(pwd).hexdigest())+'='+(hashlib.md5(pwd).hexdigest())
			email=email+'@gmail.com'
			data={'account':email,'password':pwd}
			x.client.sendmessage('common.saveUnregisteredPlayer',data)
			x.responsehandler('common.saveUnregisteredPlayer')
			filestr+=email
			callback("8||GOODITEM"+email)
			filestr+=("    "+itemname)
			callback("8||GOODITEM"+itemname)
			alreadyreg=True
		if filestr!='':
			g=open('emaillog.txt','a')
			g.write(filestr)
			g.write('\n')
			g.close()
		return x
	except:
		try:
			x.close()
		except:
			pass
def _stamulet(server,itemsarray,proxy=None,proxytype='HTTP',useclient=None,callback=None,checksource=None,timeout=30,totalrunning=None):
	x=0
	useclient=None
	while x!=None:
		if useclient!=None:
			useclient.registered=False
		if checksource!=None:
			if checksource.killsignal:
				break
		x=createacc(server,itemsarray,proxy,proxytype,useclient,callback,timeout=timeout)
		useclient=x
	totalrunning[0]-=1
def startamulet(server,itemsarray,proxy=None,proxytype='HTTP',useclient=None,callback=None,checksource=None,timeout=30,totalconn=1):
	totalrunning=[0]
	for i in range(0,totalconn):
		totalrunning[0]+=1
		while True:
			try:
				Thread(target=_stamulet,args=(server,itemsarray,proxy,proxytype,useclient,callback),kwargs={'checksource':checksource,'totalrunning':totalrunning,'timeout':timeout}).start()
				break
			except:
				time.sleep(.3)
	while True:
		if checksource!=None:
			if checksource.killsignal:
				if totalrunning[0]>0:
					time.sleep(.3)
					continue
				callback("|NOKILL|")
				return
		if totalrunning[0]==0:
			callback("|KILL|")
			return
		time.sleep(.3)