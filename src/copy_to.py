import shutil
import os


class CopyTo:
    @staticmethod
    def copy_file(files, drive):
        for file in files:
            if os.path.isdir(file):
                copytree(file, drive+":\\")
            else:
                copyfile(file, drive+":\\")


def copyfile(file, drive):
    shutil.copy(file, drive)
    print("Copying")


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
        print("Copying")

#copytree("C:\\Users\\bikas\\Desktop\\test", "D:\\")