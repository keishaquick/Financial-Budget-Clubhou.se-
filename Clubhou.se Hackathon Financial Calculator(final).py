"""Financial Calculator based on FPL"""
"""Date: 02-04-2022"""
"""Purpose: This script will accept user data and determine the the appropriate financial tool based on FPL status"""


"""Step A: Create user account and generate userID"""
"""Author: KQuick"""


#accountname = () # blank list to capture usernames and use for parsing
minusernamelen = ("999999999999999999999") #21 characters validation check
print("Welcome to Financial PI\n Press 'Enter' to get started!\n")

print("Let's get started with creating you an username:\n Usernames must be 20 characters or less and contains no spaces.")

user_firstname = input("Please enter your first name: \n")
user_lastname = input( "Please enter your last name: \n")
user_fullname = user_firstname + " " + user_lastname # concatenate first and last name
  

"""Generated user account name"""
username1 = user_firstname + "." + user_lastname
comp_username = username1.lower()
print("\nThank you for your input", user_fullname, "your username is: ", comp_username)
    
   
"""Step B: Accept the following user data: State, Household size & Household Income (take home pay)"""
"""Eric M. Thompson"""

ak_pov = {1: 16990, 2: 22890, 3: 28790, 4: 34690,
          5: 40590, 6: 46490, 7: 52390, 8: 58290}
hi_pov = {1: 15630, 2: 21060, 3: 26490, 4: 31920,
          5: 37350, 6: 42780, 7: 48210, 8: 53640}
lower_48_pov = {1: 13590, 2: 18310, 3: 23030,
                4: 27750, 5: 32470, 6: 37190, 7: 41910, 8: 46630}

state = input("\nPlease enter your two letter state code (ie GA | AZ): ")

household = int(input(
    "Please enter your the number of people in your household (ie 8): "))

income = float(input("Please enter your gross income (ie 30000): "))
below_pov_level = False

if (state == "AK"):
    if household > 8:
        base_pov = ak_pov[8] + ((household - 8) * 5900)
        below_pov_level = income <= base_pov
    else:
        below_pov_level = income <= ak_pov[household]
    if below_pov_level:
        income_bracket = "LOW"
    elif income <= (ak_pov[household] * 2):
        income_bracket = "MODERATE"
    else:
        income_bracket = "MIDDLE"
elif (state == "HI"):
    if household > 8:
        base_pov = hi_pov[8] + ((household - 8) * 5430)
        below_pov_level = income <= base_pov
    else:
        below_pov_level = income <= hi_pov[household]
    if below_pov_level:
        income_bracket = "LOW"
    elif income <= (hi_pov[household] * 2):
        income_bracket = "MODERATE"
    else:
        income_bracket = "MIDDLE"
else:
    if household > 8:
        base_pov = lower_48_pov[8] + ((household - 8) * 4720)
        below_pov_level = income <= base_pov
    else:
        below_pov_level = income <= lower_48_pov[household]
    if below_pov_level:
        income_bracket = "LOW"
    elif income <= (lower_48_pov[household] * 2):
        income_bracket = "MODERATE"
    else:
        income_bracket = "MIDDLE"

print("Your family's income bracket is: {}".format(income_bracket))

print("\nThank you!\nPress 'Enter' to exit")
input()
        
