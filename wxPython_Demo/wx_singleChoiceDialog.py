#encoding:utf-8
"""
单选对话框
"""
import wx

class myFrame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, superior,-1,u"单选框",size=(400,500))
        #创建一个单选框
        """
        __init__(Window parent, String message, String caption,
            List choices=EmptyList, long style=CHOICEDLG_STYLE,
            Point pos=DefaultPosition) -> SingleChoiceDialog

        Constructor.  Use ShowModal method to show the dialog.
        """
        scd = wx.SingleChoiceDialog(None,u"您选择python的版本是？", u"Single Choice", ['2.0','3.0','4.0']) #即使关闭了对话，仍然会显示Frame框。
        #显示对话框并保存点击的按钮的id
        result =  scd.ShowModal()
        if result == wx.ID_OK:
            result = scd.GetStringSelection()
            print(u"显示的内容为：%s" % result)
            #关闭所有窗体
            #scd.Close()  使用Close方法窗口虽然关闭了，但是资源仍然占用，所以需要是destroy方法。
            scd.Destroy()
            self.Destroy()

if __name__ == "__main__":
    #创建app
    app = wx.App()
    #创建Frame
    frame = myFrame(None)
    #显示Frame
    frame.Show(True)
    #建立主循环
    app.MainLoop()