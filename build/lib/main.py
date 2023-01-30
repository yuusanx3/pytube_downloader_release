from frame import MainFrame
import wx

def main():
    app = wx.App()
    mainframe = MainFrame(None)
    mainframe.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()