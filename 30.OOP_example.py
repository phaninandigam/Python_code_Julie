from prettytable import PrettyTable
from prettytable import from_csv

table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="r"
print(table)
# print(table.get_string())

# reading a file form the CSV
with open("Book1.csv") as fp:
    mytable=from_csv(fp)
    mytable.align="r"
    print(mytable)