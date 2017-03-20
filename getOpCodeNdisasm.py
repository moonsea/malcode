#! /usr/bin/python

import os
from wingenasm import log

# BASEPATH = './/resource//vxheaven//class//virus.win//'
BASEPATH = './/resource//ndisasm//'
# BASEPATH = './/resource//vxheaven//class//virus.dos//'
# PATH = '..//resource//vxheaven//vl//virus.win/'


def checkDir(dirpath):
    if not os.path.exists(dirpath):
        try:
            os.makedirs(dirpath)
        except:
            print '[-] Mkdir error'


def checkFile(filepath):
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
        except:
            print '[-] Delete error'


def getOpCode(content, filename, opfiledir):

    # opfiledir = os.path.join(BASEPATH, 'opcode')
    checkDir(opfiledir)

    opfilepath = os.path.join(opfiledir, filename)
    checkFile(opfilepath)

    for line in content:
        line = line.split()
        # print line
        if(len(line) > 3):
            opcode = line[2].strip()
            if(not opcode.isalpha()):
                continue

            opcode = ''.join([opcode, '\n'])
            with open(opfilepath, 'a+') as opfile:
                opfile.write(opcode)
            # print opcode
            # print line


def traveseFile(path, type):
    for parent, dirnames, filenames in os.walk(path):
        log('Entering', parent, subpath='ndisasm')

        for filename in filenames:
            filepath = os.path.join(parent, filename)
            print filepath

            with open(filepath) as asmfile:
                lines = asmfile.readlines()

            log('OpCoding', filename, subpath='ndisasm')
            opfiledir = os.path.join(BASEPATH, 'opcode', type)
            getOpCode(lines, filename, opfiledir)


if __name__ == '__main__':

    log('Starting', 'getopcode', '********', '********', subpath='ndisasm')

    # test
    # testpath = os.path.join(BASEPATH, 'asm', 'test')
    # traveseFile(testpath, 'test')

    # virus
    # viruspath = './resource/vxheaven/vl//asm'
    # viruspath = os.path.join(BASEPATH, 'asm', 'virus')
    viruspath = ".//resource//vxheaven//vl//asm//"
    traveseFile(viruspath, 'virus')

    # benign
    # benignpath = os.path.join(BASEPATH, 'asm', 'benign')
    benignpath = ".//resource//benign//asm//"
    traveseFile(benignpath, 'benign')
