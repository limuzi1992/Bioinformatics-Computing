Result
------

The python program is found in the file exercise_8.1.py

Method
------

The python program is used to translate a DNA sequence in six frames.

The python program requires the users to input a codon-table file and a DNA sequence 
file on the command line.

The python program defines three functions, Not_in_CodonTable(), Translation() ,and 
ReverseComplement(). 

If an unknown symbol is at the third position of a codon and all four possible codons 
correspond to the same amino-acid, the Not_in_CodonTable() function will translate the 
the codon into that amino acid. Otherwise, the function will output 'X'. The Not_in_CodonTable 
function has two arguments. The first one is a codon that is composed of one to three 
nucleotides. The second argument is a codon-table dictionary.


The Translation() function can translate the input DNA sequence into an amino acid 
sequence. It will call the Not_in_CodonTable() function if a codon is not in the codon 
table. The Translation() function can also check whether the initial codon is a start 
codon. This function requires three arguments, a DNA sequence string, a codon-table 
dictionary, and a start-codon dictionary.

The ReverseComplement() function is used to obtain the reverse complement of the input 
DNA sequence. It asks for one argument that is the DNA sequence string.

Strengths 
------------------------

The python program can handle lower-case DNA sequence.

When an unknown symbol is at the third position of a codon, the program can translate 
the codon into an amino acid if all four possible codons correspond to the same amino 
acid.

Weaknesses
------------------------

The program can not find the start codon and the stop codon of the input DNA sequence.

If there is an unknown symbol in a codon, the program fail to list all possible amino 
acids that correspond to the codon.

What I have learned from the exercise
------------------------
In this exercise, I started to learn to organize my codes into functions. In this way, 
I didn't need to repeat a large block of codes in my program. I just called the functions 
several times.
