import wx

APP_EXIT = 1

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # создание пунктов меню
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        item = wx.MenuItem(fileMenu, APP_EXIT, "Выйти\tCtrl+Q", "Выход из приложения")
        item.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.Append(item)
        # item = fileMenu.Append(wx.ID_EXIT, "Выйти\tCtrl+Q", "Выход из приложения")

        menubar.Append(fileMenu, "&Файл")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, item)

    # обработчик при выборе пункта меню
    def onQuit(self, event):
        self.Close()


app = wx.App()
frame = MyFrame(None, 'Тренажёр')
frame.Center()
frame.Show()
app.MainLoop()
