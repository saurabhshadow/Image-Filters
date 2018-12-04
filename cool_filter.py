import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline

class cool_filter:
    """cool_filter ---
        This class will apply cool filter to an image 
        by giving a sky blue effect to the input image.
    """

    def __init__(self):
        # create look-up tables for increasing and decreasing red and blue resp.
        self.increaseChannel = self.LUT_8UC1([0, 64, 128, 192, 256],
                                                 [0, 70, 140, 210, 256])
        self.decreaseChannel = self.LUT_8UC1([0, 64, 128, 192, 256],
                                                 [0, 30,  80, 120, 192])

    def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        cv2.imshow("Original", img_rgb)
        r,g,b = cv2.split(img_rgb)
        r = cv2.LUT(r, self.increaseChannel).astype(np.uint8)
        b = cv2.LUT(b, self.decreaseChannel).astype(np.uint8)
        img_rgb = cv2.merge((r,g,b))

        # saturation decreased
        h,s,v = cv2.split(cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV))
        s = cv2.LUT(s, self.decreaseChannel).astype(np.uint8)


        return cv2.cvtColor(cv2.merge((h,s,v)), cv2.COLOR_HSV2RGB)

    def LUT_8UC1(self, x, y):
        #Create look-up table using scipy spline interpolation function
        spl = UnivariateSpline(x, y)
        return spl(range(256))

class_object = cool_filter()
file_name = "beach.jpg" #File_name will come here
res = class_object.render(file_name)
cv2.imwrite("cool_image.jpg", res)
cv2.imshow("Cool-Filter version", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
