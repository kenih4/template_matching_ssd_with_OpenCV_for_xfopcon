#-*- coding:utf-8 -*-
"""
python template_matching_ssd_with_OpenCV_for_xfopcon.py xfopcon-09.png xfopcon-09_cathodeFB.png xfopcon-09_chopperFB.png xfopcon-09_alarmvoice.png
python template_matching_ssd_with_OpenCV_for_xfopcon.py xfopcon-04.png xfopcon-04_cathodeFB.png xfopcon-04_chopperFB.png xfopcon-04_unitchange.png


Necessary module
pip install opencv-python
pip install numpy
pip install pillow
"""
import sys
import cv2
import numpy as np
import time
from tkinter import messagebox

import subprocess

def template_maching(input, target):
#    print(input.shape)
#    print(target.shape)

    output = input.copy()

#    gray = cv2.cvtColor(input, cv2.COLOR_RGB2GRAY)   
#    target = cv2.cvtColor(target, cv2.COLOR_RGB2GRAY)
#    gray = cv2.cvtColor(input, cv2.COLOR_RGB2BGR)   
#    target = cv2.cvtColor(target, cv2.COLOR_RGB2BGR)   

 #   cv2.namedWindow("out", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
 #   cv2.imshow("out",gray)

    print(input.shape)
    print(target.shape)

#    h, w = target.shape
    h, w, c = target.shape
#    print (h)

    # テンプレートマッチング（OpenCVで実装）
#    match = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)   #cv2.TM_SQDIFF)
    match = cv2.matchTemplate(input, target, cv2.TM_CCOEFF_NORMED)   #cv2.TM_SQDIFF)
#    print (match)
#    threshold = 0.8
#    loc = np.where(match >= threshold)
#    print (loc)

    min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
    pt = max_pt #min_pt
    print('max value(類似度): {}, position: {}'.format(max_value, max_pt))
#    print('min value: {}, position: {}'.format(min_value, min_pt))
#   ※比較方法がcv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMEDの場合は類似度が高いほど小さくなるのでminが類似度の高い領域になる

#    print('matching: {}'.format(max_value))
    if max_value < 0.99:
        print('Not match!!!!!!!!!!!!! {}'.format(max_value))
        return output,False

    print('pt[0]: {}, pt[1] {}'.format(pt[0], pt[1]))
    cv2.rectangle(output, (pt[0], pt[1] ), (pt[0] + w, pt[1] + h), (0,0,200), 3)    
    cv2.imwrite("output.png", output)
#    cv2.imshow('result',output)
#    cv2.waitKey(0)
    return output,True

def main():

    print("arg len:",len(sys.argv))
    print("argv:",sys.argv)
    if len(sys.argv) <= 1:
        print("Arg NONE:    Set input img!")
        return
    if len(sys.argv) <= 2:
        print("Arg NONE:    Set target img!")
        return



#    result = subprocess.check_output('\"C:\\Program Files (x86)\\WinSCP\\WinSCP.exe\" /console /script=\"getscript.txt\" /parameter \"C:\\me\\template_matching\" \"/home/xfel/xfelopr/kenichi/screenshot_loop/xfopcon-09.png\"'   , shell=True)
#    print(result.decode())
#    exit()
#    """
    cmd = '\"C:\\Program Files (x86)\\WinSCP\\WinSCP.exe\" /console /script=\"getscript.txt\" /parameter \"C:\\me\\template_matching\" \"/home/xfel/xfelopr/kenichi/screenshot_loop/' + sys.argv[1]
    print(cmd)
#    exit()
    try:
        print(subprocess.run(cmd , shell=True, stdout=subprocess.PIPE , stderr=subprocess.STDOUT))
#       print(subprocess.run('\"C:\\Program Files (x86)\\WinSCP\\WinSCP.exe\" /console /script=\"getscript.txt\" /parameter \"C:\\me\\template_matching\" \"/home/xfel/xfelopr/kenichi/screenshot_loop/xfopcon-09.png\"' , shell=True, stdout=subprocess.PIPE , stderr=subprocess.STDOUT))
    except:
        print('失敗')
#    exit()
#    """
    print("arg1:" + sys.argv[1])

    targets = [[]]
    for num in range(2, len(sys.argv)):
        print("num: " + str(num) + "    " + sys.argv[num])
        targets.append([sys.argv[num],False])

    print(targets)
    del targets[0]
    print(targets)

    input = cv2.imread(sys.argv[1])

    """
    input = cv2.imread("xfopcon-09.png")
    targets = [["xfopcon-09_cathodeFB.png",False]]
    targets.append(["xfopcon-09_chopperFB.png",False])
    targets.append(["xfopcon-09_alarmvoice.png",False])
    """

 #   print(input.shape)
 #   print(input.dtype)
#    cv2.namedWindow("image", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
#    cv2.imshow("image",input)
#    time.sleep(3)

    ans = ""
    for target in targets:
        print (target[0])
        t = cv2.imread(target[0])
        input,res = template_maching(input, t)
#        print('res: ', res)
        if res == True:
            ans += target[0]    + "\n"  

#    print (ans)
    print('Ans: ', ans)
    if ans != "":
        messagebox.showinfo("title", ans)
        cv2.namedWindow('result', cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
        cv2.imshow('result',input)
        cv2.waitKey(0)


if __name__ == "__main__":
    main()