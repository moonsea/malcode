#! /usr/bin/python

import os
import datetime

# idal -c -A -S//usr//local//src//ida-pro-6.4//idc//analysis_fullname.idc inputfile
idalPath = "//usr//local//src//ida-pro-6.4//idal"
idcPath = "//usr//local//src//ida-pro-6.4//idc//analysis_fullname.idc"
# PATH = './/resource//vxheaven//class//virus.win//compress//compress/'
benignPath = "./resource/benign/md5/"
# unpackPath = "./resource/vxheaven/class/virus.win/compress/unpack/"
logName = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logPath = "./log"


def genAsm(filepath, total):
    ExecStr = idalPath + " -c -A -S" + idcPath + " '" + filepath + "'"
    # print ExecStr
    os.system(ExecStr)

    return total + 1


def traveseFile(path, initClean=False):
    for parent, dirnames, filenames in os.walk(path):

        if(initClean):
            log('Cleaning', '', '[-]')

            for filename in filenames:
                filepath = os.path.join(parent, filename)

                cleanFile(filename, filepath)

            continue

        log('Entering', parent)
        # normal file
        log('origin', str(len(filenames)))
        # unpack file
        # log('origin', str(countFile(parent, 'dump')))

        total = 0
        for filename in filenames:
            filepath = os.path.join(parent, filename)

            if (cleanFile(filename, filepath)):
                continue

            log('asming', filename)

            total = genAsm(filepath, total)

        log('genasm', str(countFile(parent, 'asm')))


def countFile(dirpath, suffix=''):
    return len([x for x in os.listdir(dirpath) if (x.split('.')[-1] == suffix)])


def cleanFile(filename, filepath):
    filetype = filename.split('.')[-1]
    if (filetype == 'asm' or filetype == 'idb'):
        os.remove(filepath)
        print '[-] Clean ', filename
        return True

    return False


def getNowTime():
    return datetime.datetime.now().strftime('%m-%d-%H:%M:%S')


def log(action, content, prefix='[+]', suffix='', subpath=''):
    logDir = os.path.join(logPath, subpath)
    if not os.path.exists(logDir):
        try:
            os.makedirs(logDir)
        except:
            print '[-] Mkdir error'

    logpath = os.path.join(logDir, logName)

    with open(logpath, 'a+') as logfile:
        logfile.write(''.join([prefix, getNowTime(), ' ', action, ' ', content, suffix, '\n']))


if __name__ == '__main__':

    log('Starting', 'asm benign file', '********', '********')

    # normal file
    traveseFile(benignPath, True)
    traveseFile(benignPath)
