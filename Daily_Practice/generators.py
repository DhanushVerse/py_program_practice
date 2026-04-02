""" Generators """
# A Python Generators is a special type of function that returns an iterator object.Instead of storing all values in memory at once,it generates values one-at-time,on-demand,using the yield keyword.

""" How it works """
# In Normal function we use return and it will terminate the function.but in generator we use yield.
# When we use 'yield' the function will pause and get the value.
# When the function is called again, it resumes exactly from where it left off instead of starting from the beginning.
# When the function is called it can't executed instead it will send a generator object.when you use next() then only it will executed.

""" Example """
def my_generator():
    yield "one"
    yield "two"
    yield "three"

gen = my_generator()
print(next(gen))

# Note:
#  -> when you call it again next yield will be execute

# Task name : Log File Monitor
def error_filter(log_data):
    for line in log_data:
        if "ERROR" in line:
            yield line
logs = [
    "INFO: System started",
    "ERROR: Database connection failed",
    "INFO: User logged in",
    "ERROR: Timeout occurred",
    "INFO: Task completed"
]
# Create generator object
my_filter = error_filter(logs)

# In this we can't use next() instead in your generator object and take the values using for loop.
for error in my_filter:
    print(f'Found: {error}')

""" generator expressions """
# We can create a generator with generator expression

gen_exp = (x*x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# why we use it:
#  -> we use list comprehension for huge amount of data the RAM size is fully occupied and your system is slow.
#  -> Incase we use generator expression it takes less memory.

