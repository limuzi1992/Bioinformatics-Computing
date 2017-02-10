from sqlobject import *
import os.path

def init_db(blast_db, new=False):
    connection = os.path.abspath(blast_db)
    connection = 'sqlite:' + connection

    sqlhub.processConnection = connectionForURI(connection)
    
    if new:
        Protein.dropTable(ifExists=True)
        Alignment.dropTable(ifExists=True)
        Protein.createTable()
        Alignment.createTable()

class Protein(SQLObject):
    accession = StringCol(alternateID=True)
    name = StringCol()
    description = StringCol()
    organism = StringCol()
    q_alignment = MultipleJoin('Alignment', joinColumn='query_id')
    s_alignment = MultipleJoin('Alignment', joinColumn='subject_id')

class Alignment(SQLObject):
    query = ForeignKey('Protein')
    subject = ForeignKey('Protein')
    length = IntCol()
    e_value = FloatCol()
    query_seq = StringCol()
    match_seq = StringCol()
    
    
    
    
    
    


    
