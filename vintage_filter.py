import cv2
class BlacknWhite1:

    def __init__(self):
        pass

    def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        img_rgb = cv2.resize(img_rgb, (1024,600))
        numDownSamples = 2       # number of downscaling steps
        numBilateralFilters = 50  # number of bilateral filtering steps

        # -- STEP 1 --
        # downsample image using Gaussian pyramid
        img_color = img_rgb
        for _ in range(numDownSamples):
            img_color = cv2.pyrDown(img_color)
        #cv2.imshow("downcolor",img_color)
        #cv2.waitKey(0)
        # repeatedly apply small bilateral filter instead of applying
        # one large filter
        for _ in range(numBilateralFilters):
            img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
        #cv2.imshow("bilateral filter",img_color)
        #cv2.waitKey(0)
        # upsample image to original size
        for _ in range(numDownSamples):
            img_color = cv2.pyrUp(img_color)
        #cv2.imshow("upscaling",img_color)
        #cv2.waitKey(0)
        #img_color = cv2.imread('lena.jpg')
        newImage = img_color.copy()
        i, j, k = img_color.shape
        #apply sepia formula
        for x in range(i):
            for y in range(j):
                R = img_color[x,y,2] * 0.393 + img_color[x,y,1] * 0.769 + img_color[x,y,0] * 0.189
                G = img_color[x,y,2] * 0.349 + img_color[x,y,1] * 0.686 + img_color[x,y,0] * 0.168
                B = img_color[x,y,2] * 0.272 + img_color[x,y,1] * 0.534 + img_color[x,y,0] * 0.131
                if R > 255:
                    newImage[x,y,2] = 255
                else:
                    newImage[x,y,2] = R
                if G > 255:
                    newImage[x,y,1] = 255
                else:
                    newImage[x,y,1] = G
                if B > 255:
                    newImage[x,y,0] = 255
                else:
                    newImage[x,y,0] = B
        # -- STEPS 2 and 3 --
        # convert to grayscale and apply median blur
        #img_color_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        return newImage

tmp_canvas =BlacknWhite1()
file_name = "car.jpg" #File_name will come here
res = tmp_canvas.render(file_name)
cv2.imwrite("BW1 version.jpg", res)
cv2.imshow("BW1 version", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
