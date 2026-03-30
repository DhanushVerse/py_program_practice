""" Generators """
# A Python Generators is a special type of function that returns an iterator object.Instead of storing all values in memory at once,it generates values one-at-time,on-demand,using the yield keyword.

""" How it works """
# In Normal function we use return and it will terminate the function.but in generator we use yield.
# When we use 'yield' the function will pause and get the value.
# When the function is called again, it resumes exactly from where it left off instead of starting from the beginning.

""" Example """
def my_generator():
    yield "one"
    yield "two"
    yield "three"

gen = my_generator()
print(next(gen))

# Note:
#  -> when you call it again next yield will be execute