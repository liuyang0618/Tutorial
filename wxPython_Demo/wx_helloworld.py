#encoding:utf-8
__author__ = 'Administrator'

#导入 wx 模块
import wx

#定义应用程序类的一个对象
app = wx.App()
#创建一个顶层窗口的 wx.Frame 类的对象。 给出构造标题和尺寸参数。
window = wx.Frame(None, title = "wxPython - http://www.yiibai.com/", size = (400,300))
#虽然其他控件可以在Frame对象加入，但它们的布局无法管理。因此，把一个Panel对象到框架。
panel = wx.Panel(window)
#添加一个静态文本对象，以显示 ‘Hello World’在窗口内的任意位置。
label = wx.StaticText(panel, label = "Hello World", pos = (100,100))
#通过show()方法激活框架窗口。
window.Show(True)
#输入应用程序对象的主事件循环。
app.MainLoop()

