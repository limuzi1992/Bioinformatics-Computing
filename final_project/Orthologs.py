from model import *
import sys
import os.path

def print_alignment(obj):
    print '**************ALignment**************'
    print 'Query:', obj.query.accession, '|', obj.query.description, '|', obj.query.organism
    print 'Subject:', obj.subject.accession, '|', obj.subject.description, '|', obj.subject.organism
    print 'Query Length:', obj.length
    print 'E-value:', obj.e_value
    print obj.query_seq[0:75]
    print obj.match_seq[0:75]
    print '\n'

def write_alignment(obj, fout):
    fout.write('**************ALignment**************'+'\n')
    fout.write('Query: '+obj.query.accession+' | '+obj.query.description+' | '+obj.query.organism+'\n')
    fout.write('Subject: '+obj.subject.accession+' | '+obj.subject.description+' | '+obj.subject.organism+'\n')
    fout.write('Query Length: '+str(obj.length)+'\n')
    fout.write('E-value: '+str(obj.e_value)+'\n')
    fout.write(obj.query_seq[0:75]+'\n')
    fout.write(obj.match_seq[0:75]+'\n')
    fout.write('\n')

def get_best(aligns, evalue):
    a_evalue = evalue
    best = []
    for a in aligns:
        if a.e_value<a_evalue:
            best = [[a.query.id, a.subject.id, a]]
            a_evalue = a.e_value
        elif a.e_value==a_evalue:
            best.append([a.query.id, a.subject.id, a])
    return best
            
if len(sys.argv)<3:
    print >>sys.stderr, 'Please provide your database file and e-value'
    sys.exit(1)

blast_db = sys.argv[1]
evalue = float(sys.argv[2])

if not os.path.exists(blast_db):
    print >>sys.stderr, 'The database', blast_db, 'does not exist!'
    sys.exit(1)
    
init_db(blast_db)

write_file = raw_input('Do you want to write or print the results? (W or P)')
if write_file=='W':
    fout = open('./Orthologs.txt', 'w')


count = 0
for r in Protein.selectBy(organism='Escherichia coli (strain K12)'):
    query = r.q_alignment
    subject = r.s_alignment
    q_best = get_best(query, evalue)
    s_best = get_best(subject, evalue)
    for i in q_best:
        for j in s_best:
            if i[0]==j[1] and i[1]==j[0]:
                count = count + 1
                q = i[2]
                s = j[2]
                if write_file=='W':
                    fout.write('-----------------------------Orthologs------------------------------'+'\n')
                    write_alignment(q,fout)
                    write_alignment(s,fout)
                else:
                    print '-----------------------------Orthologs------------------------------'
                    print_alignment(q)
                    print_alignment(s)

print 'There are', count, "pairs of orthologous proteins that are mutually best hits in the species' proteomes!"

if write_file=='W':
    fout.write('There are '+str(count)+" pairs of orthologous proteins that are mutually best hits in the species' proteomes!")
    fout.close()
        
    







































































































    
        
    
