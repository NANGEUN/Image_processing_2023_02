import numpy as np
import matplotlib.pyplot as plt

input_image = plt.imread('dgu_gray.png')
gray_image = input_image.mean(axis=2, keepdims=True)/225.0
gray_image = np.concatenate([gray_image]*3, axis=2)

Gx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])
Gy = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]])

n, m, d = gray_image.shape

edge_image = np.zeros_like(gray_image)

for row in range(3, n-2):
    for col in range(3, m-2):
        input_pixels = gray_image[row-1:row+2, col-1:col+2, 0]

    # convloution
    Ix = (np.sum(Gx*input_pixels))
    Iy = (np.sum(Gy*input_pixels))
    edge_score = np.abs((Ix**2 + Iy**2)**0.5)
    edge_image[row, col] = [edge_score]*3
    edge_image = edge_image/edge_image.max()
    
plt.imshow(edge_image)
plt.show()
