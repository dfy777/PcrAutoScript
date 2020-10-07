import cv2
import os

'''
显示matchtemplate匹配区在原图上的位置
'''
def ShowImageMatchPoint(img, tmp_shape, left_upper_loc):
    img_y, img_x = img.shape[:2]
    tmp_y, tmp_x = tmp_shape[:2]

    px, py = left_upper_loc[:2]

    if (py + tmp_y > img_y):
        tmp_y = img_y - py
    
    if (px + tmp_x > img_x):
        tmp_x = img_x - px

    img_show = cv2.rectangle(img, (px, py), (px+tmp_x, py+tmp_y),
                                (0,255,0), 2)
    
    cv2.imshow("img_show", img_show)
    cv2.waitKey(0)