Result
------

The python program is found in the file exercise_10.py

Method
------

The python program is used to compute the mean and standard deviation of 
the expression values of a specific gene overall, and within each sample category.

The python program requies the users to input the microarray data(csv file) and the gene of 
interest on the command line. The example command line is shown below.
python exercise_10.py data.csv R00884

The program defines two functions, mean() and std(). The mean() function calculates the mean of 
a list of numbers. The mean formula is Xmean = (X1+X2+...+Xn)/N. The std() function calculates 
the standard deviation of a list of numbers. The standard deviation formula is 
s = sqrt(((X1-Xmean)^2+(X2-Xmean)^2+...+(Xn-Xmean)^2)/N). 

The program requires the users to have the csv package installed in their python. The program 
reads the microarray data in csv format and extracts the expression values of the specific 
gene overall and within each sample category. The overall expression values of the gene is 
stored in a list. And the expression values of the gene in different sample categories are 
stored in a dictionary. Each sample category is a key of the dictionary. And the expression 
values of the gene within the sample category are the corresponding values. 

Finally, the python program calls the mean() and std() functions to compute the mean and
standard deviation of the expression values of the gene overall, and within each sample category.

Strengths 
------------------------

The program stores the expression values of the gene in different sample categories in a dictionary.
If the users don't know how many sample categories are in the microarray data, the program can still
extract the expression values of the gene in all sample categories.

Weaknesses
------------------------

The program fails to read microarray data in other formats. 

If the gene of interest is not in the microarray data, the program can not report the error.

Solutions
-------

The python program defines two functions to compute the mean and standard deviation of a list of values.
There is another way to do the calculation. We can import the package numpy and call the functions 
numpy.mean() and numpy.std().
