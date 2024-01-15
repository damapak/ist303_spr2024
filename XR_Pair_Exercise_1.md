<h1 style="text-align: center;">Pair Exercise #1</h1>

<p style="text-align: center;">Last Revised January 10, 2024</p>

Due: PDF \
Assignment type: Pair

#### INSTRUCTIONS
Complete the assignment synchronously with a partner. Submit by uploading a pdf with responses to the numbered questions. Each person should submit individually in canvas and include the name of your partner in your submission.

Unless otherwise noted, the assignment should be done within an interactive python session (at the `>>>` prompt).

## Python installation
1) What is the version of your Python installation?
2) Print "Hello, World!" in the python interactive interpreter. Store the "Hello, World!" program in a file named _hello.py_ and run it. Attach a screenshot of your terminal and output.

## Data types, values, and variables (Lubanovic ch. 2)

#### Data types
Determine the types of the following literals in the python interpreter:

3) 15
4) 3.14
5) False
6) (55, 33, 67)
7) [55, 33, 67]
8) {"food": "pizza", "drink": "lemonade", "snack": "chips"}

#### Variables
9) what is meant by the term variable?
10) what does it mean for an object to be _immutable_?
11) what does it mean to assign a value to an object?

#### Variable assignment: mutable vs. immutable
Integers in python are an immutable type. Perform the steps below and then answer the question(s) that follow.
- assign the number 12 to a variable named _a_
- check the internal python id of the object using `id(a)`
- assign a variable named _b_ equal to _a_ (the variable name, not the value of _a_)
- check the python id of the object _b_: `id(b)`
- assign the value of 99 to the variable _a_
- check the id of _a_
12) **What does this tell you about how python stores and tracks variable assignment for immutable data types? [2 pts]**

Lists are mutable data types (more on lists later). Perform the steps below and then answer the question(s) that follow.
- assign the variable _list1_ equal to `[1,2,3]`
- assign the variable _list2_ equal to _list1_
- check the id of _list1_ and _list2_
- add an item to _list1_ using the following command: `list1.append(4)`
- print the contents of _list1_ and _list2_ to the terminal
- check the id of _list1_ and _list2_
13) **What insight does this give you into how python stores and tracks mutable data types? [2 pts]**

For each of the following, indicate whether it is a valid variable name:

14) _a
15) &b
16) True
17) T
18) shrek
19) string
20) 77
21) "donkey"

## Numbers (Lubanovic ch. 3)
Determine the output of the following code snippets

22) bool(33)
23) bool(2.789)
24) bool (0.00)
25) bool("False")
26) 100 + 02
27) 17 // 5
28) 17 % 5
29) what is the `//` operator calculating? 
30) what is the `%` operator calculating?

Write code to compute the following:

31) 17 squared
32) True * 9
33) The area of a circle with radius 7
