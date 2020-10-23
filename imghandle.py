#-*- coding: UTF-8-*-
import test

import cv2


class ImgHandle:

    def __init__(self):
        pass


    def GetLocationByImageName(self, img, template, testshow=False):
        img = cv2.imread('.\sources\{}.png'.format(img), 0)
        template = cv2.imread('.\sources\{}.png'.format(template), 0)

        return self.__GetLocationByImageMatch(img, template, testshow=testshow)


    def GetLocationByImageName_Mul(self, img, template, testshow=False):
        img = cv2.imread('.\sources\{}.png'.format(img), 0)
        template = cv2.imread('.\sources\{}.png'.format(template), 0)

        return self.__GetLocationByImageMatch_Mul(img, template, testshow=testshow)


    def __GetLocationByImageMatch(self, img, template, testshow=False):
        py, px = template.shape[:2]

        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        loc = (max_loc[0], max_loc[1], px, py)

        if testshow:
            test.ShowImageMatchPoint(img, loc)

        if max_val > 0.85:
            return loc
        else:
            return False

    def __GetLocationByImageMatch_Mul(self, img, template, testshow=False):
        py, px = template.shape[:2]
        origin_img = img

        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        loc_lis = [(max_loc[0], max_loc[1], px, py)]

        while (True):
            origin_img = cv2.rectangle(origin_img, (max_loc[0], max_loc[1]), (max_loc[0] + px, max_loc[1] + py),
                                    (255,0,0), thickness=-1 )
            img = origin_img

            result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            if (max_val < 0.9):
                break

            loc_lis.append( (max_loc[0], max_loc[1], px, py) )

        if (testshow == True):
            for item in loc_lis:
                test.ShowImageMatchPoint(img, item)

        #sort by y coordinates
        loc_lis.sort(key=lambda x:x[1])
        return loc_lis

    '''
    判断一张图片是否为纯色
    是纯色返回True
    '''
    def CheckIsBrokenImg(self, name) -> bool:
        img = cv2.imread('.\sources\{}.png'.format(name))

        py, px = img.shape[:2]
        num_lis = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        result = True
        img_color = img[int(py*0.1), int(px*0.1)]

        for it in num_lis:
            #print(img[int(py*it), int(px*it)])
            if (img_color != img[int(py*it), int(px*it)]).all():
                result = False
                break

        return result
