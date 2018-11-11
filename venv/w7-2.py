import wx


class test_Frame(wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title = title)
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(self.panel, value = 'here is input', size=(300,200),style = wx.TE_MULTILINE)
        self.sizer.Add(self.text1)

        self.btn1 = wx.Button(self.panel, label = 'click me')
        self.sizer.Add(self.btn1)

        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1)

        self.panel.SetSizerAndFit(self.sizer)
        self.panel.Layout()

        self.Show()

    def OnClick(self, text):
        self.text1.AppendText('\nhello!')


if __name__ == '__main__':
    a = wx.App()
    f = test_Frame(None, r"hello ljj")
    a.MainLoop()