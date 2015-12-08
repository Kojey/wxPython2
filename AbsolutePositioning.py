
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(260, 180))
        self.initUI()
        self.Centre()
        self.Show()

    def initUI(self):
        menubar = wx.MenuBar()
        filem=wx.Menu()
        editm=wx.Menu()
        helpm=wx.Menu()

        menubar.Append(filem, '&File')
        menubar.Append(editm, '&Edit')
        menubar.Append(helpm, '&Help')

        self.SetMenuBar(menubar)
        wx.TextCtrl(self)

def main():
    ex=wx.App()
    Example(None, title='Absolute positioning')
    ex.MainLoop()

if __name__=='__main__':
    main()