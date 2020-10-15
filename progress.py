import cal
import time
import jsonos as jsos
from configparser import ConfigParser

cf = ConfigParser()
cf.read('config.ini',encoding='utf-8')
cf_map = dict(cf.items('progress'))

IS_MATCH_IMAGE_BYLOC = cf_map['ismatchimagebyloc'] != "false"
IS_RECORD_LOC = cf_map['isrecordloc'] != "false"
TEAM_NUM = int(cf_map['teamnum'])
DELAY = list(cf_map['delaylist'].replace(' ', '').split(","))

def InitializeProgress():
    '''
    initial location.json
    get location of avator-cancel
    '''
    jsos.InitializeJson()
    
    avator_cancel_loc = cal.GetLocationByImageName(cal.nameDic["pjjc-team-config"],
                            cal.nameDic["avator-cancel"],testshow=True)
    
    jsos.WriteJson(cal.nameDic["avator-cancel"], avator_cancel_loc)
    #print(avator_cancel_loc)

def Start():
    PjjcMainPageScript()
    lis = PjjcTeamConfigScript()
    PjjcChangeTeamScript(lis)



def PjjcMainPageScript():
    loc = False
    if (IS_MATCH_IMAGE_BYLOC):
        loc = jsos.ReadJson(name=cal.nameDic["fangyusheding"])
        if loc[0] == -1:
            pass
        else:
            cal.ClickInRandomArea(loc)
            return
    
    cal.ScreenShot(cal.DEFAULT_NAME)
    loc = cal.GetLocationByImageName(cal.DEFAULT_NAME, 
                                    cal.nameDic["fangyusheding"])

    if (IS_RECORD_LOC):
        #TODO 记录
        pass
    cal.ClickInRandomArea(loc)


def PjjcTeamConfigScript():
    #gei avator-cancel location
    avator_loc = jsos.ReadJson(cal.nameDic["avator-cancel"])
    team_lis = [False, False, False, False, False]
    cal.ScreenShot(cal.DEFAULT_NAME)

    if (IS_MATCH_IMAGE_BYLOC):
        js_dict = jsos.ReadJson()
        team_lis[0] = js_dict[cal.nameDic["team-config-page-1-selected"]]
        team_lis[1] = js_dict[cal.nameDic["team-config-page-2"]]
        team_lis[2] = js_dict[cal.nameDic["team-config-page-3"]]
        team_lis[3] = js_dict[cal.nameDic["wodeduiwu"]]
        team_lis[4] = js_dict[cal.nameDic["bianzuwancheng"]]

        if ((team_lis[0][0] == -1)
                or (team_lis[1][0] == -1)
                or (team_lis[2][0] == -1) 
                or (team_lis[3][0] == -1)
                or (team_lis[4][0] == -1)):
            team_lis[0] = False
            team_lis[1] = False
            team_lis[2] = False
            team_lis[3] = False
            team_lis[4] = False

    if ((team_lis[0] == False)
            or (team_lis[1] == False)
            or (team_lis[2] == False) 
            or (team_lis[3] == False)
            or (team_lis[4] == False) ):
        team_lis[0] = cal.GetLocationByImageName(cal.DEFAULT_NAME,
                                cal.nameDic["team-config-page-1-selected"])
        team_lis[1] = cal.GetLocationByImageName(cal.DEFAULT_NAME,
                                cal.nameDic["team-config-page-2"])
        team_lis[2] = cal.GetLocationByImageName(cal.DEFAULT_NAME,
                                cal.nameDic["team-config-page-3"])
        team_lis[3] = cal.GetLocationByImageName(cal.DEFAULT_NAME, 
                                cal.nameDic["wodeduiwu"])
        team_lis[4] = cal.GetLocationByImageName(cal.DEFAULT_NAME,
                                cal.nameDic["team-config-next-1"], testshow=True)

    #cancel already exists avators
    for page in range(3):
        for index in range(5):
            cal.ClickInRandomArea(avator_loc, 0.2, 0.1)

        if (page == 0):
            cal.ClickInRandomArea(team_lis[1],DELAY[0], DELAY[0])
        elif (page == 1):
            cal.ClickInRandomArea(team_lis[2],DELAY[0], DELAY[0])
        else:
            cal.ClickInRandomArea(team_lis[3], DELAY[0], DELAY[0])

    if (IS_RECORD_LOC):
        #TODO   记录
        pass
    
    return team_lis


def PjjcChangeTeamScript(team_lis_loc):
    myteam_lis = [False, False, False]
    myteam_guanbi = False
    hujiao_lis = [False, False]
    shengxu_loc = False
    
    cal.ScreenShot(cal.DEFAULT_NAME)

    if (IS_MATCH_IMAGE_BYLOC):
        js_dict = jsos.ReadJson()
        myteam_lis[0] = js_dict[cal.nameDic["myteam-1"]]
        myteam_lis[1] = js_dict[cal.nameDic["myteam-2"]]
        myteam_lis[2] = js_dict[cal.nameDic["myteam-3"]]
        hujiao_lis[0] = js_dict[cal.nameDic["hujiao"]]
        hujiao_lis[1] = js_dict[cal.nameDic["hujiao"]]
        shengxu_loc = js_dict[cal.nameDic["shengxu"]]
        myteam_guanbi = js_dict[cal.nameDic["myteam-guanbi"]]
        
        if ((myteam_lis[0][0] == -1)
                or (myteam_lis[1][0] == -1)
                or (myteam_lis[2][0] == -1)
                or (hujiao_lis[0][0] == -1)
                or (hujiao_lis[1][0]) == -1
                or (shengxu_loc[0] == -1)
                or (myteam_guanbi[0] == -1)):
            myteam_lis[0] = False
            myteam_lis[1] = False
            myteam_lis[2] = False
            hujiao_lis[0] = False
            hujiao_lis[1] = False
            shengxu_loc = False
            myteam_guanbi = False
    
    if ((myteam_lis[0] == False)
            or (myteam_lis[1] == False)
            or (myteam_lis[2] == False)
            or (hujiao_lis[0] == False)
            or (hujiao_lis[1] == False)
            or (shengxu_loc == False)
            or (myteam_guanbi == False) ):
        myteam_lis[0] = cal.GetLocationByImageName(cal.DEFAULT_NAME,
                            cal.nameDic["myteam-1"])
        myteam_lis[1] = cal.GetLocationByImageName(cal.DEFAULT_NAME,
                            cal.nameDic["myteam-2"])
        myteam_lis[2] = cal.GetLocationByImageName(cal.DEFAULT_NAME,
                            cal.nameDic["myteam-3"])
        shengxu_loc = cal.GetLocationByImageName(cal.DEFAULT_NAME, 
                            cal.nameDic["shengxu"])
        hujiao_lis = cal.GetLocationByImageName_Mul(cal.DEFAULT_NAME, 
                            cal.nameDic["hujiao"])
        myteam_guanbi = cal.GetLocationByImageName(cal.DEFAULT_NAME,
                            cal.nameDic["myteam-guanbi"])

    team_randomlis = cal.GetRandomList( [1, 2, 3] )
    #myteam_loc = myteam_lis[cal.GetRadomInt(3)]
    myteam_loc = myteam_lis[1]
    team_index = 1


    for cnt in range(3):
        cal.ClickInRandomArea(myteam_loc, DELAY[1], DELAY[0])
        if (team_randomlis[cnt] == 1):
            cal.ClickInRandomArea(hujiao_lis[0], DELAY[1], DELAY[0])
        elif (team_randomlis[cnt] == 2):
            cal.ClickInRandomArea(hujiao_lis[1], DELAY[1], DELAY[0]) 
        else:
            cal.ClickInRandomArea(shengxu_loc, DELAY[1], DELAY[0])
            cal.ClickInRandomArea(hujiao_lis[0], DELAY[1], DELAY[0])

            if (cnt != 2):
                cal.ClickInRandomArea(team_lis_loc[3], DELAY[1], DELAY[0])
                cal.ClickInRandomArea(shengxu_loc, DELAY[1], DELAY[0])
                cal.ClickInRandomArea(myteam_guanbi, DELAY[1], DELAY[0])
        
        if (team_index >= 0):
            cal.ClickInRandomArea(team_lis_loc[team_index], DELAY[1], DELAY[0])
            cal.ClickInRandomArea(team_lis_loc[3], DELAY[1], DELAY[0])
            team_index -= 1

    cal.ClickInRandomArea(team_lis_loc[2], DELAY[1], DELAY[0])
    cal.ClickInRandomArea(team_lis_loc[4], DELAY[1], DELAY[0])