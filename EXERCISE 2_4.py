# (a)
a = list(b'Magdalena')
print("Magdalena --> {}".format(a) )


# (b)
from tabulate import tabulate

pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3, "Lithium", "Li", 7), (4, "Beryllium", "Be", 9),
      (5, "Boron", "B", 11), (6, "Carbon", "C", 12), (7, "Nitrogen", "N", 14), (8, "Oxygen", "O", 16),
      (9, "Fluorine", "F", 19), (10, "Neon", "Ne", 20)]
head = ["No.", "Name (en)", "Symbol", "Weight (u)"]

widths = [3, 20, 6, 10]

tab = tabulate(pt, headers=head, tablefmt="pretty", colalign=("right","left","center","right"))

print(tab)
