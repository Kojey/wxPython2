import wx


class MyWindow(wx.Panel):

    def __init__(self, parent):
        super(MyWindow, self).__init__(parent)
        self.color = '#b3b3b3'
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)

    def OnSize(self, event):
        self.Refresh()

    def OnSetFocus(self, event):
        self.color = '#0099f7'
        self.Refresh()

    def OnKillFocus(self, event):
        self.color = '#b3b3b3'
        self.Refresh()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([
            (MyWindow(self),0,wx.EXPAND|wx.TOP|wx.LEFT,9),
            (MyWindow(self),0,wx.EXPAND|wx.TOP|wx.RIGHT,9),
            (MyWindow(self),0,wx.EXPAND|wx.BOTTOM|wx.LEFT,9),
            (MyWindow(self),0,wx.EXPAND|wx.BOTTOM|wx.RIGHT,9)
        ])

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

        self.SetSizer(grid)
        self.SetSize((350,250))
        self.SetTitle('Focus Event')
        self.Centre()
        self.Show()

    def OnKeyDown(self, event):
        key=event.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox('Are you sure to quit', 'Question', wx.YES_NO|wx.NO_DEFAULT, self)
            if ret == wx.YES:
                self.Close()

    def OnMove(self, event):
        print event.GetEventObject()
        x, y = event.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))

def main():
    ex=wx.App()
    Example(None)
    ex.MainLoop()

if __name__=='__main__':
    main()