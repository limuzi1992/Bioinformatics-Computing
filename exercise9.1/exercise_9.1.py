import sys

if len(sys.argv) < 2:
    print 'Please provide a DNA sequence on the command-line'
    sys.exit(1)

def ReverseComplement(seq):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'a':'t', 't':'a', 'c':'g', 'g':'c'}
    seq_list = list(seq)
    seq_list.reverse()
    seq_list = map(lambda x: complement.get(x, x), seq_list)
    seq_rc = ''.join(seq_list)
    return seq_rc

input_seq = sys.argv[1]

if '.txt' in sys.argv[1]:
    seq = ''.join(open(input_seq).read().split())
    print 'The reverse complement DNA sequence is', ReverseComplement(seq)
else:
    print 'The reverse complement DNA sequence is', ReverseComplement(input_seq)
