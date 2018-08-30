#Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
user_num = int(input("Please enter a number: "))
prime_fact = []
try:
    if user_num > 0:
        for i in range(2,user_num):
            if user_num % i == 0:
                prime_fact.append(i)
except Exception as e:
    print(e)
else:
    if(len(prime_fact)>0):
        print(f"Prime factors of {user_num} is : {tuple(prime_fact)}")
    else:
        print(f" Sorry no prime facors found found for {user_num} ".center(150,"*"))