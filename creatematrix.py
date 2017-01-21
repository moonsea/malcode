#! /usr/bin/python

from __future__ import division
import os
import copy
import math
from wingenasm import log
from gengram import checkDir
from gengram import checkFile
from feasec import BASEPATH


def createFeaMatrix(feafile, tfpath):
    desfiledir = os.path.join(BASEPATH, 'feature')
    checkDir(desfiledir)

    desfilepath = os.path.join(desfiledir, '2_gram_training_feature_new')
    checkFile(desfilepath)

    log('Generating', 'feature list', subpath='classfier')
    with open(feafile) as feafile:
        lines = feafile.readlines()

    fealist = []
    for line in lines:
        fealist.append(line.split('----')[0].strip())

    log('Complete', str(fealist), subpath='classfier')
    # matrixlist = []

    # benignpath = os.path.join(tfpath, 'benign')
    #
    # filelist = os.listdir(benignpath)
    # for item in filelist:
    #     filepath = os.path.join(benignpath, item)
    #     vector = ''.join([item, getVector(fealist, filepath), '1'])
    #     matrixlist.append(vector)

    log('Generating', 'matrix of benign', subpath='classfier')
    createMatrix(desfilepath, fealist, tfpath, 'benign')
    log('Generating', 'matrix of malcode', subpath='classfier')
    createMatrix(desfilepath, fealist, tfpath, 'malcode')

    # with open(desfilepath, 'w') as desfile:
    #     desfile.writelines(matrixlist)


def createMatrix(desfilepath, fealist, tfpath, type):
    tmppath = os.path.join(tfpath, type)
    filelist = os.listdir(tmppath)
    # classname = '1' if (type == 'benign')
    for item in filelist:
        log('Generating', item, subpath='classfier')
        filepath = os.path.join(tmppath, item)
        vector = '----'.join([item, str(getVector(fealist, filepath)).replace('[', '').replace(']', '').replace('\'', ''), '1' if type == 'benign' else '2'])
        with open(desfilepath, 'a+') as desfile:
            desfile.writelines(vector + '\n')
        log('Complete', vector, subpath='classfier')
        # matrixlist.append(vector)


def getVector(fealist, filepath):
    tmplist = []

    with open(filepath) as orifile:
        lines = orifile.readlines()

    sortedLines = sorted(lines, lambda x, y: cmp(int(x.split('----')[1]), int(y.split('----')[1])), reverse=True)
    maxtf = int(sortedLines[0].split('----')[1])

    for feature in fealist:
        tmplist.append('0')
        for line in lines:
            line = line.split('----')
            if(feature == line[0]):
                tmplist[-1] = str(int(line[1]) / maxtf * 1000)
        # tmplist.append()

    return tmplist


if __name__ == '__main__':

    log('Starting', 'create feature matrix',
        '********', '********', subpath='classfier')

    # 2-gram opcode with tf
    feafile = './/resource//classifier//feature//300'
    tfpath = './/resource//classifier//training//2-gram-tf//'

    createFeaMatrix(feafile, tfpath)
