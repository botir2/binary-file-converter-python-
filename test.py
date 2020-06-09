
import glob

try:
    #data = open("C:/Users/ceo/Desktop/SCubeBinFileView/20200519/03/CM91005013_202005190305.bin", "rb+").read(8)
    path = 'C:/Users/ceo/Desktop/SCubeBinFileView/ACC/**/**/CM92005013*.bin'
    files = glob.glob(path)
    for name in files:
        if name.endswith(".bin"):
            print(name)

except:
    print('Error')