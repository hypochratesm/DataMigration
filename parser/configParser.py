from configparser import ConfigParser


class ConfParser:

    def __init__(self):
        pass

    def parseIni(self):
        
        #설정파일 읽기
        config = ConfigParser()
        config.read('../config.ini', 'utf-8')
        config.sections()
        #설정파일 섹션 확인

        #섹션값 읽기

        return config.sections()


if __name__ == '__main__':

    a= ConfParser()
    a.parseIni()



        
        
        


