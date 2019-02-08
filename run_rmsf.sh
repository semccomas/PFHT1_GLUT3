#going to read from input_files and put the 

in_dest=input_files
out_dest=output_files

for i in ../input_output_f/*/replica_?/
do
	echo $i
	ls $i/$in_dest/protein_only_traj
	ls $i/$out_dest/RMSF
	echo
done

#gmx rmsf -f ../../input_files/glut3_holo.0_1000ns.skip500.aligned.protonly.WITHich.trr -s ../../input_files/glut3_holo.system.protonly.WITHich.pdb -xvg none -res -o rmsf_res.xvg
#gmx rmsf -f ../../input_files/glut3_holo.0_1000ns.skip500.aligned.protonly.WITHich.trr -s ../../input_files/glut3_holo.system.protonly.WITHich.pdb -xvg none -o rmsf_atom.xvg
