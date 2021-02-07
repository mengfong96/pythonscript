
import os, shutil

#修改原曲位置
source = 'C:\\Users\\mf\\Desktop\\source'

#修改USB位置（固定），原定是4个，可增加。
destination = ['E:\\','G:\\','H:\\','I:\\']

#开始脚本
print('Start')
for basename in os.listdir(source):
    
    if basename.endswith('.mp3') or basename.endswith('.pdf'):
        
        basename_path = os.path.join(source, basename)

        if os.path.isfile(basename_path):
            print('Processing file: ' + basename)
            for usb_location in destination:
                try:
                    shutil.copy(basename_path, usb_location)
                    print("Success - '"+usb_location+"'")
                except:
                    print("'"+usb_location+"' failed")
                    pass

print('Process Completed!')
input('Press any key to continue...')
