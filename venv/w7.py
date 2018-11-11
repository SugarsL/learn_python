import wx


class Frame1(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(200, 200), size=(400, 200))
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, value="Hello, World!", size=(200, 100))
        text2 = wx.TextCtrl(panel, value='ljj',pos=(200,200),size=(200,100))
        self.Show(True)


if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None, "Example")
    app.MainLoop()