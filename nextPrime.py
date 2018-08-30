#Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
prime_no = []
prime_count = 1
for num in range(2,1001):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            prime_no.append(num)

print("Welcome to Prime number generation".center(100,'*'))
print(f"Numbers are :{prime_no[0]}")
for i in range(1001):
    try:
        user_input= str(input("Do you wish to see the next prime number? (Y/N): "))
        if(user_input == 'Y'):
            print(prime_no[prime_count])
            prime_count+=1
        elif(user_input == 'N'):
            print(" Thank you for using our services! ".center(100,"*"))
            break
        else:
            print("Please enter the correct choice!")
    except Exception as e:
        raise e
    