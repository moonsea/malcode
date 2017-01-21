#! /usr/bin/python

import os
from wingenasm import log

# BASEPATH = './/resource//vxheaven//class//'
BASEPATH = './/resource//benign//'
# BASEPATH = './/resource//vxheaven//class//virus.dos//'
# PATH = '..//resource//vxheaven//vl//virus.win/'

__GRAM_SIZE__ = 2
__GRAM_TYPE__ = '2-gram'


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


def genGram(content, filename):

    desfiledir = os.path.join(BASEPATH, __GRAM_TYPE__)
    checkDir(desfiledir)

    desfilepath = os.path.join(desfiledir, filename)
    checkFile(desfilepath)

    end = len(content)
    strgram = ''

    for i in range(0, end):
        bigram = content[i: i + __GRAM_SIZE__]
        strgram += str(bigram).replace('[', '').replace(']', '').replace('\\n', '').replace('\'', '').replace(' ', '') + '\n'
        # strgram += str(bigram) + '\n'

    # print strgram

    # gramlist = [content[i:i + __GRAM_SIZE__] for i in range(0, len(content) - 1)]

    # print gramlist

    with open(desfilepath, 'w') as desfile:
        desfile.write(strgram)


def traveseFile(path):
    for parent, dirnames, filenames in os.walk(path):
        log('Entering', parent, subpath='opcode')

        for filename in filenames:

            filepath = os.path.join(parent, filename)
            print filepath

            with open(filepath) as asmfile:
                lines = asmfile.readlines()
            # print lines
            log('Generating', filename, subpath='opcode')
            genGram(lines, filename)


if __name__ == '__main__':

    log('Starting', 'generate 2-gram in benign', '********', '********', subpath='opcode')

    # viruswin
    # winopcodepath = os.path.join(BASEPATH, 'virus.win', 'opcode', 'origin')
    # traveseFile(winopcodepath)

    # virusdos
    # dosopcodepath = os.path.join(BASEPATH, 'virus.dos', 'opcode', 'filter')
    # traveseFile(dosopcodepath)

    # virusdos
    benignpath = os.path.join('.//resource//benign//opcode//')
    traveseFile(benignpath)
