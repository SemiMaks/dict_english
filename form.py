import wx

APP_EXIT = 1
VIEW_STATUS = 2
STATUS_A = 3
STATUS_B = 4
MINIMUM = 5
MAXIMUM = 6


class AppContextMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        it_min = self.Append(MINIMUM, "Минимизировать")
        it_max = self.Append(MAXIMUM, "Распахнуть")
        self.Bind(wx.EVT_MENU, self.onMinimize, it_min)
        self.Bind(wx.EVT_MENU, self.onMaximize, it_max)

    def onMinimize(self, event):
        self.parent.Iconize()

    def onMaximize(self, event):
        self.parent.Maximize()

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # создание пунктов меню
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        expMenu = wx.Menu()

        fileMenu.Append(wx.ID_NEW, "&Новый\tCntrl+N")
        fileMenu.Append(wx.ID_OPEN, "&Открыть\tCntrl+O")
        fileMenu.Append(wx.ID_SAVE, "&Сохранить\tCntrl+S")
        fileMenu.AppendSubMenu(expMenu, "&Экспорт")
        fileMenu.AppendSeparator()

        expMenu.Append(wx.ID_ANY, "Экспорт изображения")
        expMenu.Append(wx.ID_ANY, "Экспорт видео")
        expMenu.Append(wx.ID_ANY, "Экспорт данных")

        item = wx.MenuItem(fileMenu, APP_EXIT, "Выйти\tCtrl+Q", "Выход из приложения")
        item.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.Append(item)
        # item = fileMenu.Append(wx.ID_EXIT, "Выйти\tCtrl+Q", "Выход из приложения")

        viewMenu = wx.Menu()
        self.vStatus = viewMenu.Append(VIEW_STATUS, 'Статусная строка', kind=wx.ITEM_CHECK)
        self.vA = viewMenu.Append(STATUS_A, 'A', 'A', kind=wx.ITEM_RADIO)
        self.vB = viewMenu.Append(STATUS_B, 'B', 'A', kind=wx.ITEM_RADIO)

        menubar.Append(fileMenu, "&Файл")
        menubar.Append(viewMenu, "&Вид")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onImageType, id=STATUS_A)
        self.Bind(wx.EVT_MENU, self.onImageType, id=STATUS_B)

        self.ctx = AppContextMenu(self)


        self.Bind(wx.EVT_RIGHT_DOWN, self.onRightDown)

        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(APP_EXIT, "Exit", wx.Bitmap('exit.png'))
        toolbar.Realize()

    # обработчик при выборе пункта меню
    def onQuit(self, event):
        self.Close()

    def onStatus(self, event):
        if self.vStatus.IsChecked():
            print("Показать статусную строку")
        else:
            print("Скрыть статусную строку")

    def onImageType(self, event):
        if self.vA.IsChecked():
            print('A')
        elif self.vB.IsChecked():
            print('B')


    def onRightDown(self, event):
        self.PopupMenu(self.ctx, event.GetPosition())


app = wx.App()
frame = MyFrame(None, 'Тренажёр')
frame.Center()
frame.Show()
app.MainLoop()
