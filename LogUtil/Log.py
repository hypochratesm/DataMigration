import logging
import logging.handlers
from parser.configParser import ConfParser
import os
import pathlib as Path
import datetime
import pandas as pd


class Log:

    def __init__(self):
        conf = ConfParser()

        dict =  conf.parseIni()
        self.logCf = conf.parseIni()


    def logger(self, str):


        logger = logging.getLogger(__name__)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s]%(filename)s:%(lineno)s]>>%(message)s')

        filename = str(self.path) + str(self.fileName)
        streamHandler = logging.StreamHandler()
        fileHandler = logging.FileHandler(filename)
        # logger instancedp formatter 설정
        streamHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)

        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)
        logger.setLevel(level=f'logging.{self.level}')
        logging.debug(str)
