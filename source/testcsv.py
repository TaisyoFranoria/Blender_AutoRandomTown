import csv

with open('C:\\Users\\taisy\\Documents\\GameEngineproject\\basemap\\data\\basemap.csv','r') as f:
    lis = list(csv.reader(f))

count = 0

for x in range(10):
    for y in range(10):
        if(lis[x][y]=='0'):
            count += 1

print(count)

