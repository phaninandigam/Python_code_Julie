# Syntax:
# ["key":"Value"]

dictionary={
    "NPR":"Nandigam Phani Raghavendra",
    "NSR": "Nandigam Subbarayudu",
    123: "One two three"
}

print(dictionary["NPR"])
print(dictionary[123])
# Case sensitive

print(dictionary)


# adding an item to the dictionary
dictionary["NAK"]="Nandigam Anil Kumar"
dictionary[456]="Four five and Six"
print(dictionary)

# edit an item in the dictionary
dictionary[123]="OneTwo and Three"
print(dictionary)


# loop through dictionary
for i in dictionary:
    print(i) #this will return the keys
    print(dictionary[i])

# create an empty dictionary
empty_dictionary={}

# wipe out all the data from the exisitign dictionary
dictionary={}
print(dictionary)
print(empty_dictionary)

# nesting a list inside a dictionary
travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}
print("Nested List")
print(travel_log)
for i in travel_log:
    print(i)
    print(travel_log[i])

# nesting dictionary inside another dictionary
travel_log1={
    "France":{"city_visited":["Paris,Lille,Dijon"]},
    "Germany":["Berlin","Hamburg","Stuttgart"]
}
print("Nested dictionary")
print(travel_log1)
for i in travel_log1:
    print(i)
    print(travel_log1[i])