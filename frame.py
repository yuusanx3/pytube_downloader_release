# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.html
import wx.html2
import wx.xrc
import os
import urllib.request
from youtube_dl import Youtube

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PYTUBE ダウンローダー", pos = wx.DefaultPosition, size = wx.Size( 500,330 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 400,330 ), wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		b_sizer_all = wx.BoxSizer( wx.VERTICAL )

		b_sizer_1 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.statictext_1 = wx.StaticText( self, wx.ID_ANY, u"動画URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext_1.Wrap( -1 )

		bSizer8.Add( self.statictext_1, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


		bSizer6.Add( bSizer8, 1, 0, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"YouTubeを開く", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button7, 0, wx.ALIGN_RIGHT|wx.ALL, 3 )


		bSizer6.Add( bSizer7, 1, 0, 5 )


		b_sizer_1.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.textctrl_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,20 ), 0 )
		b_sizer_1.Add( self.textctrl_1, 0, wx.ALL|wx.EXPAND, 5 )

		self.statictext_2 = wx.StaticText( self, wx.ID_ANY, u"保存フォルダ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext_2.Wrap( -1 )

		b_sizer_1.Add( self.statictext_2, 0, wx.ALIGN_LEFT|wx.ALL, 5 )

		self.textctrl_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,20 ), 0 )
		b_sizer_1.Add( self.textctrl_2, 0, wx.ALL|wx.EXPAND, 5 )


		b_sizer_all.Add( b_sizer_1, 0, wx.ALL|wx.EXPAND, 5 )

		b_sizer_2 = wx.BoxSizer( wx.HORIZONTAL )

		s_b_sizer_1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"ダウンロード" ), wx.VERTICAL )

		self.button_1 = wx.Button( s_b_sizer_1.GetStaticBox(), wx.ID_ANY, u"動画＋音声", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_b_sizer_1.Add( self.button_1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.button_2 = wx.Button( s_b_sizer_1.GetStaticBox(), wx.ID_ANY, u"動画のみ", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_b_sizer_1.Add( self.button_2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.button_3 = wx.Button( s_b_sizer_1.GetStaticBox(), wx.ID_ANY, u"音声のみ", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_b_sizer_1.Add( self.button_3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		b_sizer_2.Add( s_b_sizer_1, 1, wx.ALL|wx.EXPAND, 5 )

		s_b_sizer_2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"形式を選択してダウンロード" ), wx.VERTICAL )

		combobox_1Choices = [ u"「ファイル情報取得」ボタンを押してください" ]
		self.combobox_1 = wx.ComboBox( s_b_sizer_2.GetStaticBox(), wx.ID_ANY, u"c", wx.DefaultPosition, wx.DefaultSize, combobox_1Choices, 0 )
		self.combobox_1.SetSelection( 0 )
		self.combobox_1.SetMinSize( wx.Size( 400,-1 ) )

		s_b_sizer_2.Add( self.combobox_1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		b_sizer_3 = wx.BoxSizer( wx.HORIZONTAL )

		self.button_4 = wx.Button( s_b_sizer_2.GetStaticBox(), wx.ID_ANY, u"ファイル情報取得", wx.DefaultPosition, wx.DefaultSize, 0 )
		b_sizer_3.Add( self.button_4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.button_5 = wx.Button( s_b_sizer_2.GetStaticBox(), wx.ID_ANY, u"ダウンロード", wx.DefaultPosition, wx.DefaultSize, 0 )
		b_sizer_3.Add( self.button_5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		s_b_sizer_2.Add( b_sizer_3, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		b_sizer_2.Add( s_b_sizer_2, 1, wx.ALL|wx.EXPAND, 5 )


		b_sizer_all.Add( b_sizer_2, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( b_sizer_all )
		self.Layout()
		self.statusbar_1 = self.CreateStatusBar( 1, wx.STB_DEFAULT_STYLE, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.open_youtube )
		self.button_1.Bind( wx.EVT_BUTTON, self.download_all )
		self.button_2.Bind( wx.EVT_BUTTON, self.download_video )
		self.button_3.Bind( wx.EVT_BUTTON, self.download_audio )
		self.button_4.Bind( wx.EVT_BUTTON, self.get_info )
		self.button_5.Bind( wx.EVT_BUTTON, self.download )

		self.myframe2 = MyFrame2(self)
		self.myframe2.Show()

	def __del__( self ):
		pass

	# Virtual event handlers, override them in your derived class
	def open_youtube( self, event ):
		try:
			self.myframe2.Enabled
		except RuntimeError:
			self.myframe2 = MyFrame2(self)
			self.myframe2.Show()

	def download_all( self, event ):
		if "" == self.textctrl_1.Value:
			self.SetStatusText("動画URLを入力してください。")
		elif "" == self.textctrl_2.Value:
			self.SetStatusText("保存フォルダを入力してください。")
		elif not CheckValue.url_check(self.textctrl_1.Value):
				self.SetStatusText("動画URLが間違っています。")
		elif not CheckValue.folder_check(self.textctrl_2.Value):
				self.SetStatusText("保存フォルダが間違っています。")
		else:
			self.SetStatusText("ダウンロードしています...")
			result = Youtube(self.textctrl_1.Value).download(self.textctrl_2.Value)
			if 0 == result["code"]:
				self.SetStatusText("ダウンロードしました。ファイル名=\"{}\"".format(result["file_path"]))
			elif 1 == result["code"]:
				self.SetStatusText(result["message"])

	def download_video( self, event ):
		if "" == self.textctrl_1.Value:
			self.SetStatusText("動画URLを入力してください。")
		elif "" == self.textctrl_2.Value:
			self.SetStatusText("保存フォルダを入力してください。")
		elif not CheckValue.url_check(self.textctrl_1.Value):
				self.SetStatusText("動画URLが間違っています。")
		elif not CheckValue.folder_check(self.textctrl_2.Value):
				self.SetStatusText("保存フォルダが間違っています。")
		else:
			self.SetStatusText("ダウンロードしています...")
			result = Youtube(self.textctrl_1.Value).download_video(self.textctrl_2.Value)
			if 0 == result["code"]:
				self.SetStatusText("ダウンロードしました。ファイル名=\"{}\"".format(result["file_path"]))
			elif 1 == result["code"]:
				self.SetStatusText(result["message"])

	def download_audio( self, event ):
		if "" == self.textctrl_1.Value:
			self.SetStatusText("動画URLを入力してください。")
		elif "" == self.textctrl_2.Value:
			self.SetStatusText("保存フォルダを入力してください。")
		elif not CheckValue.url_check(self.textctrl_1.Value):
				self.SetStatusText("動画URLが間違っています。")
		elif not CheckValue.folder_check(self.textctrl_2.Value):
				self.SetStatusText("保存フォルダが間違っています。")
		else:
			self.SetStatusText("ダウンロードしています...")
			result = Youtube(self.textctrl_1.Value).download_audio(self.textctrl_2.Value)
			if 0 == result["code"]:
				self.SetStatusText("ダウンロードしました。ファイル名=\"{}\"".format(result["file_path"]))
			elif 1 == result["code"]:
				self.SetStatusText(result["message"])

	def get_info( self, event ):
		if "" == self.textctrl_1.Value:
			self.SetStatusText("動画URLを入力してください。")
		elif not CheckValue.url_check(self.textctrl_1.Value):
				self.SetStatusText("動画URLが間違っています。")
		else:
			self.SetStatusText("検索しています...")
			result = Youtube(self.textctrl_1.Value).show_list()
			if 0 == result["code"]:
				self.SetStatusText("検索終了")
				self.combobox_1.Clear()
				self.combobox_1.AppendItems("形式を選択してください")
				for p in result["data"]:
					self.combobox_1.AppendItems("{} : {}".format(p["itag"],p["data"]))
				self.combobox_1.Select(0)
			elif 1 == result["code"]:
				self.SetStatusText(result["message"])

	def download( self, event ):
		if "" == self.textctrl_1.Value:
			self.SetStatusText("動画URLを入力してください。")
		elif "" == self.textctrl_2.Value:
			self.SetStatusText("保存フォルダを入力してください。")
		elif "「ファイル情報取得」ボタンを押してください" == self.combobox_1.Value or "形式を選択してください" == self.combobox_1.Value:
			self.SetStatusText("形式を選択してください。")
		elif not CheckValue.url_check(self.textctrl_1.Value):
				self.SetStatusText("動画URLが間違っています。")
		elif not CheckValue.folder_check(self.textctrl_2.Value):
				self.SetStatusText("保存フォルダが間違っています。")
		else:
			self.SetStatusText("ダウンロードしています...")
			result = Youtube(self.textctrl_1.Value).download_by_itag(self.combobox_1.Value.split(" : ")[0],self.textctrl_2.Value)
			if 0 == result["code"]:
				self.SetStatusText("ダウンロードしました。ファイル名=\"{}\"".format(result["file_path"]))
			elif 1 == result["code"]:
				self.SetStatusText(result["message"])

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"YouTube", pos = wx.Point( -1,-1 ), size = wx.Size( 900,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 400,330 ), wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.browser = wx.html2.WebView.New(self, backend=wx.html2.WebViewBackendEdge)
		bSizer5.Add(self.browser, 22, wx.EXPAND, 10)
		self.browser.LoadURL("https://www.youtube.com/")

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"戻る", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"進む", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"更新", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"ホーム", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button11, 0, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"URLを反映", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer10.Add( self.m_button6, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer9.Add( bSizer10, 1, 0, 5 )


		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.SetSizer( bSizer5 )
		self.Layout()

		self.Center( wx.BOTH )

		# Connect Events
		self.m_button8.Bind( wx.EVT_BUTTON, self.previous_page )
		self.m_button9.Bind( wx.EVT_BUTTON, self.next_page )
		self.m_button10.Bind( wx.EVT_BUTTON, self.refresh_page )
		self.m_button11.Bind( wx.EVT_BUTTON, self.go_home )
		self.m_button6.Bind( wx.EVT_BUTTON, self.reflect_url )

	def __del__( self ):
		pass

	# Virtual event handlers, override them in your derived class
	def previous_page( self, event ):
		if self.browser.CanGoBack():
			self.browser.GoBack()

	def next_page( self, event ):
		if self.browser.CanGoForward():
			self.browser.GoForward()

	def refresh_page( self, event ):
		self.browser.Reload()

	def go_home( self, event ):
		self.browser.LoadURL("https://www.youtube.com/")

	def reflect_url( self, event ):
		url = self.browser.GetCurrentURL()
		self.Parent.textctrl_1.SetValue(url)

class CheckValue:
	def url_check(url):
		flag = True
		if "https://www.youtube.com/watch?v=" in url:
			try:
				f = urllib.request.urlopen(url)
				f.close()
			except urllib.request.HTTPError:
				flag = False
		else:
			flag = False
		return flag

	def folder_check(folder_path):
		return os.path.exists(folder_path)