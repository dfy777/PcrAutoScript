import time
import os

import cal
import connect as cn
import jsonos as jsos
import progress as pg

'''
time.sleep(3)

cal.ClickByTemplate('xitongyingyong')
time.sleep(1)
cal.ClickByTemplate('xitong')
time.sleep(1)
cal.ClickByTemplate('gengduo')
time.sleep(1)
cal.ClickByTemplate('fanhui')
'''

#loc = (34, 123, 55, 55)
#js.WriteJson("avator-cancel", loc)
#js.WriteJson("team-config-next-1", loc)
#js.InitializeJson()


if __name__ == "__main__":
    #cal.InitializeProgress()
    #time.sleep(2)
    #pg.Start()
    active = True
    while active:
        print("请输入指令")
        print("start开始脚本\nquit结束脚本")
        msg = input()
        if msg == "start":
            if (cn.ConnectSimulator()):
                pg.Start()
        elif msg == "quit":
            active = False

        print("=======================")
    
