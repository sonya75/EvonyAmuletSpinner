# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 359,429 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		self.bSizer1=bSizer1
		self.m_checklist=None
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,583 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Choose Items", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Spin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Proxy-Manager", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Use Proxybroker", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Maximum number of proxies to be used", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer51.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_textCtrl41, 0, wx.ALL, 0 )
		
		
		bSizer3.Add( bSizer51, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Maximum number of proxies to be checked simultaneously", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl6, 0, wx.ALL, 0 )
		
		
		bSizer3.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer07 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText06 = wx.StaticText( self, wx.ID_ANY, u"Maximum number of connections per proxy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText06.Wrap( -1 )
		bSizer07.Add( self.m_staticText06, 0, wx.ALL, 5 )
		
		self.m_textCtrl06 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer07.Add( self.m_textCtrl06, 0, wx.ALL, 0 )
		
		
		bSizer3.Add( bSizer07, 0, wx.EXPAND, 5 )

		bSizer900 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText600 = wx.StaticText( self, wx.ID_ANY, u"Timeout(in seconds)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText600.Wrap( -1 )
		bSizer900.Add( self.m_staticText600, 0, wx.ALL, 5 )
		
		self.m_textCtrl600 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer900.Add( self.m_textCtrl600, 0, wx.ALL, 0 )
		
		
		bSizer3.Add( bSizer900, 0, wx.EXPAND, 5 )


		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"All Items", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText2.Wrap( -1 )
		bSizer5.Add( self.m_staticText2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Good Items and emails", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText3.Wrap( -1 )
		bSizer5.Add( self.m_staticText3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer4.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer4.Add( self.m_textCtrl5, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

