import sys

if len(sys.argv) < 3:
    print 'Please provide a codon-table and a sequence file on the command-line'
    sys.exit(1)

input_code = sys.argv[1]
input_seq = sys.argv[2]

def Not_in_CodonTable(codon, codon_table):
    if len(codon) == 1:
        return 'X'
    else:
        if codon[0] in 'ATCG' and codon[1] in 'ATCG':
            for nuc in 'TCG':
                if codon_table[codon[0:2]+nuc] != codon_table[codon[0:2]+'A']:
                    return 'X'
            return codon_table[codon[0:2]+'A']
        else:
            return 'X'

def Translation(seq, codon_table, start_codon):
    aa_list = []
    for i in range(0,len(seq),3):
        if seq[i:i+3] in codon_table.keys():
            aa_list.append(codon_table[seq[i:i+3]])
        else:
            aa_list.append(Not_in_CodonTable(seq[i:i+3], codon_table))   
    if aa_list[0] is 'X':
        print '(Not sure the initial codon is a start codon or not!)'
    else:
        if start_codon[seq[0:3]]:
            print '(The initial codon is a start codon!)'
            aa_list[0] = 'M'
        else:
            print '(The initial codon is not a start codon!)'
    return ''.join(aa_list)
        
def ReverseComplement(seq):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    reverse_complement = []
    for i in range(-1,-len(seq)-1,-1):
        if seq[i] in complement.keys():
            reverse_complement.append(complement[seq[i]])
        else:
            reverse_complement.append(seq[i])
    seq_rc = ''.join(reverse_complement)
    return seq_rc

file_code = open(input_code)
file_seq = open(input_seq)

code = {}
for line in file_code:
    data = line.split('=')
    code[data[0].strip()] = data[1].strip()
   
codon_table = {}
start_codon = {}
for i in range(0, len(code['AAs'])):
    codon_table[code['Base1'][i] + code['Base2'][i] + code['Base3'][i]] = code['AAs'][i]
    start_codon[code['Base1'][i] + code['Base2'][i] + code['Base3'][i]] = (code['Starts'][i] == 'M')    
   
seq = ''.join(file_seq.read().split()).upper()
for frame in range(0,3):
    print 'The amino acid sequence in translation frame', frame+1, ':'
    print Translation(seq[frame:], codon_table, start_codon), '\n'

seq_rc = ReverseComplement(seq)
for frame in range(0,3):
    print 'The amino acid sequence in reverse translation frame', frame+1, ':'
    print Translation(seq_rc[frame:], codon_table, start_codon), '\n'


