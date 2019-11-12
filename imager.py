import matplotlib.pyplot as plt
import math

def show(images, n):
    imgs = images[0:n]
    imgs = [imgs[i][0].reshape(28, 28) for i in range(n)]
    
    plt.figure(figsize=(7, 7))

    rows = math.floor(math.sqrt(n))
    cols = n // rows

    for i in range(n):
        plt.subplot(rows, cols, i+1)
        plt.imshow(imgs[i])

    plt.show()
    return

def show_w(weights):
    n = weights.__len__()
    rows = math.floor(math.sqrt(n))
    cols = n // rows

    weights = [weights[i].reshape(28, 28) for i in range(30)]

    plt.figure(figsize=(7, 7))

    for i in range(30):
        plt.subplot(5, 6, i+1)
        plt.imshow(weights[i])

    plt.show()
    return