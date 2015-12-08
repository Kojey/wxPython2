import wx

class Example(wx.Frame):
    def __init__(self, *a, **b):
        super(Example, self).__init__(*a, **b)
        self.initUI()

    def initUI(self):
        self.count = 5
        self.toolbar = self.CreateToolBar()
        tundo = self.toolbar.AddLabelTool(wx.ID_UNDO, 'Undo', wx.Bitmap('tundo.png'))
        tredo = self.toolbar.AddLabelTool(wx.ID_REDO, 'Redo', wx.Bitmap('tredo.png'))
        self.toolbar.EnableTool(wx.ID_REDO, False)# Disable redo
        self.toolbar.AddSeparator()
        qtool = self.toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))

        self.Bind(wx.EVT_TOOL, self.OnRedo, tredo)
        self.Bind(wx.EVT_TOOL, self.OnUndo, tundo)
        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)
        self.toolbar.Realize()
        self.SetSize((250, 200))
        self.SetTitle('Undo Redo')
        self.Centre()
        self.Show(True)

    def OnUndo(self, event):
        if self.count in range(2,6):
            self.count-=1
        if self.count==1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)
        if self.count==4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, event):
        if self.count in range(1,5):
            self.count+=1
        if self.count==5:
            self.toolbar.EnableTool(wx.ID_REDO, False)
        if self.count==2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)

    def OnQuit(self, event):
        self.Close()

def main():
    ex=wx.App()
    Example(None)
    ex.MainLoop()

if __name__=='__main__':
    main()