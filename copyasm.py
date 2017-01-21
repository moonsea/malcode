#! /usr/bin/python

import os
import shutil
from wingenasm import log

BasePath = './/resource//vxheaven//class/'


def CopyFile(srcDir, desDir, filename):
    if not os.path.exists(desDir):
        try:
            os.makedirs(desDir)
        except:
            print '[-] Mkdir error'

    desfile = os.path.join(desDir, filename)
    if os.path.isfile(desfile):
        log('Ignore', filename, '[-]', subpath='copyasm')
        print '[-]Ignore ', filename
        return
        # os.remove(desfile)

    log('Copying', filename, subpath='copyasm')
    print '[+]Copying ', filename

    try:
        shutil.copy(srcDir, desDir)
    except:
        log('Copying error', filename, '[-]', subpath='copyasm')
        print '[-]Copy error ', filename


def traveseFile(path, despath):
    for parent, dirnames, filenames in os.walk(path):

        for filename in filenames:
            filepath = os.path.join(parent, filename)
            filetype = filename.split('.')[-1]
            if (filetype == 'asm'):
                CopyFile(filepath, despath, filename)


if __name__ == '__main__':
    # print filetype('.//FirstClass//8f84a46017151d935c34878ad4c53293')

    log('Starting', '', '********', '********', subpath='copyasm')

    # viruswin
    winnormalsrc = os.path.join(BasePath, 'virus.win', 'normal')
    winunpacksrc = os.path.join(BasePath, 'virus.win', 'compress', 'unpack')
    windes = os.path.join(BasePath, 'virus.win', 'asm')

    # dossrc = os.path.join(BasePath, 'virus.dos', 'normal')
    # dosdes = os.path.join(BasePath, 'virus.dos', 'asm')

    traveseFile(winnormalsrc, windes)
    traveseFile(winunpacksrc, windes)
