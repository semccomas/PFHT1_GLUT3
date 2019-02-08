#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:53:21 2019

@author: semccomas

input PDB needs to be specified for each file
"""
import numpy as np
import matplotlib.pyplot as plt

prot = ['pfht1_apo', 'pfht1_holo', 'glut3_apo', 'glut3_holo']

pfht1_betas = []
glut3_betas = []

for prot_name in prot:
    for rep in xrange(1,4):
        inpath='/data3/PFHT1_GLUT3/analysis/input_output_f/%s/replica_%i/input_files/protein_only_traj' %(prot_name, rep)
        outpath='/data3/PFHT1_GLUT3/analysis/input_output_f/%s/replica_%i/output_files/RMSF' %(prot_name, rep)
        ## process PDB function here
        ## make RMSF plot here 
        


#plot RMSF plot
prot_name = 'pfht1_holo'
rep=1
inpath = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/replica_%i/input_files/protein_only_traj' %(prot_name, rep)
outpath = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/replica_%i/output_files/RMSF' %(prot_name, rep)
pdb_in = open('%s/%s.system.protonly.WITHich.pdb' %(inpath, prot_name)).read().splitlines()
beta_in = np.loadtxt('%s/rmsf_atom.xvg' %outpath)

#pdb_in[61:66] is ' 0.00' ie beta
beta_scaled=beta_in[:,1]*1000


    