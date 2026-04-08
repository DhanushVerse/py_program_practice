""" range() """
# In python range() is a built in function and commonly used for looping a specific number of times.
# This set of numbers has its own data type called range.

""" Creating ranges """
# The range() function can be called with 1,2,3 arguments, using this syntax.
# syntax : range(start, stop, step)

""" Call range() With One Arguments """
# If the range function is called with only one argument, the argument represents the stop value.
# The start argument is optional, and if not provided, it defaults to 0.
one_arg = range(10)
print(one_arg)
print(list(one_arg))

""" Call range() With Two Arguments """
# If the range function is called with two arguments, the first argument represents the start value, and the second argument represents the stop value.
two_arg = range(3,10)
print(list(two_arg))

""" Call range() With Three Arguments """
# If the range function is called with three arguments, the third argument represents the step value.
# The step value means the difference between each number in the sequence. it is optional, and if not provided,it defaults to 1.
three_arg = range(3,10,2)
print(list(three_arg))




