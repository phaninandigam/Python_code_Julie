print("Welcome to the program which finds out if the year is leap or not!")
year=int(input("Please enter the year:\n"))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap Year.")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year.")
else:
    print("Not a Leap Year.")
print("---------Thank you, Visit again!------------")
#2024 is a leap year
#1900 is not a leap year, but when we do 1900%4 the result will be 0