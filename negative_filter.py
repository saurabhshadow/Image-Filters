import cv2

# find max GSV
def findMax(k):
    mx = 0
    for i in k:
        if i>mx:
            mx = i
    return mx

class Negative(object):

    def __init__(self):
        pass

    def render(self, img_rgb):
        img_gray = cv2.imread(img_rgb, 0)
        img_gray = cv2.resize(img_gray, (1024,600))
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

    def start(self, img_path):
        tmp_canvas = Negative() #make a temporary object
        file_name = img_path #File_name will come here
        res = tmp_canvas.render(file_name)
        cv2.imwrite("Negative_version.jpg", res)
        cv2.imshow("Negative Version", res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image saved as 'Negative_version.jpg'")
	
