'''Write a program which will find factors of given number and find whether the factor is even or odd'''

def find_factors(n):
    factors = []

    #finding factors
    for i in range(1,n+1):
        if(n%i==0):
            factors.append(i)


    for factor in factors:
        if(factor %2 == 0):
           print(factor , "Even")
        else:
            print(factor, "Odd")




input_number = int(input("Enter a number : "))
find_factors(input_number)



