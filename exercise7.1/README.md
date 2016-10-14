Result
------
The python programs are found in the files exercise_7.1_method1.py, exercise_7.1_method2.py, 
and exercise_7.1_method3.py.

Method
------
The three python programs use different methods to define the ReverseComplement() function
which computes the reverse complement of a sequence.

The three python programs all require the users to give a command-line input like
python exercise_7.1_method1.py atcg, call the ReverseComplement() function, and print 
out the reverse complement of the sequence. 

Comparison
------
Among the three methods, the first one is the fastest way to compute the reverse 
complement sequence. It uses a dictionary to map the nuleotide to its complement. 
This program runs through the sequence backwards, quickly finds the complement of 
the nucleotide, and appends the complement to a list. Finally, the reverse complement 
sequence can be obtained by joining the elements of the list to a string.

Compared with the first method, the second program goes through the sequence five times 
to get the final result. Firstly, it uses [::-1] to reverse the sequence, and then it 
reads through the sequence four times to replace the nucleotide with its complement. 
This program takes longer time than the first one.

The third method is also slower than the first program. This method converts the sequence 
string to a list first, and uses the reverse() function to reverse the list. Next, it runs 
through the list to change the nucleotide into its complement. To find the complement of 
a nucleotide, the program finds the position of the nucleotide in the variable 'nucleotide' 
first, and then gets its complement by looking at what's the character at the same 
position in the variable 'complement'. This method takes longer time than directly using a 
dictionary to find the complement of a nucleotide.
