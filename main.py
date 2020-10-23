#-*- coding: UTF-8-*-
import test
import time
import random

import autod
import connect as cn

if __name__ == "__main__":

    """ time.sleep(2)
    at = autod.AutoD()
    at.Start() """

    at = autod.AutoD()

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
                time.sleep(random.random() * 10)
                at.Start()
        elif msg == "quit":
            active = False

        print("=======================")
    
