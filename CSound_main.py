import numpy as np
import matplotlib.pyplot as plt
from skimage import io as skio

if __name__ == '__main__':
    filename = './images/IMG1.JPG'
    a = skio.imread(filename)
    plt.figure()
    plt.imshow(a)
    plt.show()
