#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:09:39 2019

@author: semccomas
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd
import scipy.ndimage as sp 

protname = 'glut3_holo'
indir = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/output_files/HOLE' %protname

run_calc = 1
def make_df_from_npy(profile):
    #z = 34 is bottom of glut3, 76 is top
    framenr = 503
    df_index = np.arange(10.02,120,0.005) #TODO change this to match z in all cases
    zero_df = np.zeros((np.shape(df_index)[0], framenr)) #TODO change this guy to be actual
    df = pd.DataFrame(data= zero_df, index = np.round(df_index,3), columns = np.arange(framenr))   #make an empty dataframe, index needs to be round because the arange is weird with decimals
        
    for line in profile.iteritems():
        frame = line[0]
        rxn = line[1]['rxncoord']
        radius = line[1]['radius']
        print frame   #just to see how progress is going
        for index, coord in enumerate(rxn): 
            df.loc[coord,frame] = radius[index]     #where the rxn coord matches the index, put the correponding radius
  
    df_cleaned = df.replace(0, np.nan).dropna()  #remove all rows that have a zero so that only rxn coords that are in all frames considered
    return df, df_cleaned
    
if run_calc:
    hole_profile = np.load('%s/%s_HOLE.npy' %(indir, protname))
    df, df_cleaned = make_df_from_npy(hole_profile)
    df_cleaned.to_csv('%s/%s_HOLE_cleaned.csv' %(indir, protname)) #save so we don't have to calculate all the time
    
    
#### reshaping and gaussian filter
df_cleaned = pd.read_csv('%s/%s_HOLE_cleaned.csv'%(indir, protname))
df_cleaned.index = df_cleaned.iloc[:,0]
df_cleaned = df_cleaned.drop(df_cleaned.columns[0:2], axis = 1)  #remove 0 frame because label and first b/c v diff

df_filtered = sp.filters.gaussian_filter(df_cleaned, sigma = 2) #do gaussian filter smoothing to smooth image a bit 
df_filtered = np.flip(df_filtered,0) #want ec gate on top for representation


### plot stuff 
plt.imshow(df_filtered, interpolation = 'none', cmap = 'gnuplot2', vmin =0, vmax = 4, extent=[0, 1000, 33, 62], aspect = 20) 
#vmin = 0, smallest radius, vmax = 4 == largest radius we really care about                                         
#extent doesn't change the values of the plot but does change aspect so just set this manually
plt.xlabel('time (ns)')
plt.ylabel(ur'z coordinate in \u00c5')
plt.colorbar()                                                 
plt.show()

#print df_cleaned.iloc[0:,]


'''
df2 = df.loc[30:85]
df2f = sp.filters.gaussian_filter(df2, sigma = 10)
s = pd.DataFrame(df2f)
plt.imshow(s, aspect = 0.02)
'''











