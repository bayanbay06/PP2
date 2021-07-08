def find(number):
    if number % 2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

number = int(input('Enter the number: '))  
numtype = find(number)                   
print('Given number is',numtype)
