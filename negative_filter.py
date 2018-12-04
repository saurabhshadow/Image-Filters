import cv2

# find max GSV
def findMax(k):
    mx = 0
    for i in k:
        if i>mx:
            mx = i
    return mx

class negativeFilter:

    def __init__(self):
        pass

    def render(self, img_rgb):
        img_gray = cv2.imread(img_rgb, 0)
        #get all image values
        k = []
        for i in range(img_gray.shape[0]):
            for j in range(img_gray.shape[1]):
                k.append(img_gray[i,j])

        L = findMax(k) #max GSV
        dst = img_gray[:] #copy image

        #update dst
        for i in range(img_gray.shape[0]):
          for j in range(img_gray.shape[1]):
            dst[i,j] = L - dst[i,j]
        return dst



tmp_canvas = negativeFilter()
file_name = "car.jpg" #File_name will come here
res = tmp_canvas.render(file_name)
cv2.imwrite("BW1 version.jpg", res)
cv2.imshow("BW1 version", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
