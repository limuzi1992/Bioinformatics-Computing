import sys

if len(sys.argv) < 2:
    print 'Please provide a DNA sequence on the command-line'
    sys.exit(1)

input_seq = sys.argv[1]
seq = ''.join(open(input_seq).read().split())
nuc_count = {}
for i in range(0,len(seq)):
    nuc = seq[i]
    if nuc not in nuc_count.keys():
        nuc_count[nuc] = 1
    else:
        nuc_count[nuc] = nuc_count[nuc]+1

for nuc, count in sorted(nuc_count.items(), key=lambda x: x[1], reverse=True):
    print nuc, ':', count
