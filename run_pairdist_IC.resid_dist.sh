prot=pfht1_apo
indir=../input_output_f/$prot/input_files
outdir=../input_output_f/$prot/output_files/resid_dists

gate=1
resid1="403"
resid2="133"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=2
resid1="82"
resid2="133"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=3
resid1="396"
resid2="140"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=4
resid1="396"
resid2="336"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=5
resid1="332"
resid2="140"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=6
resid1="332"
resid2="336"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"




#################################################################################################
#################################################################################################

prot=glut3_apo
indir=../input_output_f/$prot/input_files
outdir=../input_output_f/$prot/output_files/resid_dists

gate=1
resid1="398"
resid2="144"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=2
resid1="90"
resid2="144"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=3
resid1="391"
resid2="151"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=4
resid1="391"
resid2="331"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=5
resid1="327"
resid2="151"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


gate=6
resid1="327"
resid2="331"
gmx pairdist -f $indir/$prot.0_1000ns.skip500.aligned.protonly.WITHich.trr -xvg none -o $outdir/$prot.$gate.IC.xvg -s $indir/protein_only.tpr -ref "resid $resid1" -sel "resid $resid2"


