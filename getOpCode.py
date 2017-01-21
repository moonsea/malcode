#! /usr/bin/python

import os
from wingenasm import log

# BASEPATH = './/resource//vxheaven//class//virus.win//'
BASEPATH = './/resource//benign//'
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


def getOpCode(content, filename):

    opfiledir = os.path.join(BASEPATH, 'opcode')
    checkDir(opfiledir)

    opfilepath = os.path.join(opfiledir, filename)
    checkFile(opfilepath)

    for line in content:
        line = line.split(' ')
        prefix = line[0]
        if(len(prefix) > 2 and prefix[0:2] == '\t\t'):
            prefix = prefix.strip()
            if(prefix == '' or prefix is None):
                continue

            if(prefix[0] == '.' or prefix[0] == ';' or prefix[0] == '/'):
                continue

            opcode = prefix.split('\t')[0]
            if(not opcode.isalpha()):
                continue

            opcode = ''.join([opcode, '\n'])
            with open(opfilepath, 'a+') as opfile:
                opfile.write(opcode)
            # print prefix.strip()
            # print line


def isOpCodeFile(lines):
    for line in lines:
        if ('; Format      :	Binary file' in line):
            return False

    return True


def getByteCode(parent, filename):
    rawname = filename[0:-4]
    # print rawfile

    desfiledir = os.path.join(BASEPATH, 'bytecode')
    checkDir(desfiledir)

    desfilepath = os.path.join(desfiledir, rawname)
    checkFile(desfilepath)

    rawpath = os.path.join(parent, rawname)

    with open(rawpath, 'rb') as rawfile:
        rawfile.seek(0, 0)
        while True:
            byte = rawfile.read(1)
            if byte == '':
                break
            else:
                hexstr = "%s" % byte.encode('hex')

                bytecode = ''.join([hexstr, '\n'])
                with open(desfilepath, 'a+') as bytefile:
                    bytefile.write(bytecode)


def checkFileType(filename, type='asm'):
    return filename.split('.')[-1] == type


def traveseFile(path):
    for parent, dirnames, filenames in os.walk(path):
        log('Entering', parent, subpath='opcode')

        for filename in filenames:
            if(not checkFileType(filename, 'asm')):
                continue

            filepath = os.path.join(parent, filename)
            print filepath

            with open(filepath) as asmfile:
                lines = asmfile.readlines()

            if(isOpCodeFile(lines)):
                print 'opcode'
                log('OpCoding', filename, subpath='opcode')
                getOpCode(lines, filename)
            else:
                print 'Binary'
                log('Bytecoding', filename, subpath='opcode')
                getByteCode(parent, filename)


if __name__ == '__main__':

    log('Starting', 'getopcode from benign', '********', '********', subpath='opcode')

    # viruswin
    # winnormalpath = os.path.join(BASEPATH, 'normal')
    # winunpackpath = os.path.join(BASEPATH, 'compress', 'unpack')
    #
    # traveseFile(winnormalpath)
    # traveseFile(winunpackpath)

    # virusdos
    # dosnormalpath = os.path.join(BASEPATH, 'normal')
    #
    # traveseFile(dosnormalpath)

    # benign
    benignpath = os.path.join('.//resource//benign//md5//')
    #
    # traveseFile(winnormalpath)
    traveseFile(benignpath)
