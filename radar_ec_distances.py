#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 18:56:00 2019

@author: semccomas
"""

import matplotlib.pyplot as plt
import numpy as np
import os 
import scipy.ndimage as sp 
import pandas as pd 

sim_run = ['pfht1_apo', 'pfht1_holo', 'glut3_apo', 'glut3_holo']
gate_num = xrange(1,6)
df = pd.DataFrame(0, index = gate_num, columns = sim_run)  #initialize empty DF to add values into
#gate_resids_P = {1:'K30-E298', 2:'N27-S294', 3:'K30-N295', 4:'K30-D426', 5:'D426-N295'}
#gate_resids_G = {1:'E35-G294', 2:'N32-Y290', 3:'E35-Y291', 4:'E35-P421', 5:'P421-Y291'}
gate_resids = {1:'K30-E298\nE35-G294', 2:'N27-S294\nN32-Y290', 3:'K30-N295\nE35-Y291', 4:'K30-D426\nE35-P421', 5:'D426-N295\nP421-Y291'}


for protname in sim_run:
    indir = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/output_files/resid_dists' %protname
    for x in gate_num:
        f = '%s.%i.EC.xvg' %(protname, x)    #load in gate number order
        dist = np.loadtxt(indir+'/' + f)
        dist = np.mean(dist[400:][:,1])   #take last 100 frames => 200ns average  so we arent biased by jumps in traj
        df.loc[x, protname] = dist    # make df of each average
        pfht1 = df.loc[:,['pfht1_apo', 'pfht1_holo']].mean(axis = 1)
        glut3 = df.loc[:,['glut3_apo', 'glut3_holo']].mean(axis = 1)




#########################
#### RADAR
##############################
labels = [gate_resids[x] for x in list(gate_num)]
markers = np.linspace(0, 2, 3)   #for y label, right now I want 3 data points and the max to be 2 angstrom
str_markers = ["0", "1", "2", "3", "4", "5"] # for y label, not really being used right now


fig= plt.figure()
ax = fig.add_subplot(111, polar=True)
def make_radar_chart(title_n, label_name, color_name, stats, attribute_labels = labels, plot_markers = markers, plot_str_markers = str_markers):

    labels = np.array(attribute_labels)  #just making an array of the labels cat above

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)   # 0 - 6.13 
    stats = np.concatenate((stats,[stats[0]]))     # => end array where you start
    angles = np.concatenate((angles,[angles[0]]))  # => end array where you start


    ax.plot(angles, stats, 'o-', linewidth=2, color = color_name) ## this is the edges connecting dots
    ax.fill(angles, stats, alpha=0.25, label = label_name, color = color_name)   #fill between these plots
    ax.set_thetagrids(angles * 180/np.pi, labels)  #draw labels at each corner
    plt.yticks(markers)  #draw the 0, 1, 2 ... on the plot
    #ax.set_title(title_n) 
    lgd = plt.legend(loc='lower right', bbox_to_anchor=(1.2, 0),prop={'size': 8})
    ax.grid(True) #draws the bullseye looking things, set to false for empty circle

    return stats


a = make_radar_chart("notitle",'PfHT1', '#FF1A1A', pfht1.values) # example
a = make_radar_chart("notitle",'GLUT3', '#6E8A94', glut3.values) # example

plt.savefig('../images_graphs/EC_saltbr.png', dpi = 1000)
    


