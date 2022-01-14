import os
import sys
import pandas as pd
import datetime
from datetime import datetime
from LogUtil.Log import Log



class ScrpiptMaker:

    def __init__(self):
        pass

    if __name__ == '__main__':
        #로그파일 만들기
        exe = Log();
        filename = 'logfilename.log'
        path = f'D:\log + {filename}'

        date = datetime.now()

        exe.logger(date)













