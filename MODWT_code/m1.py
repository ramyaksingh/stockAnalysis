import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from modwt import modwt, modwtmra


def reed(inVec):
    data = pd.read_csv(inVec)
    dList = data['Volume'].values
    return dList

def arr_gen(inVec):
    arr = []
    lenDList = len(inVec)
    for i in range (0,lenDList):
        arr.append(i)
    return arr

def t_coeff(inVec, level):
    mdwt1 = modwt(inVec,"db4",level)
    ret_T_coef = mdwt1[level-1]
    return ret_T_coef

def display(inVec, t_coeff, level):
    fig = plt.figure()
    ax = Axes3D(fig)
    arr = arr_gen(inVec)
    trans_coeff = t_coeff(inVec, level)
    x = np.reshape(inVec, (82, 102))
    y = np.reshape(arr,(82, 102))
    z = np.reshape(trans_coeff,(82, 102))
    ax.plot_surface(X=z, Y=x, Z=y)
    plt.show()

if __name__ == "__main__":
    inn = ("<enter file path>)
    inVec = reed(inn)
    mdwt_coeff = t_coeff(inVec, level=7)
