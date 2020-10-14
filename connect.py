#-*- coding: UTF-8-*-

import time
import subprocess as subp
import myexcept as myex
import chardet

ADB_SERVER = "adb_server"
SIMU_NAME = "mumu"
simulator_port = {
    "mumu":7555
}

def ConnectSimulator():
    try:
        result = subp.Popen("{} devices".format(ADB_SERVER), shell=True, stdout=subp.PIPE)
        output = result.stdout.read().decode('utf-8')
        #print(output)

        if (output.find("List of devices attached") == -1):
            raise myex.UnfindAdbException("未找到adb程序")

        result = subp.Popen("{} connect 127.0.0.1:{}".format(ADB_SERVER, 
                        simulator_port[SIMU_NAME]), shell=True, stdout=subp.PIPE)
        
        output = result.stdout.read().decode('utf-8')
        #print(output)
        #out, err = result.communicate(timeout=5)
        #print(out)
        #output = out.decode(encoding='utf-8')
        #print(output)

        if (output.find("cannot connect")):
            raise myex.UnfindSimulatorException("未找到模拟器")

        result = subp.Popen("{} devices".format(ADB_SERVER), shell=True, stdout=subp.PIPE)
        output = result.stdout.read().decode('utf-8')

        if (output.find("127.0.0.1") == -1):
            raise myex.ConnectException("连接失败")
        
        return True

    except OSError as osex:
        print("输入指令失败")
        return False
        
    except myex.UnfindAdbException as adbex:
        print("发生异常")
        print(adbex)
        return False

    except myex.UnfindSimulatorException as simuex:
        print("发生异常")
        print(simuex)
        return False

    except myex.ConnectException as conex:
        print("发生异常")
        print(conex)
        return False