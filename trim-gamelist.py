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

def reduceList(gamedir):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    dup = 0
    i = 0
    write = False
    while (i < len(root)):
        game = root[i]
        path = game.find('path').text
            
        if not os.path.isfile(path):
            dup += 1
            print("Remove {}: {}".format(curr, path))
            root.remove(game)
        else:
            ipath = "~/.emulationstation/downloaded_images/" + gamedir
            image = game.find('image')
            if image is None:
                print("warning: image is None: ", path)
            if image is not None and ipath in image.text:
                print("replace image path: {}".format(image.text))
                image.text = image.text.replace(ipath, './snap')
            i += 1
    print("{} xml size: {} remove: {}".format(gamedir, len(root), dup))

    print("write {} {}".format(gamedir, xmlfile)) 
    tree.write(xmlfile, 'UTF-8')

for game in games:
    curr = os.path.join(rootdir, game)
    os.chdir(curr)
    reduceList(game)
