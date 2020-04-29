#QFileDialog对话框使用
from PyQt5.QtWidgets import QFileDialog,QTextEdit,QFontDialog, QLineEdit,QStyle,QFormLayout, QInputDialog,QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon,QPixmap,QFont
from PyQt5.QtCore import  Qt

import sys

class WindowClass(QWidget):

    def __init__(self,parent=None):

        super(WindowClass, self).__init__(parent)
        layout=QVBoxLayout()
        self.btn=QPushButton("加载图片")
        self.btn.clicked.connect(self.getFile)
        layout.addWidget(self.btn)

        self.le=QLabel("")
        layout.addWidget(self.le)

        self.btn1=QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.getText)
        layout.addWidget(self.btn1)

        self.contents=QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle("File Dialog　Demo")

    def getFile(self):
        fname,_ =QFileDialog.getOpenFileName(self,'OpenFile',"c:/","Image files (*.jpg *.gif *.png)")
        """
        参数一：设置父组件
        参数二：QFileDialog的标题
        参数三：默认打开的目录，“.”点表示程序运行目录，/表示当前盘符根目录
        参数四：对话框的文件扩展名过滤器Filter，比如使用 Image files(*.jpg *.gif) 表示只能显示扩展名为.jpg或者.gif文件
        设置多个文件扩展名过滤，使用双引号隔开；
        “All Files(*);;PDF Files(*.pdf);;Text Files(*.txt)”
        """
        self.le.setPixmap(QPixmap(fname))
    def getText(self):
        dialog=QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)#可选任意文件
        dialog.setFilter(QDir.Files)

        if dialog.exec_():#该方法用于选择文件，如果选中文件则返回true
            filenames=dialog.selectedFiles()#获取选中文件名列表
            print(filenames)
            f=open(filenames[0],'r')
            with f:
                data=f.read()
                self.contents.setText(data)


if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WindowClass()
    win.show()
    sys.exit(app.exec_())