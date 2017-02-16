#pylab inline
from pandas import read_csv
from matplotlib.pyplot import *
import sys,os

##########################################################################

ignore=[0,0,0]
for j in range(0,len(sys.argv)):
  if sys.argv[j]=='-on':
    ignore[0]=1
  if sys.argv[j]=='-soon':
    ignore[1]=1
  if sys.argv[j]=='-uc':
    ignore[2]=1
ig=ignore[0]+ignore[1]+ignore[2]

if ig==3:
  sys.exit("ERROR--IGNORANDO TODO!!!")

#########################################################################
os.system("python sorteador.py "+sys.argv[1]+" 2 > misdatos.dat")
files=open('misdatos.dat')

labels=[]
x=[]
xon=[]
yon=[]
xso=[]
yso=[]
xuc=[]
yuc=[]

cont=0
for line in files:
  row=line.split(',')
  if row[0][0]=='#':
    continue
  cont+=1
  x.append(cont)
  labels.append(row[0])
  if ig!=3:
    #print row[4]
    if ignore[0]>0 and row[4]=='on':
      continue
    elif row[4]=='on':
      xon.append(row[1])
      yon.append(row[2])
    if ignore[1]>0 and row[4]=='soon':
      continue
    elif row[4]=='soon':
      xso.append(row[1])
      yso.append(row[2])
    if ignore[2]>0 and row[4]=='uc':
      continue
    elif row[4]=='uc':
      xuc.append(row[1])
      yuc.append(row[2])
#print x
#print xuc
# These are the "Tableau 20" colors as RGB.
tableau20 = [(25,25,112),(31, 119, 180), (255, 127, 14), (255, 187, 120),
    (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
  r, g, b = tableau20[i]
  tableau20[i] = (r / 255., g / 255., b / 255.)
#figure size
figure(figsize=(30,18))

# Remove the plot frame lines. They are unnecessary chartjunk.
ax = subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Ticks on the right and top of the plot are generally unnecessary chartjunk.
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

yticks(fontsize=32)
xticks(fontsize=32)

# Provide tick lines across the plot to help your viewers trace along
# the axis ticks. Make sure that the lines are light and small so they
# don't obscure the primary data lines.
#print xon[3], yon[3]
#plot(xon[3],int(float(yon[4]))*range(0,len(xon)), "--", lw=0.5, color="black", alpha=0.3)

for y in range(0,7000,1000):
  print [y]
#  plot(range(0,len(xon)), [y] * len(range(0,len(xon))), "--", lw=0.5, color="black", alpha=0.3)

####################################################################
####################################################################

if ignore[0]==0:
  plot(xon,yon,lw=2.5,color=tableau20[5],marker='o',ms=10,label='working')
  scatter(xon,yon,marker='o',zorder=10,s=110,color=tableau20[5])
if ignore[1]==0:
  plot(xso,yso,lw=2.5,color=tableau20[7],marker='x',ms=10,label='coming soon')
  scatter(xso,yso,marker='x',zorder=10,s=110,color=tableau20[7])
if ignore[2]==0:
  plot(xuc,yuc,lw=2.5,color=tableau20[1],marker='d',ms=10,label='under consideration')
  scatter(xuc,yuc,marker='d',zorder=10,s=110,color=tableau20[1])


######################################################################
################### final tweks######################################


text(3000, -95, "m a.s.l", fontsize=40, ha="center")
text(-1500, -10, "Latitude", fontsize=45, ha="center",rotation='vertical')
lg = ax.legend(loc='upper left', fontsize=35, numpoints=1)
lg.get_frame().set_alpha(.8) # A little transparency

os.system('rm misdatos.dat')


savefig("alturas.png")#, bbox_inches="tight");
