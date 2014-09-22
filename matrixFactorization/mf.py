#!/usr/bin/python
#
# Created by Albert Au Yeung (2010)
#
# An implementation of matrix factorization
#
try:
    import numpy
    import csv
    import time
except:
    print "This implementation requires the numpy module."
    exit(0)

###############################################################################

"""
@INPUT:
    R     : a matrix to be factorized, dimension N x M
    P     : an initial matrix of dimension N x K
    Q     : an initial matrix of dimension M x K
    K     : the number of latent features
    steps : the maximum number of steps to perform the optimisation
    alpha : the learning rate
    beta  : the regularization parameter
@OUTPUT:
    the final matrices P and Q
"""
def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in xrange(steps):
        t1=time.time()
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in xrange(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = numpy.dot(P,Q)
        e = 0
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in xrange(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        t2=time.time()
        print "Step : "+str(step)+"\tError = "+str(e)+"\tTime taken = "+str(t2-t1)
        if e < 0.001:
            break
    return P, Q.T

###############################################################################

def getMatrix():
    item={}
    with open("u.item","rb") as f:
        reader=csv.reader(f,delimiter='|')
        for row in reader:
            index=int(row[0])
            item[index]=[int(i) for i in row[5:]]

    user={}
    occ=[]
    with open("u.occupation","rb") as f:
        reader=csv.reader(f)
        for row in reader:
            occ.append(row[0])
    
    with open("u.user","rb") as f:
        reader=csv.reader(f,delimiter='|')
        for row in reader:
            index=int(row[0])
            user[index]=[i for i in row[1:-1]]

    for i in user.keys():
        user[i][0]=int(user[i][0])
        assert(user[i][1]=='M' or user[i][1]=='F')
        if user[i][1]=='M':
            user[i][1]=1
        else:
            user[i][1]=-1
        user[i][2]=occ.index(user[i][2])

    R=[[0 for i in range(len(item.keys()))] for j in range(len(user.keys()))]
    with open("u.data","rb") as f:
        reader=csv.reader(f,delimiter='\t')
        for row in reader:
            R[int(row[0])-1][int(row[1])-1]=int(row[2])
    return R

def validate(R):
    users=len(R)
    movies=len(R[0])
    r=0
    for i in R:
        for j in i:
            if j!=0:
                r+=1
    ratings=r
    assert(users==943 and movies==1682 and ratings==100000)
    
if __name__ == "__main__":
    R = getMatrix()
    validate(R)
    R = numpy.array(R)

    N = len(R)
    M = len(R[0])
    K = 2

    P = numpy.random.rand(N,K)
    Q = numpy.random.rand(M,K)
    print "Rating Matrix Initialized : Going to Stochastic Gradient Descent Algorithm"

    nP, nQ = matrix_factorization(R, P, Q, K)
    nR = numpy.dot(nP, nQ.T)
    print nR
