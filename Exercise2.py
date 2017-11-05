import os
import sys
import cv2
import numpy as np

DIRECT = "/home/grazianomj/Repositories/EC601_OpenCV/Resources/Test_Images/"

def main():
    if len(sys.argv) < 2:
        exit(1)
    BGRimg = cv2.imread(DIRECT+sys.argv[1], cv2.IMREAD_COLOR)
    YCCimg = cv2.cvtColor(BGRimg, cv2.COLOR_BGR2YCR_CB)
    HSVimg = cv2.cvtColor(BGRimg, cv2.COLOR_BGR2HSV)
    BGRchans = cv2.split(BGRimg)
    YCCchans = cv2.split(YCCimg)
    HSVchans = cv2.split(HSVimg)
    if ".png" in sys.argv[1]:
        ftype = ".png"
    else:
        ftype = ".jpg"
    target = "./Exercise2_Output/"+sys.argv[1].rstrip(ftype)+"/"
    if not os.path.exists(target):
        os.makedirs(target)
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Red"+ftype,
                BGRchans[2]
    )
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Green"+ftype,
                BGRchans[1]
    )
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Blue"+ftype,
                BGRchans[0]
    )
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Y"+ftype,
                YCCchans[0]
    )
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Cb"+ftype,
                YCCchans[1]
    )
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Cr"+ftype,
                YCCchans[2]
    )
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Hue"+ftype,
                HSVchans[0]
    )
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Saturation"+ftype,
                HSVchans[1]
    )
    cv2.imwrite(target+sys.argv[1].rstrip(ftype)+"_Value"+ftype,
                HSVchans[2]
    )

    print(BGRimg[20, 25])
    print(YCCimg[20, 25])
    print(HSVimg[20, 25])

if __name__ == "__main__":
    main()
