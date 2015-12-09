import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(450,350))
        self.initUI()
        self.Centre()
        self.Show()

    def initUI(self):
        panel = wx.Panel(self)
        frameSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer = wx.GridBagSizer(5,5)

        txt1 = wx.StaticText(panel, label='Java Class')
        img1 = wx.StaticBitmap(panel,bitmap=wx.Bitmap('icon/settings.png'))
        mainSizer.Add(txt1,pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=15)
        mainSizer.Add(img1,pos=(0,4),flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT, border=5)
        mainSizer.Add(wx.StaticLine(panel),pos=(1,0),span=(1,5),flag=wx.EXPAND|wx.BOTTOM, border=10)

        tx1 = wx.StaticText(panel, label='Name')
        tx2 = wx.StaticText(panel, label='Package')
        tx3 = wx.StaticText(panel, label='Extends')
        txCtrl1 = wx.TextCtrl(panel)
        txCtrl2 = wx.TextCtrl(panel)
        txCtrl3 = wx.ComboBox(panel)
        but1 = wx.Button(panel, label='Browse...')
        but2 = wx.Button(panel, label='Browse...')
        mainSizer.Add(tx1,pos=(2,0), flag=wx.LEFT, border=10)
        mainSizer.Add(tx2,pos=(3,0), flag=wx.LEFT|wx.TOP, border=10)
        mainSizer.Add(tx3,pos=(4,0), flag=wx.LEFT|wx.TOP, border=10)
        mainSizer.Add(txCtrl1,pos=(2,1),span=(1,3),flag=wx.EXPAND|wx.BOTTOM, border=5)
        mainSizer.Add(txCtrl2,pos=(3,1),span=(1,3),flag=wx.EXPAND|wx.BOTTOM, border=5)
        mainSizer.Add(txCtrl3,pos=(4,1),span=(1,3),flag=wx.EXPAND|wx.BOTTOM, border=5)
        mainSizer.Add(but1,pos=(3,4),flag=wx.BOTTOM|wx.RIGHT, border=5)
        mainSizer.Add(but2,pos=(4,4),flag=wx.BOTTOM|wx.RIGHT, border=5)

        staticBox = wx.StaticBox(panel, label='Optional Attributes')
        staticBoxSizer = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        staticBoxSizer.Add(wx.CheckBox(panel, label='Public'))
        staticBoxSizer.Add(wx.CheckBox(panel, label='Generate Default Constructor'))
        staticBoxSizer.Add(wx.CheckBox(panel, label='Generate Main Methods'))
        mainSizer.Add(staticBoxSizer,pos=(5,0),span=(1,5),flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        butt1 = wx.Button(panel,label='Help')
        butt2 = wx.Button(panel,label='Ok')
        butt3 = wx.Button(panel,label='Cancel')
        mainSizer.Add(butt1, pos=(7,0),flag=wx.BOTTOM|wx.LEFT, border=10)
        mainSizer.Add(butt2, pos=(7,3))
        mainSizer.Add(butt3, pos=(7,4),flag=wx.BOTTOM|wx.RIGHT, border=10)

        mainSizer.AddGrowableCol(2)
        panel.SetSizer(mainSizer)


def main():
    ex=wx.App()
    Example(None, title='Create a Java Class')
    ex.MainLoop()

if __name__=='__main__':
    main()