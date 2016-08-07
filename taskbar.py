import wx
import  time

'''global stop
stop = 0

class BibTaskBarIcon(wx.TaskBarIcon):
	def __init__(self, frame):
		wx.TaskBarIcon.__init__(self)
		self.frame = frame
		self.icon = wx.Icon('./sources/pitaya01.png', wx.BITMAP_TYPE_ANY)
		#https://icons8.com/web-app/for/all/pitaya
		self.SetIcon(self.icon, "title")
		self.OnMsg()

	def CreatePopupMenu(self):
		self.menu = wx.Menu()
		self.menu.Append(wx.NewId(), "resitore ")
		self.menu.Append(wx.NewId(), "minisize")
		self.menu.Append(wx.NewId(), "exit")
		return self.menu

	def OnMsg(self):
		while 1:
			if stop:
				self.SetIcon(self.icon, "title")
				break
			self.icon1 = wx.Icon('./sources/pitaya02.png', wx.BITMAP_TYPE_ANY)
			self.SetIcon(self.icon1, "title")
			time.sleep(1)
			self.SetIcon(self.icon, "title")


class TaskBarFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, style=wx.FRAME_NO_TASKBAR)
		self.tbicon = BibTaskBarIcon(self)
		wx.EVT_TASKBAR_RIGHT_DOWN(self.tbicon, self.OnTaskBarLeftClick)
		wx.EVT_TASKBAR_LEFT_DCLICK(self.tbicon,self.OnShowChatFrame)


	def OnTaskBarLeftClick(self, evt):
		self.tbicon.PopupMenu(self.tbicon.CreatePopupMenu())
	def OnShowChatFrame(self,evt):
		global stop
		stop = 1
		MainWindow.Show(True)
'''
ID_ICON_TIMER = wx.NewId()

class TaskBarFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.FRAME_NO_TASKBAR | wx.NO_FULL_REPAINT_ON_RESIZE)
        self.icon_state = False
        self.blink_state = False

        self.tbicon = wx.TaskBarIcon()
        icon = wx.Icon('./sources/pitaya01.png', wx.BITMAP_TYPE_ANY)
        self.tbicon.SetIcon(icon, '')
        wx.EVT_TASKBAR_LEFT_DCLICK(self.tbicon, self.OnTaskBarLeftDClick)
        wx.EVT_TASKBAR_RIGHT_UP(self.tbicon, self.OnTaskBarRightClick)
        self.Show(True)

    def OnTaskBarLeftDClick(self, evt):
        try:
            self.icontimer.Stop()
        except:
            pass
         if self.icon_state:
            icon = wx.Icon('./sources/pitaya01.png', wx.BITMAP_TYPE_ANY)
            self.tbicon.SetIcon(icon, 'Yellow')
            self.icon_state = False
        else:
            self.SetIconTimer()
            self.icon_state = True

    def OnTaskBarRightClick(self, evt):
        self.Close(True)
        wx.GetApp().ProcessIdle()

    def SetIconTimer(self):
        self.icontimer = wx.Timer(self, ID_ICON_TIMER)
        wx.EVT_TIMER(self, ID_ICON_TIMER, self.BlinkIcon)
        self.icontimer.Start(1000)

    def BlinkIcon(self, evt):
        if not self.blink_state:
            icon = wx.Icon('./sources/pitaya02.png', wx.BITMAP_TYPE_ANY)
            self.tbicon.SetIcon(icon, 'Red')
            self.blink_state = True
        else:
            icon = wx.Icon('./sources/pitaya05.png', wx.BITMAP_TYPE_ANY)
            self.tbicon.SetIcon(icon, 'Black')
            self.blink_state = False


app = wx.App(False)
frame = TaskBarFrame(None)
frame.Show(False)
app.MainLoop()

def main(argv=None):
	global MainWindow
	app = wx.App(False)
	MainWindow = TaskBarFrame(None, "testing frame")
	#MainWindow.Show(True)
	app.MainLoop()

if __name__ == "__main__":
	main()
