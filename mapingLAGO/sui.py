import shapefile
import numpy as np
from matplotlib import cm, rcParams
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Coordinates (from Wikipedia) and shift
DF = [-99.1333, 19.4333]
TH = [  8.1042, 47.4375]

proj = 'tmerc'
# Colours
cMX = '#0000cc' # Blue tone
cCH = '#006600' # Green tone

# 70 km by 70 km, Transverse Mercator, resolution does not
# matter, as we use other data for the borders
width = 1500000
height = 1500000
dshift = [-.133, -.05]

fig2 = plt.figure(figsize=(8,8))

# Create basemaps for Mexico and Switzerland
m_ch = Basemap(width=width, height=height, projection=proj,
            lon_0=TH[0], lat_0=TH[1],resolution='l')
m_ch.drawcoastlines()
#m_ch.drawcountries()
# Draw the district of Aargau
CHE_adm1 = shapefile.Reader('data/basemap/CHE_adm0')
iag = [i for i, s in enumerate(CHE_adm1.records()) if 'SWITZERLAND' in s][0]
aglonlat = np.array(CHE_adm1.shapes()[iag].points)
print aglonlat
print aglonlat[:,1]
m_ch.plot(aglonlat[:, 0], aglonlat[:, 1], '-', c=cCH, lw=6)
agx, agy = m_ch(aglonlat[:, 0], aglonlat[:, 1])
#plt.(agx, agy, cCH, ec='none', alpha=.4)
CHE_adm0 = shapefile.Reader('data/basemap/CHE_adm0')
chlonlat = np.array(CHE_adm0.shape().points)
m_ch.plot(chlonlat[:, 0], chlonlat[:, 1] , '-', c=cCH, latlon=True, ms=1)

# Draw scales to cross-check that the scales are the same
#sdf = np.array(m_mx(DF[0], DF[1])) - np.array([28000, 10000])
#sth = np.array(m_ch(TH[0], TH[1])) - np.array([28000, 10000])
#isdf = m_mx(sdf[0], sdf[1], inverse='True')
#isth = m_ch(sth[0], sth[1], inverse='True')
#m_mx.drawmapscale(isdf[0], isdf[1], DF[0], DF[1]+dshift[0],
#                  4, barstyle='fancy', fillcolor2=cMX, fontsize=12)
#m_ch.drawmapscale(isth[0], isth[1], TH[0], TH[1]+dshift[1],
#                  4, barstyle='fancy',  fillcolor2=cCH, fontsize=12)

# Draw locations
#hPT = [-99.12, 19.47]
#pPT = [-99.11, 19.33]
#m_mx.plot(hPT[0], hPT[1], '*', c='k', ms=14, mew=1)
#m_mx.plot(pPT[0], pPT[1], 'o', c='k', ms=10, mew=1)

# Remove border around the whole
#m_mx.drawmapboundary(color='none')

plt.show()
