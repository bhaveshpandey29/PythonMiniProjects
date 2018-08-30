#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def fibo(limit):
    num1,num2 = 0,1
    fibonacci = [num1,num2]
    for i in range(limit-2):
        fib = num1+num2
        fibonacci.append(fib)
        num1 = num2
        num2 = fib
    return(fibonacci)
    
user_def_range = int(input("Please enter the length of Fibonacci series you wish to display: "))
try:
    if(user_def_range > 0):
        if(user_def_range == 1):
            print(f"here is the fibonacci series with lenght of {user_def_range}: 0")
        elif(user_def_range == 2):
            print(f"here is the fibonacci series with lenght of {user_def_range}: 0,1")
        else:
            print(f"here is the fibonacci series with lenght of {user_def_range}: {fibo(user_def_range)}")
    else:
        print("Please enter a positive integer")
except Exception as e:
    raise e