import numpy as np
# import matplotlib.pyplot as plt
# import skimage.io as skio
import skvideo.io as vidio
# import imageio as imio

if __name__ == '__main__':
    filename = './images/Wildlife.mp4'
    vid = vidio.vread(filename)
    print(vid.shape)
    # vid = imio.get_reader(filename, 'ffmpeg')
    # metadata = vid.get_meta_data()
    # print(metadata)
    # print('hi')