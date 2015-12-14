from ftplib import FTP, all_errors
import wx


class MyStatusBar(wx.StatusBar):

    def __init__(self, parent):
        super(MyStatusBar, self).__init__(parent)

        self.SetFieldsCount(2)
        self.SetStatusText('Welcome to Kika', 0)
        self.SetStatusWidths([-1, 50])

        self.icon = wx.StaticBitmap(self, bitmap=wx.Bitmap('disconnected.png'))
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.PlaceIcon()

    def PlaceIcon(self):

        rect = self.GetFieldRect(1)
        self.icon.SetPosition((rect.x+5, rect.y+1))

    def OnSize(self, e):

        e.Skip()
        self.PlaceIcon()


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        wx.StaticText(self, label='Ftp site', pos=(10, 20))
        wx.StaticText(self, label='Login', pos=(10, 60))
        wx.StaticText(self, label='Password', pos=(10, 100))

        self.ftpsite = wx.TextCtrl(self, pos=(110, 15),
            size=(120, -1))
        self.login = wx.TextCtrl(self,  pos=(110, 55),
            size=(120, -1))
        self.password = wx.TextCtrl(self, pos=(110, 95),
            size=(120, -1), style=wx.TE_PASSWORD)

        self.ftp = None

        con = wx.Button(self, label='Connect', pos=(10, 160))
        discon = wx.Button(self, label='DisConnect', pos=(120, 160))

        self.Bind(wx.EVT_BUTTON, self.OnConnect, con)
        self.Bind(wx.EVT_BUTTON, self.OnDisConnect, discon)
        self.Bind(wx.EVT_MAXIMIZE, self.OnMaximize)
        self.Bind(wx.EVT_SHOW, self.OnShown)

        self.sb = MyStatusBar(self)
        self.SetStatusBar(self.sb)

        self.SetSize((250, 270))
        self.SetTitle('Kika')
        self.Centre()
        self.Show()


    def OnShown(self, e):

        if self.sb:
            self.sb.PlaceIcon()

    def OnMaximize(self, e):

        self.sb.PlaceIcon()

    def OnConnect(self, e):

        if not self.ftp:

            ftpsite = self.ftpsite.GetValue()
            login = self.login.GetValue()
            password = self.password.GetValue()

            try:
                self.ftp = FTP(ftpsite)
                var = self.ftp.login(login, password)

                self.sb.SetStatusText('User connected')
                self.sb.icon.SetBitmap(wx.Bitmap('connected.png'))

            except AttributeError:

                self.sb.SetStatusText('Incorrect params')
                self.ftp = None

            except all_errors, err:

                self.sb.SetStatusText(str(err))
                self.ftp = None

    def OnDisConnect(self, e):

        if self.ftp:

            self.ftp.quit()
            self.ftp = None

            self.sb.SetStatusText('User disconnected')
            self.sb.icon.SetBitmap(wx.Bitmap('disconnected.png'))


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()   