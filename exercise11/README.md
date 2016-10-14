Result
------

The python program is found in the file exercise_11.py

Method
------

The python program is used to compute amino acid frequencies for two human proteomes from 
different databases and compare the human amino acid frequencies of these two proteomes.

The python program requires the users to have the biopython package installed in their python.
It also requires the users to input the human proteomes from the two databases on the command line.
In this case, the first input file should be the human proteome from RefSeq, the second input file
should be the human proteome from SwissProt. The example command line is shown below.
python exercise_11.py human.protein.fasta.gz uniprot_sprot_human.dat.gz

The program defines three functions, Freq(), MaxandMin(), and Compare2Dict().

The Freq() function computes the frequency of each amino acid of the human proteome and returns a
dictionary that stores the amino acid frequencies. The function has two arguments, the proteome 
file and the file format. 

The MaxandMin() function finds the amino acid that occurs most in the human proteome and the amino
acid that occurs least in the human proteome. The function also has two arguments, the dictionary 
produced by the Freq() function and the data source from which the human proteome comes.

The Compare2Dict() function compares the human amino acid frequencies of the two proteomes. It prints
out the result like 'L RefSeq : SwissProt = 6425942 : 1127071'. The function has four arguments, the two
dictionaries that are produced by the Freq() function and need to be compared, and the data sources of the two
human proteomes.

For the two human proteomes, the program first calls the Freq() function to get the amino acid frequencies of the 
human proteome. Next, it calls the MaxandMin() funtion to find the amino acid that occurs most and the amino acid 
that occurs least. Finally, the program calls the Compare2Dict() function to compare the amino acid frequencies of 
the two human proteomes.

Strengths 
------------------------

The program can read both gz file and plain txt file.

What's more, the program prints out the comparison result from the amino acid that occurs most in the first input 
proteome to the amino acid that occurs least in that proteome.

What I have learnt in the exericse
-------
In this exercise, I continued to practice organizing my codes by defining functions. 
And I got more familiar with using 'key' and lambda expression in max(), min(), and sorted().
