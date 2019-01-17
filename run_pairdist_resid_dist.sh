prot=pfht1_holo
indir=../input_output_f/$prot/input_files
outdir=../input_output_f/$prot/output_files/resid_dists

gate=1
resid1="30"
resid2="298"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=2
resid1="27"
resid2="294"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=3
resid1="30"
resid2="295"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=4
resid1="30"
resid2="426"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=5
resid1="426"
resid2="295"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"





#################################################################################################
#################################################################################################

prot=glut3_holo
indir=../input_output_f/$prot/input_files
outdir=../input_output_f/$prot/output_files/resid_dists

gate=1
resid1="35"
resid2="294"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=2
resid1="32"
resid2="290"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=3
resid1="35"
resid2="291"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=4
resid1="35"
resid2="421"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=5
resid1="421"
resid2="291"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.EC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


