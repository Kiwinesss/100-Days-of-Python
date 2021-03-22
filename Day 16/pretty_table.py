from prettytable import PrettyTable  # import the PrettyTable CLASS
 
table = PrettyTable()  # create the object table
table.add_column("Pokemon Name", ["Chespin", "Fennekin", "Froakie"])
table.add_column("Type", ["Grass", "Fire", "Water"])
table.align = "l"
print(table)
