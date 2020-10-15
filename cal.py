#-*- coding: UTF-8-*-
import cv2
import test
import os
import random
import time

from configparser import ConfigParser

cf = ConfigParser()
cf.read('config.ini', encoding='utf-8')
cf_map = dict(cf.items('cal'))

BORDER_PIXCEL = int(cf_map['borderpixel'])
DELAY = float(cf_map['delay'])
DEFAULT_NAME = cf_map['defaultname']

nameDic = {
    "avator-cancel":"avator-cancel",
    "pjjc-team-config":"pjjc-team-config-1",
    "team-config-next-1":"team-config-next-1",
    "team-config-next-2":"team-config-next-2",
    "team-config-next-3":"team-config-next-3",
    "team-config-page-1":"team-config-page-1",
    "team-config-page-1-selected":"team-config-page-1-selected",
    "team-config-page-2":"team-config-page-2",
    "team-config-page-2-selected":"team-config-page-2-selected",
    "team-config-page-3":"team-config-page-3",
    "team-config-page-3-selected":"team-config-page-3-selected",
    "myteam-1":"myteam-1",
    "myteam-2":"myteam-2",
    "myteam-3":"myteam-3",
    "myteam-guanbi":"myteam-guanbi",
    "bianzuwancheng":"bianzuwancheng",
    "hujiao":"hujiao",
    "fangyusheding":"fangyusheding",
    "shengxu":"shengxu",
    "jiangxu":"jiangxu",
    "wodeduiwu":"wodeduiwu"
}


def GetLocationByImageName(img, template, testshow=False):
    img = cv2.imread('.\sources\{}.png'.format(img), 0)
    template = cv2.imread('.\sources\{}.png'.format(template), 0)

    return GetLocationByImageMatch(img, template, testshow=testshow)


def GetLocationByImageName_Mul(img, template, testshow=False):
    img = cv2.imread('.\sources\{}.png'.format(img), 0)
    template = cv2.imread('.\sources\{}.png'.format(template), 0)

    return GetLocationByImageMatch_Mul(img, template, testshow=testshow)


def GetLocationByImageMatch(img, template, testshow=False):
    py, px = template.shape[:2]

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    loc = (max_loc[0], max_loc[1], px, py)

    if testshow:
        test.ShowImageMatchPoint(img, loc)

    if max_val > 0.85:
        return loc
    else:
        return False

def GetLocationByImageMatch_Mul(img, template, testshow=False):
    py, px = template.shape[:2]
    origin_img = img

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    loc_lis = [(max_loc[0], max_loc[1], px, py)]

    while (True):
        origin_img = cv2.rectangle(origin_img, (max_loc[0], max_loc[1]), (max_loc[0] + px, max_loc[1] + py),
                                (255,0,0), thickness=-1 )
        img = origin_img

        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if (max_val < 0.9):
            break

        loc_lis.append( (max_loc[0], max_loc[1], px, py) )

    if (testshow == True):
        for item in loc_lis:
            test.ShowImageMatchPoint(img, item)

    #sort by y coordinates
    loc_lis.sort(key=lambda x:x[1])
    return loc_lis



def GetRandomTime(const, delay=0):
    const = const + random.random() * delay
    return const


def GetRandomList(rd_list):
    random.shuffle(rd_list)
    return rd_list

def GetRadomInt(rd_int):
    rd_int = random.randint(0, rd_int-1)
    return rd_int


def ClickByPoint(location, delay_const=DELAY, delay_random=DELAY):
    cmd_tap = 'adb_server shell input tap {} {}'.format(
                str(location[0]), str(location[1]))

    os.system(cmd_tap)
    time.sleep(GetRandomTime(delay_const, delay_random))


def ClickInRandomArea(location, delay_const=DELAY, delay_random=DELAY):
    
    ptx, pty, inc_x, inc_y = location[:4]
    #避免取到边界点
    x = random.randint(ptx + BORDER_PIXCEL, 
                            ptx + inc_x - BORDER_PIXCEL)
    y = random.randint(pty + BORDER_PIXCEL,
                            pty + inc_y - BORDER_PIXCEL)

    cmd_tap = 'adb_server shell input tap {} {}'.format(str(x), str(y))
    os.system(cmd_tap)
    time.sleep(GetRandomTime(delay_const, delay_random))


def ClickByTemplate(name, delay_const=DELAY, delay_random=DELAY):
    ScreenShot(DEFAULT_NAME)
    loc = GetLocationByImageName(DEFAULT_NAME, name)
    if (loc):
        ClickInRandomArea(loc, delay_const, delay_random)


def ScreenShot(name="screencap"):
    cmd_cap = 'adb_server shell screencap -p /sdcard/{}.png'.format(name)
    cmd_pull = 'adb_server pull sdcard/{}.png C:\Projects\PcrArenaDefend\sources'.format(name)

    os.system(cmd_cap)
    os.system(cmd_pull)
    time.sleep(GetRandomTime(DELAY*2))