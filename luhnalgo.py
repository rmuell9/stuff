#Luhn's Algorithm is a method for checking if identification numbers are valid using a check number as the last number

def verify(digits):
    total = 0
    for i, d in enumerate(reversed(digits[:-1])): #dropping the check digit from the number
        x = int(d) * (2 - i % 2) #creating payload digits by multiplying every second digit by two
        xx = x // 10 + x % 10 #Adds the digits in a two digit num together, doesnt work with higher digit numbers 
        total = total + xx 
    check = 10 - (total % 10) % 10 #calculating check digit with (10 - (total mod10))mod10)
    if check == int(digits[-1]):
        print('valid')
    else: 
        print('invalid')

verify('17893729974')

def efficientVerify(digits):
    total = 0
    for i, d in enumerate(reversed(digits)):
        x = int(d) * (1 + i % 2)
        total += x // 10 + x
    return total % 10 == 0

if __name__ == '__main__':
    assert efficientVerify('17893729974')
    assert not efficientVerify('17893729975')
    print('valid too')
