import wx
import wx.lib.gestures as gest

class MyMouseGestures(wx.Frame):

    def __init__ (self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 200))

        panel = wx.Panel(self, -1)
        mg = gest.MouseGestures(panel, True, wx.MOUSE_BTN_LEFT)
        mg.SetGesturePen(wx.Colour(255, 0, 0), 2)
        mg.SetGesturesVisible(True)
        mg.AddGesture('DR', self.OnDownRight)

        self.Centre()
        self.Show(True)

    def OnDownRight(self):
          self.Close()

app = wx.App()
MyMouseGestures(None, -1, 'mousegestures.py')
app.MainLoop()