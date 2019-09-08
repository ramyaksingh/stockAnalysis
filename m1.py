import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from MODWT import modwt, imodwt, modwtmra
import datetime

def reed(inVec):
    """
    This reads a vector in the right format
    """
    data = pd.read_csv(inVec)
    dList = data['Volume'].values
    return dList

def arr_gen(inVec):
    """
    This is for the plot only
    """
    arr = []
    lenDList = len(inVec)
    for i in range (0,lenDList):
        arr.append(i)
    return arr

def t_coeff(inVec,filter,level):
    filter = "db4"
    mdwt1 = modwt(inVec,filter,level)
    r_t_c =  modwtmra(mdwt1,filter)
    ret_T_coef = r_t_c[2] # 3 is chosen based on the size of the data being used
    return ret_T_coef

def invert(inVec, filter):
    trans = modwt(inVec,filter,7)
    inv  = imodwt(trans,filter)
    return inv


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
    now = datetime.datetime.now()

    inn = '/Users/rahulnairjaishankar/Documents/Code/Stocks/stockAnalysis/SourceData/Stocks/ge.us.test.csv'
    data = pd.read_csv(inn)
    dList = data['Volume'].values
    mdwt_coeff = t_coeff(dList,"db4", level= 8)

    ar = arr_gen(dList)
    a = invert(dList,"sym6")
    npa = np.asarray(a)
    npar = np.asarray(ar)


    plt.plot(npar, mdwt_coeff, 'r-')
    plt.plot(npar, npa, 'g-')
    plt.show()


    later = datetime.datetime.now()

    print(later-now)
