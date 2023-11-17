import math

def module_vector(a, b):
    module = math.sqrt(a**2 + b**2)
    
    return module

print(module_vector(4, 3))