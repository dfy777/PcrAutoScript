#-*- coding: UTF-8-*-
from configparser import ConfigParser

import controller

cf = ConfigParser()
cf.read('config.ini',encoding='utf-8')
cf_map = dict(cf.items('progress'))

IS_MATCH_IMAGE_BYLOC = cf_map['ismatchimagebyloc'] != "false"
IS_RECORD_LOC = cf_map['isrecordloc'] != "false"
TEAM_NUM = int(cf_map['teamnum'])
DELAY = list(map(float, cf_map['delaylist'].replace(' ', '').split(",")))

class AutoD:
    def __init__(self) -> None:
        self.ctrl = controller.Controller()


    def Start(self) -> None:
        #=============mainpage=================
        self.MainPageInit()
        self.ctrl.Click("fangyusheding", DELAY[1], DELAY[0])

        #========change team page==============
        self.ChangeTeamPageInit()
        for page in range(3):
            #self.ctrl.Click("avator-cancel", 0.1, 0.1)
            self.ctrl.ContinousClick("avator-cancel", 5, 0.1, 0.1)
            if (page == 0):
                self.ctrl.Click("team-config-next-1", DELAY[0], DELAY[0])
            elif (page == 1):
                self.ctrl.Click("team-config-next-2", DELAY[0], DELAY[0])
            else:
                self.ctrl.Click("wodeduiwu", DELAY[0], DELAY[0])

        #===========choose myteam page============
        self.MyteamPageInit()
        team_randomlis = self.ctrl.GetRandomList( [1, 2, 3] )
        team_name = "myteam-" + str(1 + self.ctrl.GetRadomInt(3))

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


    def MainPageInit(self):
        self.ctrl.ScreenShot()
        self.ctrl.LocInjection("fangyusheding", "1")


    def ChangeTeamPageInit(self):
        self.ctrl.ScreenShot()
        self.ctrl.LocInjection("team-config-page-1-selected", "2")
        self.ctrl.LocInjection("team-config-page-2", "2")
        self.ctrl.LocInjection("team-config-page-3", "2")
        self.ctrl.LocInjection("wodeduiwu", "2")
        self.ctrl.LocInjection("team-config-next-1", "2")

    def MyteamPageInit(self):
        self.ctrl.ScreenShot()
        self.ctrl.LocInjection("myteam-1", "3")
        self.ctrl.LocInjection("myteam-2", "3")
        self.ctrl.LocInjection("myteam-3", "3")
        self.ctrl.LocInjection("myteam-guanbi", "3")
        self.ctrl.LocInjection("shengxu", "3")
        self.ctrl.LocInjection_Mul("hujiao", "3")
