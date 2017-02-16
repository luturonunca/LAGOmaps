import os,sys
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def logo():
    print " \n\n\n "
    print "      ___       ___           ___           ___"
    print "     /\__\     /\  \         /\  \         /\  \ "
    print "    /:/  /    /::\  \       /::\  \       /::\  \ "
    print "   /:/  /    /:/\:\  \     /:/\:\  \     /:/\:\  \ "
    print "  /:/  /    /::\~\:\  \   /:/  \:\  \   /:/  \:\  \ "
    print " /:/__/    /:/\:\ \:\__\ /:/__/_\:\__\ /:/__/ \:\__\ "
    print " \:\  \    \/__\:\/:/  / \:\  /\ \/__/ \:\  \ /:/  / "
    print "  \:\  \        \::/  /   \:\ \:\__\    \:\  /:/  / "
    print "   \:\  \       /:/  /     \:\/:/  /     \:\/:/  / "
    print "    \:\__\     /:/  /       \::/  /       \::/  / "
    print "     \/__/ __ _\/__/__ _ _ __\/____   ___ _\/__/ " 
    print "        | '_ ` _ \ / _` | '_ \| '_ \ / _ \ '__| "
    print "        | | | | | | (_| | |_) | |_) |  __/ | "
    print "        |_| |_| |_|\__,_| .__/| .__/ \___|_| "
    print "                        | |   | | "
    print "                        |_|   |_| "
    return



logo()
comand='python mapingLAGO/AutoMap.py '
comand2='python SitiosAlturas/plotalturas3.py '

for i in range(1, len(sys.argv)):
  comand+=sys.argv[i]+' '
  comand2+=sys.argv[i]+' '


  

print  "\n\n\ngenerando mapa..... "
os.system(comand) 
print "\n\n\ngenerando curva de alturas... \n\n\n"
os.system(comand2)

fig = plt.figure()
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1.2],left=None,bottom=None,right=None,top=None,wspace=.005,hspace=.005)

ax1=plt.subplot(gs[0])
ax1.set_axis_off()
img = mpimg.imread('lagoplano.png')
lum_img = img[:,:,:]
imgplot = plt.imshow(lum_img)

ax2=plt.subplot(gs[1])
ax2.set_axis_off()
img2 = mpimg.imread('alturas3.png')
lum_img2 = img2[:,:,:]
imgplot2 = plt.imshow(lum_img2)
#plt.show()
#plt.figure(figsize=(30,18))
plt.savefig("MAPAtodo.png",dpi=600,bbox_inches='tight', pad_inches = 0)
