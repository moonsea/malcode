#! /usr/bin/python

import os

BASEPATH = './/resource//vxheaven//class//virus.win//'
# PATH = '..//resource//vxheaven//vl//virus.win/'


def getOpCode(content, filename):

    opfiledir = os.path.join(BASEPATH, 'opcode')
    if not os.path.exists(opfiledir):
        try:
            os.makedirs(opfiledir)
        except:
            print '[-] Mkdir error'

    opfilepath = os.path.join(BASEPATH, 'opcode', filename)
    if os.path.exists(opfilepath):
        try:
            os.remove(opfilepath)
        except:
            print '[-] Delete error'

    for line in content:
        line = line.split(' ')
        prefix = line[0]
        if(len(prefix) > 2 and prefix[0:2] == '\t\t'):
            prefix = prefix.strip()
            if(prefix == '' or prefix is None):
                continue

            if(prefix[0] == '.' or prefix[0] == ';'):
                continue

            opcode = ''.join([prefix.split('\t')[0], '\n'])
            with open(opfilepath, 'a+') as opfile:
                opfile.write(opcode)
            # print prefix.strip()
            # print line


if __name__ == '__main__':

    asmdir = os.path.join(BASEPATH, 'asm')

    filelist = os.listdir(asmdir)

    for item in filelist:
        file_path = os.path.join(asmdir, item)

        if(os.path.isdir(file_path)):
            continue

        asmfile = open(file_path)

        try:
            lines = asmfile.readlines()
        finally:
            asmfile.close()

        getOpCode(lines, item)
