#coding:utf-8
import os
import sys
import re
from pulp import *
import numpy.linalg
from itertools import product
import rpy2.robjects as robjects
import numpy as np, pandas as pd
from collections import defaultdict

# usage: python soc.py [sig file] [sig dir] [html file]

robjects.r['library']('lpSolve')
transport = robjects.r['lp.transport']

def KLDiv(mu1, S1, mu2, S2):
    S1[np.isnan(S1)] = 0
    S2[np.isnan(S2)] = 0

    try:
        invS1 = np.linalg.pinv(S1)
    except:
        pinvS1 = np.dot(S1.T, S1)
        invS1 = np.linalg.pinv(pinvS1)
    try:
        invS2 = np.linalg.pinv(S2)
    except:
        pinvS2 = np.dot(S2.T, S2)
        invS2 = np.linalg.pinv(pinvS2)

    t1 = np.sum(np.diag(np.dot(invS2, S1)))
    t2 = (mu2 - mu1).transpose()
    t3 = mu2 - mu1
    return t1 + np.dot(np.dot(t2, invS2), t3)

def symKLDiv(mu1, S1, mu2, S2):
    return 0.5 * (KLDiv(mu1, S1, mu2, S2) + KLDiv(mu2, S2, mu1, S1))

def loadSignature(sigFile):
    mat = []
    fp = open(sigFile, "r")
    for line in fp:
        line = line.rstrip()
        mat.append([float(x) for x in line.split()])
    fp.close()
    return np.array(mat)

def calcEMD(sigFile1, sigFile2):
    sig1 = loadSignature(sigFile1)
    sig2 = loadSignature(sigFile2)
    numFeatures = sig1.shape[0] 
    dist = np.zeros(numFeatures * numFeatures)


    for i in range(numFeatures):
        mu1 = sig1[i, 1:21].reshape(20, 1)         
        S1 = sig1[i, 21:421].reshape(20, 20)
        for j in range(numFeatures):
            mu2 = sig2[j, 1:21].reshape(20, 1)
            S2 = sig2[j, 21:421].reshape(20, 20)
            dist[i * numFeatures + j] = symKLDiv(mu1, S1, mu2, S2)
    w1 = sig1[:,0]
    w2 = sig2[:,0]
    costs = dist.reshape(len(w1),len(w2))

    pr = list(product(range(numFeatures),range(numFeatures))) #16
    row_rhs = robjects.FloatVector(w1)
    col_rhs = robjects.FloatVector(w2)

    nw, nf = numFeatures, numFeatures
    pr = list(product(range(numFeatures),range(numFeatures)))
    supply = row_rhs
    demand = col_rhs
    transport_cost = costs

    m1 = LpProblem()
    v1 = {(i,j):LpVariable('v%d_%d'%(i,j), lowBound = 0, cat = 'Continuous') for i,j in pr}
    m1 += lpSum(transport_cost[i][j] * v1[i,j] for i,j in pr)
    for i in range(nw):
        m1 += lpSum(v1[i,j] for j in range(nf)) <= supply[i]
    for j in range(nf):
        m1 += lpSum(v1[i,j] for i in range(nw)) >= demand[j]
    m1.solve()
    flow = {k:value(x) for k,x in v1.items()} #if value(x) > 0}

    flow_array = np.array([[0 for i in range(16)] for j in range(16)], dtype = float)

    flow_point = flow.keys()
    for i in range(256):
        x = flow_point[i][0]
        y = flow_point[i][1]
        flow_num = flow.values()
        flow_array[x][y] = flow_num[i]
    flow_array = flow_array.reshape(16,16)

    dist = dist.reshape(len(w1), len(w2))
    work = np.sum(flow_array * dist)
    emd = work / np.sum(flow_array)
    return emd


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "python mir.py [sig file] [sig dir] [html file]"
        sys.exit()

    targetSigPath = sys.argv[1]
    sigDir = sys.argv[2]
    htmlFile = sys.argv[3]

    ranking = defaultdict(float)

    for sigFile in os.listdir(sigDir):
        print sigFile
        sigPath = os.path.join(sigDir, sigFile)
        emd = calcEMD(targetSigPath, sigPath)
        break
        if emd < 0: continue
        ranking[sigFile] = emd

