import re

#Checks if a postcode has a vlid format
def postcode_check (test):

    # Starts with capital letter; folowed by capital letters or numeric digits until a space; a digit and 2 final capital letters end the rule.
    # Note, this rule could lead to incorrect long post codes such as IPAD10 0AD being passed.  
    # The len command is also used to ensure that any postcodes with more than 8 character are not passed
     
    rule = r'?[0-9]'

    # Invalid if either longer than 8 characters or the match returns None to indicate it is not a match
    if len(test)>8 or re.match(rule, test) ==None:
        result= test + ' is invalid'
    else:
    # The match is extracted using group()
        result= re.match(rule, test).group() + ' is a valid format'
    return result



def main():
    
    # specified test postcodes
    test = ['M1 1AA', 'M60 1NW', 'CR2 6XH', 'DN55 1PT', 'W1A 1HQ', 'EC1A 1BB']
    more_test = ['IP10 0AD', 'iP10 0AD', 'IPF11 0AD']

    test+=more_test

    for pc in test:
        print (postcode_check(pc))


main()