#Exercise 1
#Write a recursive function called recursive_sum that takes an integer as a parameter. 
#Return the sum of all integers between 0 and the number passed to recursive_sum.

def recursive_sum(n):
    if n<=0:
        return 0
    else:
        return n + recursive_sum(n-1)
    
#Exercise 2
#Write a recursive function called list_sum that takes a list of numbers as a parameter. 
#Return the sum of all of the numbers in the list. 
#Hint, the slice operator will be helpful in solving this problem.
def list_sum(list):
    if len(list)==1:
        return list[0]
    else:
        return list[-1] + list_sum(list[0:-1])

#Exercise 3
#Write a recursive function called bunny_ears that takes the number of bunnies (an integer) as a parameter. 
#Return the number of bunny ears (2 per bunny). 
#Do not use multiplication; instead use addition.
def bunny_ears(b):
    if b==0:
        return 0
    else:
        return 2 + bunny_ears(b-1)

#Exercise 4
#Write a recursive function called reverse_string that takes a string as a parameter. 
#Return the string in reverse order. 
#Hint, the slice operator will be helpful when solving this problem.
def reverse_string(s):
    if len(s)==1:
        return s[0]
    else:
        return s[-1] + reverse_string(s[0:-1])
    
#Exercise 5
#Write a recursive function called get_max that takes a list of numbers as a parameter. 
#Return the largest number in the list.
def get_max(list):
    if len(list)==1:
        return list[0]
    else:
        return max(list[-1], get_max(list[0:-1]))

#main
print('Exercise 1:')
print(recursive_sum(5))
print(recursive_sum(10))

print('Exercise 2')
print(list_sum([1,2,3,4,5]))
print(list_sum([10, 12.5, 10, 7]))

print('Exercise 3')
print(bunny_ears(8))
print(bunny_ears(0))

print('Exercise 4')
print(reverse_string('cat'))
print(reverse_string('house'))

print('Exercise 5')
print(get_max([1, 2, 3, 4, 5]))
print(get_max([11, 22, 3, 41, 15]))