import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

# import data 
title = pd.read_table("../MatlabFolder/specificData/data3.txt", sep=';')
mydata = pd.read_table("../MatlabFolder/specificData/data3.txt", sep=';', names= title.loc[0,:].values)

    
def getSignalName(index):
    name = title.loc[0,:].values
    return name[index]


def getSignal(index):
    names = title.loc[0,:].values
    name =  names[index] 
    signal = mydata.loc[:,[name]].values
    signal = np.delete(signal, 0, 0)
    signal = np.delete(signal, 0, 0)
    intSignal = []  
    for i in signal:
        num = int(i)
        intSignal.append(num)
    return intSignal


def displaySignal(signal, signalName, T, F):
    t = np.arange(0, len(signal)/F, T)
    plt.plot(t,signal)
    plt.title(signalName)
    plt.xlabel('Time in s')
    plt.ylabel('Amplitude')
    plt.show()


# def createMatrix():
#     print('Creation des données')

#     return matrix


# def PrincipalComponentAnalysis(nbComponents, matrix):

#     # Standardizing the features
#     matrix = StandardScaler().fit_transform(matrix)

#     pca = PCA(n_components=2)
#     principalComponents = pca.fit_transform(matrix)
#     principalDf = pd.DataFrame(data = principalComponents
#              , columns = ['principal component 1', 'principal component 2'])

#     print('ok')


def main():
    T = 0.03
    F = 1/T
    index = 1
    signalName = getSignalName(index)
    signal = getSignal(index)
    displaySignal(signal, signalName, T, F)


if __name__ == "__main__":
    main()
