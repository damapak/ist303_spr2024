<h1 style="text-align: center;">Team Exercise #1</h1>

<p style="text-align: center;">David Kallemeyn</p>
<p style="text-align: center;">Last Revised Spring 2024</p>

**Due:** 3/20/2024 by 10:15 PM 

**Submission:** github repo link uploaded in canvas. Repo should contain two .py files: (1) a Python code file and (2) a Python test file. Naming conventions for filenames included below. 

**Assignment type:** Team, In-class 

**Points:** 50

#### INSTRUCTIONS
Each team will have a problem to code a solution for as well as a problem to code a test for (to test code written by another team). Create a github repository and push your code (both files). The repo should have one file for your solution code, and one for your test code that tests another team's solution. Use the naming conventions below when coding your functions and tests so that they are able to run properly.

Reminders/helpful snippets:
- use _help(FUNCTION)_ to view help on Python functions
- use the _raise_ keyword to raise an exception, i.e. `raise Exception("Your exception message here")`
- use the _assert_ keyword to test conditions, i.e. `assert func(args) == True, "message to display if false"`

## Problem 1
The sieve of Eratosthenes is an ancient algorithm used to get a list of prime numbers from within a specified range that starts with the number 2. Additional background can be found at [wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).  A description of the algorithm is listed below:

- Input: a positive integer, n
- Output: a list of prime numbers contained in the range 2...n
- Computation steps
  1. Create an initial list of all integers in the range
  2. Let p initially equal 2, the smallest prime number
  3. Enumerate through the multiples of p in increments of p, from 2p to n, marking the multiples in the list (i.e. 2p, 3p, 4p, ... ; the p itself should not be marked).
  4. Find the smallest number in the list greater than p that has not been marked. If there is no such number, stop. Otherwise, let p now equal this new number and repeat from step 3.
  5. When the algorithm terminates, the numbers remaining unmarked in the list are all the primes below n.

### 1.1 - Team 2 (Anjan, Roberta, Chun Chen, Haifa)
In a file named ***problem1_code.py***, write a function in Python with definition **`def determine_primes(n:int)`** to return a tuple where the first item is a list of all primes in the range 2...n, and the second item is the number of times the algorithm has traversed the initial list of integers. You are free to choose your own approach such as updating a list of True/False boolean values to mark non-primes as you iterate over the list, removing non-primes from the list directly as you iterate, or any other approach. Regardless of your implementation approach, it needs to return the same 2-item tuple of the list of primes, and the # of times iterated over initial list.

Additionally, the function should fit the following specifications:
- the function should accept only a single integer value; any other input type should throw an exception of type _Exception_

Example function calls: \
**determine_primes(11)** returns the tuple ( [2, 3, 5, 7, 11], 2 ) \
**determine_primes(22)** returns the tuple ( [2, 3, 5, 7, 11, 13, 17, 19], 2 )

Resources:
- recall that the range function accepts a third argument, a step value, such as the _p_ in `range(0, n + 1, p)`

### 1.2 - Team 3 (Mohammed, Akhilesh, Aote)
In a file named ***problem1_tests.py***, write tests to assess the function **determine_primes(n)** based on the specifications above.


## Problem 2
The state of a tic-tac-toe board can be represented by a list of lists (for the rules of the game, see [wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)):
```
game_state = [[0, 1, 2], 
              [0, 1, 0],
              [2, 1, 0]
             ]
```
Where 1 indicates a mark by player 1, 2 indicates a mark by player 2, and 0 indicates an unused square. A player wins if they have three marks in any consecutive arrangement (across a row, down a column, or across a diagonal that includes the center). In the example above, player 1 wins as they have three consecutive marks in the center column.

### 2.1 - Team 1 (Trevor, Marcie, HJ)
In a file named ***problem2_code.py***, write a function in Python with definition **`def determine_board_state(input_list)`** to determine the result of the input board state. The function should return _True_ if there is a win condition and print the winner, and return _False_ if there is no win condition present.

Additionally, the function should fit the following specifications:
- _input_list_ must be of type _list_ and contain 3 items that are all of type _list_, otherwise throw an exception of type _Exception_
- If the values of the inner lists contain types other than _int_, throw an exception of type _Exception_
- If a win condition exists, return _True_. If player 1 has won, print "Player 1 win". If player 2 has won, print "Player 2 win".
- If both players satisfy a winning condition, player 1 wins 
- If neither player satisfies a winning condition, return _False_ and print "No winner"

Resources:
- the _all_ builtin function can test whether all values in an iterable meet a condition. Example: `all( item < 3 for item in flat_list)` will return _True_ if all items in the flat_list object are less than 3.
- the _isinstance_ builtin function can test whether an object is of a specific type and return a bool
- you can combine _all_ with _isinstance_ to test if all items in an iterable are of a specified type. For example, given the list `mylist = ['a', 'b', 'c']`, the code `all( isinstance( item, str) for item in mylist)` will return _True_ as all of the items are strings.
- you can flatten a nested list via a list comprehension, similar to `[x for y in mylist for x in y]`
- accessing nested list items is done via double indexing, where mylist[0][1] gets the second item (index position 1) of the first outer list (index position 0) 

### 2.2 - Team 2 (Anjan, Roberta, Chun Chen, Haifa)
In a file named ***problem2_tests.py***, write tests to assess the function **determine_board_state(input_list)** based on the specifications above.

## Problem 3

### 3.1 - Team 4 (Ahmed, Ameya, Clement, Divya)
In a file named ***problem3_code.py***, write two functions in Python: _send_msg_ and _get_msg_. The _send_msg_ function should store a message (msg) along with an amount of time (delay) during which access to the message is disallowed. The _get_msg_ function will take a message _id_ and check if the alotted time for that message has passed and return True if it has as well as print the message; if the delay time has not passed it should return False and not display the message. 

The functions should have the following definitions:
- **`def send_msg(msg:str, delay:int, units:str):`** 
- **`def get_msg(id:int):`**

In addition to the definition above, the _send_msg_ function should:
- calculate a random 6-digit integer _id_ for the message
- store the message in a dictionary named _message_dict_ with a key value equal to the randomly generated _id_
- print the value of the key to the console 
- return the value of the key
- allow only the following values in the _units_ argument: "seconds", "minutes", "hours"; any other value should throw an exception of type _Exception_
- allow only _int_ type for the _delay_ argument; any other value should throw an exception of type _Exception_

The _get_msg_ function should:
- check if the current time is greater than the time the message should be available/unlocked
- if the time requirement has NOT been met, the function should print the message "cannot retrieve your message. The message may not exist or more time may need to pass." and return _False_
- if the time requirement has been met, print the message and return _True_

Resources:
- the _random_ builtin library has a _randint_ function that generates random numbers between a starting and endpoint
- the _time_ builtin library has a _time_ function that reports the current time in **seconds** (other units will first need to be converted to seconds before dealing with delay and unlock times) 

### 3.2 - Team 1 (Trevor, Marcie, HJ)
In a file named ***problem3_tests.py***, write tests to assess the functions **send_msg** and **get_msg** based on the specifications above.

Resources:
- the _time_ builtin library has a _sleep_ function that will pause code execution for the specified number of seconds

## Problem 4
The following is a description of the Euclidean Algorithm for finding the greatest common divisor of two integers:

**Formal description of the Euclidean algorithm**
- Input: two positive integers, a and b
- Output: the greatest common divisor, g, of a and b.
- Computation
  1. If a < b, exchange a and b.
  2. Divide a by b and get the remainder, r. If r = 0, report b as the GCD of a and b.
  3. Replace a with b and replace b with r. Return to step 2.

For additional information, refer to [wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm).


### 4.1 - Team 3 (Mohammed, Akhilesh, Aote)
In a file named ***problem4_code.py***, write a function in Python with definition **`def find_gcd(a:int, b:int):`** to implement the above algorithm to fit the following specifications:
- ***a*** and ***b*** are positive integers. If not, the function should throw an exception of type _Exception_
- the function should return a tuple that contains the GCD as the first item and the number of division operations needed to arrive at the GCD as the second item

Example function calls: \
**find_gcd(124, 12)** returns the tuple ( 4, 2 ) \
**find_gcd(476, 630)** returns the tuple ( 14, 3 ) 

### 4.2 - Team 4 (Ahmed, Ameya, Clement, Divya)
In a file named ***problem4_tests.py***, write tests to assess the function **find_gcd** based on the specifications above.