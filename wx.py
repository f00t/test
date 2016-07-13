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
        self.MainSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.MainSizer)
        self.Layout()
        self.Fit()
        self.SetMinSize(wx.Size(900, 500))
        self.CreatMenuBar()
        self.SetBotList()
        self.SetPopup()

    def SetBotList(self):
        self.BotList = MyListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                   wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        #self.BotList.SetMinSize(wx.Size(900, 400))
        self.BotList.SetAutoLayout(True)
        for index,text in enumerate(Header):
            self.BotList.InsertColumn(index, text, format=wx.LIST_FORMAT_CENTRE, width=-1)
        for index,text in enumerate(botlist):
            row = self.BotList.InsertStringItem(index, label = "")
            bot = text.split(":")
            self.BotList.SetStringItem(row, 0, bot[0])
            self.BotList.SetStringItem(row, 1, bot[1])
            self.BotList.SetStringItem(row, 2, bot[2])
            self.BotList.SetStringItem(row, 3, bot[3])
            self.BotList.SetStringItem(row, 4, bot[4])
        # set the width of the columns in various ways
        self.BotList.SetColumnWidth(0, 190)
        self.BotList.SetColumnWidth(1, 180)
        self.BotList.SetColumnWidth(2, 170)
        self.BotList.SetColumnWidth(3, 170)
        self.BotList.SetColumnWidth(4, 170)
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
        self.MainSizer.Add(self.BotList,1,wx.ALL|wx.EXPAND,0)
    # self.Bind(wx.EVT_LIST_COL_RIGHT_CLICK,self.OnShowPopup)

    def SetPopup(self):
        self.popupmenu = wx.Menu()
        for text in [u"CMD", u"Download", u"Upload", u"Kill", u"File manager"]:
            item = self.popupmenu.Append(-1, text)
            self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)

    def OnShowPopup(self, event):
        pos = event.GetPosition()
        pos = self.ScreenToClient(pos)
        self.PopupMenu(self.popupmenu, pos)

    def OnPopupItemSelected(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        text = item.GetText()
        if text == "CMD":
            Cmd = wx.Frame(self, id=-1, title="CMD", pos=wx.DefaultPosition, size=(600, 400),
                           style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
            Cmd.Show(True)
            Cmd.SetMinSize(wx.Size(600, 400))
            multiText = wx.TextCtrl(Cmd, -1, "", pos=wx.DefaultPosition, size=(580, 380), style=wx.TE_MULTILINE)
            multiText.SetMinSize(wx.Size(580, 380))
            multiText.SetForegroundColour(wx.Colour(255, 255, 255))
            multiText.SetBackgroundColour(wx.Colour(0, 0, 0))

        if text == "Download":
            DownloadFrame = wx.Frame(self, id=-1, title="Download File", pos=wx.DefaultPosition, size=(600, 400),
                                     style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
            DownloadFrame.Show(True)

        if text == "Upload":
            UploadFrame = wx.Frame(self, id=-1, title="Upload File", pos=wx.DefaultPosition, size=(600, 400),
                                   style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
            UploadFrame.Show(True)
            StackText = wx.StaticText(UploadFrame, wx.ID_ANY, u"LocalPath", wx.DefaultPosition, wx.DefaultSize, 0)
            StackText.Wrap(-1)
            DirCtrl = wx.GenericDirCtrl(UploadFrame, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.DIRCTRL_3D_INTERNAL | wx.SUNKEN_BORDER, wx.EmptyString, 0)
            DirCtrl.ShowHidden(False)
            # wx.MessageBox("You selected item %s" % text)

    def CreatMenuBar(self):
        self.StatusBar = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.StatusBar.SetFieldsCount(2)
        self.StatusBar.SetStatusText("Server: %s:%s" % (Server,str(port)),0)
        self.StatusBar.SetStatusText("BotNumbers: %s" % botnums, 1)
        self.MyMenuBar = wx.MenuBar(0)

        self.FileMenu = wx.Menu()
        self.ServerItem = wx.MenuItem(self.FileMenu, wx.ID_ANY, u"Server", wx.EmptyString, wx.ITEM_NORMAL)
        self.FileMenu.AppendItem(self.ServerItem)
        self.ExitMenuItem = wx.MenuItem(self.FileMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.FileMenu.AppendItem(self.ExitMenuItem)
        self.MyMenuBar.Append(self.FileMenu, u" Start")

        self.OptionMenu = wx.Menu()
        self.BuildClientItem = wx.MenuItem(self.OptionMenu, wx.ID_ANY, u"Build client", wx.EmptyString, wx.ITEM_NORMAL)
        self.OptionMenu.AppendItem(self.BuildClientItem)
        self.MyMenuBar.Append(self.OptionMenu, u"Options")

        self.HelpMenu = wx.Menu()
        self.AboutMenuItem = wx.MenuItem(self.HelpMenu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL)
        self.HelpMenu.AppendItem(self.AboutMenuItem)
        self.MyMenuBar.Append(self.HelpMenu, u"Help")

        self.SetMenuBar(self.MyMenuBar)

        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_MENU, self.OnExit, self.ExitMenuItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.AboutMenuItem)
        self.Bind(wx.EVT_MENU, self.OnBuildClient, self.BuildClientItem)
        self.Bind(wx.EVT_MENU, self.OnServer, self.ServerItem)

    def OnExit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox(u"Powered by xxx\n2016/07/15")
    def OnServer(self,event):
        ServerFrame = wx.Frame(self,id=wx.ID_ANY, title="Server Option", pos=wx.DefaultPosition,
                          size=wx.Size(432, 252), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        ServerFrame.Show(True)
        panel = wx.Panel(ServerFrame)
        #panel.SetMaxSize(500, 400)
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
        self.Centre()

        panel.Fit()

    def OnBuildClient(self, event):
            BuildFrame = wx.Frame(self)
            BuildFrame.Show(True)

    def __del__(self):
        pass


app = wx.App(False)
MainWindow = MainFrame(None, u"PassRatServer")
MainWindow.Show(True)
app.MainLoop()
