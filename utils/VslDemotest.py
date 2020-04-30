import unittest
from ddt import ddt,data,unpack
from utils.pywins import *
from pywinauto.application import Application

import traceback
import time
from utils.logs import *
log = Log()

def FreshRoom(business,env,communicate,role,channelid,userid,path,runNum):
    '''
    刷新教室
    :param business: 业务
    :param env: 环境
    :param communicate: 通话方式
    :param role: 角色
    :param channelid: 频道id
    :param userid: 用户id
    :param path 软件路径
    :param runNum 运行次数
    :return:
    '''
    roomwin=None
    try:
        # 打开软件
        app = Application(backend="uia").start(path)
        # 进行设置
        win = app.window(title="Form")
        win.Button5.click()

        # 切换到对话框
        setwin = app["Dialog"]


        # 选择业务
        batch_combobox = setwin.child_window(title=" Down", control_type="ComboBox", found_index=0)
        batch_combobox.select(business)

        # 选择环境
        batch_combobox = setwin.child_window(title=" Down", control_type="ComboBox", found_index=1)
        batch_combobox.select(env)

        # 通话方式，角色信息
        setwin.child_window(title="communicationmode", control_type="Tab").child_window(title=communicate, control_type="TabItem").click_input()
        setwin.child_window(title="学生", control_type="Tab").child_window(title=role, control_type="TabItem").click_input()

        # 返回到主窗口
        setwin.child_window(title=" Enter", control_type="Button").click()

        # 输入频道id,用户id，进入房间
        win['Edit1'].type_keys(channelid)
        win.type_keys("{TAB}")
        win['Edit2'].type_keys(userid)
        win.child_window(title="进入房间", control_type="Button").click()
        time.sleep(3)
        #确定弹框确定
        roomwin=app.window(title="classroom")

        roomwin.type_keys("{VK_RETURN}")
        log.Info("======fresh room start======")
        for i in range(runNum):
            roomwin.Button5.click()
            roomwin.type_keys("{VK_RETURN}")
        #避免弹框还在
        roomwin.type_keys("{VK_RETURN}")
        log.Info("======fresh room end======")


    except:
        log.error(traceback.format_exc())
        roomwin.close()
        log.Info("Please change channelid or userid")
    finally:
        log.Info("======window close======")
        roomwin.close()





def switchcaOrMicrophone(business,env,communicate,role,channelid,userid,cameraname,Microphone,path):
    '''
    切换摄像头及麦克风
    :param business: 业务
    :param env: 环境
    :param communicate: 通话方式
    :param role: 角色
    :param channelid: 频道id
    :param userid: 用户id
    :param cameraname 摄像头名称
    :param Microphone 麦克风名称
    :param path 软件路径
    :return:
    '''
    roomwin=None
    try:
        # 打开软件
        app = Application(backend="uia").start(path)

        # 进行设置
        win = app.window(title="Form")
        win.Button5.click()

        # 切换到对话框
        setwin = app["Dialog"]


        # 选择业务
        batch_combobox = setwin.child_window(title=" Down", control_type="ComboBox", found_index=0)
        batch_combobox.select(business)

        # 选择环境
        batch_combobox = setwin.child_window(title=" Down", control_type="ComboBox", found_index=1)
        batch_combobox.select(env)

        # 通话方式，角色信息
        setwin.child_window(title="communicationmode", control_type="Tab").child_window(title=communicate, control_type="TabItem").click_input()
        setwin.child_window(title="学生", control_type="Tab").child_window(title=role, control_type="TabItem").click_input()

        # 返回到主窗口
        setwin.child_window(title=" Enter", control_type="Button").click()

        # 输入频道id,用户id，进入房间
        win['Edit1'].type_keys(channelid)
        win.type_keys("{TAB}")
        win['Edit2'].type_keys(userid)
        win.child_window(title="进入房间", control_type="Button").click()
        time.sleep(3)
        #确定弹框确定
        roomwin=app.window(title="classroom")
        roomwin.type_keys("{VK_RETURN}")
        roomwin.print_control_identifiers()
        roomwin.Button7.click()
        camerawin=app.window(title="Form")
        # camerawin.print_control_identifiers()
        #切换摄像头
        log.Info("======switch camera start======")
        batch_combobox=camerawin.child_window(title=" Down", control_type="ComboBox",found_index=1)
        batch_combobox.select(cameraname)
        camerawin.close()
        log.Info("======switch camera end======")
        #切换麦克风
        log.Info("======switch Microphone start======")
        roomwin.Button8.click()
        microphonewin = app.window(title="Form")
        batch_combobox = microphonewin.child_window(title=" Down", control_type="ComboBox", found_index=0)
        batch_combobox.select(Microphone)
        microphonewin.close()
        log.Info("======switch Microphone end======")
    except:
        log.Info(traceback.format_exc())
        roomwin.close()
        log.Info("Please change channelid or userid")
    finally:
        log.Info("======window close======")
        roomwin.close()