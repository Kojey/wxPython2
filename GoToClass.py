import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=((390, 350)))
        self.initUI()
        self.Centre()
        self.Show()

    def initUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Class Name')
        tx1 = wx.TextCtrl(panel)
        sbox1.Add(st1,flag=wx.RIGHT,border=8)
        sbox1.Add(tx1,1)

        sbox2 = wx.BoxSizer(wx.VERTICAL)
        tx2 = wx.StaticText(panel,label='Matching Classes')
        txtCtrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        sbox2.Add(tx2)
        sbox2.Add(txtCtrl, 1, wx.EXPAND)
    
        sbox3 = wx.BoxSizer(wx.HORIZONTAL)
        chk1 = wx.CheckBox(panel, label='Case Sensitive')
        chk2 = wx.CheckBox(panel, label='Nested Classes')
        chk3 = wx.CheckBox(panel, label='Non-Project')
        sbox3.Add(chk1)
        sbox3.Add(chk2)
        sbox3.Add(chk3)

        sbox4 = wx.BoxSizer(wx.HORIZONTAL)
        but1 = wx.Button(panel, label='Ok')
        but2 = wx.Button(panel, label='Close')
        sbox4.Add(but1)
        sbox4.Add(but2)

        vbox.Add(sbox1,0,flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=8)
        vbox.Add(sbox2,1,flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, border=8)
        vbox.Add(sbox3,0,flag=wx.ALIGN_CENTER)
        vbox.Add(sbox4,0,flag=wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.RIGHT, border=8)

        panel.SetSizer(vbox)


def main():
    ex=wx.App()
    Example(None, 'Go To Class')
    ex.MainLoop()

if __name__=='__main__':
    main()