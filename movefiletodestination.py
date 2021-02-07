# Idea to move screenshot file to Pictures folder  to clean up desktop. 

import os
import shutil

fromPath='C:\\Users\\mf\\Desktop'
sourcefile = os.listdir(sourcepath)
toPath = 'C:\\Users\\mf\\Pictures'

for file in sourcefile:
    if file.endswith('.png') or file.endswith('.jpg'):
        shutil.move(os.path.join(fromPath, file), os.path.join(toPath, file))
