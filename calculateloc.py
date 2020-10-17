import jsonos as jsos
import cal
import cv2
import test


def CalculateLoc():
    js_dict = {}

    #1
    js_dict["fangyusheding"] = cal.GetLocationByImageName("1", "fangyusheding")
    

    #2
    js_dict["team-config-page-1-selected"] = cal.GetLocationByImageName("2", "team-config-page-1-selected")
    js_dict["team-config-page-1"] = js_dict["team-config-page-1-selected"]

    js_dict["team-config-page-2"] = cal.GetLocationByImageName("2", "team-config-page-2")
    js_dict["team-config-page-2-selected"] = js_dict["team-config-page-2"]

    js_dict["team-config-page-3"] = cal.GetLocationByImageName("2", "team-config-page-3")
    js_dict["team-config-page-3-selected"] = js_dict["team-config-page-3"]

    js_dict["team-config-next-1"] = cal.GetLocationByImageName("2", "team-config-next-1")
    js_dict["team-config-next-2"] = js_dict["team-config-next-1"]
    js_dict["bianzuwancheng"] =     js_dict["team-config-next-1"]

    js_dict["wodeduiwu"] = cal.GetLocationByImageName("2", "wodeduiwu")


    #3
    js_dict["shengxu"] = cal.GetLocationByImageName("3", "shengxu")
    js_dict["jiangxu"] = js_dict["shengxu"]

    js_dict["myteam-1"] = cal.GetLocationByImageName("3", "myteam-1")
    js_dict["myteam-2"] = cal.GetLocationByImageName("3", "myteam-2")
    js_dict["myteam-3"] = cal.GetLocationByImageName("3", "myteam-3")

    js_dict["myteam-guanbi"] = cal.GetLocationByImageName("3", "myteam-guanbi")

    hujiao_lis = cal.GetLocationByImageName_Mul("3", "hujiao")
    js_dict["hujiao-1"] = hujiao_lis[0]
    js_dict["hujiao-2"] = hujiao_lis[1]

    jsos.WriteJsonDict(js_dict)



def CalculateLoc_Test():
    js_dict = jsos.ReadJson()
    img1 = cv2.imread('.\sources\{}.png'.format(1), 0)
    img2 = cv2.imread('.\sources\{}.png'.format(2), 0)
    img3 = cv2.imread('.\sources\{}.png'.format(3), 0)

    #1
    test.ShowImageMatchPoint(img1, js_dict["fangyusheding"])

    #2
    test.ShowImageMatchPoint(img2, js_dict["team-config-page-1"])
    test.ShowImageMatchPoint(img2, js_dict["team-config-page-1-selected"])
    test.ShowImageMatchPoint(img2, js_dict["team-config-page-2"])
    test.ShowImageMatchPoint(img2, js_dict["team-config-page-2-selected"])
    test.ShowImageMatchPoint(img2, js_dict["team-config-page-3"])
    test.ShowImageMatchPoint(img2, js_dict["team-config-page-3-selected"])
    test.ShowImageMatchPoint(img2, js_dict["team-config-next-1"])
    test.ShowImageMatchPoint(img2, js_dict["team-config-next-2"])
    test.ShowImageMatchPoint(img2, js_dict["wodeduiwu"])
    test.ShowImageMatchPoint(img2, js_dict["bianzuwancheng"])

    #3
    test.ShowImageMatchPoint(img3, js_dict["shengxu"])
    test.ShowImageMatchPoint(img3, js_dict["jiangxu"])
    test.ShowImageMatchPoint(img3, js_dict["myteam-1"])
    test.ShowImageMatchPoint(img3, js_dict["myteam-2"])
    test.ShowImageMatchPoint(img3, js_dict["myteam-3"])
    test.ShowImageMatchPoint(img3, js_dict["myteam-guanbi"])
    test.ShowImageMatchPoint(img3, js_dict["hujiao-1"])
    test.ShowImageMatchPoint(img3, js_dict["hujiao-2"])