# My favorate gene is TP53
# The forward primer is ACGACGGTGACACGCTTCCCTG
# The reverse primer is CGCTAGGATCTGACTGCGGCTC

import sys
input_primer = sys.argv[1]

def complement(nuc):
    nucleotide = 'ATCGatcg'
    complement = 'TAGCtagc'
    i = nucleotide.find(nuc)
    if i == -1:
        return False
    else:
        nuc_comp = complement[i]
        return nuc_comp

def reverse_complement(primer):
    new_primer = ''
    for nuc in primer:
        if complement(nuc) == False:
            return False
        else:
            new_primer = complement(nuc) + new_primer
    return new_primer

if reverse_complement(input_primer) == False:
    print 'ERROR: Invalid Primer'
else:
    print 'The reverse complement sequence for the primer is', reverse_complement(input_primer)
