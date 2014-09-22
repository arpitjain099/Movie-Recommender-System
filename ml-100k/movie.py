import csv

nm=1682
nu=943
f=19

def dotp(x,y):
    s=0
    assert len(x)==len(y)
    for k in range(len(x)):
        s+=x[k]*y[k]
    return s

def s(theta,rate,movies,j,k,l,lamda):
    sm=0
    for i in range(len(rate)):
        if not rate[i][j]==0:
            sm+=(dotp(theta[j],movies[i])-rate[i][j])*movies[i][k]
    if not l==0:
        sm+=lamda*theta[j][k]
    return sm
                
#movies array for movies' genre
movies=[]
with open('u.item','rb') as f:
    reader=csv.reader(f,delimiter='|')
    for row in reader:
        temp=[]
        #temp.append(row[1])
        for i in row[5:]:
            temp.append(int(i))
        temp.insert(0,1)
        movies.append(temp)

#rate array:[#movies X #users]
rate=[[0 for i in range(nu)] for i in range(nm)]

#user movie rating
with open('u.data','rb') as f1:
    reader=csv.reader(f1,delimiter='\t')
    for row in reader:
        rate[int(row[1])-1][int(row[0])-1]=int(row[2])

#start of gradient descent
alpha=0.1
lamda=1
theta=[[0 for i in range(20)] for i in range(nu)]
theta1=list(theta)
while iter<100:
    for k in range(20):
        for j in range(nu):
            if k==0:
                theta1[j][k]=theta[j][k]-alpha*(s(theta,rate,movies,j,k,0,lamda))
            else:
                theta1[j][k]=theta[j][k]-alpha*(s(theta,rate,movies,j,k,1,lamda))
    theta=list(theta1)
    iter+=1
