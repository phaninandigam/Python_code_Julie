# Your program should print each number from 1 to 100 in turn and include number 100.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1,16):
    if number%3==0:
        if number%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)

print("------------------------------")
# OR
for number in range(1,16):
  if number%3==0 and number%5==0:
      print("FizzBuzz")
  elif number%3==0:
    print("Fizz")
  elif number%5==0:
    print("Buzz")
  else:
    print(number)