import logging
import colorlog
import time
import sys


log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'purple',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}


class Log:
    def __init__(self, logName):
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