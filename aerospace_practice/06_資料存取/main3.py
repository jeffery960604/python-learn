import csv

Time = []
U = []
N = []
E = []

with open('EQ data.csv','rt') as fin:
    reader = csv.reader(fin)
    
    data = list(reader)
    
    for i in range(11,31):
        Time.append(data[i][0])
        U.append(data[i][1])
        N.append(data[i][2])
        E.append(data[i][3])
