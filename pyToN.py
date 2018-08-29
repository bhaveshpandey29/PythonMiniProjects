# #Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

from mpmath import mp
user_def_input = int(input("Please enter the digits you wish to see after decimals in Pi: "))
try:
    if(user_def_input < 0):
        print("Please enter the positive value.")
    else:
        mp.dps = user_def_input
        print(mp.pi)
except Exception as e:
    raise e