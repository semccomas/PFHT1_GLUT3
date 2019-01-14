#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 10:23:37 2019

@author: semccomas
"""


'''
The order of this should go, load trajectory in VMD. Align it on itself
Save as trr 

'''
import numpy as np
from MDAnalysis.analysis.hole import HOLE
from MDAnalysis.analysis.hole import HOLEtraj
import MDAnalysis as mda

protname = 'pfht1_apo'
#indir = '../input_output_f/%s/input_files' %protname
#outdir = '../input_output_f/%s/output_files' %protname
indir = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/input_files' %protname   #HOLE made me have an absolute path for whatever reason
outdir = '/data3/PFHT1_GLUT3/analysis/input_output_f/%s/output_files' %protname
def run_hole(file, name, color):
        if 'pfht1' in name:
            H = HOLE(file, executable = '/home/semccomas/hole2/exe/hole', cvect = [0,0,1], cpoint = [51.435, 51.255, 38.52], sample = 0.01) #52.935 #diff cvect for pfht1 and glut3
        elif 'glut' in name:
            H = HOLE(file, executable = '/home/semccomas/hole2/exe/hole', cvect = [0,0,1], cpoint = [50.035, 51.655, 52.52], sample = 0.01)
            
        H.run()
        H.collect()
        H.plot(linewidth = 2, color = color, label = True)
        np.save(outdir + '/' + name + '.hole_profile.npy', H.profiles[0]) #this is the rxn coordinates that we used below. If you have multiple frames in traj they will be profiles[1], [2] etc

        H.create_vmd_surface(filename = outdir + '/' + name + 'notTTfinalf_sample0.1.vmd')

#runf = '%s/%s.notTTsame_as_finalframe.pdb' %(indir, protname)  #input too long for HOLE but this is the same as protname.system.noich.protonly.alignedaxis.finalframe.pdb 
#run_hole(runf , protname , 'blue')
# run the function above if you need to test how the protein is aligning

     
def run_hole_traj(file, outname,name):
    if 'pfht1' in name:
        H = HOLEtraj(file, executable = '/home/semccomas/hole2/exe/hole', cvect = [0,0,1], cpoint = [51.435, 51.255, 38.52], sample = 0.01) #52.935 #diff cvect for pfht1 and glut3
    elif 'glut' in name:
        H = HOLEtraj(file, executable = '/home/semccomas/hole2/exe/hole', cvect = [0,0,1], cpoint = [50.035, 51.655, 52.52], sample = 0.01)    
    ##old H = HOLEtraj(file, executable = '/home/semccomas/hole2/exe/hole', cvect = [0,0,1], cpoint = [50.035, 51.655, 52.52])
    H.run()
    H.save(outname)

mda_traj = mda.Universe('%s/%s.system.noich.protonly.alignedaxis.pdb' %(indir, protname), 
                         '%s/%s.0_1000ns.skip500.aligned.protonly.trr' %(indir,protname))

run_hole_traj(mda_traj, '%s/%s_HOLE.npy' %(outdir,protname), protname)









