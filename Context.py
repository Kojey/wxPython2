import wx


class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()
        self.parent=parent

        minimize = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.AppendItem(minimize)
        self.Bind(wx.EVT_MENU, self.OnMinimize, minimize)

        close = wx.MenuItem(self, wx.NewId(), 'Close')
        self.AppendItem(close)
        self.Bind(wx.EVT_MENU, self.OnClose, close)

    def OnMinimize(self, event):
        self.parent.Iconize()

    def OnClose(self, event):
        self.parent.Close()


class Example (wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.SetSize((400,200))
        self.SetTitle('Content')
        self.Centre()
        self.Show(True)

    def OnRightDown(self,event):
        self.PopupMenu(MyPopupMenu(self), event.GetPosition())

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()