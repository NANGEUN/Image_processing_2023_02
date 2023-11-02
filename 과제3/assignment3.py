import numpy as np
import cv2

image = cv2.imread('dgu_gray.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
n, m = gray_image.shape

# Sobel 필터 정의
Gx = np.array([[-1, 0, 1],
               [-2, 0, 2], 
               [-1, 0, 1]])
Gy = np.array([[-1, -2, -1], 
               [0, 0, 0], [1, 2, 1]])

# 필터 적용 및 sobel edge 적용
edge_image = np.zeros((n-2, m-2)) # 빈 numpy 배열 생성
for row in range(1, n-1):
    for col in range(1, m-1):
        input_pixels = gray_image[row-1:row+2, col-1:col+2] # 현 픽셀 기준 3x3 픽셀 선택해 필터 적용
        Ix = (np.sum(Gx * input_pixels)) # horizontal direction 계산
        Iy = (np.sum(Gy * input_pixels)) # vertical direction 계산
        edge_score = np.abs((Ix**2 + Iy**2)**0.5) # overall gradient edge magnitude 계산
        edge_image[row-1, col-1] = edge_score

# 엣지 이미지 저장
cv2.imwrite('edge_result.jpg', edge_image)
