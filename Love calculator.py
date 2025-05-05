print("Wlecome to the love calculator program:")
name1 = input("Please enter the first person name.\n")  # What is your name?
name2 = input("Please enter the second person name.\n")  # What is their name?
print("The Love Calculator is calculating your score...")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_name = combined_names.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

score1 = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

score2 = l + o + v + e
total_score = int(str(score1) + str(score2))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
