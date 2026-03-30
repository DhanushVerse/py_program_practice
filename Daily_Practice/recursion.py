""" Recursion """
# A function can call itself again and again until the specified condition is satisfied.
# Assume if you have a complex task you split the piece of task and check the condition is satisfied or not if satisfies return it.otherwise call it again

# Note:
#  -> Base case is very important for stop the function
#  -> Recursive step is for calling the function again and again

# Example:
# -> Countdown:                             
def countdown(n):                           # o/p:
     if n == 0:                             # 3
        print(f'Blast off')                 # 2
        return                              # 1
     print(n)                               # Blast off
     countdown(n-1) 
countdown(3)                    

# Factorial of n numbers:
def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n-1)

fact_num = int(input('Enter the factorial number:'))
fact = find_factorial(fact_num)
print(fact)


        
        
    
    
                             



