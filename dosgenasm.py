#! /usr/bin/python

import os
import datetime

# idal -c -A -S//usr//local//src//ida-pro-6.4//idc//analysis_fullname.idc inputfile
# idalPath = "//usr//local//src//ida-pro-6.4//idal"
# idcPath = "//usr//local//src//ida-pro-6.4//idc//analysis_fullname.idc"
idalPath = "C:\\IDA6.8\\idaw.exe"
idcPath = "C:\\IDA6.8\\idc\\analysis_fullname.idc"

# normalPath = "D:\\malcode\\20170107\\virus.dos\\normal\\"
unpackPath = "D:\\malcode\\20170107\\virus.dos\\compress\\unpack\\"
logName = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logPath = "./log"


def genAsm(filepath, total):
    ExecStr = idalPath + " -c -A -S" + idcPath + " \"" + filepath + "\""
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
        # log('origin', str(len(filenames)))
        # unpack file
        log('origin', str(countFile(parent, 'dump')))

        total = 0
        for filename in filenames:
            filepath = os.path.join(parent, filename)

            if (cleanFile(filename, filepath)):
                continue

            log('asming', filename)

			# windows platform
            filepath = filepath.replace('\\', '\\\\')

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

    # unpack file
    if (filetype == 'dump'):
        return False
    return True

    # return False


def getNowTime():
    return datetime.datetime.now().strftime('%m-%d-%H:%M:%S')


def log(action, content, prefix='[+]', suffix=''):
    if not os.path.exists(logPath):
        try:
            os.makedirs(logPath)
        except:
            print '[-] Mkdir error'

    log = ''.join([prefix, getNowTime(), ' ', action, ' ', content, suffix, '\n'])
    print log
	
    logpath = os.path.join(logPath, logName)

    with open(logpath, 'a+') as logfile:
        # logfile.write(''.join([prefix, getNowTime(), ' ', action, ' ', content, suffix, '\n']))
        logfile.write(log)


if __name__ == '__main__':

    log('Starting', '', '********', '********')

    # normal file
    # traveseFile(normalPath, True)
    # traveseFile(normalPath)

    # unpack file
    traveseFile(unpackPath, True)
    traveseFile(unpackPath)
