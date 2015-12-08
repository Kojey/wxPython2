import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example,self).__init__(parent, title=title,size=(300,400))
        self.initUI()
        self.Centre()
        self.Show()

    def initUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')

        txtCtrl = wx.TextCtrl(self, style=wx.TE_RIGHT)
        grid = wx.GridSizer(5, 4, 5, 5)
        gridLabel = ['Cls','Bck','','Close','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']

        for e in gridLabel:
            if e!='':
                grid.Add(wx.Button(self, label=e), 0, wx.EXPAND)
            else:
                grid.Add(wx.StaticText(self), wx.EXPAND)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(txtCtrl,0,wx.EXPAND)
        vbox.Add(grid,1,wx.EXPAND)

        self.SetMenuBar(menubar)
        self.SetSizer(vbox)

def main():
    ex=wx.App()
    Example(None, 'Calculator')
    ex.MainLoop()

if __name__=='__main__':
    main()