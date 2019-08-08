# -*- coding: utf-8 -*-

import os
# import sys
import shutil

PIC_PATH = 'C:\\Users\\zfr_Rambo\\Desktop\\200'

XML_OLD_PATH = 'C:\\Users\\zfr_Rambo\\Desktop\\200-xml'

XML_NEW_PATH = 'C:\\Users\\zfr_Rambo\\Desktop\\200-xml-new'


def main():

    label = 0
    while label < 12:
        
        PIC_LABEL_PATH = os.path.join(PIC_PATH, str(label+1))
        # print PIC_LABEL_PATH

        img_list = os.listdir(PIC_LABEL_PATH)

        for img in img_list:
            namefpic = os.path.splitext(img)[0] + '.xml'
            # print namefpic
            xml_path_1 = os.path.join(XML_OLD_PATH, str(label+1), namefpic)
            xml_path_2 = os.path.join(XML_NEW_PATH, str(label+1), namefpic)
            # print xml_path_1, xml_path_2
            print "move file ", xml_path_1, "to ", xml_path_2
            shutil.copy(xml_path_1, xml_path_2)

        label += 1


if __name__ == "__main__":
    main()
