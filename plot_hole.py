#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:09:39 2019

@author: semccomas
"""
from mpl_toolkits.axes_grid1 import make_axes_locatable

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd
import scipy.ndimage as sp 

sim_run = ['glut3_holo', 'glut3_apo', 'pfht1_holo', 'pfht1_apo']
run_calc = 0

fig, axes = plt.subplots(nrows=4, ncols=1, sharex = True)

for ax,protname in zip(axes, sim_run):
    print 'Running %s .....' %protname
    indir = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/output_files/HOLE' %protname
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
        df.to_csv('%s/%s_HOLE_raw.csv' %(indir, protname))       
        df_cleaned.to_csv('%s/%s_HOLE_cleaned.csv' %(indir, protname)) #save so we don't have to calculate all the time
        
    #### reshaping and gaussian filter
    df = pd.read_csv('%s/%s_HOLE_raw.csv' %(indir, protname), index_col = 0)
    df_cleaned = pd.read_csv('%s/%s_HOLE_cleaned.csv'%(indir, protname))
    df_cleaned.index = df_cleaned.iloc[:,0]
    df_cleaned = df_cleaned.drop(df_cleaned.columns[0:2], axis = 1)  #remove 0 frame because label and first b/c v diff
    df_filtered = sp.filters.gaussian_filter(df_cleaned, sigma = 2) #do gaussian filter smoothing to smooth image a bit 
    df_filtered = np.flip(df_filtered,0) #want ec gate on top for representation
    
    
    df2 = df.loc[30:80]
    df2f = sp.filters.gaussian_filter(df2, sigma = 10)
    df2f = np.flip(df2f, 0)
    
    #ax = fig.add_subplot(4, 1, n)
    im = ax.imshow(df2f, aspect = 3, vmin = 0, vmax = 4, extent = [0, 1000, 30, 80])
    ax.set_ylabel(r'$R(\zeta)$')
    if 'apo' in protname:
        ax.set_title(protname[0:5].upper() + ' ' + 'apo')
    else:
        ax.set_title(protname[0:5].upper() + ' ' + 'holo')


cbar = fig.colorbar(im, ax=axes.ravel().tolist())
ax.set_xlabel('time (ns)')
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 2}
plt.rc('font', **font)
plt.savefig('../images_graphs/hole3d.png', bbox_inches='tight')
    


#GLUT3 delete after 
protname = 'glut3_apo'
indir = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/output_files/HOLE' %protname
df, df_cleaned = make_df_from_npy(np.load('%s/%s_HOLE.npy' %(indir, protname)))







