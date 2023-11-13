

def num_factorial(n):
 
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp
        

print(num_factorial(6))
