import sys,os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

################ ignorar algun estado on,soon,uc desde el argumento ##
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
  
##################### define el marker y color segun el estado #######

def estatus(x):
  status=(0,0)
  if x=='on':
    status=('^','#0033CC')
  elif x=='uc':
    status=('o','#FFFF00')
  elif x=='soon':
    status=('s','#CC0000')
  else:
    sys.exit("ERROR--ESTAUS DE SITIO NO VALIDO!!!")
  return status

################### ordena el archivo de datos por latitud#######

os.system('python sorteador.py '+sys.argv[1]+' 2 > misdatos.dat')
files=open('misdatos.dat')



#### genera mapa basico  #################################################
map = Basemap(projection='cyl',llcrnrlat=-84,urcrnrlat=33.56,llcrnrlon=-118.25,urcrnrlon=-33.56,resolution='l')
plt.figure(figsize=(13,18))

map.drawcoastlines(linewidth=.5)
map.drawcountries(linewidth=.5)
map.shadedrelief()
parallels = np.arange(-90.,50,10)
map.drawparallels(parallels,labels=[False,True,True,False])
#map.drawmapboundary(fill_color = 'aqua')
   
######################### grafica puntos sobre el mapa#############
lat = []
lon = []
yaux=0
yaux2=0
xaux=0
xaux2=0
x=0
y=0
cont=0
def crosletras(y,yaux,x,xaux,lengo,i):
  salida=[0,0]
  xo=0
  yo=0

  if abs(x-xaux)<8 and abs(y-yaux)<5:
    #salida[0]=x-3-(2*i/10)
    salida[0]=x-3-(1.5*i/10)+((abs(x-xaux)/(x-xaux))*(2-abs(x-xaux)))
  else:
    salida[0]=x-3-(2*i/10)
  if abs(y-yaux)<5:
    salida[1]=y+(5-abs(y-yaux)-2)
  if abs(y-yaux)>5:
    salida[1]=y-1
  return salida

for line in files:
  row = line.split(',')
  if ig>0:
    if ignore[0]>0 and row[4]=='on': #ignora on
      continue
    if ignore[1]>0 and row[4]=='soon':#ignora soon
      continue
    if ignore[2]>0 and row[4]=='uc': #ingnora uc
      #print row[0],ignore
      continue
  if row[0][0]=='#':
    continue
  if row[1]=='':
    continue
  cont+=1
  lat=float(row[2])
  lon=float(row[3])
  tatus=estatus(row[4]) # determina color y marker segun estatus
  x,y = map(lon,lat)
  map.scatter(x,y,marker=tatus[0],facecolor=tatus[1][0:7],s=150,zorder=10)#grafica los puntos
  #print row[0], x,xaux, y,yaux
  cornu=crosletras(y,yaux,x,xaux,len(row[1]),cont)
  #print crosletras(y,yaux,x,xaux,len(row[1]),cont)
  m=((-1)**(cont))
  plt.text(-117,13-(2.6*cont),str(cont)+' = '+row[0]+' ('+str(int(float(row[1])))+' m)',color='w',fontsize=17,zorder=10, fontweight='bold')#grafica la leyenda que numero-lugar en blanco a la derecha
  if cont==5 or cont==14:
    plt.text(x+(m*3.5)-((0.5+(cont/10))*m)+m*(cont/10)-1.2,y-2,str(cont),color='black',fontsize=12,zorder=15,fontweight='bold')# grafica los nuero 5 y 14 mas cerca de los marker esto tal vez de ba quitarse ###############
    continue

  plt.text(x+(m*3)-((0.5+(cont/10))*m)+m*(cont/10)-1.2,y-0.5,str(cont),color='black',fontsize=12,zorder=15,fontweight='bold')# grafica numeros impares a la izquierda del marker y pares a la derecha

##################### genera etiquetas para la leyenda superior sobre los puntos##############################
xi=23
yi=23
xi,yi=map(lon,lat)
if ignore[0]==0:
  plt.scatter(xi,yi,marker='^',s=200,color='#0033CC',label='operational')
if ignore[2]==0:
  plt.scatter(xi,yi,marker='o',s=200,color='#FFFF00',label='under consideration')
if ignore[1]==0:
  plt.scatter(xi,yi,marker='s',s=200,color='#CC0000',label='coming soon')
lg = plt.legend(loc='upper right', fontsize=26,scatterpoints=1)
lg.get_frame().set_alpha(.8) # A little transparency


os.system("rm misdatos.dat")
plt.savefig('lagoplano.png',dpi=300,bbox_inches='tight', pad_inches = 0)

#plt.show()
