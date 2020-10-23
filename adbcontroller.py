#-*- coding: UTF-8-*-
import os
import random
import time
from configparser import ConfigParser

import imghandle

cf = ConfigParser()
cf.read('config.ini', encoding='utf-8')
cf_map = dict(cf.items('cal'))

BORDER_PIXCEL = int(cf_map['borderpixel'])
DELAY = float(cf_map['delay'])
DEFAULT_NAME = cf_map['defaultname']

class AdbController:
    def __init__(self):
        self.__imgHdl = imghandle.ImgHandle()
        pass

    def ClickByPoint(self, location, const_delay=DELAY, random_delay=DELAY):
        cmd_tap = 'adb_server shell input tap {} {}'.format(
                    str(location[0]), str(location[1]))

        os.system(cmd_tap)
        time.sleep(self.__GetRandomTime(const_delay, random_delay))


    def ClickInRandomArea(self, location, const_delay=DELAY, random_delay=DELAY):
        ptx, pty, inc_x, inc_y = location[:4]
        #避免取到边界点
        x = random.randint(ptx + BORDER_PIXCEL, 
                                ptx + inc_x - BORDER_PIXCEL)
        y = random.randint(pty + BORDER_PIXCEL,
                                pty + inc_y - BORDER_PIXCEL)

        cmd_tap = 'adb_server shell input tap {} {}'.format(str(x), str(y))
        os.system(cmd_tap)
        time.sleep(self.__GetRandomTime(const_delay, random_delay))


    def ClickMultipleTimes(self, location, times, const_delay=DELAY, random_delay=DELAY):
        ptx, pty, inc_x, inc_y = location[:4]
        #避免取到边界点
        x = random.randint(ptx + 15, ptx + inc_x - 15)
        y = random.randint(pty + 15, pty + inc_y - 15)
        
        loc_range = (x - 15, y - 15, 15 * 2, 15 * 2)

        for cnt in range(times):
            self.ClickInRandomArea(loc_range, const_delay, random_delay)


    def ClickByTemplate(self, name, const_delay=DELAY, random_delay=DELAY):
        self.ScreenShot(DEFAULT_NAME)
        loc = self.__imgHdl.GetLocationByImageName(DEFAULT_NAME, name)
        if (loc):
            self.ClickInRandomArea(loc, const_delay, random_delay)


    def ScreenShot(self, name=DEFAULT_NAME):
        cmd_cap = 'adb_server shell screencap -p /sdcard/{}.png'.format(name)
        cmd_pull = 'adb_server pull sdcard/{}.png C:\Projects\PcrArenaDefend\sources'.format(name)

        os.system(cmd_cap)
        os.system(cmd_pull)
        time.sleep(self.__GetRandomTime(const=1, delay=0))    


    def __GetRandomTime(self, const, delay=0):
        return const + random.random() * delay
