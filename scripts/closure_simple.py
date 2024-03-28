# illustrate a closure in python

def outer_function(outer):
  print(f'{outer = }')

  def inner_function(inner):
    # this function is the closure - accesses vars from outer function
    print(f'{inner = }')
    return outer - inner

  return inner_function # outer function returns inner function

# create closure object that stores the inner function with the outer value
closure = outer_function(100)
print(f'closure object is of type: {type(closure)}')

# run the closure object passing a value in to inner_function
closure_result = closure(25)
print(f'result of inner function run: {closure_result}')