#! /usr/bin/python

import os
import datetime
import hashlib

# virusPath = "./resource/vxheaven/vl/virus/"
# asmPath = "./resource/vxheaven/vl/asm/"
benignPath = "./resource/benign/origin/"
asmPath = "./resource/benign/asm/"
logName = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logPath = "./log"


def getMd5(filename):
    if not os.path.isfile(filename):
        return

    filehash = hashlib.md5()
    f = file(filename, 'rb')
    while True:
        b = f.read(4096)
        if not b:
            break
        filehash.update(b)
    f.close()
    return filehash.hexdigest()


def genAsm(filepath, total, asmpath):
    ExecStr = "ndisasm -a -u '" + filepath + "' > " + asmpath
    # print ExecStr
    res = os.system(ExecStr)
    log('asming', filepath + '(' + asmpath + ') :' + str(res), subpath='ndisasm')

    return total + 1


def traveseFile(path):
    for parent, dirnames, filenames in os.walk(path):
        print filenames
        log('Entering', parent, subpath='ndisasm')
        # normal file
        log('origin', str(len(filenames)), subpath='ndisasm')
        # unpack file
        # log('origin', str(countFile(parent, 'dump')))

        total = 0
        for filename in filenames:
            print filename
            filepath = os.path.join(parent, filename)
            log('asming', filename, subpath='ndisasm')

            filemd5 = getMd5(filepath)
            asmpath = os.path.join(asmPath, filemd5)

            total = genAsm(filepath, total, asmpath)

        log('genasm', str(countFile(asmPath)), subpath='ndisasm')


def countFile(dirpath, suffix=''):
    return len([x for x in os.listdir(dirpath) if (x.split('.')[-1] == suffix)])


def getNowTime():
    return datetime.datetime.now().strftime('%m-%d-%H:%M:%S')


def log(action, content, prefix='[+]', suffix='', subpath=''):
    logDir = os.path.join(logPath, subpath)
    checkDir(logDir)

    logpath = os.path.join(logDir, logName)

    with open(logpath, 'a+') as logfile:
        logfile.write(''.join([prefix, getNowTime(), ' ', action, ' ', content, suffix, '\n']))


def checkDir(dir):
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except:
            print '[-] Mkdir error'
    print '[+]' + dir + ' is ok'


if __name__ == '__main__':

    log('Starting', 'generate asm using ndisasm', '********', '********', subpath='ndisasm')

    checkDir(asmPath)

    # virus file
    # traveseFile(virusPath, True)
    # traveseFile(virusPath)

    # benign file
    # traveseFile(unpackPath, True)
    traveseFile(benignPath)
