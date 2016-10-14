import sys
input_seq = sys.argv[1]

def tandem_repeat(seq):
    for i in range(1,len(seq)/2+1):   
	indicator = True
	if len(seq) % i != 0:
            continue
        repeats = seq[0:i]
        for j in range(i,len(seq),i):
            if seq[j:j+i] != repeats:
	        indicator = False
                break
        if indicator == True:
            print 'The DNA sequence consists of a number of tandem repeats'
            return
    print 'The DNA sequence does not consist of a number of tandem repeats'
    return

tandem_repeat(input_seq)                
                            
