import sys
import os.path
from model import *
import Bio.SeqIO
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIXML


def blast(query, database, output):
    program = '/usr/bin/blastp'
    commandline = NcbiblastpCommandline(cmd=program, query=query, db=database, outfmt=5, out=output)
    stdout, stderr = commandline()


def load_protein(fasta_file):
    seq_file = open(fasta_file)
    for seq in Bio.SeqIO.parse(seq_file, 'fasta'):
        seqid = seq.id.split('|')
        accession = seqid[1]
        name = seqid[2].split('_')[0]
        seqdesc = seq.description
        description = seqdesc[seqdesc.find(' ')+1:seqdesc.find('OS=')-1]
        organism = seqdesc[seqdesc.find('OS=')+3:seqdesc.find('GN=')-1]
        p = Protein(accession=accession, name=name, description=description, organism=organism)

        
def load_alignment(xml_file):
    handle = open(xml_file)
    for result in NCBIXML.parse(handle):
        query = result.query.split('|')[1]
        query = Protein.selectBy(accession=query)[0]
        for alignment in result.alignments:
            hsp = alignment.hsps[0]
            subject = alignment.title.split('|')[3]
            subject = Protein.selectBy(accession=subject)[0]
            length = alignment.length
            e_value = hsp.expect
            query_seq = hsp.query
            match_seq = hsp.match
            a = Alignment(query=query, subject=subject, length=length, e_value=e_value, query_seq=query_seq, match_seq=match_seq)
                          
#Check input files
if len(sys.argv)<3:
    print >>sys.stderr, 'Please provide your two fasta files'
    sys.exit(1)

#Define blast output names and database name
file1 = sys.argv[1]
file2 = sys.argv[2]
name1 = file1.split('/')[-1].split('.')[0]
name2 = file2.split('/')[-1].split('.')[0]
blastout1 = name1+'TO'+name2+'.xml'
blastout2 = name2+'TO'+name1+'.xml'
blast_db = name1+'AND'+name2+'.db3'

#Check the existence of the database
if os.path.exists(blast_db):
    print 'The database', blast_db, 'has already existed!'
    create_new = raw_input('Do you want to create a new one? (Y or N)')
    if create_new == 'N':
        sys.exit()
    
#Check the existence of the blast results
if not os.path.exists(blastout1):
    print 'BLAST RUNNING ...'
    blast(file1, './blastdb/'+file2, blastout1)
    print 'BLAST DONE'
else:
    print 'The blast result', blastout1, 'has already existed!'

if not os.path.exists(blastout2):
    print 'BLAST RUNNING ...'
    blast(file2, './blastdb/'+file1, blastout2)
    print 'BLAST DONE'
else:
    print 'The blast result', blastout2, 'has already existed!'
    
#Create database
print 'CREATE DATABASE ...'
init_db(blast_db, True)

#Load protein data
print 'LOAD PROTEIN DATA ...'
load_protein(file1)
load_protein(file2)

#Load alignment data
print 'LOAD ALIGNMENT DATA ...'
load_alignment(blastout1)
load_alignment(blastout2)

    
