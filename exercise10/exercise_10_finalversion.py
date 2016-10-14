import sys

if len(sys.argv)<3:
    print >>sys.stderr, 'Please provide your microarray data and query gene'
    sys.exit(1)
    
def mean(values):
    return sum(values)/len(values)

def std(values):
    meanvalue = mean(values)
    sq_diff = map(lambda x: (x-meanvalue)**2, values)
    return (sum(sq_diff)/len(sq_diff))**0.5

input_file = sys.argv[1]
input_gene = sys.argv[2]    
    
import csv
microarray_file = open(input_file)
rows = csv.DictReader(microarray_file)
tumors = {}
overall = []
for r in rows:
    overall.append(float(r[input_gene]))
    if r['TUMOUR'] not in tumors:
        tumors[r['TUMOUR']] = [float(r[input_gene])]
    else:
        tumors[r['TUMOUR']].append(float(r[input_gene]))

print 'The mean of the expression values of', input_gene, 'overall is', mean(overall)
print 'The standard deviation of the expression values of', input_gene, 'overall is', std(overall)

for tumor in tumors:
    print 'The mean of the expression values of', input_gene, 'within', tumor, 'is', mean(tumors[tumor])
    print 'The standard deviation of the expression values of', input_gene, 'within', tumor, 'is', std(tumors[tumor])

microarray_file.close()
