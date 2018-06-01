#!/usr/bin/env python3

import scipy.spatial.distance
import imageio
import os

files = [f for f in os.listdir('.') if f.endswith('png')]

imgs = []

print ('first is ', files[0])
print ('total ', len(files))

for f in files:
    img = imageio.imread(f, pilmode = 'RGBA')
    if len(imgs) == 0 or img.size == imgs[0].size:
        imgs.append(img)
        if len(imgs) % 100 == 0: print(len(imgs))
    else:
        print("discarded " + f + " due to size mismatch")
        

print('read ', len(imgs))

def imgsort(_imgs):
    flat0 = _imgs[0].flat
    _imgs.sort(key = lambda a : scipy.spatial.distance.canberra(a.flat, flat0))

groupsize = 25
res = []
while len(imgs) > 0:
    imgsort(imgs)
    res = res + imgs[:groupsize]
    imgs = imgs[groupsize:]
    print(len(res), len(imgs))

print('writing animation.gif')

imageio.mimwrite('animation.gif', res, 'GIF')