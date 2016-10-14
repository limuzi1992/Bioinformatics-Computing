#Assign the gene name to the variable gene
gene = 'SASP'

#Assign the gene sequence to the variable DNA
DNA = 'TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG'




#Find out whether the gene sequence starts with Met codon and print out the result
print 'Does the', gene, 'gene start with Met codon:', DNA.startswith('ATG')




#Find out the position of the Met codon in the gene
Met_pos = DNA.find('ATG')

#Find out the translation frame of the Met codon
trans_frame = Met_pos % 3 + 1

#Print out whether the first Met codon in the gene is a frame 1 Met codon
if trans_frame == 1:
    print 'The', gene, 'gene has a frame 1 Met codon'
else:
    print 'The first Met codon in the', gene, 'gene is not the frame 1 Met codon, please look for the next Met codon'



	
#Count the number of nucleotides in the gene
nucleotide_num = len(DNA)

#Print out the number of nucleotides in the gene
print 'The', gene, 'gene has', nucleotide_num, 'nucleotides'




#Find out the number of amino acids in the protein translated from the gene
amino_acid_num = nucleotide_num / 3 - 1

#Print out the number of amino acids in the protein
print 'The', gene, 'protein has', amino_acid_num, 'amino acids'




#Count the number of G and C in the gene
GC_count = DNA.count('G') + DNA.count('C')

#Calculate the GC content of the gene
GC_content = float(GC_count) / nucleotide_num

#Print out the GC content of the gene
print 'The GC content of the', gene, 'gene is', GC_content * 100, '%'
