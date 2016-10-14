Result
------

The python program is found in the file exercise_9.1.py

Method
------

The python program is used to get the reverse complement of the input DNA sequence.

The python program requires the users to input a DNA sequence string or a DNA sequence 
file on the command line.

The python program defines a function, ReverseComplement(). 

The ReverseComplement() function is used to obtain the reverse complement of the input 
DNA sequence. It has one argument, the DNA sequence string. Firstly, the function 
constructs a dictionary that maps a nucleotide to its complement. Next, it converts the 
DNA sequence string into a list and reverse the list. Then, it applies the get() function 
to each element of the list. Finally, the function joins the list into a reverse complement 
DNA sequence.

Strengths 
------------------------

The program can handle both upper-case and lower-case DNA sequence.

The DNA sequence can be input as a string or a file on the command-line.

If there is an invalid symbol in the sequence, the program will put the invalid symbol 
in the reverse complement sequence rather than report an Error.

Weaknesses
------------------------
If there are invalid symbols in the sequence, the program can not report the positions 
of the invalid symbols.

What I have learned from the exercise
------------------------
In this exercise, I practiced how to use the map() function to apply a function to each 
element of a list.
