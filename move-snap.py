# move it to ~/.emulationstation/downloaded_images/ and run 

import os

# get dir
root = os.getcwd()
target = '/home/pi/roms/'
dirs = [d for d in os.listdir() if os.path.isdir(d)]

for d in dirs:
    curr = os.path.join(root,d)
    tdir = os.path.join(target, d)
    os.chdir(curr)
    imgs = os.listdir()
    if len(imgs) == 0:
        print('remove empty {}'.format(curr))
        os.rmdir(curr)
        continue
    for f in imgs:
        print('move {}/{}'.format(curr,f))
        os.rename(os.path.join(curr,f), os.path.join(tdir,'snap',f))

