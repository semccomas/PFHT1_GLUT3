prot=glut3_holo
indir=../input_output_f/$prot/input_files

gmx select -f $indir/$prot.system.protonly.WITHich.pdb -on $indir/$prot.gate_residues.ndx -ofpdb $indir/$prot.testing_gate_residues.pdb -s $indir/protein_only.tpr -sf $indir/resid_select.dat

gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -n $indir/$prot.gate_residues.ndx -xvg none -o $indir/$prot.EC_gate_dist.xvg -s $indir/protein_only.tpr -ref "com of group 0" -sel "com of group 1"

gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -n $indir/$prot.gate_residues.ndx -xvg none -o $indir/$prot.IC_gate_dist.xvg -s $indir/protein_only.tpr -ref "com of group 2" -sel "com of group 3"





prot=pfht1_holo
indir=../input_output_f/$prot/input_files

gmx select -f $indir/$prot.system.protonly.WITHich.pdb -on $indir/$prot.gate_residues.ndx -ofpdb $indir/$prot.testing_gate_residues.pdb -s $indir/protein_only.tpr -sf $indir/resid_select.dat

gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -n $indir/$prot.gate_residues.ndx -xvg none -o $indir/$prot.EC_gate_dist.xvg -s $indir/protein_only.tpr -ref "com of group 0" -sel "com of group 1"

gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -n $indir/$prot.gate_residues.ndx -xvg none -o $indir/$prot.IC_gate_dist.xvg -s $indir/protein_only.tpr -ref "com of group 2" -sel "com of group 3"






prot=glut3_apo
indir=../input_output_f/$prot/input_files

gmx select -f $indir/$prot.system.protonly.WITHich.pdb -on $indir/$prot.gate_residues.ndx -ofpdb $indir/$prot.testing_gate_residues.pdb -s $indir/protein_only.tpr -sf $indir/resid_select.dat

gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -n $indir/$prot.gate_residues.ndx -xvg none -o $indir/$prot.EC_gate_dist.xvg -s $indir/protein_only.tpr -ref "com of group 0" -sel "com of group 1"

gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -n $indir/$prot.gate_residues.ndx -xvg none -o $indir/$prot.IC_gate_dist.xvg -s $indir/protein_only.tpr -ref "com of group 2" -sel "com of group 3"








prot=pfht1_apo
indir=../input_output_f/$prot/input_files

gmx select -f $indir/$prot.system.protonly.WITHich.pdb -on $indir/$prot.gate_residues.ndx -ofpdb $indir/$prot.testing_gate_residues.pdb -s $indir/protein_only.tpr -sf $indir/resid_select.dat

gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -n $indir/$prot.gate_residues.ndx -xvg none -o $indir/$prot.EC_gate_dist.xvg -s $indir/protein_only.tpr -ref "com of group 0" -sel "com of group 1"

gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -n $indir/$prot.gate_residues.ndx -xvg none -o $indir/$prot.IC_gate_dist.xvg -s $indir/protein_only.tpr -ref "com of group 2" -sel "com of group 3"
