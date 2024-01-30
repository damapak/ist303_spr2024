<h1 style="text-align: center;">Pair Exercise #2</h1>

<p style="text-align: center;">Last Revised January 2024</p>

Due: PDF \
Assignment type: Pair \
Points: 40 (5 extra credit points possible on top of that)

#### INSTRUCTIONS
Complete the assignment synchronously with a partner. One person should be the "driver" (writing the code) as both of you discuss it. Submit by uploading a pdf with responses to the numbered questions. Each person should submit individually in canvas (the same document) and include the name of your partner in canvas your submission. 

Note that not all responses require screenshots. Questions that ask you to "print" to the terminal, create a variable, or provide your code should have a screenshot, but a number of the questions simply ask for a response and you can simply type the answer, such as "there are 5 words in the poem".

Unless otherwise noted, the assignment should be done within an interactive python session (at the `>>>` prompt).

All questions are 1 point unless otherwise noted. 

## Strings

#### String assignment
1) Describe the key characteristics of a string data type.

Assign the following values to a variable named _mystring_ and then print the variable with the print function:

2) "Hello, World!"
3) 'Hello, World!"

#### String manipulation
4) Assign the poem _At the zoo_ to a variable named _poem_. You can find the text of the poem below:
```
First I saw the white bear, then I saw the black;
Then I saw the camel with a hump upon his back;
Then I saw the grey wolf, with mutton in his maw;
Then I saw the wombat waddle in the straw;
Then I saw the elephant a waving of his trunk;
Then I saw the monkeys - mercy, how unpleasantly they smelt!
```

5) How many characters are in the poem?
6) How many unique characters are in the poem? _(hint: you can use a different data type to save time_)
7) Remove the punctuation from _poem_ and assign it to a new string variable named _poem_nopunc_. _(hint: the translate function combined with string.punctuation will save you time)_
8) Convert the string _poem_nopunc_ to a list that contains the words of the poem.
9) How many words are in the poem? 
10) How many unique words are in the poem?
11) What is the 16th word from the end? (counting backwards from the end)

## Loops
12) Find two ways to output the words of the poem in reverse order. Make sure at least one of these methods utilizes a _while_ or _for_ loop. ***[2 points]***
13) Find two ways to output every other word in the poem. At least one must use a _for_ or _while_ loop. ***[2 points]***
14) Create a loop that prints all the words of the poem and stops when it encounters the word _mutton_. ***[2 points]***

## Tuples
15) create a tuple containing all the words in the poem.

## Lists
Use the list you created previously that contains only the words of the poem in this section.

16) Create a new list called _slice_ that contains the four words starting at offset 38.
17) Use index assignment to replace the first word of the list _slice_ with the word "drink".
18) Sort the list of all poem words. What can you say about how Python deals with capitalization and sorting?

### List comprehensions
Recall that 
```
[expression for item in list if conditional]
```
is the same as:
```
for item in list:
    if conditional:
        expression
```

19) Use a list comprehension to create a list of only the words that begin with the letter "h".' ***[3 points]***


Additionally,
```
[expression1 if condition else expression2 for i in items]
```
is the same as:
```
for i in items:
  if condition:
    expression1
  else:
    expression2
```
20) Use a list comprehension to create a list of all the words, converting any word that _contains_ the letter "m" to ALL CAPS ***[3 points]***
21) Create a nested list variable named _multi_table_ that contains the multiplication table for integers 1 through 12. Each row (list item) holds the list i * j for each i. You will need to iterate over i and j to ccomplish this. ***[4 points]***\
The position `multi_table[i][j]` is equal to `i * j`. Each row of the list is shown below:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[2, 4, 6, 8, 12, 14, 16, 18, 20, 22, 24]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
[6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72]
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84]
[8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
[9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
[11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132]
[12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]
```
## Dictionaries
22) Create a lowercase version of the poem that does not contain punctuation (store it as a string variable). ***[2 points]***
23)  Use a dictionary comprehension to create a dictionary with key:value pairs corresponding to _characters_ and their  corresponding counts in the lowercased poem variable from above. For example, if the letter a occurs 30 times in the poem, and b occurs 6 times, the dictionary
should look like {'a':30, 'b':6 ...} ***[2 points]***
24) Iterate over the dictionary that you created in the previous step to display just the key:value pairs for the vowels (a, e, i, o, u, y) in the poem. ***[3 points]***
- > 3 points extra credit if your code accomplishes this in a single line.
25) Which letters of the english alphabet are not present in the poem? ***[2 points]*** \
_(hint: you can use string.ascii_lowercase from the Python string module to save time.)_ 
- > 2 points extra credit if your code accomplishes this without using a loop, an _if_ statement, or the _in_ operator.
