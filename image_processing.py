# this script loads a directory with images, resizes all of them to 10x10 pixel images and makes them black/white (binary)
# the processed images are saved in a given location
# after processing the images, a csv is written with an image per row and 0's and 1's for the white/black pixels

import matplotlib.pyplot as plt
import os
import imageio
import glob
from skimage.filters import threshold_minimum
from skimage.color import rgb2gray
from skimage.transform import resize

for pic in os.listdir('/path/to/directory/with/pics/'):
    original = plt.imread('/path/to/directory/with/pics/'+pic)
    image_gray = rgb2gray(original)
    image_resized = resize(image_gray, (10, 10), anti_aliasing=False)

    #thresh = threshold_minimum(image_resized)
    thresh = 0.63
    binary = image_resized < thresh
    binary = binary.astype(int)

    plt.imsave('/path/to/image/save/'+pic,binary,cmap="binary")
    
    flat = binary.flatten()
    
    with open(r'/path/to/csv/file.csv', 'a') as f:        
        flat_str = ','.join(map(str,flat))
        line = pic+','+flat_str+'\n'
        f.write(line)
