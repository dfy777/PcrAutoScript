
import imghandle
import jsonos as jsos
import adbcontroller
from configparser import ConfigParser

cf = ConfigParser()
cf.read('config.ini',encoding='utf-8')
cf_map = dict(cf.items('progress'))

IS_MATCH_IMAGE_BYLOC = cf_map['ismatchimagebyloc'] != "false"
IS_RECORD_LOC = cf_map['isrecordloc'] != "false"
TEAM_NUM = int(cf_map['teamnum'])
DELAY = list(map(float, cf_map['delaylist'].replace(' ', '').split(",")))

class Controller:
    def __init__(self) -> None:
        self.__adbCtrl = adbcontroller.AdbController()
        self.__imgHdl = imghandle.ImgHandle()
        self.__imgLocDict = jsos.ReadJson()
        self.__mappingName =jsos.ReadJson(False, jsos.LOC_MAPPING_1_PATH)
        self.__mappingLis = jsos.ReadJson(False, jsos.LOC_MAPPING_2_PATH)
        self.__tmpLoc = False

    def LocInjection(self, name) -> None:
        self.__tmpLoc = False

        if (IS_MATCH_IMAGE_BYLOC):
            self.__tmpLoc = self.__imgLocDict[name]

        if (self.__tmpLoc == False or self.__tmpLoc[0] == -1):
            self.__tmpLoc = self.__imgHdl.GetLocationByImageName(name, adbcontroller.DEFAULT_NAME)
            self.__imgLocDict[name] = self.__tmpLoc
        
        #记录不同模板但位置相同的坐标
        if (name in self.__mappingName):
            index = self.__mappingName[name]
            maplis = self.__mappingLis[str(index)]
            for mapname in maplis:
                self.__imgLocDict[mapname] = self.__tmpLoc


    def LocInjection_Mul(self, name) -> None:
        self.__tmpLoc = False

        if (name in self.__mappingLis):
            namelis = self.__mappingLis[name]
            loclis = []

            if (IS_MATCH_IMAGE_BYLOC):
                for itname in namelis:
                    loclis.append(self.__imgLocDict[itname])
            
            #如果loclis没有元素或者含有错误的坐标
            #则重新匹配模板得到坐标
            if len(loclis) == 0 or (bool([False for x in loclis if x[0]==-1])):
                loclis = self.__imgHdl.GetLocationByImageName_Mul(name, adbcontroller.DEFAULT_NAME)
                for index, itname in namelis:
                    self.__imgLocDict[itname] = loclis[index]