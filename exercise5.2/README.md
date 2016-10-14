Result
------
The python program is found in the file exercise_5.2.py

Method
------
The python program defines two functions, complement() and reverse_complement().

The complement() function computes the complement of a nucleotide. 

The reverse_complement function calls the complement() function and computes 
the reverse complement of a sequence.

The python program requires the users to give a command-line input. If the first half
of the input sequence is the same as the second half of the sequence, the DNA sequence 
is a reverse complement palindrome. 

Strengths 
------------------------
If the users input some invalid characters, the program will report the error as
'ERROR: Invalid Primer'.

Weaknesses
------------------------
If the input primer contains a mixture of upper and lower-case nucleotide symbols 
like atgCat, the program will fail to tell whether the primer is a reverse
complement palindrome or not.
