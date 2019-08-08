# -*- coding: utf-8 -*-

import os
import sys
import shutil

GOODNUMBER = 1
IMAGE_NUMBER = 200
train_file = "C:\\Users\\zfr_Rambo\\Desktop\\train-2.txt"
FILE_PATH = "C:\\Users\\zfr_Rambo\\Desktop\\526"
NEW_PATH = "C:\\Users\\zfr_Rambo\\Desktop\\5-26-1"

def writeTrain(name, label):
    """TODO: Docstring for writeTrain.
    :returns: TODO

    """
    fp = file(train_file, 'at+')
    fp.write(name + " " + label + '\n')
    fp.close()


def movFiles(fileindex, label, srcpath, destpath):
    """TODO: Docstring for movFiles.
    :returns: TODO

    """
    
    filelist = os.listdir(srcpath)

    if len(filelist) < IMAGE_NUMBER:
        print srcpath, " contain ", len(filelist), " error"
        sys.exit(1)

    for fitem in filelist:
        fileabs = os.path.join(srcpath, fitem)

        index_str = "{:0>8d}".format(fileindex)
        newfname = index_str + ".JPG"
        newfpath = os.path.join(destpath, newfname)

        # print "move file ", fileabs, "to ", newfpath
        shutil.copy(fileabs, newfpath)
        # writeTrain(index_str, label)
        fileindex += 1

    return fileindex

def main():
    loop = 0
    file_index = 1

    while loop < GOODNUMBER:
        
        label = str(loop + 1)
        print "The fi is :", label
        print label
        ItemDir = os.path.join(FILE_PATH,label)
        new_path_1 = os.path.join(NEW_PATH,label)
        destpath_1 = os.mkdir(new_path_1)
        print "destpath_1:", destpath_1
        

        file_index = movFiles(file_index, label, ItemDir, new_path_1)

        loop += 1

if __name__ == "__main__":
    main()
