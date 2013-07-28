
Problem:
An element is formed of a name and a number. 
A set is formed by partially contiguous elements. 
Merge two such sets.

Idea:
Store all the numbers associated with a name in a compressed bitset.

Implementation:

The implementation uses an open source C++ library for compressed bitset.
http://code.google.com/p/lemurbitmapindex/

Code generates a Python module from the C++ headers from EWAHBoolArray library.

You need to have installed swig (http://www.swig.org/download.html).
And please modify in the Makefile the Python version used.

Usage:

$ make
$ make test


Let me explain:

The user can input two lines with the values (name/number) delimited by comma.

INPUT
-------
a/1, a/2, a/3, a/4, a/128, a/129, b/65, b/66, c/1, c/10, c/42
a/1, a/2, a/3, a/4, a/5, a/126, a/127, b/100, c/2, c/3, d/1

The lines are processed and used to populate two vector of nodes. (please check class Node)
The vectors are printed and then merged.
The merge between bitsets is done using the bitwise OR operator.
Finally the merged vector is printed too.

OUTPUT
----------
Line 0: a/1, a/2, a/3, a/4, a/128, a/129, b/65, b/66, c/1, c/10, c/42
Line 1: a/1, a/2, a/3, a/4, a/5, a/126, a/127, b/100, c/2, c/3, d/1
Merged: a/1, a/2, a/3, a/4, a/5, a/126, a/127, a/128, a/129, b/65, b/66, b/100, c/1, c/2, c/3, c/10, c/42, d/1

