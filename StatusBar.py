import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5,2)
        but = wx.Button(panel, label='Button')
        cbox = wx.ComboBox(panel)
        ckbox = wx.CheckBox(panel, label='CheckBox')
        ckbox.SetValue(False)
        self.gauge = wx.Gauge(panel, range=50, size=(120,10))
        rbut1 = wx.RadioButton(panel, label='one')
        rbut2 = wx.RadioButton(panel, label='two')
        self.slide = wx.Slider(panel, value=20, minValue=0, maxValue=50, size=(250,-1), style=wx.SL_HORIZONTAL )
        self.gauge.SetValue(self.slide.GetValue())
        self.spin = wx.SpinCtrl(panel, value='0', size=(50,-1))
        self.spin.SetRange(0,50)

        sizer.Add(but,pos=(0,0),flag=wx.TOP|wx.ALL, border=10)
        sizer.Add(cbox,pos=(0,1),flag=wx.TOP|wx.ALL, border=10)
        sizer.Add(ckbox,pos=(1,0),flag=wx.TOP|wx.ALL, border=10)
        sizer.Add(self.gauge,pos=(1,1),flag=wx.TOP|wx.ALL, border=10)
        sizer.Add(rbut1,pos=(2,0),flag=wx.TOP|wx.ALL, border=10)
        sizer.Add(rbut2,pos=(2,1),flag=wx.TOP|wx.ALL, border=10)
        sizer.Add(self.slide,pos=(3,0),span=(1,2),flag=wx.ALL, border=10)
        sizer.Add(self.spin, pos=(4,0),span=(1,2), flag=wx.ALIGN_CENTER|wx.ALL, border=10)

        panel.SetSizer(sizer)
        self.statusBar = self.CreateStatusBar()
        self.Bind(wx.EVT_BUTTON, self.OnClick, but)
        self.Bind(wx.EVT_SCROLL, self.OnScroll, self.slide)
        self.Bind(wx.EVT_BUTTON, self.OnSpin, self.spin)
        self.SetSize((300,340))
        self.SetTitle('Exmaple')
        self.Centre()
        self.Show()
    def OnSpin(self, event):
        self.gauge.SetValue(self.spin.GetValue())
    def OnClick(self, event):
        self.gauge.SetValue(self.spin.GetValue())
        self.slide.SetValue(self.spin.GetValue())
        self.statusBar.SetStatusText('value changed to '+str(self.gauge.GetValue()))
        event.Skip()
    def OnScroll(self, event):
        value= self.slide.GetValue()
        self.gauge.SetValue(value)
        self.spin.SetValue(value)
def main():
    ex=wx.App()
    Example(None)
    ex.MainLoop()

if __name__=='__main__':
    main()