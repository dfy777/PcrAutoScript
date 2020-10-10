import cv2
import os

SIMULATOR_RESOLUTION = [1280, 720]

'''
显示matchtemplate匹配区在原图上的位置
'''
def ShowImageMatchPoint(img, location):
    img_x, img_y = SIMULATOR_RESOLUTION[:2]
    
    px, py, tmp_x, tmp_y = location[:4]

    if (py + tmp_y > img_y):
        tmp_y = img_y - py
    
    if (px + tmp_x > img_x):
        tmp_x = img_x - px

    img_show = cv2.rectangle(img, (px, py), (px+tmp_x, py+tmp_y),
                                (0,255,0), 2)
    
    cv2.imshow("img_show", img_show)
    cv2.waitKey(0)