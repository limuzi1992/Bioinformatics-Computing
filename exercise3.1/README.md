Result
------

The python program is found in the file exercise_3.py

Method
------

The python program assigns the gene name to the varibale 'gene' 
and the DNA string to the variable 'DNA' at the top of the program.

We use the .startswith() method to find whether the gene starts with 
a Met codon. Note that we are presuming that the DNA sequence is in 
upper-case, since we are looking for 'ATG' instead of 'atg'. The 
.startswith() function returns a logical value (Ture or False).

To figure out whether the gene has a frame 1 Met codon, we first use 
the .find() method to find the position where the first Met codon appears 
in the string. Then, to get the tanslation frame of the first Met codon, we  
use the remainder function % to turn the position into a remainder after 
division by three, and add one to the remainder. Finally, we use the 
if...else statement to print out the result. If the translation frame of the 
first Met codon is 1, the program will show that the gene has a frame 1 Met codon.
If the translation frame of the first Met codon is not 1, the program will ask 
the user to look for the next Met codon.

We use the len() method to count the number of nucleotides in the gene.
The value is assigned to the variable nucleotide_num.

Since we are presuming that the provided sequence has no 5'UTR , we divide the 
number of numcleotides by three to get the number of amino acids in the gene, 
and assign the value to the variable amino_acid_num.

To get the GC content of the gene, we use the .count() method to count the 
number of 'G' and 'C' in the gene, and then we divide the number of 'G' and 'C' 
by the total number of nucleotides in the gene. 

Strengths 
------------------------

The program creates a variable called 'gene' and assigns a value to it. If we want to 
test our program with other gene sequences, we don't need to change the gene name in 
every print statement. We can just assigns another gene name to the varable 'gene'.

Weaknesses
------------------------
The program will produce incorrect answers to the first, second and fifth questions,
if the DNA sequence is in lower-case symbols.

The program can only find out whether the first Met codon in the gene is a frame 1 condon.
If the first Met codon in the gene is not a frame 1 condon, the program fails to figure out
whether the gene has another frame 1 Met codon.

The program presumes that the provided sequence is the sequence to be translated (no 5'UTR).
It will provide wrong number of amino acids in the gene if the sequence doesn't begin with a 
start codon and end with a stop codon.

Solutions
-------
Other solution for question 2:
# We are presuming that the provided sequence is the sequence to be translated (no 5'UTR)
# The program will return the first frame 1 Met condon in the sequence
j = 0
f1_Met_pos = ''
while j < len(DNA):
     if DNA[j:j+3] == 'ATG':
         f1_Met_pos = j
         break
     else:
        j += 3
if f1_Met_pos == '':
    print 'The', gene, 'gene does not have a frame 1 Met codon'
else:
    print 'The', gene, 'gene has a frame 1 Met condon, and its position is', f1_Met_pos + 1

Other solution for question 4:
# We are presuming that the start codon is among 'ATG and 'TTG', and the stop codon is among 'TAG', 'TAA', and 'TGA'
# We can define our own start or stop codon by changing the values of the variables 'start_codon' and 'stop_codon'
start_codon = ['ATG', 'TTG']
stop_codon = ['TAG', 'TAA', 'TGA']
nucleotide_num = len(DNA)
i = 0
start_pos = ''
while i < nucleotide_num:
    if DNA[i:i+3] in start_codon:
        k = i
        stop_pos = ''
        while k < nucleotide_num:
            if DNA[k:k+3] in stop_codon:
                start_pos = i
                stop_pos = k
                break
            else:
                k += 3
        if stop_pos != '':
            trans_frame_len = stop_pos - start_pos 
            amino_acid_num = trans_frame_len / 3
            print 'The start codon', DNA[i:i+3], 'is at position', start_pos + 1
            print 'The stop codon', DNA[k:k+3], 'is at position', stop_pos + 1
            print 'Amino acid number is', amino_acid_num
            break
    else:
        i += 1
    
if start_pos == '':
    print 'Fail to find the translation frame' 
