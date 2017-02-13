#encoding:gbk
"""
可选择的listbox列表框，checklistbox是listbox的子类
"""
import wx

class myFrame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, superior,-1,u"列表框",pos=(100,200),size=(400,400),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX))
        #创建一个panel
        panel = wx.Panel(self)

        #创建一个列表框
        li = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期二','星期三','星期四','星期五','星期六','星期日vvcvcxvxzvxvzxv']
        """

        __init__(self, Window parent, int id=-1, Point pos=DefaultPosition,
            Size size=DefaultSize, wxArrayString choices=wxPyEmptyStringArray,
            long style=0, Validator validator=DefaultValidator,
            String name=ListBoxNameStr) -> CheckListBox

        """
        #
        wx.CheckListBox(panel,-1,pos=(40,50),choices=li)  #Todo 如果使用utf-8编码会报错，目前不知道变量li如何解决？
        #wx.ListBox(panel,-1,pos=(40,50),choices=li)  #Todo 如果使用utf-8编码会报错，目前不知道变量li如何解决？
        #wx.StaticText(panel,-1,u"业余爱好",(110,20),style=wx.ALIGN_RIGHT)

if __name__ == "__main__":
    #创建app
    app = wx.App()
    #创建Frame
    frame = myFrame(None)
    #显示Frame
    frame.Show(True)
    #建立主循环
    app.MainLoop()