states_of_India=["Kerala","TN","AP","TS","Karnataka"]
print(states_of_India)
print(states_of_India[0])
print(states_of_India[1])


print(states_of_India[-1]) # -1 will be the last item of the list

# edit the list
states_of_India[1]= "Tamil Nadu"
print(states_of_India)

# add a item at the end of the list
states_of_India.append("Goa")
print(states_of_India)

states_of_India.extend(["Odissa","UP"])
print(states_of_India)

print(len(states_of_India )) #8
print(states_of_India[8]) #error IndexError: list index out of range



# for more function on list, go throgh the below doc
# https://docs.python.org/3/tutorial/datastructures.html