import sys
input_seq = sys.argv[1]

def ReverseComplement(seq):
    newseq = seq[::-1]
    newseq = newseq.replace('A','%').replace('T', 'A').replace('%', 'T')
    newseq = newseq.replace('C', '%').replace('G', 'C').replace('%', 'G')
    newseq = newseq.replace('a', '%').replace('t', 'a').replace('%', 't')
    newseq = newseq.replace('c', '%').replace('g', 'c').replace('%', 'g')
    return newseq

print 'The reverse complement DNA sequence is', ReverseComplement(input_seq)
