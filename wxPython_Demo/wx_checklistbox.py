#encoding:gbk
"""
��ѡ���listbox�б��checklistbox��listbox������
"""
import wx

class myFrame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, superior,-1,u"�б��",pos=(100,200),size=(400,400),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX))
        #����һ��panel
        panel = wx.Panel(self)

        #����һ���б��
        li = ['����һ','���ڶ�','������','������','������','������','������','���ڶ�','������','������','������','������','������vvcvcxvxzvxvzxv']
        """

        __init__(self, Window parent, int id=-1, Point pos=DefaultPosition,
            Size size=DefaultSize, wxArrayString choices=wxPyEmptyStringArray,
            long style=0, Validator validator=DefaultValidator,
            String name=ListBoxNameStr) -> CheckListBox

        """
        #
        wx.CheckListBox(panel,-1,pos=(40,50),choices=li)  #Todo ���ʹ��utf-8����ᱨ��Ŀǰ��֪������li��ν����
        #wx.ListBox(panel,-1,pos=(40,50),choices=li)  #Todo ���ʹ��utf-8����ᱨ��Ŀǰ��֪������li��ν����
        #wx.StaticText(panel,-1,u"ҵ�మ��",(110,20),style=wx.ALIGN_RIGHT)

if __name__ == "__main__":
    #����app
    app = wx.App()
    #����Frame
    frame = myFrame(None)
    #��ʾFrame
    frame.Show(True)
    #������ѭ��
    app.MainLoop()