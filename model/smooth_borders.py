from PIL import Image
import numpy as np

a = 0.5
b = 2
n = 24
k = 2

image_path = './model/input2.jpg'
im = Image.open(image_path, 'r')
img = im.load()
h, w = im.size

for row in range(n):
    for col in range(h):
        # right
        pos = w - n + row
        # rl
        sm1 = np.array([0, 0, 0])
        for it in range(n):
            for clr in range(3):
                sm1[clr] += img[pos-it, col][clr] * (1 - it / n)

        for clr in range(3):
            sm1[clr] = 2 * sm1[clr] / (n + 1)
        # rr
        sm2 = np.array([0, 0, 0])
        for it in range(min(n, w - pos)):
            for clr in range(3):
                sm2[clr] += img[pos + it, col][clr] * (1 - it / n)

        for it in range(n + pos - w):
            for clr in range(3):
                sm2[clr] += img[it, col][clr] * (1 - (it + w - pos) / n)

        for clr in range(3):
            sm2[clr] = 2 * sm2[clr] / (n + 1)

        cur = np.array([img[pos, col][0], img[pos, col][1], img[pos, col][2]])
        sm = (sm1 * a + sm2 * b) / 2
        sm = (sm * (row / n) + cur * (1 - row / n))
        img[pos, col] = (int(sm[0]), int(sm[1]), int(sm[2]))

        # left
        pos = n - row - 1
        sm1 = np.array([0, 0, 0])
        for it in range(n):
            for clr in range(3):
                sm1[clr] += img[pos + it, col][clr] * (1 - it / n)

        for clr in range(3):
            sm1[clr] /= (n + 1) / 2

        sm2 = np.array([0, 0, 0])
        for it in range(pos):
            for clr in range(3):
                sm2[clr] += img[pos - it, col][clr] * (1 - it / n)

        for it in range(1, n - pos):
            for clr in range(3):
                sm2[clr] += img[w - it, col][clr] * (1 - (it + pos) / n)

        for clr in range(3):
            sm2[clr] /= (n + 1) / 2

        # img[row, col] = (sm1 * a + sm2 * b) / 2
        cur = np.array([img[pos, col][0], img[pos, col][1], img[pos, col][2]])
        sm = (sm1 * a + sm2 * b) / 2
        sm = (sm * (row / n) + cur * (1 - row / n))
        img[pos, col] = (int(sm[0]), int(sm[1]), int(sm[2]))


im.save('image_smooth.jpg', "JPEG")
