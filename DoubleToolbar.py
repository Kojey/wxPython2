import wx


class Example (wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        toolbar = wx.ToolBar(self)
        toolbar1 = wx.ToolBar(self)
        toolbar.AddLabelTool(wx.ID_NEW, 'New', wx.Bitmap('tnew.png'))
        toolbar.AddLabelTool(wx.ID_OPEN, 'Open', wx.Bitmap('topen.png'))
        toolbar.AddLabelTool(wx.ID_SAVE, 'Save', wx.Bitmap('tsave.png'))
        qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))
        toolbar1.AddLabelTool(wx.ID_UNDO,'Undo', wx.Bitmap('tundo.png'))
        toolbar1.AddLabelTool(wx.ID_REDO, 'Redo', wx.Bitmap('tredo.png'))

        toolbar.Realize()
        toolbar1.Realize()

        sizer.Add(toolbar, 0, wx.EXPAND)
        sizer.Add(toolbar1, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)
        self.SetSizer(sizer)

        self.SetTitle('Simple toolbar')
        self.SetSize((300,250))
        self.Centre()
        self.Show()

    def OnQuit(self, event):
        self.Close()

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__=='__main__':
    main()