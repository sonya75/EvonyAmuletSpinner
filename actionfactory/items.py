class Item:
	def __init__(self,city,castleid=None):
		self.city=city
		self.castleid=castleid
	def useitem(self,itemid,castleid=None,num=1):
		if castleid==None:
			castleid=self.castleid
		self.city.client.sendmessage('shop.useGoods',{'itemId':itemid,'castleId':castleid,'num':num})
		res=self.city.responsehandler('shop.useGoods')
		return res
	def buyitem(self,itemid,castleid=None):
		if castleid==None:
			castleid=self.castleid
		self.city.client.sendmessage('shop.buy',{'itemId':itemid,'amount':1})
		res=self.city.responsehandler('shop.buy')