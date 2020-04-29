from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from utils.logs import *
import traceback
import sys
sys.coinit_flags = 2 #修正pyqt5 和pywinauto 不能同时引入的问题
from utils.VslDemotest import *


class Stream(QObject):
    '''
    控制台输出定向到Qtextedit中
    '''
    """Redirects console output to text widget."""
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class Ui_MainWindow(QWidget):

    def __init__(self,parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.Widget=QtWidgets.QWidget()
        self.setupUi(self.Widget)
        sys.stdout = Stream(newText=self.onUpdateText)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(20, 290, 54, 12))
        self.label_19.setObjectName("label_19")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 1011, 171))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(10, 0, 54, 12))
        self.label_28.setObjectName("label_28")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(10, 120, 61, 31))
        self.label_25.setObjectName("label_25")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(770, 30, 31, 31))
        self.label_27.setObjectName("label_27")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame)
        self.comboBox_6.setGeometry(QtCore.QRect(550, 40, 161, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(550, 80, 161, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setPlaceholderText("请输入摄像头名称")

        self.comboBox_11 = QtWidgets.QComboBox(self.frame)
        self.comboBox_11.setGeometry(QtCore.QRect(810, 40, 161, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 80, 161, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText("请输入用户")

        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(260, 80, 41, 31))
        self.label_8.setObjectName("label_8")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(490, 80, 51, 31))
        self.label_23.setObjectName("label_23")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 80, 161, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("请输入频道")

        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(70, 130, 161, 21))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setPlaceholderText("请输入运行次数")


        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(810, 80, 161, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setPlaceholderText("请输入麦克风名称")


        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(490, 30, 61, 31))
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(20, 30, 41, 31))
        self.label_20.setObjectName("label_20")
        self.comboBox_10 = QtWidgets.QComboBox(self.frame)
        self.comboBox_10.setGeometry(QtCore.QRect(300, 40, 161, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 31, 21))
        self.label_9.setObjectName("label_9")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(260, 40, 41, 21))
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(760, 80, 51, 31))
        self.label_24.setObjectName("label_24")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 130, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_12 = QtWidgets.QComboBox(self.frame)
        self.comboBox_12.setGeometry(QtCore.QRect(70, 40, 161, 21))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(250, 130, 51, 21))
        self.label_10.setObjectName("label_10")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 130, 161, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setPlaceholderText("请选择文件")

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 130, 71, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.getFiles)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 210, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.FreshRoomRoom)




        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 210, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 210, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 310, 961, 181))
        self.textEdit.setObjectName("textEdit")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 23))
        self.menubar.setObjectName("menubar")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_19.setText(_translate("MainWindow", "运行日志"))
        self.label_28.setText(_translate("MainWindow", "通用配置"))
        self.label_25.setText(_translate("MainWindow", "运行次数"))
        self.label_27.setText(_translate("MainWindow", "角色"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "communicationmode"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "livemode"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "老师"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "学生"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "监课"))
        self.label_8.setText(_translate("MainWindow", "用户"))
        self.label_23.setText(_translate("MainWindow", "摄像头"))
        self.label_11.setText(_translate("MainWindow", "通话方式"))
        self.label_20.setText(_translate("MainWindow", "业务"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "env2"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "env5"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "env6"))
        self.label_9.setText(_translate("MainWindow", "频道"))
        self.label_21.setText(_translate("MainWindow", "环境"))
        self.label_24.setText(_translate("MainWindow", "麦克风"))
        self.pushButton_4.setText(_translate("MainWindow", "保存"))
        self.pushButton_4.clicked.connect(self.save_setting)
        self.comboBox_12.setItemText(0, _translate("MainWindow", "1v1"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "双优class"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "蜂校测试"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "小班class"))
        self.comboBox_12.setItemText(4, _translate("MainWindow", "微米测试"))
        self.label_10.setText(_translate("MainWindow", "软件路径"))
        #打开file 选择框
        self.pushButton_5.setText(_translate("MainWindow", "选择文件"))


        self.pushButton.setText(_translate("MainWindow", "刷新教室"))
        self.pushButton_2.setText(_translate("MainWindow", "切换摄像头及麦克风"))
        self.pushButton_3.setText(_translate("MainWindow", "混动音效"))

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def getFiles(self):
        '''
        查找exe 文件路径
        :return:
        '''
        selectedFile,_ = QFileDialog.getOpenFileName(self.Widget, "选择exe",
                                                 "C:\\", "Docement ( *.exe )")
        self.lineEdit_6.setText(str(selectedFile))

    def save_setting(self):
        '''
        保存配置信息
        :return:
        '''
        settings = QSettings("config.ini", QSettings.IniFormat)
        settings.setValue("bussiness",self.comboBox_12.currentText())
        settings.setValue("env", self.comboBox_10.currentText())
        settings.setValue("communicate", self.comboBox_6.currentText())
        settings.setValue("role", str(self.comboBox_11.currentText()))
        settings.setValue("channelid", self.lineEdit_4.text())
        settings.setValue("userid", self.lineEdit_5.text())
        settings.setValue("cameraname", self.lineEdit_13.text())
        settings.setValue("Microphone",self.lineEdit_14.text())
        settings.setValue("runNum", self.lineEdit_15.text())
        settings.setValue("path", self.lineEdit_6.text())
        QMessageBox.about(self, "保存", "保存成功")


    def init_settings(self):
        '''
        初始化读取配置
        :return:
        '''
        settings = QSettings("config.ini", QSettings.IniFormat)
        self.bussiness=settings.value("bussiness")
        self.env = settings.value("env")
        self.communicate = settings.value("communicate")
        self.role = settings.value("role")
        self.bussiness = settings.value("bussiness")
        self.channelid = settings.value("channelid")
        self.userid = settings.value("userid")
        self.cameraname = settings.value("cameraname")
        self.Microphone = settings.value("Microphone")
        self.runNum = settings.value("runNum")
        self.path = settings.value("path")

    def FreshRoomRoom(self):
        '''
        刷新教室方法
        :return:
        '''
        self.init_settings()
        FreshRoom(self.bussiness, self.env, self.communicate, self.role, self.channelid, self.userid)

    def switchcaOrMicrophone(self):
        '''
        切换摄像头及麦克风
        :return:
        '''
        self.init_settings()
        switchcaOrMicrophone(self.bussiness, self.env, self.communicate, self.role, self.channelid, self.userid,
                             self.cameraname,self.Microphone)

    def efect(self):
        pass





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    log=Log()
    log.Info("start test")
    ui.Widget.show()
    sys.exit(app.exec_())