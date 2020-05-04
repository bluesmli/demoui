import logging
import colorlog
import time
import os
import sys



cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)
logName = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'purple',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}


class Log:
    def __init__(self, logName=logName):
        self.logName = logName
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
            log_colors=log_colors_config)

    def __console(self, level, message):
        fh = logging.FileHandler(self.logName, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch = colorlog.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def formatime(self,pattern):
        '''

        :param pattern: '%Y-%m-%d %H:%M:%S'
        :return:
        '''
        return time.strftime(pattern, time.localtime(time.time()))

    def Info(self,message):
        nowtime=self.formatime("%Y-%m-%d %H:%M:%S")
        infomation="["+nowtime+"]"+" [message]:"+message+"\n"
        sys.stdout.write(infomation)
        with open(self.logName,'a+') as f:
            f.write(infomation)
            f.close()


if __name__ == '__main__':
    log=Log()
    log.Info("start login room".ljust(30))
    log.Info("start system settings".ljust(30))