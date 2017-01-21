#! /usr/bin/python

from __future__ import division
import os
import copy
import math
from wingenasm import log
from gengram import checkDir
from gengram import checkFile

# feature
BASEPATH = './/resource//classifier//'


__TOP_FEATURE__ = 1000


def initFeature(orifeapath):
    desfiledir = os.path.join(BASEPATH, 'feature')
    checkDir(desfiledir)

    desfilepath = os.path.join(desfiledir, 'init_sorted_feature')
    checkFile(desfilepath)

    with open(orifeapath) as orifile:
        lines = orifile.readlines()

    sortedLines = sorted(lines, lambda x, y: cmp(int(x.split('----')[4]), int(y.split('----')[4])), reverse=True)
    # print sortedLines

    with open(desfilepath, 'w') as desfile:
        desfile.writelines(sortedLines)

    if(os.path.isfile(desfilepath)):
        return desfilepath
    else:
        return 'init error'


def selectFeature(filepath, feasize):
    desfiledir = os.path.join(BASEPATH, 'feature')
    checkDir(desfiledir)

    desfilepath = os.path.join(desfiledir, str(feasize))
    checkFile(desfilepath)

    with open(filepath) as orifile:
        lines = orifile.readlines()

    secfeature = lines[0:feasize]

    with open(desfilepath, 'w') as desfile:
        desfile.writelines(secfeature)

    # return lines[0:feasize]


if __name__ == '__main__':

    # log('Starting', 'caulate 2-gram frequncy for classfier',
    #     '********', '********', subpath='classfier')

    # 2-gram opcode with tf
    # orifile = './/resource//classifier//training//2-gram-totaltf'
    # feafile = initFeature(orifile)
    feafile = './/resource//classifier//feature//init_sorted_feature'

    selectFeature(feafile, 1000)
    selectFeature(feafile, 300)
