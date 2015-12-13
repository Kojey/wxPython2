import wx
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin


packages = [('abiword', '5.8M', 'base'), ('adie', '145k', 'base'),
    ('airsnort', '71k', 'base'), ('ara', '717k', 'base'), ('arc', '139k', 'base'),
    ('asc', '5.8M', 'base'), ('ascii', '74k', 'base'), ('ash', '74k', 'base')]


class CheckListBox(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)


class Repository(wx.Frame):
    def __init__(self,parent):
        super(Repository,self).__init__(parent)
        self.initUI()

    def initUI(self):
        panel = wx.Panel(self)
        leftPanel = wx.Panel(panel)
        rightPanel = wx.Panel(panel)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        leftSizer = wx.BoxSizer(wx.VERTICAL)
        rightSizer = wx.BoxSizer(wx.VERTICAL)
        hSizer.Add(leftPanel,1,wx.ALL,5)
        hSizer.Add(rightPanel,2,wx.ALL,5)
        panel.SetSizer(hSizer)

        selBut = wx.Button(leftPanel, label='Select All')
        desBut = wx.Button(leftPanel, label='Deselect All')
        appBut = wx.Button(leftPanel, label='Apply')

        leftSizer.Add(selBut)
        leftSizer.Add(desBut)
        leftSizer.Add(appBut)
        leftPanel.SetSizer(leftSizer)
       # """
        self.list = CheckListBox(rightPanel)
        self.list.InsertColumn(0, 'Package', width=140)
        self.list.InsertColumn(1, 'Size')
        self.list.InsertColumn(2, 'Repository')

        for i in packages:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])
        #"""
        self.txtCtrl = wx.TextCtrl(rightPanel, style=wx.TE_MULTILINE)

        rightSizer.Add(self.list)
        rightSizer.Add(self.txtCtrl,0,wx.EXPAND|wx.TOP,5)
        rightPanel.SetSizer(rightSizer)

        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, selBut)
        self.Bind(wx.EVT_BUTTON, self.OnDeselectAll, desBut)
        self.Bind(wx.EVT_BUTTON, self.OnApply, appBut)

        self.SetTitle('Repository')
        self.SetSize((400, 250))
        self.Centre()
        self.Show()

    def OnSelectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i)

    def OnDeselectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i, False)
    def OnApply(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            if self.list.IsChecked(i):
                self.txtCtrl.AppendText(self.list.GetItemText(i))



def main():
    re = wx.App()
    Repository(None)
    re.MainLoop()

if __name__=='__main__':
    main()