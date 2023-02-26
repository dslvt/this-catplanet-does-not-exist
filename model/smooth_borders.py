from PIL import Image
import numpy as np


border = 20

image_path = './model/input1.jpg'
# im = Image.open(image_path, 'r')
# img = im.load()
img = np.array(Image.open(image_path, 'r'))
w, h, c = img.shape

# h, w = im.size
alpha = np.linspace(0.1, 1, border)

for b in range(border):
    row = img[:, b, :] * alpha[b] + img[:, w - border + b, :] * (1 - alpha[b])
    img[:, b, :] = row
    img[:, w - border + b, :] = row

img = img[:, :w - border, :]

Image.fromarray(np.uint8(img)).save('tmp.jpg')
