import  wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        subMenu = wx.Menu()
        viewMenu = wx.Menu()

        # add item to fileMenu
        fileMenu.Append(wx.ID_NEW, '&New\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Open\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Save\tCtrl+S')
        fileMenu.AppendSeparator()

        # add item to viewMenu
        self.view1 = viewMenu.Append(wx.ID_ANY, 'Show statusbar', 'Display statusbar', kind=wx.ITEM_CHECK)
        self.view2 = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 'Display toolbar', kind=wx.ITEM_CHECK)

        viewMenu.Check(self.view1.GetId(), True)
        viewMenu.Check(self.view2.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToogleStatusbar, self.view1)
        self.Bind(wx.EVT_MENU, self.ToogleToolbar, self.view2)

        # add item to subMenu
        subMenu.Append(wx.ID_ANY, 'Import newfeed list...')
        subMenu.Append(wx.ID_ANY, 'Import bookmarks...')
        subMenu.Append(wx.ID_ANY, 'Import mail...')
        qut = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')

        # add subMenu to fileMenu
        fileMenu.AppendMenu(wx.ID_ANY, '&Import', subMenu)
        fileMenu.AppendItem(qut)

        self.Bind(wx.EVT_MENU, self.OnQuit, qut)

        menuBar.Append(fileMenu, '&File')
        menuBar.Append(viewMenu, '&View')

        self.SetMenuBar(menuBar)

        self.toolBar = self.CreateToolBar()
        self.toolBar.AddLabelTool(1, '', wx.Bitmap('texit.png'))
        self.toolBar.Realize()

        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetStatusText('Ready')

        self.SetTitle('Submenu')
        self.SetSize((350, 250))
        self.Center()
        self.Show()

    def OnQuit(self, event):
        self.Close()

    def ToogleStatusbar(self,event):
        if self.view1.IsChecked():
            self.statusBar.Show()
        else:
            self.statusBar.Hide()

    def ToogleToolbar(self,event):
        if self.view2.IsChecked():
            self.toolBar.Show()
        else:
            self.toolBar.Hide()


def main():
    a=wx.App()
    Example(None)
    a.MainLoop()

if __name__ == '__main__':
    main()