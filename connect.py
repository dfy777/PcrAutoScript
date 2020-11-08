#-*- coding: UTF-8-*-

import time
import subprocess as subp
import myexcept as myex

from configparser import ConfigParser

cf = ConfigParser()
cf.read('config.ini', encoding='utf-8')
cf_map = dict(cf.items('connect'))

ADB_SERVER = cf_map['adbserver']
SIMU_NAME = cf_map['simuname']
simulator_port = {
    "mumu":7555,
    "xiaoyao":21503,
    "yeshen":62001,
    "haima":26944,
    "bluestacks":5555,
    "leidian":5555
}


def FindAdb():
    print("寻找adb程序。。。。。。")
    time.sleep(0.5)

    result = subp.Popen("{} devices".format(ADB_SERVER), shell=True, stdout=subp.PIPE)
    output = result.stdout.read().decode('utf-8')
    #print(output)

    #if not found text wanted
    if (output.find("List of devices attached") == -1):
        print(output)
        raise myex.UnfindAdbException("错误：未找到adb程序")

    print("adb程序已找到。。。。。。")
    return output


def ConnectSimulator(output):
    print("检查是否连接到{}模拟器。。。。。".format(SIMU_NAME))
    time.sleep(0.5)
    if (output.find("127.0.0.1") == -1):
        print("尚未连接到模拟器。。。。。")
        print("寻找{}模拟器。。。。。。".format(SIMU_NAME))
        time.sleep(0.5)
        result = subp.Popen("{} connect 127.0.0.1:{}".format(ADB_SERVER, 
                            simulator_port[SIMU_NAME]), shell=True, stdout=subp.PIPE)
        output = result.stdout.read().decode('utf-8')
        

        #if can not find simulator
        if (output.find("cannot connect") >= 0):
            print(output)
            print("未检查到{}模拟器".format(SIMU_NAME))
            raise myex.UnfindSimulatorException("错误：未找到模拟器")

        
        #checkout connect condition
        result = subp.Popen("{} devices".format(ADB_SERVER), shell=True, stdout=subp.PIPE)
        output = result.stdout.read().decode('utf-8')

        #if still not connect
        if (output.find("127.0.0.1") == -1):
            print(output)
            print("错误：连接失败")
            raise myex.ConnectException("错误：连接失败")

    print("连接成功！")
    
    return True


def Connect():
    try:

        #input adb command

        output = FindAdb()
        
        #checkout it has already connect or not
        #if not, input connect command
        
        result = ConnectSimulator(output)

        return result

    except OSError as osex:
        print("错误：输入指令失败")
        return False
        
    except myex.UnfindAdbException as adbex:
        print("错误：发生异常")
        print(adbex)
        return False

    except myex.UnfindSimulatorException as simuex:
        print("错误：发生异常")
        print(simuex)
        return False

    except myex.ConnectException as conex:
        print("错误：发生异常")
        print(conex)
        return False