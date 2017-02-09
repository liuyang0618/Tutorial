#encoding:utf-8

"""
状态栏和菜单栏详解
"""
import wx

class myFrame(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self, superior , -1, u"文本输入框",pos=(10,10),size=(400, 500))
        #wx.Frame.__init__(self,superior, -1, u"示范静态文本框", size=(950,320))

        #创建一个pannel
        panel = wx.Panel(self, -1);

        #创建状态栏
        self.statusBar = self.CreateStatusBar()
        #创建工具栏 ,它会自动的放在框架的顶部
        toolbar = self.CreateToolBar()
        #为工具栏添加工具(工具一般都是有icon的)
        toolbar.AddSimpleTool(11,wx.Image('file.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),"Open","Click it to open a file")
            #第一个参数：toolbar 的id
            #第二个参数：imge 是一个bitmap的图片
            #第三个参数： 聚焦的显示
            #第四个参数：点击的状态栏提示语
        toolbar.AddSimpleTool(12,wx.Image('file2.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),"OpenAgain","Click it to open a file again")

        #显示工具栏
        toolbar.Realize()
        #为工具栏添加EVT_TOOL响应事件
        wx.EVT_TOOL(self, 11, self.OnToolOpen)
        wx.EVT_TOOL(self, 12, self.OnToolOpen)

        #创建一个MenuBar
        menubar = wx.MenuBar()
        #创建一个menu
        menu = wx.Menu()
        #为menu添加内容
        menu.Append(101,"&new","Create a New File")
        menu.Append(102,"&open", "")
        menu.Append(103,"&Close", "")
        #添加分隔符
        menu.AppendSeparator()
        menu.Append(104,"&Exit", "")

        #将menu添加到menuBar中
        menubar.Append(menu,"&File")

        #将menuBar添加到Frame中
        self.SetMenuBar(menubar)

        #给menu绑定事件
        wx.EVT_MENU(self,104,self.OnMenuExit)

    def OnToolOpen(self,event):
        self.statusBar.SetStatusText('You open a file!')

    def OnMenuExit(self,event):
        self.Close(True)

if __name__ == "__main__":
    #创建app对象
    app = wx.App()
    #创建框架类对象
    frame = myFrame(None)
    #框架显示
    frame.Show(True)
    #创建事物循环
    app.MainLoop()

