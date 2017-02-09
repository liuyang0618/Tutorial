#encoding:utf-8
"""
组合框comboBox
"""
import wx

class myFrame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, superior,-1,u"多选框",pos=(100,200),size=(400,500),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX))
        #创建一个panel
        panel = wx.Panel(self)
        #创建一个组合框
        """
        __init__(Window parent, int id=-1, String value=EmptyString,
            Point pos=DefaultPosition, Size size=DefaultSize,
            List choices=EmptyList, long style=0, Validator validator=DefaultValidator,
            String name=ComboBoxNameStr) -> ComboBox

        Constructor, creates and shows a ComboBox control.
        """
        comboBox = wx.ComboBox(panel,-1,choices=["abc","123"],pos=(20,10),size=(60,100))
        #组合框默认选择项
        comboBox.SetSelection(0)


if __name__ == "__main__":
    #创建app
    app = wx.App()
    #创建Frame
    frame = myFrame(None)
    #显示Frame
    frame.Show(True)
    #建立主循环
    app.MainLoop()
