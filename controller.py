#-*- coding: UTF-8-*-
import random
from configparser import ConfigParser

import adbcontroller
from adbcontroller import AdbController
import imghandle
import jsonos as jsos

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

        #for key in self.__imgLocDict:
        #    self.__imgLocDict[key][0] = -1
        #self.__imgLocDict["avator-cancel"][0] = 659

    def LocInjection(self, template_name, img_name=adbcontroller.DEFAULT_NAME) -> None:
        self.__tmpLoc = False

        if (IS_MATCH_IMAGE_BYLOC):
            self.__tmpLoc = self.__imgLocDict[template_name]

        if (self.__tmpLoc == False or self.__tmpLoc[0] == -1):
            self.__tmpLoc = self.__imgHdl.GetLocationByImageName(img_name, template_name)
            self.__imgLocDict[template_name] = self.__tmpLoc
            print("false")
        
        #记录不同模板但位置相同的坐标
        if (template_name in self.__mappingName):
            index = self.__mappingName[template_name]
            maplis = self.__mappingLis[str(index)]
            for mapname in maplis:
                self.__imgLocDict[mapname] = self.__tmpLoc


    def LocInjection_Mul(self, template_name, img_name=adbcontroller.DEFAULT_NAME) -> None:
        self.__tmpLoc = False

        if (template_name in self.__mappingLis):
            namelis = self.__mappingLis[template_name]
            loclis = []

            if (IS_MATCH_IMAGE_BYLOC):
                for itname in namelis:
                    loclis.append(self.__imgLocDict[itname])
            
            #如果loclis没有元素或者含有错误的坐标
            #则重新匹配模板得到坐标
            if len(loclis) == 0 or (bool([False for x in loclis if x[0]==-1])):
                loclis = self.__imgHdl.GetLocationByImageName_Mul(img_name, template_name)
                for index, itname in enumerate(namelis):
                    self.__imgLocDict[itname] = loclis[index]


    def Click(self, name, const_delay=DELAY[1], random_delay=DELAY[0]):
        self.__adbCtrl.ClickInRandomArea(self.__imgLocDict[name], const_delay, random_delay)


    def ContinousClick(self, name, times, const_delay=DELAY[1], random_delay=DELAY[0]):
        self.__adbCtrl.ClickMultipleTimes(self.__imgLocDict[name], 
                                            times, const_delay, random_delay)

    def Swipe(self, startp, endp, const_delay=DELAY[1], random_delay=DELAY[0]):
        self.__adbCtrl.SwipeScreen(startp, endp, const_delay, random_delay)
    

    def ScreenShot(self, name=adbcontroller.DEFAULT_NAME):
        self.__adbCtrl.ScreenShot(name)

        cnt = 0
        while cnt < 3:
            if self.__imgHdl.CheckIsBrokenImg(name):
                self.__adbCtrl.ScreenShot(name)
                cnt += 1
            else:
                break

    def CheckImgLoc(self, name) ->bool:
        if (self.__imgHdl.GetLocationByImageName(adbcontroller.DEFAULT_NAME, name)):
            return True
        else:
            return False
            

    def GetRandomList(self, rd_list):
        random.shuffle(rd_list)
        return rd_list

    def GetRadomInt(self, rd_int):
        rd_int = random.randint(0, rd_int-1)
        return rd_int

    def GetRandomLoc(self, area):
        rd_x = random.randint(area[0], area[0] + area[2])
        rd_y = random.randint(area[1], area[1] + area[3])
        return (rd_x, rd_y)

    def GetLocationByName(self, name):
        return self.__imgLocDict[name]

    def PrintImgLocDict(self):
        for key in self.__imgLocDict:
            print(key + ": "+ str(self.__imgLocDict[key]) )
