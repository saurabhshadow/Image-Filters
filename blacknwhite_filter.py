import cv2
class BlacknWhite1:
    """BlacknWhite Filter
        A class that applies BlacknWhite filter to an image.
        The class uses downsampling, bilateral filter and upsampling to create
        a BlacknWhite filter.
    """
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
        cv2.imshow("upscaling",img_color)
        cv2.waitKey(0)
        # -- STEPS 2 and 3 --
        # convert to grayscale and apply median blur
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        return img_gray

tmp_canvas =BlacknWhite1()
file_name = "car.jpg" #File_name will come here
res = tmp_canvas.render(file_name)
cv2.imwrite("BW1 version.jpg", res)
cv2.imshow("BW1 version", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
