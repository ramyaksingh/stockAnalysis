import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from modwt import modwt, modwtmra

fig = plt.figure()
ax = Axes3D(fig)

data = pd.read_csv('/Users/varunvasudevan/Desktop/Purdue/5_Fin/Research/Stocks/stockAnalysis/SourceData/Stocks/aapl.us.csv')
volume = data['Volume'].values
mdwt = modwt(volume,'db4',10)
mdwtu = mdwt[6]
arr = []
for i in range (0,len(volume)):
    arr.append(i)

X = np.reshape(volume,(82,102))
Y = np.reshape(arr, (82,102))
Z = np.reshape(mdwtu, (82,102))
ax.plot_surface(X=Z,Y=X,Z=Y)
plt.show()