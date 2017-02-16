import sys
larg=0
l=0
lats=[]
file=open(sys.argv[1])
for line in file:
  row = line.split(',')
  fin = len(row)
  if row[0][0]=='#':
    continue
  lats.append((row[0],float(row[1]),float(row[2]),float(row[3]),row[4],float(row[5]),float(row[6]),float(row[7])))
  larg+=1

array=sorted(lats, key=lambda lat: lat[int(sys.argv[2])])
for i in range(0,len(array)):
  print str(array[i][0])+','+str(array[i][1])+','+str(array[i][2])+','+str(array[i][3])+','+str(array[i][4])+','+str(array[i][5])+','+str(array[i][6])+','+str(array[i][7])+','
