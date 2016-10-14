Result
------
The python program is found in the file exercise_4.2.py

Method
------
The python program defines a function tandem_repeat(). 

The tandem_repeat() function determines whether a DNA sequence is 
composed of a number of perfect tandem repeats.

The length of a tandem repeat is greater than or equal to one and 
less than or equal to the length of half sequence.

The function tests different repeat length from one to half length 
of the sequence, and partitions the sequence according to the repeat 
length. If all of sequence fragments are the same, the function will 
admit that the DNA sequence consists of a number of perfect tandem 
repeats.   

The python program requires the users to give a command-line input
, calls the tandem_repeat() function, and returns the decision.

Strengths 
------------------------
The program allows the users to enter the DNA sequence in the command line.

Weaknesses
------------------------
If the users enter some invalid characters, the program will not report the error.

If the input sequence contains a mixture of upper and lower-case nucleotide symbols 
like atgAtg, the program will fail to tell whether the DNA sequence consists of perfect 
tandem repeats or not.

What's more, the program can't determine whether a sequence contains a number of 
tandem repeats or not.
