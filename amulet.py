from evony import *
import time
import os
import sys
import random
import string
from actionfactory.builder import *
from actionfactory.quest import *
from actionfactory.items import *
import hashlib
server=sys.argv[1].strip()
itemsarray=sys.argv[2].strip().split('||')
def createacc(server,useclient=None):
	global itemsarray
	try:
		if useclient==None:
			x=Client(server)
		else:
			x=useclient
		y=x.registernewplayer()
		builder=Builder(x)
		castleid=y['data']['player']['castles'][0]['id']
		quest=Quest(x,castleid)
		items=Item(x,castleid)
		items.useitem('player.box.present.2')
		x.client.sendmessage('common.addToFavorites',{})
		res=x.responsehandler('common.addToFavorites')
		builder.createbuilding(castleid,0,1)
		quest.completequest(1)
		quest.completequest(226)
		quest.completequest(535)
		builder.createbuilding(castleid,1,23)
		time.sleep(.5)
		builder.speedup(castleid,'consume.2.a',1)
		while True:
			res=x.responsehandler('server.BuildComplate',checkok=False)
			if res['data']['buildingBean']['endTime']==0.0:
				break
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
		for p in result:
			print("BADITEM"+p['id'])
			if p['id']=='player.box.gambling.medal.10':
				if (str(p['count'])+'cents') not in itemsarray:
					continue
			elif p['id'] not in itemsarray:
				continue
			if alreadyreg:
				print("GOODITEM"+p['id'])
				continue
			email=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
			pwd='aaaaaa'
			pwd=(hashlib.sha1(pwd).hexdigest())+'='+(hashlib.md5(pwd).hexdigest())
			email=email+'@gmail.com'
			data={'account':email,'password':pwd}
			x.client.sendmessage('common.saveUnregisteredPlayer',data)
			x.responsehandler('common.saveUnregisteredPlayer')
			print("GOODITEM"+email)
			if p['id']=='player.box.gambling.medal.10':
				print("GOODITEM"+(str(p['count'])+'cents'))
			else:
				print("GOODITEM"+p['id'])
			alreadyreg=True
			g=open('emaillog.txt','a')
			g.write(email)
			g.write('\n')
			g.close()
		return x
	except:
		try:
			x.close()
		except:
			pass
		print("ERRORREPORT")
		return None
yo=createacc(server)
while True:
	if yo==None:
		break
	yo.registered=False
	yo=createacc(server,useclient=yo)