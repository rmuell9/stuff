#Luhn's Algorithm is a method for checking if identification numbers are valid using a check number as the last number

def verify(digits):
    total = 0
    for i, d in enumerate(reversed(digits[:-1])): #dropping the check digit from the number
        if i % 2 == 0:
            multiplier = 2
        else:
            multiplier = 1
        x = int(d) * multiplier #creating payload digits by multiplying every second digit by two
        xx = x // 10 + x % 10 #Adds the digits in a two digit num together, doesnt work with higher digit numbers 
        total = total + xx 
    check = 10 - (total % 10) #calculating check digit with (10 - (total mod10))mod10
    if int(digits[-1:]) == check:
        print('valid')
    else:
        print('invalid')

verify('17893729974')
