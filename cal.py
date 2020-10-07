import cv2
import test
import os
import random

BORDER_PIXCEL = 5

def GetImageByName(img, template):
    img = cv2.imread('.\sources\{}.png'.format(img), 0)
    template = cv2.imread('.\sources\{}.png'.format(template), 0)

    return GetImage(img, template)


def GetImage(img, template):
    py, px = template.shape[:2]

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #test.ShowImageMatchPoint(img, (py, px), max_loc)

    if max_val > 0.85:
        return [max_loc[0], max_loc[1], px, py]
    else:
        return False


def ClickByPoint(location):
    cmd_tap = 'adb_server shell input tap {} {}'.format(
                str(location[0]), str(location[1]))

    os.system(cmd_tap)


def ClickInRandomArea(location):
    
    ptx, pty, inc_x, inc_y = location[:4]
    #避免取到边界点
    x = random.randint(ptx + BORDER_PIXCEL, 
                            ptx + inc_x - BORDER_PIXCEL)
    y = random.randint(pty + BORDER_PIXCEL,
                            pty + inc_y - BORDER_PIXCEL)

    cmd_tap = 'adb_server shell input tap {} {}'.format(str(x), str(y))
    os.system(cmd_tap)


def ClickByTemplate(name):
    ScreenShot('main')
    loc = GetImageByName('main', name)
    if (loc):
        ClickInRandomArea(loc)


def ScreenShot(name):
    cmd_cap = 'adb_server shell screencap -p /sdcard/{}.png'.format(name)
    cmd_pull = 'adb_server pull sdcard/{}.png C:\Projects\PcrArenaDefend\sources'.format(name)

    os.system(cmd_cap)
    os.system(cmd_pull)
