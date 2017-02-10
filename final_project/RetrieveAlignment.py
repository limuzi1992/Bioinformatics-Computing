from model import *
import sys
import os.path


if len(sys.argv)<4:
    print >>sys.stderr, 'Please provide your database file, query and subject accession numbers'
    sys.exit(1)

blast_db = sys.argv[1]
query = sys.argv[2]
subject = sys.argv[3]

if not os.path.exists(blast_db):
    print >>sys.stderr, 'The database', blast_db, 'does not exist!'
    sys.exit(1)

init_db(blast_db)

try:
    q = Protein.byAccession(query)
except SQLObjectNotFound:
    print >>sys.stderr, 'The query protein', query, 'does not exist!'
    sys.exit(1)

try:
    s = Protein.byAccession(subject)
except SQLObjectNotFound:
    print >>sys.stderr, 'The subject protein', subject, 'does not exist!'
    sys.exit(1)


results = Alignment.selectBy(query=q, subject=s)
    
if results.count()==0:
    print 'No alignment between the two proteins!'
else:
    for r in results:
        print '*********************************************Alignment*************************************************'
        print 'Query:', query, '|', r.query.description, '|', r.query.organism
        print 'Subject:', subject, '|', r.subject.description, '|', r.subject.organism
        print 'Query Length:', r.length
        print 'E-value:', r.e_value
        print  r.query_seq[0:100]
        print r.match_seq[0:100]
