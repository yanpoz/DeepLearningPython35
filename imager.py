import matplotlib.pyplot as plt
import math
import pylab

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

def show_wb(weights, biases):
    n = weights.__len__()
    rows = math.floor(math.sqrt(n))
    cols = n // rows

    plt.figure(1, figsize=(7, 7))
    weights0 = weights[0] + biases[0]
    weights0 = [weights0[i].reshape(28, 28) for i in range(30)]
    for i in range(30):
        plt.subplot(5, 6, i+1)
        plt.imshow(weights0[i])

    plt.figure(2, figsize=(7, 3))
    weights1 = weights[1] + biases[1]
    weights1 = [weights1[i].reshape(5, 6) for i in range(10)]
    for i in range(10):
        plt.subplot(1, 10, i+1)
        plt.imshow(weights1[i])

    pylab.show()
    return