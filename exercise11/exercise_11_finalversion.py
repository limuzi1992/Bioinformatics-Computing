import Bio.SeqIO
import sys
import gzip

if len(sys.argv) < 3:
    print >> sys.stderr, 'Please provide two sequence files that need to be compared'
    sys.exit(1)

def Freq(seq_file, fileformat):
    if seq_file.endswith('.gz'):
        seqs = gzip.open(seq_file)
    else:
        seqs = open(seq_file)
    aa_dict = {}
    for seqrec in Bio.SeqIO.parse(seqs, fileformat):
        for aa in seqrec.seq:
            if aa not in aa_dict:
                aa_dict[aa] = 1
            else:
                aa_dict[aa] = aa_dict[aa] + 1
    seqs.close()
    return aa_dict

def MaxandMin(aa_dict, datasource):
    aa_max = max(aa_dict, key=aa_dict.get)
    aa_min = min(aa_dict, key=aa_dict.get)
    print 'The amino acid occurs most in the',datasource, 'proteome is', aa_max, 'and its frequency is', aa_dict[aa_max]
    print 'The amino acid occurs least in the', datasource, 'proteome is', aa_min, 'and its frequency is', aa_dict[aa_min]

def Compare2Dict(dict1, dict2, datasource1, datasource2):
    key_list = sorted(dict1, key = lambda x: -dict1[x])
    for key in dict2:
        if key not in key_list:
            key_list.append(key)
    for key in key_list:
        print key, datasource1, ':', datasource2, '=', dict1.get(key, 0), ':', dict2.get(key, 0)
    
refseq_file = sys.argv[1]
swiss_file = sys.argv[2]
refseq_dict = Freq(refseq_file, 'fasta')
MaxandMin(refseq_dict, 'RefSeq')
swiss_dict = Freq(swiss_file, 'swiss')
MaxandMin(swiss_dict,'SwissProt')
Compare2Dict(refseq_dict, swiss_dict, 'RefSeq', 'SwissProt')






    
    
