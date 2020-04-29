import cv2
def PicCut():
    img = cv2.imread("D:/pytest/cool.jpg")
    print(img.shape)
    cropped = img[0:135, 0:200]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("D:/pytest/out.jpg", cropped)

if __name__ == "__main__":
    PicCut()
