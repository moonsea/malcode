#! /usr/bin/python

from __future__ import division
import os
import copy
import math
from wingenasm import log
from gengram import checkDir
from gengram import checkFile


# virus
# BASEPATH = './/resource//vxheaven//class//opcode//'
# benign
# BASEPATH = './/resource//benign//'
# classfier
BASEPATH = './/resource//classifier//training/'
# BASEPATH = './/resource//vxheaven//class//virus.dos//'
# PATH = '..//resource//vxheaven//vl//virus.win/'

__GRAM_SIZE__ = 2
__GRAM_TYPE__ = '2-gram-tf'


def genSingleTF(content, filename):

    desfiledir = os.path.join(BASEPATH, __GRAM_TYPE__)
    checkDir(desfiledir)

    desfilepath = os.path.join(desfiledir, filename)
    checkFile(desfilepath)

    freq = dict()
    for line in content:
        # print line
        freq[line.strip()] = freq.get(line.strip(), 0) + 1

    # total = len(content)

    # desfile = open(desfilepath, 'w')
    #
    # for key in freq.keys():
    #     # print key, freq[key]
    #     desfile.write(key + '----' + str(freq[key]) + '----' + str(total) + '----' + str(freq[key] / total) + '\n')
    #
    # desfile.close()
    maxterm = max(freq.values())
    total = len(freq)
    with open(desfilepath, 'w') as desfile:
        for key in freq.keys():
            # print key, freq[key]
            desfile.write(key + '----' + str(freq[key]) + '----' + str(
                total) + '----' + str(freq[key] / maxterm) + '\n')


def getTotalTF(content, tf, df):
    tmp = copy.deepcopy(df)
    for line in content:
        # print line
        tf[line.strip()] = tf.get(line.strip(), 0) + 1
        df[line.strip()] = tmp.get(line.strip(), 0) + 1


def traveseFile(path):
    totaltf = dict()
    totaldf = dict()
    totalterm = 0
    maxterm = 0
    totaldocument = 0
    maxdocument = 0

    for parent, dirnames, filenames in os.walk(path):
        log('Entering', parent, subpath='classfier')

        totaldocument += len(filenames)
        for filename in filenames:

            filepath = os.path.join(parent, filename)
            print filepath

            with open(filepath) as asmfile:
                lines = asmfile.readlines()

            log('Generating', filename, subpath='classfier')
            genSingleTF(lines, filename)
            # totalterm += len(lines)
            getTotalTF(lines, totaltf, totaldf)

    # print totaltf
    desfilepath = os.path.join(BASEPATH, '2-gram-totaltf')
    maxterm = max(totaltf.values())
    maxdocument = max(totaldf.values())
    totalterm = len(totaltf)
    with open(desfilepath, 'w') as desfile:
        for key in totaltf.keys():
            # print key, totaltf[key]
            tmp = '----'.join([key, str(totaltf[key]), str(totalterm), str(totaltf[key] / maxterm), str(
                totaldf.get(key, 0)), str(totaldocument), str(totaldf.get(key, 0) / maxdocument), str(math.log(totaldocument / totaldf.get(key, 1)))])
            desfile.write(tmp + '\n')


if __name__ == '__main__':

    log('Starting', 'caulate 2-gram frequncy for classfier',
        '********', '********', subpath='classfier')

    # 2-gram
    # grampath = os.path.join(BASEPATH, '2-gram')
    # traveseFile(grampath)

    # 2-gram of benign
    grampath = os.path.join('.//resource//classifier//training//', '2-gram')
    traveseFile(grampath)
