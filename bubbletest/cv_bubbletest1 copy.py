import numpy as np
import os
import cv2
from imutils import contours
from fileRename import FileRename
from PicCut import PicCut
import random
#塗顏色用

scan_answer = [5]
circle_minheight = 50
circle_maxheight = 87
circle_minweight = 57
circle_maxweight = 80
ar_min = 0.84
ar_max = 1.4

def bubbletest(imgpath):
    img = cv2.imread(imgpath)
    height, weight, _ = img.shape # 獲取圖片尺寸
    img = cv2.resize(img, (500, int(weight * 500 / height))) # 改圖片顯示時的尺寸 
    imgc = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (3, 3), 0) #高斯模糊
    edged = cv2.Canny(blurred, 50, 200) #邊緣檢測（找出任何形式的邊緣）

    #cv2.imshow("edged", edged) 

    cnts, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #挑選出邊緣（要注意會挑到其他邊邊，下面要把它篩選掉）
    questionCnts = []
    cntnum = [] #for debug use
    num = 0 #for debug use
    
    for i in range(0, len(cnts)):
        cv2.drawContours(imgc, cnts[i], -1, (0, 0, 255), 3)
    
    
    ANSWER_KEY = {0: 0, 1: 2, 2: 1, 3: 1, 4: 3} #設定「考卷」的正解（作為測試辨識成功與否的一個依據）
    correct = 0
    
    
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c) 
        ar = w / float(h)
        print(str(num) + ": 寬 = " + str(w) + ", 高 = " + str(h))
        
        if w >= circle_minweight and w <= circle_maxweight and h >= circle_minheight and h <= circle_maxheight and ar >= ar_min and ar <= ar_max: 
           #調整上面這行的數值，去準確挑出「選項框框」
            questionCnts.append(c)
            cntnum.append(num)
    #這裡利用「寬」與「高」的長短，以及「長寬比」的數值，去篩選出真正的「選項框框」所屬的邊緣
    #w = 寬,  h = 高,  ar = 長寬比 = w / h
        num += 1
        

    
    questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
    print("抓到的問題框框 ： " + str(len(questionCnts)))
    print(cntnum)
    cv2.drawContours(img, questionCnts, -1, (0, 0, 255), 3)
    cv2.drawContours(imgc, questionCnts, -1, (0, 255, 0), 3)
    cv2.imshow("contours", imgc)
    
    thresh = cv2.threshold(blurred, 0, 255,
    	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] #將圖片再一次模糊，並轉換成二值圖（顏色非白即黑，只有兩種極端的顏色）
    cv2.imshow("pic", img)

    '''
    for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)): #問題有幾題，這個數字就改成多少（預設是5）

        cnts = contours.sort_contours(questionCnts[i:i + 5])[0] #每個問題有幾個選項，這個數字就改成多少
        bubbled = None

        for (j, c) in enumerate(cnts):
            mask = np.zeros(thresh.shape, dtype="uint8") 
            cv2.drawContours(mask, [c], -1, 255, -1) #設計一個mask，影響範圍為選項框框

            mask = cv2.bitwise_and(thresh, thresh, mask=mask) #將當前想要檢測的選項以外的像素變黑，只留下這個選項
            total = cv2.countNonZero(mask) #實際檢測框框內部有沒有塗到的地方

            if bubbled is None or total > bubbled[0]:
                bubbled = (total, j)

        color = (0, 0, 255)
        k = ANSWER_KEY[q]

        if k == bubbled[1]:
            color = (0, 255, 0)
            correct += 1

        cv2.drawContours(img, [cnts[k]], -1, color, 3)
        #依照上面設定的答案，那格有畫到並成功辨識，就會把外框塗上綠色，反之塗上紅色
    
    cv2.imshow("test", img)
    '''
    cv2.waitKey(0)       

if __name__ == '__main__':
    FileRename()
    f = os.listdir("/home/unix/python/bubbletest/__pycache__/testpic/")
    for i in range(0, len(f)):
        imgpath = "D:/home/unix/python/bubbletest/__pycache__/testpic/" + str(i + 1) + ".jpg"
        bubbletest(imgpath)