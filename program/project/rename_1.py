# -*- coding: utf-8 -*-

import os
import sys 
import shutil

GOODNUMBER = 1
IMAGE_NUMBER = 200
train_file = "C:\\Users\\zfr_Rambo\\Desktop\\train.txt"
FILE_PATH = "C:\\Users\\zfr_Rambo\\Desktop\\rename"
OLD_PATH = "C:\\Users\\zfr_Rambo\\Desktop\\200"
NEW_PATH = "C:\\Users\\zfr_Rambo\\Desktop\\rename-2"


def movFiles( label, srcpath, destpath, file_list):
    """TODO: Docstring for movFiles.
    :returns: TODO

    """
    filelist = os.listdir(srcpath)
    if len(filelist) < IMAGE_NUMBER:
        print srcpath, " contain ", len(filelist), " error"
        sys.exit(1)

    for i in range(0,len(filelist)):
        fileabs = os.path.join(srcpath, filelist[i])

        # index_str = "{:0>8d}".format(fileindex)
        # newfname = index_str + os.path.splitext(fileabs)[1]
        newfname = file_list[i]
        newfpath = os.path.join(destpath, newfname)

        print "move file ", fileabs, "to ", newfpath
        shutil.copy(fileabs, newfpath)
        
        # writeTrain(index_str, label)
        # fileindex += 1

    # return 0

def main():
    loop = 0
    # file_index = 9001

    while loop <GOODNUMBER:
        
        label = str(12)
        ItemDri_1 = os.path.join(OLD_PATH, label)
        ItemDri_2 = os.path.join(FILE_PATH, label)
        print ItemDri_1
        file_list = os.listdir(ItemDri_1)
        print type(file_list), len(file_list)
        new_path_1 = os.path.join(NEW_PATH,label)
        destpath_1 = os.mkdir(new_path_1)
        print "destpath_1:", destpath_1

        movFiles(label, ItemDri_2, new_path_1, file_list)

        loop += 1

if __name__ == "__main__":
    main()