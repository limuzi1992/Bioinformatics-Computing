import sys
input_seq = sys.argv[1]

def ReverseComplement(seq):
    seqlist = list(seq)
    seqlist.reverse()
    nucleotide = 'ATCGatcg'
    complement = 'TAGCtagc'
    for i in range(0,len(seqlist)):
        seqlist[i] = complement[nucleotide.find(seqlist[i])]
    newseq = ''.join(seqlist)
    return newseq

print 'The reverse complement DNA sequence is', ReverseComplement(input_seq)
