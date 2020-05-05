
from pywinauto.application import Application
import pywinauto
import traceback
from pyautogui import *
from utils.logs import *

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)
logName = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))
log = Log(logName)

class vlsdemo(object):

    def __init__(self,business,env,communicate,role,channelid,userid,path,runNum):
        '''
        :param business:
        :param env:
        :param communicate:
        :param role:
        :param channelid:
        :param userid:
        :param path:
        :param runNum:
        '''
        self.business=business
        self.env=env
        self.communicate=communicate
        self.role=role
        self.channelid=channelid
        self.userid=userid
        self.path=path
        self.runNum=runNum
        self.roomwin = None
        #初始化登录教室
        try:
            # 打开软件
            log.Info("open software".ljust(30))
            self.app = Application(backend="uia").start(path)
            # 进行设置
            win = self.app.window(title="Form")
            #import  pywinauto.win32structures.RECT
            # print(win.rectangle().left,win.rectangle().right)

            win.Button5.click()

            log.Info("start system settings".ljust(30))
            # 切换到对话框
            setwin = self.app["Dialog"]

            # 选择业务
            batch_combobox = setwin.child_window(title=" Down", control_type="ComboBox", found_index=0)
            batch_combobox.select(business)

            # 选择环境
            batch_combobox = setwin.child_window(title=" Down", control_type="ComboBox", found_index=1)
            batch_combobox.select(env)

            # 通话方式，角色信息
            setwin.child_window(title="communicationmode", control_type="Tab").child_window(title=communicate,
                                                                                            control_type="TabItem").click_input()
            setwin.child_window(title="学生", control_type="Tab").child_window(title=role,
                                                                             control_type="TabItem").click_input()

            # 返回到主窗口
            setwin.child_window(title=" Enter", control_type="Button").click()

            # 输入频道id,用户id，进入房间
            log.Info("start login room".ljust(30))
            win['Edit1'].type_keys(channelid)
            win.type_keys("{TAB}")
            win['Edit2'].type_keys(userid)
            win.child_window(title="进入房间", control_type="Button").click()
            time.sleep(3)
            # 确定弹框确定
            self.roomwin = self.app.window(title="classroom")
            time.sleep(3)
            self.roomwin.type_keys("{VK_RETURN}")
        except:
            log.Info(traceback.format_exc())
            self.roomwin.close()
            log.Info("Please change channelid or userid".ljust(30))


    def FreshRoom(self):
        '''
        刷新教室
        :return:
        '''

        try:
            log.Info("fresh room start".ljust(30))
            for i in range(int(self.runNum)):
                self.roomwin.Button5.click()
                time.sleep(2)
                self.roomwin.type_keys("{VK_RETURN}")
                time.sleep(2)
            #避免弹框还在
            self.roomwin.type_keys("{VK_RETURN}")
            log.Info("fresh room end".ljust(30))
        except:
            log.Info(traceback.format_exc())
            self.roomwin.close()
            log.Info("Please change channelid or userid".ljust(30))
        finally:
            log.Info("window close".ljust(30))
            self.roomwin.close()

    def switchcaOrMicrophone(self,cameraname,Microphone):
        '''
        切换摄像头及麦克风
        :param cameraname 摄像头名称
        :param Microphone 麦克风名称
        :return:
        '''
        try:
            self.roomwin.print_control_identifiers()
            self.roomwin.Button7.click()
            camerawin=self.app.window(title="Form")

            #切换摄像头
            log.Info("switch camera start".ljust(30))
            batch_combobox=camerawin.child_window(title=" Down", control_type="ComboBox",found_index=1)
            batch_combobox.select(cameraname)
            camerawin.close()
            log.Info("switch camera end".ljust(30))
            #切换麦克风
            log.Info("switch Microphone start".ljust(30))
            self.roomwin.Button8.click()
            microphonewin = self.app.window(title="Form")
            batch_combobox = microphonewin.child_window(title=" Down", control_type="ComboBox", found_index=0)
            batch_combobox.select(Microphone)
            microphonewin.close()
            log.Info("switch Microphone end".ljust(30))
        except:
            log.Info(traceback.format_exc())
            self.roomwin.close()
            log.Info("Please change channelid or userid".ljust(30))
        finally:
            log.Info("window close".ljust(30))
            self.roomwin.close()


    def audioMix(self,musicPath):
        '''
        混音效
        :param musicPath:
        :return:
        '''
        try:
            self.roomwin.child_window(title="混音效", control_type="Button").click()
            self.roomwin.child_window(title="Float", control_type="Button").click()
            log.Info("pull window start".ljust(30))
            pywinauto.mouse.move(coords=(self.roomwin.Dialog.rectangle().right-3, 500))
            dragTo(self.roomwin.Dialog.rectangle().right+500, 500, button='left')
            left,top=self.roomwin['VEdit'].rectangle().left, self.roomwin['VEdit'].rectangle().top
            moveTo(left,top)
            log.Info("pull window end".ljust(30))
            click(x=left, y=top)
            log.Info("audio effect start".ljust(30))
            typewrite(musicPath)
            if (len(str(musicPath).split(";"))==2):
                self.roomwin.child_window(title="        111.mp3", control_type="CheckBox").click()
                self.roomwin.child_window(title="        222.mp3", control_type="CheckBox").click()
            elif (len(str(musicPath).split(";"))==3):
                self.roomwin.child_window(title="        111.mp3", control_type="CheckBox").click()
                self.roomwin.child_window(title="        222.mp3", control_type="CheckBox").click()
                self.roomwin.child_window(title="        333.mp3", control_type="CheckBox").click()
            else:
                self.roomwin.child_window(title="        111.mp3", control_type="CheckBox").click()
            self.roomwin.Button4.click()
            time.sleep(10)
            self.roomwin.Button5.click()
            log.Info("audio effect end".ljust(30))
        except:
            log.Info(traceback.format_exc())
            self.roomwin.close()
            log.Info("Please change channelid or userid".ljust(30))
        finally:
            log.Info("window close".ljust(30))
            self.roomwin.close()