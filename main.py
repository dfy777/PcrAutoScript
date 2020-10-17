import time
import os

import cal
import connect as cn
import jsonos as jsos
import progress as pg
import calculateloc as cloc
from configparser import ConfigParser


if __name__ == "__main__":
    
    cloc.CalculateLoc()
    #cloc.CalculateLoc_Test()

    active = False
    while active:
        print("请输入指令")
        print("start开始脚本\nquit结束脚本")
        msg = input()
        if msg == "start":
            #if (cn.ConnectSimulator()):
            time.sleep(2)
            print(pg.IS_MATCH_IMAGE_BYLOC)
            print(pg.IS_RECORD_LOC)
            pg.Start()
        elif msg == "quit":
            active = False

        print("=======================")
    
