import tkinter 
#导入Tkinter模块
root = tkinter.Tk()
#生成一个主窗口对象
#实例化标签组件
label= tkinter.Label(root, text="Python, tkinter!")
label.pack()
#将标签添加到窗口中
button1 = tkinter.Button(root, text="按钮1")
#创建按钮1
button1.pack(side=tkinter.LEFT)
#将按钮1添加到窗口中
button2 = tkinter.Button(root, text="按钮2")
#创建按钮2
button2.pack(side=tkinter.RIGHT)
#将按钮2添加到窗口中
#如果按钮1被点击，则执行以下代码
def button1_click(a1):
    return "按钮1被点击"
#窗口大小
root.geometry("400x300")
#如果按钮一被点击，则执行以下代码
root.mainloop()
#进入消息循环