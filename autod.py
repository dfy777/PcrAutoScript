import controller 
import jsonos as jsos
from configparser import ConfigParser

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


    def Start() -> None:
        pass


    def MainPageInit(self):
        self.ctrl.LocInjection("fangyusheding")

    def ChangeTeamPageInit(self):
        self.ctrl.LocInjection("team-config-page-1-selected")
        self.ctrl.LocInjection("team-config-page-2")
        self.ctrl.LocInjection("team-config-page-3")
        self.ctrl.LocInjection("wodeduiwu")
        self.ctrl.LocInjection("bianzuwancheng")