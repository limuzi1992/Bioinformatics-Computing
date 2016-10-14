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

def reverse_complement(seq):
    new_seq = ''
    for nuc in seq:
        if complement(nuc) == False:
            return False
        else:
            new_seq = complement(nuc) + new_seq
    return new_seq

def palindrome(primer):
    if reverse_complement(primer) == False:
        print 'ERROR: Invalid Primer'
    else:
        if reverse_complement(primer[:len(primer)/2])== primer[len(primer)/2:]:
            print 'The DNA sequence is a reverse complement palindrome'
        else:
            print 'The DNA sequence is not a reverse complement palindrome'

palindrome(input_primer)
        
