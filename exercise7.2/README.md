Result
------

The python program is found in the file exercise_7.2.py

Method
------

The python program requires the users to give command-line inputs like
python exercise_7.2.py /media/sf_python/bacteria.code.txt /media/sf_python/anthrax_sasp.nuc.txt.
/media/sf_python/bacteria.code.txt is the path of the codon table file.
/media/sf_python/anthrax_sasp.nuc.txt is the path of the nucleotide sequence file.

The program reads the codon table from the first input file, and creates a dictionary
'codon_table' which maps the codon to its corresponding amino acid. 

The program reads the nucleotide sequence from the second input file, and translates the 
DNA sequence into amino acid sequence according to the dictionary 'codon_table'.

Strengths 
------------------------

The program checks whether the initial codon is a start codon. If the sequence starts
with a start codon, the program will print out 'The initial codon is a start codon !' 
and assign 'M' as the first amino acid. If the sequence doesn't start with a start 
codon, the program will print out 'The initial codon is not a start codon !' and 
directly translate the initial codon.

Weaknesses
------------------------

The program doesn't consider the translation of a nucleotide sequence in six frames. 

What's more, the program fail to find the start codon and stop codon in six frames.
