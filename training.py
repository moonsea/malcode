#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import os
import copy
import math
from wingenasm import log
from gengram import checkDir
from gengram import checkFile
from feasec import BASEPATH
import numpy as np
import scipy as sp
from sklearn import svm
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt


def train(filepath):
    data = []
    labels = []
    with open(filepath) as ifile:
        for line in ifile:
            line = line.split('----')
            tokens = [i.strip().replace('\'', '') for i in line[1].split(',')]
            # print tokens
            data.append([float(i) for i in tokens])
            labels.append(line[-1])
    x = np.array(data)
    print x
    labels = np.array(labels)
    y = np.zeros(labels.shape)
    # y[labels == 'fat'] = 1
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.0)

    h = .02
    # create a mesh to plot in
    # x_min, x_max = x_train[:, 0].min() - 0.1, x_train[:, 0].max() + 0.1
    # y_min, y_max = x_train[:, 1].min() - 1, x_train[:, 1].max() + 1
    # xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    #                      np.arange(y_min, y_max, h))

    ''' SVM '''
    # title for the plots
    titles = ['LinearSVC (linear kernel)',
              'SVC with polynomial (degree 3) kernel',
              'SVC with RBF kernel',
              'SVC with Sigmoid kernel']
    clf_linear = svm.SVC(kernel='linear').fit(x, y)
    print clf_linear
    # clf_linear  = svm.LinearSVC().fit(x, y)
    clf_poly = svm.SVC(kernel='poly', degree=3).fit(x, y)
    clf_rbf = svm.SVC().fit(x, y)
    clf_sigmoid = svm.SVC(kernel='sigmoid').fit(x, y)

    # for i, clf in enumerate((clf_linear, clf_poly, clf_rbf, clf_sigmoid)):
    #     answer = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    #     print(clf)
    #     print(np.mean(answer == y_train))
    #     print(answer)
    #     print(y_train)
    #
    #     plt.subplot(2, 2, i + 1)
    #     plt.subplots_adjust(wspace=0.4, hspace=0.4)
    #
    #     # Put the result into a color plot
    #     z = answer.reshape(xx.shape)
    #     plt.contourf(xx, yy, z, cmap=plt.cm.Paired, alpha=0.8)
    #
    #     # Plot also the training points
    #     plt.scatter(x_train[:, 0], x_train[:, 1],
    #                 c=y_train, cmap=plt.cm.Paired)
    #     plt.xlabel(u'身高')
    #     plt.ylabel(u'体重')
    #     plt.xlim(xx.min(), xx.max())
    #     plt.ylim(yy.min(), yy.max())
    #     plt.xticks(())
    #     plt.yticks(())
    #     plt.title(titles[i])
    #
    # plt.show()


if __name__ == '__main__':

    # log('Starting', 'create feature matrix',
    #     '********', '********', subpath='classfier')

    # 2-gram opcode with tf
    trainfile = './/resource//classifier//feature//2_gram_training_feature_new'

    train(trainfile)
