# local root
rootdir = 'E:\\Retropie'

# dirs to sync
games = [
    'arcade',
    'megadrive',
    'nes',
    'snes',
    'msx',
    'pcengine',
    'segacd',
    'fds',
    'gba',
    'mastersystem',
    'psx',
]

xmlfile = 'gamelist.xml'

import os
import xml.etree.ElementTree as ET

def removeSnap(gamedir):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    image_dict = {}
    r = 0

    for game in root:
        image = game.find('image').text.replace('./snap/','')
        image_dict[image] = 1    
        if not os.path.isfile(os.path.join('snap', image)):
            print("Not exist: ", image)

    images = os.listdir('snap')

    for f in images:
        if f not in image_dict:
            r += 1
            print("remove {}: ".format(f))
            os.remove(os.path.join('snap', f))
    print('xml: {} file: {}', len(image_dict), len(images))

for game in games:
    curr = os.path.join(rootdir, game)
    print(curr)
    os.chdir(curr)
    removeSnap(game)
