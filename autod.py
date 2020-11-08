#-*- coding: UTF-8-*-
from configparser import ConfigParser
from imghandle import ImgHandle
from typing import Match
import test
import random

import controller

cf = ConfigParser()
cf.read('config.ini',encoding='utf-8')
cf_map = dict(cf.items('progress'))

IS_MATCH_IMAGE_BYLOC = cf_map['ismatchimagebyloc'] != "false"
IS_RECORD_LOC = cf_map['isrecordloc'] != "false"
TEAM_NUM = int(cf_map['teamnum'])
DELAY = list(map(float, cf_map['delaylist'].replace(' ', '').split(",")))
CHANGE_TIME = int(cf_map['changetime'])
IS_RANDOM_CHANGE_TIME = cf_map['israndomchangetime'] != "false"

DEFAULT_TIME = 2

class AutoD:
    def __init__(self) -> None:
        self.ctrl = controller.Controller()
        #self.imgHdl = ImgHandle()
        self.__isInit = False
        self.delta_hujiao_loc = False
        self.__lastTeamLog = False
        self.swipe_area = False
        self.match_area = False


    def InitSleepTime(self):
        tim = 2.0
        if (IS_RANDOM_CHANGE_TIME):
            tim += random.random() * CHANGE_TIME
        else:
            tim += CHANGE_TIME
        return tim


    def Start(self) -> None:
        #=============mainpage=================
        self.__MainPageInit()
        self.ctrl.Click("fangyusheding", DELAY[2], DELAY[1])

        #========change team page==============
        self.__ChangeTeamPageInit()
        for page in range(3):
            #self.ctrl.Click("avator-cancel", 0.1, 0.1)
            self.ctrl.ContinousClick("avator-cancel", 5, 0.4, 0.2)
            if (page == 0):
                self.ctrl.Click("team-config-next-1", DELAY[1], DELAY[0])
            elif (page == 1):
                self.ctrl.Click("team-config-next-2", DELAY[1], DELAY[0])
            else:
                self.ctrl.Click("wodeduiwu", DELAY[1], DELAY[0])

        #===========choose myteam page============
        self.__MyteamPageInit()
        
        team_randomid, team_randomlis = self.__GetRandomTeam()
        team_name = "myteam-" + str(team_randomid)

        self.ctrl.ScreenShot()
        if (not self.ctrl.CheckImgLoc("shengxu")):
            self.ctrl.Click("shengxu", DELAY[1], DELAY[0])

        for cnt in range(3):
            self.ctrl.Click(team_name, DELAY[1], DELAY[0])
            if (team_randomlis[cnt] == 1):
                self.ctrl.Click("hujiao-1", DELAY[1], DELAY[0])
            elif (team_randomlis[cnt] == 2):
                self.ctrl.Click("hujiao-2", DELAY[1], DELAY[0])
            else:
                self.ctrl.Click("shengxu", DELAY[1], DELAY[0])
                self.ctrl.Click("hujiao-1", DELAY[1], DELAY[0])
                self.ctrl.Click("wodeduiwu", DELAY[1], DELAY[0])
                self.ctrl.Click("shengxu", DELAY[1], DELAY[0])
                self.ctrl.Click("myteam-guanbi", DELAY[1], DELAY[0])

            if cnt == 0:
                self.ctrl.Click("team-config-page-2", DELAY[1], DELAY[0])
                self.ctrl.Click("wodeduiwu", DELAY[1], DELAY[0])
            elif cnt == 1:
                self.ctrl.Click("team-config-page-1", DELAY[1], DELAY[0])
                self.ctrl.Click("wodeduiwu", DELAY[1], DELAY[0])

        self.ctrl.Click("team-config-page-3", DELAY[1], DELAY[0])
        self.ctrl.Click("team-config-next-1", DELAY[1], DELAY[0])


    def __MainPageInit(self):
        #self.ctrl.ScreenShot()
        self.ctrl.LocInjection("fangyusheding", "1")


    def __ChangeTeamPageInit(self):
        #self.ctrl.ScreenShot()
        self.ctrl.LocInjection("team-config-page-1-selected", "2")
        self.ctrl.LocInjection("team-config-page-2", "2")
        self.ctrl.LocInjection("team-config-page-3", "2")
        self.ctrl.LocInjection("wodeduiwu", "2")
        self.ctrl.LocInjection("team-config-next-1", "2")

    def __MyteamPageInit(self):
        #self.ctrl.ScreenShot()
        self.ctrl.LocInjection("myteam-1", "3")
        self.ctrl.LocInjection("myteam-2", "3")
        self.ctrl.LocInjection("myteam-3", "3")
        self.ctrl.LocInjection("myteam-guanbi", "3")
        self.ctrl.LocInjection("shengxu", "3")
        self.ctrl.LocInjection_Mul("hujiao", "3")


    def __GetRandomTeam(self) -> list:
        rdlis = self.ctrl.GetRandomList( [1, 2, 3] )
        rdid = 1 + self.ctrl.GetRadomInt(3)

        #避免换队和上次重复的问题
        while(True):
            if (not self.__lastTeamLog):
                break
            
            flag = False
            if rdid == self.__lastTeamLog[0]:
                for index in range(3):
                    if rdlis[index] == self.__lastTeamLog[index+1]:
                        flag = True
            
            if flag:
                rdlis = self.ctrl.GetRandomList( [1, 2, 3] )
                rdid = 1 + self.ctrl.GetRadomInt(3)
            else:
                break
            
        tmplis = [rdid]
        self.__lastTeamLog = tmplis + rdlis
        #print(self.__lastTeamLog)

        return (rdid, rdlis)


    """ def SelectMyTeam(self):
        rd_teamlis = self.ctrl.GetRandomList( [1, 2, 3] )
        team_name = "myteam-" + str(self.ctrl.GetRadomInt(3))

        rd_int = self.ctrl.GetRadomInt(3)
        team_grouplis = [x + rd_int * 3  for x in range(3)]
        hujiao_1_loc = self.ctrl.GetLocationByName("hujiao-1")
        hujiao_2_loc = self.ctrl.GetLocationByName("hujiao-2")

        if (not self.__isInit):
            myteam_2_loc = self.ctrl.GetLocationByName("myteam-2")
            self.delta_hujiao_loc = hujiao_2_loc[1] - hujiao_1_loc[1]
            self.swipe_area = [myteam_2_loc[0], hujiao_2_loc[1] + hujiao_2_loc[3], 
                                hujiao_2_loc[0] + hujiao_2_loc[2] - myteam_2_loc[0], 
                                self.delta_hujiao_loc - hujiao_2_loc[3]]
            self.match_area = [hujiao_2_loc[1], hujiao_1_loc[1] + 2 * self.delta_hujiao_loc]
            #test.ShowImageMatchPointByName("3", self.swipe_area)
            print(self.match_area)
            #test.ShowLinesOnImgByName("3", (970, self.match_area[0]), (970, self.match_area[1]))

        team_grouplis = [0, 1, 2]

        hujiao_loclis = [[hujiao_1_loc[0], hujiao_1_loc[1] + x * self.delta_hujiao_loc, 
                                hujiao_1_loc[2], hujiao_1_loc[3]] for x in team_grouplis]
        print(hujiao_loclis)

        for cnt in range(3):
            #self.ctrl.Click(team_name, DELAY[1], DELAY[0])
            hujiao_loc = hujiao_loclis[cnt]
            while(hujiao_loc[1] - hujiao_1_loc[1] > 4 * self.delta_hujiao_loc):
                startp, endp = self.__RandomSwipeLines(2 * self.delta_hujiao_loc + 2, 
                                                        int(2.4 * self.delta_hujiao_loc - 2))
                self.ctrl.Swipe(startp, endp, DELAY[1])
                hujiao_loc[1] -= (startp[1] - endp[1])
                
                print(hujiao_loc)

            if (hujiao_loc[1] + hujiao_loc[3] < self.match_area[1]):
                print(1)
                #self.ctrl.ScreenShot()
                #test.ShowImageMatchPointByName("screencap", hujiao_loc)
            elif (hujiao_loc[1]<self.match_area[1] and hujiao_loc[1]+hujiao_loc[3]>self.match_area[1]):
                print(2)
                startp, endp = self.__RandomSwipeLines(hujiao_loc[1]+hujiao_loc[3]-self.match_area[1], 
                                                        hujiao_loc[1] - self.match_area[0])
                self.ctrl.Swipe(startp, endp, DELAY[1])
                hujiao_loc[1] -= (startp[1] - endp[1])
                print(hujiao_loc[1])
                #self.ctrl.ScreenShot()
                #test.ShowImageMatchPointByName("screencap", hujiao_loc)
            else:
                print(3)
                startp, endp = self.__RandomSwipeLines(hujiao_loc[1]+hujiao_loc[3]-self.match_area[1], 
                                                        hujiao_loc[1] - self.match_area[0])
                startp = (970, 410)
                endp = (970, 252)
                print(startp)
                print(endp)
                self.ctrl.ScreenShot()
                test.ShowLinesOnImgByName("screencap", startp, endp)
                self.ctrl.Swipe(startp, endp, DELAY[1])
                hujiao_loc[1] -= (startp[1] - endp[1])
                print(hujiao_loc[1])
                self.ctrl.ScreenShot()
                test.ShowImageMatchPointByName("screencap", hujiao_loc)

                print(self.imgHdl.GetLocationByImageName_Mul("screencap", "hujiao", testshow=True))

        self.__isInit = True """

    

    def Atest(self):
        st, ed = self.__RandomSwipeLines(100,200)
        self.ctrl.Swipe(st, ed)
        pass




    def __RandomSwipeLines(self, low, high):
        '''
        随机上下滑动，滑动起始点在rd_point_st区域中随机
        滑动距离在[low, high]中随机
        :param low: 随机范围下界
        :param high: 随即范围上界
        :return 滑动起始点和结束点列表
        '''
        rd_point_st = self.ctrl.GetRandomLoc(self.swipe_area)
        rd_dist = random.randint(low, high)
        rd_res = random.randint(6, 20)
        if (random.randint(0,3) == 0):
            rd_res = -rd_res

        rd_point_ed = (rd_point_st[0] + rd_res, rd_point_st[1] - rd_dist)

        return (rd_point_st, rd_point_ed)