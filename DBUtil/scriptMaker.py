import os
import sys
import pandas as pd
import datetime
from datetime import datetime
import logging
class ScrpiptMaker:

    def __init__(self):
        pass

    if __name__ == '__main__':
        
        #로그파일 만들기
        
        filename = 'logfilename.log'
        path = f'D:\log + {filename}'

        logging.basicConfig(filename=path, level=logging.INFO)

        date = datetime.now()
        logging.debug("log4j")
        logging.info("log4j")
        logging.error("log4j")
        logging.warning("log4j")
        logging.critical("log4j")
        print(date)













