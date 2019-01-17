#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:26:44 2019

@author: semccomas
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sp

indir = '/data3/PFHT1_GLUT3/analysis/input_output_f' 
RMSD_file = 'RMSD_TM7B_alignTM7B.dat'

def plot_RMSD(sim_name, cname, lname):
    arr = np.loadtxt('%s/%s/output_files/RMSD/%s_%s' %(indir,sim_name,sim_name,RMSD_file), skiprows = 2)
    #arr = np.loadtxt('%s/%s_RMSD_TM7B_alignTM7B.dat' %(indir, sim_name), skiprows = 2)
    arr = np.insert(arr, 0, [0,0], axis = 0)   #add on the 0 at the beginning because I don't want to read the NAN
    a = sp.filters.gaussian_filter(arr[:,1], sigma = 0)  #0 = no filter
    plt.plot(arr[:,0], a, color = cname, label = lname)
    plt.legend(loc=2, prop={'size': 8})
    plt.xlim(0,1000)
    plt.ylim(0,3)

plot_RMSD('pfht1_apo', '#FF1A1A', 'PfHT1 apo')
plot_RMSD('pfht1_holo', '#FFA47E', 'PfHT1 holo')
plot_RMSD('glut3_apo', '#2B494F', 'GLUT3 apo')
plot_RMSD('glut3_holo', '#6E8A94', 'GLUT3 holo')

##3D548E grey blue
## #0C2FBD more blue
plt.xlabel('time (ns)')
plt.ylabel(ur'TM7b RMSD (\u00c5)')
plt.savefig('../images_graphs/RMSD_TM7b.png', dpi = 1500)    

