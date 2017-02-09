#encoding:utf-8

"""
文本输入对话框
"""
import wx

class myFrame(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,superior,-1,u"使用对话框",size=(500,450))
        #创建pannel
        panel = wx.Panel(self,-1)
        #创建一个button
        self.btnEdit = wx.Button(parent=panel,label=u"编辑",pos=(300,300),size=(-1,-1))
        #绑定退出按钮的事件
        self.Bind(wx.EVT_BUTTON,self.OnEdit,self.btnEdit)

    def OnEdit(self,event):
        """
        __init__(self, Window parent, String message, String caption=GetTextFromUserPromptStr,
            String defaultValue=EmptyString,
            long style=TextEntryDialogStyle, Point pos=DefaultPosition) -> TextEntryDialog

        Constructor.  Use ShowModal method to show the dialog.
        """
        #caption 就是标题
        dialog = wx.TextEntryDialog(self,u"请输入姓名？",u"可输入对话框",style=wx.OK|wx.CANCEL)  #|wx.ICON_QUESTION  如果添加这个就不会显示icon图标
        #对话框的模态显示
        result = dialog.ShowModal()

        if result == wx.ID_OK:
            print(result)
            response = dialog.GetValue()
            print(u"姓名：%s" % (response))
        else:
            dialog.Destroy()
            self.Destroy()

if __name__ == "__main__":
    #创建app
    app = wx.App()
    #创建Frame
    frame = myFrame(None)
    #框架显示
    frame.Show(True)
    #创建事件循环
    app.MainLoop()




