#-*- coding: UTF-8-*-
import time

import sys
import autod
import connect as cn

def StartConnect():
    while(True):
        print("准备连接模拟器")
        flag = cn.Connect()

        if(flag):
            break
        else:
            while(True):
                print("是否重新连接y/n")
                msg = input()
                if (msg == 'y'):
                    break
                elif (msg == 'n'):
                    sys.exit()
                else:
                    print("输入格式错误,请重新输入")


if __name__ == "__main__":

    """ time.sleep(2)
    at = autod.AutoD()
    at.Start() """

    at = autod.AutoD()

    active = True
    while active:

        StartConnect()

        print("请输入指令")
        print("start开始脚本    quit退出")
        msg = input()
        if msg == "start":
            print("===========开始运行==============")
            print("输入ctrl+C停止程序")
            consis = True

            count = at.GetShutDownTime()*60


            timeout = int(time.time() + count)
            sttime = timeout - count

            if count > 0:
                #如果有设计定时器
                print("倒计时{}s后关闭脚本".format(count))

                while consis and time.time() < timeout:
                    print("已运行{}s时间".format(int(time.time()-sttime)))
                    time.sleep(at.InitSleepTime())
                    at.Start()
            else:
                #如果未设置定时器
                while consis:
                    time.sleep(at.InitSleepTime())
                    at.Start()
            active = False
            print("定时关闭")
        elif msg == "quit":
            active = False

        print("=======================")
    
    print("已退出脚本")