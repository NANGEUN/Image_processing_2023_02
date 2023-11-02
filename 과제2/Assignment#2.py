# Implement histogram equalization

# goal : enhance the contrast of low-light image

import cv2
import numpy as np

def histogram_equalization(image):
    # 이미지를 그레이스케일로 변환
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist, bins = np.histogram(gray_image.flatten(), 256, [0, 256])

    # 누적 분포 함수 계산
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # histogram_equalization
    equalized_image = np.interp(gray_image.flatten(), bins[:-1], cdf_normalized)

    # 0-255 범위로 재조정
    equalized_image = np.uint8(equalized_image.reshape(gray_image.shape))

    return equalized_image


image = cv2.imread('/Users/ayoungyang/영상처리/과제2/dgu_night.png')  # image_load

out_image = histogram_equalization(image)

cv2.imshow('Input Image', image)
cv2.imshow('Result Image', out_image)

cv2.imwrite('dgu_night_equalization.png', out_image)  # save result img
cv2.waitKey()