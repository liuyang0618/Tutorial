#encoding:utf-8
"""
树形控件
"""
import wx

class myFrame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, superior,-1,u"树形控件",pos=(100,200),size=(400,500),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX))
        #创建一个panel
        panel = wx.Panel(self)

        #创建一个树形控件
        """
        __init__(self, Window parent, int id=-1, Point pos=DefaultPosition,
            Size size=DefaultSize, long style=TR_DEFAULT_STYLE,
            Validator validator=DefaultValidator,
            String name=TreeCtrlNameStr) -> TreeCtrl
        """
        tree = wx.TreeCtrl(panel,-1,pos=(20,20),size=(100,200))
        #给树形控件添加一个根
        root = tree.AddRoot("Root")
        #给Root节点添加一个子节点A1
        childA1 = tree.AppendItem(root,"A1")
        #给A1节点添加一个子节点A11
        childA11 = tree.AppendItem(childA1,"A11")
        #给A1节点添加一个子节点A12
        childA12 = tree.AppendItem(childA1,"A12")

        #给Root节点添加另一个子节点A2
        childA2 = tree.AppendItem(root,"A2")
        #给A2节点添加一个子节点A21
        childA21 = tree.AppendItem(childA2,"A21")
        #给A2节点添加一个子节点A21
        childA22 = tree.AppendItem(childA2,"A22")

        #将树形控件下的所有节点展开
        tree.ExpandAll()
        #收缩指定的子节点
        tree.Collapse(childA2)

if __name__ == "__main__":
    #创建app
    app = wx.App()
    #创建Frame
    frame = myFrame(None)
    #显示Frame
    frame.Show(True)
    #建立主循环
    app.MainLoop()