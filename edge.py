import cv2
import numpy as np
from matplotlib import pyplot as plt


def filter2d(src, kernel):
    try:
        m, n = kernel.shape
    except ValueError:
        m = kernel.shape[0]
    d = int((m - 1) / 2)
    h, w = src.shape[0], src.shape[1]
    dst = np.zeros((h, w))
    for y in range(d, h - d):
        for x in range(d, w - d):
            dst[y][x] = np.sum(src[y - d:y + d + 1, x - d:x + d + 1] * kernel)
    return dst


class Edgetrans():
    def __init__(self, currdir="aurora.jpg"):
        self.currdir = currdir

    def kernellist(self, sel):
        if sel == 1:
            kernel_x = np.array([-1, 0, 1])
            kernel_y = np.array([[-1], [0], [1]])
            lib_x = cv2.filter2D(self.gray, -1, kernel_x)
            lib_y = cv2.filter2D(self.gray, -1, kernel_y)
        elif sel == 2:
            kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
            kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
            lib_x = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=5)
            lib_y = cv2.Sobel(self.gray, cv2.CV_64F, 0, 1, ksize=5)
        return lib_x, lib_y, kernel_x, kernel_y

    def readimg(self, sel):
        im_bgr = cv2.imread(f'{self.currdir}')
        img = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)
        self.gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        lx, ly, kx, ky = self.kernellist(sel)

        gray_x = filter2d(self.gray, kx)
        gray_y = filter2d(self.gray, ky)
        out = np.sqrt(gray_x ** 2 + gray_y ** 2)
        if sel == 1:
            outlib = lx + ly
        else:
            outlib = np.sqrt(lx ** 2 + ly ** 2)
        plt.subplot(2, 4, 1), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 4, 2), plt.imshow(gray_x, cmap='gray')
        plt.title('Horizontal'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 4, 3), plt.imshow(gray_y, cmap='gray')
        plt.title('Vertical'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 4, 4), plt.imshow(out, cmap='gray')
        plt.title('Combined'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 4, 5), plt.imshow(self.gray, cmap='gray')
        plt.title('Grayscaled'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 4, 6), plt.imshow(lx, cmap='gray')
        plt.title('Horizontal Lib'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 4, 7), plt.imshow(ly, cmap='gray')
        plt.title('Vertical Lib'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 4, 8), plt.imshow(outlib, cmap='gray')
        plt.title('Combined Lib'), plt.xticks([]), plt.yticks([])
        plt.show()
