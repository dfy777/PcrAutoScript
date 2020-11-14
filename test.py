#-*- coding: UTF-8-*-
import cv2
from configparser import ConfigParser

cf = ConfigParser()
cf.read('config.ini', encoding='utf-8')
cf_map = dict(cf.items('test'))

SIMULATOR_RESOLUTION = cf_map['simuresolution'].replace(' ','').split(',')
SIMULATOR_RESOLUTION[0] =  int(SIMULATOR_RESOLUTION[0])
SIMULATOR_RESOLUTION[1] =  int(SIMULATOR_RESOLUTION[1])

'''
显示matchtemplate匹配区在原图上的位置
'''
def ShowImageMatchPoint(img, location, name="img_show"):
    img_x, img_y = SIMULATOR_RESOLUTION[:2]
    
    px, py, tmp_x, tmp_y = location[:4]

    if (py + tmp_y > img_y):
        tmp_y = img_y - py
    
    if (px + tmp_x > img_x):
        tmp_x = img_x - px

    img_show = cv2.rectangle(img, (px, py), (px+tmp_x, py+tmp_y),
                                (0,255,0), 2)
    
    cv2.imshow(name, img_show)
    cv2.waitKey(0)


'''
根据起始点在原图显示直线
'''
def ShowLinesOnImg(img, start, end, name="img_show"):
    img_show = cv2.line(img, start, end, (0, 0, 255), 2)

    cv2.imshow(name, img_show)
    cv2.waitKey(0)


def ShowImageMatchPointByName(img_name, location):
    img = cv2.imread('.\sources\{}.png'.format(img_name))

    ShowImageMatchPoint(img, location, name=img_name)


def ShowLinesOnImgByName(img_name, start, end):
    img = cv2.imread('.\sources\{}.png'.format(img_name))
    ShowLinesOnImg(img, start, end, img_name)