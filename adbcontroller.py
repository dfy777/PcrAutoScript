import os
import time
import random

import imghandle
from configparser import ConfigParser

cf = ConfigParser()
cf.read('config.ini', encoding='utf-8')
cf_map = dict(cf.items('cal'))

BORDER_PIXCEL = int(cf_map['borderpixel'])
DELAY = float(cf_map['delay'])
DEFAULT_NAME = cf_map['defaultname']

class AdbController:
    def __init__(self):
        #self.imgHdl = imghandle.ImgHandle()
        pass

    def ClickByPoint(self, location, delay_const=DELAY, delay_random=DELAY):
        cmd_tap = 'adb_server shell input tap {} {}'.format(
                    str(location[0]), str(location[1]))

        os.system(cmd_tap)
        time.sleep(self.__GetRandomTime(delay_const, delay_random))


    def ClickInRandomArea(self, location, delay_const=DELAY, delay_random=DELAY):
        
        ptx, pty, inc_x, inc_y = location[:4]
        #避免取到边界点
        x = random.randint(ptx + BORDER_PIXCEL, 
                                ptx + inc_x - BORDER_PIXCEL)
        y = random.randint(pty + BORDER_PIXCEL,
                                pty + inc_y - BORDER_PIXCEL)

        cmd_tap = 'adb_server shell input tap {} {}'.format(str(x), str(y))
        os.system(cmd_tap)
        time.sleep(self.__GetRandomTime(delay_const, delay_random))


    def ClickByTemplate(self, name, delay_const=DELAY, delay_random=DELAY):
        self.ScreenShot(DEFAULT_NAME)
        loc = self.GetLocationByImageName(DEFAULT_NAME, name)
        if (loc):
            self.ClickInRandomArea(loc, delay_const, delay_random)


    def ScreenShot(self, name="screencap"):
        cmd_cap = 'adb_server shell screencap -p /sdcard/{}.png'.format(name)
        cmd_pull = 'adb_server pull sdcard/{}.png C:\Projects\PcrArenaDefend\sources'.format(name)

        os.system(cmd_cap)
        os.system(cmd_pull)
        it = self.__GetRandomTime(DELAY*3)
        time.sleep(it)    


    def __GetRandomTime(self, const, delay=0):
        return const + random.random() * delay


    def __GetRandomList(self, rd_list):
        random.shuffle(rd_list)
        return rd_list

    def __GetRadomInt(self, rd_int):
        rd_int = random.randint(0, rd_int-1)
        return rd_int