#Write a recursive function called recursive_power that takes two integers as parameters. 
#The first parameter is the base and the second parameter is the exponent. 
#Return the base parameter to the power of the exponent.

def recursive_power (b,e):
    if e==0:
        return 1
    else:
        return b*recursive_power(b,e-1)
    

print(recursive_power(5,3))

print(recursive_power(4,5))
    