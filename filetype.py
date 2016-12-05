#! /usr/bin/python

import magic
import os
import sys
import shutil

PATH = './/resource//vxheaven//vl//virus.dos/'
# PATH = '..//resource//vxheaven//vl//virus.win/'


def CopyFile(srcDir, desDir):
    if not os.path.exists(desDir):
        try:
            os.makedirs(desDir)
        except:
            print '[-] Mkdir error'

    print '[+]Copying ', srcDir

    try:
        shutil.copy(srcDir, desDir)
    except:
        print '[-]Copy error'


def filetype(filename):

    ms = magic.open(magic.NONE)
    ms.load()

    file_type = ms.file(filename)

    ms.close()

    return file_type

if __name__ == '__main__':
    # print filetype('.//FirstClass//8f84a46017151d935c34878ad4c53293')

    list = os.listdir(PATH)

    # ms_result_file = open('viruswintype_ms_result', 'w+')

    for line in list:
        file_path = os.path.join(PATH, line)
        # print file_path
        ftype = filetype(file_path)

        desDir = os.path.join('resource/vxheaven/class/virus.dos/', ftype)

        CopyFile(file_path, desDir)

        # if((ftype.find('executable') == -1) and (ftype.find('data') == -1) ):
        # content = ':'.join([line, ftype])
        # print content


        # content = ':'.join([line, ftype])
        # content = ''.join([content, '\n'])



        # with open('virusdostype_ms_result', 'a+') as ms_result_file:
        #     ms_result_file.write(content)
        #
        # print content

        # ms_result_file.close()
