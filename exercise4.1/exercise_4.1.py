def complement(nuc):
    nucleotide = 'ATCGatcg'
    complement = 'TAGCtagc'
    i = nucleotide.find(nuc)
    nuc_comp = complement[i]
    return nuc_comp

def reverse_complement(codon):
    new_codon = ''
    for nuc in codon:
        new_codon = complement(nuc) + new_codon
    return new_codon

codon = raw_input('Enter your codon:')
print 'The reverse complement of the "', codon, '" codon is "', reverse_complement(codon), '"'
