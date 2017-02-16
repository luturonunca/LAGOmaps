import sys
o=0
lat=[]
lon=[]
nam=[]
file=open('.kk')
for lines in file:
  o+=1
  row=lines.split(',')
  for i in range(0,9):
    if o==1:
      lat.append(row[i])
    if o==2:
      lon.append(row[i])
    if o==3:
      nam.append(row[i]) 


for i in range(0,9):
  print lat[i]+','+lon[i]+','+nam[i] 


