import csv

item={}
with open("u.item","rb") as f:
    reader=csv.reader(f,delimiter='|')
    for row in reader:
        index=int(row[0])
        item[index]=[int(i) for i in row[5:]]

user={}
with open("u.user","rb") as f:
    reader=csv.reader(f,delimiter='|')
    for row in reader:
        index=int(row[0])
        user[index]=[i for i in row[1:-1]]

fdata=open("contentBasedIndividual.arff","w")

fdata.write("@RELATION iris\n\n")
fdata.write("@ATTRIBUTE userid REAL\n")
for i in range(19):
    #fdata.write("@ATTRIBUTE f"+str(i)+" {0,1}\n")
    fdata.write("@ATTRIBUTE f"+str(i)+" REAL\n")

#fdata.write("\n@ATTRIBUTE f20 NUMERIC\n")
#fdata.write("@ATTRIBUTE f21 {M,F}\n")
#fdata.write("@ATTRIBUTE f22 {administrator,artist,doctor,educator,engineer,entertainment,executive,healthcare,homemaker,lawyer,librarian,marketing,none,other,programmer,retired,salesman,scientist,student,technician,writer}\n");
#fdata.write("@ATTRIBUTE f23 STRING\n");

#fdata.write("\n@ATTRIBUTE CLASS {1,2,3,4,5}\n")
fdata.write("\n@ATTRIBUTE CLASS REAL")

fdata.write("\n@DATA\n")


with open("u.data","rb") as f:
    reader=csv.reader(f,delimiter='\t')
    for row in reader:
        uid=int(row[0])
        iid=int(row[1])
        fdata.write(str(uid)+","+reduce(lambda x,y:x+str(y)+",",item[iid],"")+row[2]+"\n")
        #fdata.write(str(uid)+","+reduce(lambda x,y:x+str(y)+",",item[iid],"")+reduce(lambda x,y:x+str(y)+",",user[uid],"")+row[2]+"\n")
fdata.close()
