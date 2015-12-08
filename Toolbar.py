import wx


class Example (wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
         toolbar = self.CreateToolBar()
         otool = toolbar.AddLabelTool(wx.ID_OPEN, 'Open', wx.Bitmap('topen.png'))
         stool = toolbar.AddLabelTool(wx.ID_SAVE, 'Save', wx.Bitmap('tsave.png'))
         qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))

         toolbar.Realize()

         self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

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