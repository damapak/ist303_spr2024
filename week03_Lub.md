# Week 3: Python

## General
Python structures code with indentation (not brackets)
- recommend using spaces, not tabs (different text editors store tab chars differently)

Statements/conditions end in `:`
```
if 1 == 2:
  print("True")
```
compare  to C:
```
if (1==2) {
  printf("True");
}
```
comment with `#` (hash/pound)
- `# This is a comment`
- will not be executed by the python interpreter

line continuation: `\` 
```
print("this is one \
line")
```



## Lubanovic Chapter 4: If

### `If` statement
- _execute code if a condition is met (evaluates to True)_ \
`if condition:` _...code to execute if true_

```
if 2 > 1: print("2 heads are better than 1")

if 2 > 1:
  print("2 heads are better than 1")
```

Additional control statements:
### `else`
- _allows code to be run when condition is NOT met (in if or any number of elif conditions)_ \
`else:` ...code to run if all preceding conditions are False
### `elif` 
- _'else if', allows additional conditions to check for true_ \
`elif condition:` ... code to run if elif condition is true

### Example - if_fruit.py
_ps> new-item if_fruit.py_ \
_term> touch if_fruit.py_
``````
# if_fruit.py

fruit = "apple"
if fruit == "orange":
  print(f"take a bite of {fruit}")
elif fruit == "apple":
  print(f"pass your {fruit} to a friend")
else:
  print(f"you forgot to bring your {fruit}")
  ``````

### Conditions: comparison operators
Return either `True` or `False`.  _True_ and _False_ are special values in Python - you can see that they are objects of type 'bool' by typing `type(True)` in a python session. 
- `==`  equality
- `!=`  inequality
- `<`   less than
- `<=`  less than or equal
- `>`   greater than
- `>=`  greater than or equal
### Boolean operators
aka logical operators. Combine conditions using these operators for more complex testing.
- `and` : returns True if _both_ conditions are True
- `or` : returns True if _either_ condition is True
- `not` : returns True if the statement is true. Often used in conjunction with `in`.

_What do the following statements evaluate to?_
```
4 == 4 or 2 > 7
4 == "4"
True or False
True is False
True and False
```

#### Additional operators
- `in` : test membership in an object

```
'c' in 'branch'
```

#### Equality vs. Reference
- `is` : test if two variables refer to the same object in memory 
- not to be confused with equality, `==`, which tests equality of values

try: 
```
2 is 2

a=[1,2,3]
b=[1,2,3]
a is b

a=[5,6,7]
b=a
a is b
```

### True and False
The following evaluate to False:
- `False`  -boolean
- `0`  -zero integer
- `0.0`  -zero float
- `None`  -Null
- `''`  -empty string
- `[]`  -empty list
- `()`  -empty tuple
- `{}`  -empty dict
- `set()`  -empty set

**All other values evaluate to True** \
_this is extremely helpful for evaluating statements such as `if` or `while`_

# Chapter 5: Strings
- strings are immutable (can't be changed in place). Once defined, a string object cannot be edited.

- `str()` function converts object to string
- multiline strings: start and end with three quote marks  `'''` or `"""`
  - (whichever you use the start and end must be the same)
- concatenate (combine) strings with `+`
- duplicate a string with `*`

### String indexing and slicing
In Python, brackets `[]` are used to access elements of _subscriptable_ objects. 

A _subscriptable_ object is composed of smaller, independently accessible items/objects. Strings are composed of characters, lists are composed of elements, etc. Integers are not composed of any smaller objects. 

The format uses square brackets: `object[]`, this is the same for both **indexing** and **slicing**. Indexing is used if a single value is passed in, slicing utilizes `:` within the brackets.

### Indexing
Access a character by its corresponding index value (remember that Python is `0` indexed, meaning that the first position is accessed by index value `0`): 

### `mystring[0]`
  - can use integer values OR expressions
  - any expression that evaluates to a single integer will return the character at that index
  - you can use negative index values to start counting from the end of the object; `mystring[-1]` returns the last character in _mystring_

### Slicing (Strings)
A slice is similar to an index, but rather than a single item it accesses multiple items by specifying a _start_ and _end_ index position.

### `mystring[start:end]`
  - _inclusive_ of start, _exclusive_ of end [ , )
  - omitting a start or end parameter defaults to the start or end of the string
    - `mystring[:5]` will return characters from the start up until it gets to index position 5
    - `mystring[2:]` will return characters starting at index position 2 to the end
  - `mystring[:]` simply returns `mystring`

one of the following results in an error; can you guess which?
```
"park"[0]
"park"[4]
"park"[1:]
"park"[:3]
```

### Advanced slicing
Slicing also supports a third parameter, called _step_. The step parameter specifies which items to return as it traverses the object; a step of 2 returns _every other_ character.

### `mystring[start:end:step]`
  - start: starting index position
  - end: ending index position
  - **step**: the number of index places to move; default is 1, 2 would be every other character
 
    - `mystring[::]` and `mystring[::1]` both return `mystring`  
    - _What is happening in these cases?_

####  Examples of advanced slicing:
- `'hahaha'[1:6:2]` outputs `'aaa'`  \
_it says: starting at the beginning of the string, go until you reach index position 6, returning every other letter_ \
_Note the "until you reach" the defined endpoint, not AFTER you pass the endpoint_

What do you think the following will return?
- `len('hahaha')`
- `'hahaha'[1:5:2]`
- `'hahaha'[1::2]`
- `'poodle'[::-1]`
- `'poodle'[23]`
- `'poodle'[:23]` 
- `'poodle'[23::-1]`


### String editing
Strings are _immutable_, meaning a string object cannot be edited in place.

To illustrate, try the following in an interactive python session:
```
mystring = 'poodle'
mystring.replace('p', 'd')
mystring
``` 
What happened?

How about assigning by index value?
```
mystring[1] = 'w'
``````

While a string object cannot be edited in place, variable names can be re-used and assigned to a new object. Consider:
```
mystring = mystring.replace('p', 'd')
``` 
The variable _mystring_ now points to the newly created object that was made by performing the replace function on the original value of _mystring_.

This is the most common way of "changing" immutable object types in Python.

> _question_: can you think of a way to replace the first instance of 'p' with 'd' using indexing?


#### Escape character `\`
- newline is `\n`
- tab is `\t`
- _how would you represent a `\` character within a string?_

### String methods
In Python, the various data types are classes that are already coded for you (enter `type("cat")` to see this). 

Each class has a set of functions that are called _methods_.
Methods are accessed via the format:

- `object.methodName(args)`

String methods take a string object and perform actions on that string based on arguments passed to it in `( )`

The replace method from before is an example: `mystring.replace('p', 'd')` where `mystring` is the name of youre string object, `'p'` and `'d'` are function arguments.

String Methods:
- `.replace()` 
  - takes 2 arguments, replacing instances of the first with the second
  - searches for a single match criteria ("cat" will replace the substring "cat" in its entirety, not "c" and "a" and "t")
- `.split()` 
  - takes one argument, splitting the string at each instance of the specified character(s)
  - single match criteria
  - returns a list
  - split character(s) are removed
  - calling .split() without an argument will split into words
- `.join()`
  - takes one argument, a **list** of strings, and concatenates them into a single string
  - use with an empty string to join a list (convert to string): \
  `''.join(list)` 
- `.strip()`
  - removes whitespace from beginning and end of string
- `.translate()`
  - allows replacement of multiple characters
  - returns a string where specified characters are replaced with the character described in a _mapping table_ 
  - use `str.maketrans()` to create the mapping table object
  - Full usage (table creation + translate) looks like: \
  `mystring.translate(str.maketrans('', '', 'chars to replace'))`
  - use python string library for additional utility (add these in lieu of 'chars to replace' above)
    - `import string`
    - `string.whitespace` - all whitespace characters, `' \t\n\r\x0b\x0c'`
    - `string.punctuation` - all punctuation characters, `'!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'`

### Python search and select string methods
Again, the following are called using the following syntax:
_mystring.functionName()_
- `.startswith('text')`

- `.endswith('text')`
- `.find('text')` / `.rfind('text')`
  - provides offset (integer value) of the first/last  instance of the search text, returns `-1` if not found
- `.index('text')` / `.rindex('text')`
  - provides offset (integer value) of the first/last instance of the search text, returns an exception if not found
- `.count('text')` 
  - count the number of times 'text' appears in the string object

#### Some examples
```
# search a string with find
if "no sea".find("c") == -1:  
  print("i did not find a c")

# search a string with count
if "no sea".count("c") == 0:  
  print("i did not find a c")

# search a string with in
if "c" not in "no sea":
  print("i did not find a c")

"bumblebee".count("b")

"bumblebee".index("w")

"bumblebee".index("b")

"bumblebee".rindex("b")
```

#### RECAP: Options for searching strings in Python

- slicing with `[ ]` (covered previously)
- regex (requires _re_ library, covered later)
- string methods listed above: count( ), find( ), index( )

### Python len() function
Not a string method, but useful with strings. It is a Python built-in function that can take a string as an argument.

### `len(mystring)`
- return the number of characters in mystring \
_this is a Python built-in function_

#### Case & Alignment string functions
- _upper, lower, etc._
- _details avaliable in Ch 5 of Lubanovic text_

### Formatting Strings
Format strings (f strings) allow you to easily pass in variable values and expressions into strings.

In python 3.6+, use f strings (other functions available for earlier versions)

F strings begin with an `f`, followed by the quotes to begin the string and can have variable references inside curly brackets `{ }`. They follow the format:
### `f"this string uses a {var}"`

- expressions are allowed within curly brackets `{ }`
  - `f'{mystring.capitalize()}'`
  - `f'the first 4 characters in the string mystring are {mystring[:4]}'`


- great with `print` statements

- helpful for debugging
  - in python 3.8+ can use the `=` after a variable name in curly brackets to print the var name along with its value, \
  `f'{mystring =}'`
  - can use `.find()` or `.index()` string methods to print descriptive text around where matches occur

### [Go to Lubanovic Ch. 6 Slides](week03_slides.md)






