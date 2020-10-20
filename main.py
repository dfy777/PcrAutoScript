import time
import os

import cal
import connect as cn
import jsonos as jsos
import progress as pg
import calculateloc as cloc
from configparser import ConfigParser


if __name__ == "__main__":
    
    #cloc.CalculateLoc_Test()

    active = True
    while active:
        print("请输入指令")
        print("start开始脚本\nquit结束脚本")
        cn.ConnectSimulator()
        msg = input()
        if msg == "start":
            print("===========开始运行==============")
            print("输入ctrl+C停止程序")
            consis = True
            while(consis):
                time.sleep(cal.GetRandomTime(0, 10))
                pg.Start()
        elif msg == "quit":
            active = False

        print("=======================")
    
