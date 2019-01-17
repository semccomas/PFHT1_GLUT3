#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:48:52 2019

@author: semccomas
"""
import numpy as np
import matplotlib.pyplot as plt 

sim_run = ['pfht1_apo', 'pfht1_holo', 'glut3_apo', 'glut3_holo']
colors = ['#FF1A1A', '#FFA47E','#2B494F', '#6E8A94']
labels = ['PfHT1 apo', 'PfHT1 holo', 'GLUT3 apo', 'GLUT3 holo']
          
fig, (ax_IC, ax_EC) = plt.subplots(nrows =2, ncols = 1, sharex = True)

for n, protname in enumerate(sim_run):
    indir = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/input_files' %protname 
    IC = np.loadtxt('%s/%s.IC_gate_dist.xvg' %(indir, protname))
    EC = np.loadtxt('%s/%s.EC_gate_dist.xvg'%(indir, protname))
    
    ax_IC.plot(IC[:,0]*20, IC[:,1], label = labels[n], color = colors[n])
    ax_IC.set_title('Intracellular gate')
    ax_IC.set_ylabel('distance (nm)')
    ax_IC.set_ylim(0.5, 2)
    ax_IC.set_xlim(0,1000)
    ax_EC.plot(EC[:,0]*20, EC[:,1], label = labels[n], color = colors[n])
    ax_EC.set_title('Extracellular gate')
    ax_EC.set_ylim(0.5, 2)
    ax_EC.set_xlim(0,1000)
    ax_EC.set_ylabel('distance (nm)')
    ax_EC.set_xlabel('time (ns)')
    

lgd = ax_EC.legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 8})
plt.tight_layout()
plt.savefig('../images_graphs/EC_IC_gate.png',bbox_extra_artists=(lgd,), bbox_inches='tight', dpi = 1500)