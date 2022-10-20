x = int(input("Please input an integer to see whether it's a prime number or not: "))

def prime(x):
    for i in range(2,x-1):
        if (x % i) == 0:
            return False
    else:
        return True
print (prime(x))