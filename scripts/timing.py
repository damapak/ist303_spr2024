# Custom Decorator Example
# Decorators are functions that take function(s) as parameters and return a function
# This file test generators (consumed as iterated) vs. lists

import time
from datetime import datetime

# decorator function #1: time the duration of a function
def time_my_func(func): # passing/returning a function does not use parens ()
    '''decorator function to report time lapsed during function execution'''

    def exec_func():

        start_time = time.perf_counter()
        func() # call the decorated function
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"The {func.__name__} code executed in {round(elapsed_time,4)} seconds.")
    
    # decorator function MUST return a callable object (function)
    # returning it here returns the "called" function object, with persistent reference to func that was passed in
    return exec_func 

# decorator function #2: prints the time the code started execution
def timestamp(func):

    def wrapper():
        print(f'Run time: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        func()

    return wrapper


@timestamp
@time_my_func
def generator_test() -> None:
    g = (x for x in range(100_000_000))
    for item in g:
        pass

    print(f'memory used to store the generator object, no gc overhead: {g.__sizeof__()} bytes')

@timestamp
@time_my_func
def list_test() -> None:
    l = [x for x in range(100_000_000)]
    for item in l:
        pass

    print(f'memory used to store the list object, no gc overhead: {l.__sizeof__()} bytes')
    
# calling decorated functions below calls the decorator function 
#   with these functions as input parameters
generator_test()
list_test()