# coding: utf-8
import MDAnalysis as mda
from MDAnalysis.analysis.distances import self_distance_array
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

xml = input('xml: ')
dcd = input('dcd: ')

u = mda.Universe(xml,dcd)
dij = []
for ts in u.trajectory:
    dij.append(self_distance_array(x.positions))
dij = np.array(dij).T

df = pd.DataFrame({i:dij[i] for i in range(len(dij))})

print df
print 'try sns.distplot(df[1]) for histogram of distance with index 1'
print 'or plt.plot(df[1]) for timeseries of distance with index 1 '
