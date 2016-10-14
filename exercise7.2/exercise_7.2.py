import sys
input_code = sys.argv[1]
input_seq = sys.argv[2]

file_code = open(input_code)
file_seq = open(input_seq)

code = {}
for line in file_code:
    data = line.split('=')
    code[data[0].strip()] = data[1].strip()
   
codon_table = {}
start_codon = {}     
for i in range(0,len(code['AAs'])):
    codon_table[code['Base1'][i] + code['Base2'][i] + code['Base3'][i]] = code['AAs'][i]
    start_codon[code['Base1'][i] + code['Base2'][i] + code['Base3'][i]] = (code['Starts'][i] == 'M')

aa_list = []    
seq = ''.join(file_seq.read().split())
if start_codon[seq[0:3]]:
    print 'The initial codon is a start codon !'
    aa_list.append('M')
else:
    print 'The initial codon is not a start codon !'
    aa_list.append(codon_table[seq[0:3]])
for j in range(3,len(seq),3):
        aa_list.append(codon_table[seq[j:j+3]])
    
aa_seq = ''.join(aa_list)
print 'The amino acid sequence is', aa_seq
    
file_code.close()
file_seq.close()
