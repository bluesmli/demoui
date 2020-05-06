import logging
import colorlog
import time
import sys
import os

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'purple',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}

if getattr(sys, 'frozen', False):
    cur_path = sys._MEIPASS
else:
    cur_path = os.path.split(os.path.realpath(__file__))[0]

log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)
logName = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))

#日志输出文件在exe 释放路径父路径下 C:\Users\Administrator\AppData\Local\Temp\logs
print("输出日志文件路径为："+logName)


class Log:
    def __init__(self):
        self.logName = logName
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
            log_colors=log_colors_config)

    def __console(self, level, message):
        fh = logging.FileHandler(self.logName, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        self.logger.removeHandler(fh)
        fh.close()

    def formatime(self,pattern):
        '''

        :param pattern: '%Y-%m-%d %H:%M:%S'
        :return:
        '''
        return time.strftime(pattern, time.localtime(time.time()))

    def write(self,message):
        nowtime = self.formatime("%Y-%m-%d %H:%M:%S")
        infomation = "[" + nowtime + "]" + " [message]:" + message + "\n"
        sys.stdout.write(infomation)

    def debug(self, message):
        self.__console('debug', message)
        self.write(message)

    def warning(self, message):
        self.__console('warning', message)
        self.write(message)

    def error(self, message):
        self.__console('error', message)
        self.write(message)

    def Info(self,message):
        self.__console('info', message)
        self.write(message)
