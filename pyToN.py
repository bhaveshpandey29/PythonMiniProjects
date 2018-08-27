#Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
pi = (22/7)
user_def_range = int(input("Please enter the range : "))
print(f"here is the pi value till {user_def_range} digits:\n{round(pi,user_def_range)}")