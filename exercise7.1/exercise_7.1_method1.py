import sys
input_seq = sys.argv[1]

def ReverseComplement(seq):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'a':'t', 't':'a', 'c':'g', 'g':'c'}
    reverse_complement = []
    for i in range(-1,-len(seq)-1,-1):
        reverse_complement.append(complement[seq[i]])
    newseq = ''.join(reverse_complement)
    return newseq

print 'The reverse complement DNA sequence is', ReverseComplement(input_seq)
        
        
    
