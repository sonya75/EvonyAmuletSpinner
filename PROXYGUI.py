# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,446 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_dataViewListCtrl4 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn10 = self.m_dataViewListCtrl4.AppendTextColumn( u"Proxy Server" ,width=170,align= wx.ALIGN_CENTER,flags=wx.dataview.DATAVIEW_COL_SORTABLE|wx.dataview.DATAVIEW_COL_RESIZABLE)
		self.m_dataViewListColumn11 = self.m_dataViewListCtrl4.AppendTextColumn( u"Status" ,width=100,align=wx.ALIGN_CENTER,flags=wx.dataview.DATAVIEW_COL_SORTABLE|wx.dataview.DATAVIEW_COL_RESIZABLE)
		self.m_dataViewListColumn12 = self.m_dataViewListCtrl4.AppendTextColumn( u"Usage" ,width=100,align=wx.ALIGN_CENTER,flags=wx.dataview.DATAVIEW_COL_SORTABLE|wx.dataview.DATAVIEW_COL_RESIZABLE)
		self.m_dataViewListColumn13 = self.m_dataViewListCtrl4.AppendTextColumn( u"Action",width=225,align=wx.ALIGN_CENTER ,flags=wx.dataview.DATAVIEW_COL_SORTABLE|wx.dataview.DATAVIEW_COL_RESIZABLE)
		bSizer1.Add( self.m_dataViewListCtrl4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.m_textCtrl23, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_filePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		bSizer9.Add( self.m_filePicker2, 1, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Load Proxies", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 369,413 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  wx.TE_MULTILINE|wx.TE_RICH|wx.TE_RICH2)
		bSizer8.Add( self.m_textCtrl6, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	