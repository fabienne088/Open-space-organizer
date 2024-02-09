import random
import csv

# import Table from table.py
from table import Table
table_instance = Table() 

class Openspace:
    def __init__ (self, number_of_tables = 6):
        self.tables = [Table() for _ in range(number_of_tables)]                                
        self.number_of_tables = number_of_tables

    def organize(self, names):  #randomly assign people to Seat objects in the different Table objects.
        random.shuffle(names)

        for table in self.tables:
            for name in names:
                if table.assign_seat(name):
                    names.remove(name)
                    break
    
    def display(self, names):  #display the different tables and there occupants in a nice and readable way
        for i, table in enumerate(self.tables, start=1):
            print(f"\nTable {i} - Occupants: {','.join(self)}")

    def store(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["Table", "Occupants"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for i, table in enumerate(self.tables, start=1):
                writer.writerow({"Table": f"Table {i}", "Occupants": ", ".join(self)})
        
        print(f"Repartition stored in {filename}")

# Example usage
if __name__ == "__main__":
    # Assume you have a list of names
    names_list = ["Person1", "Person2", "Person3", "Person4", "Person5", "Person6", "Person7", "Person8", "Person9", "Person10", "Person11", "Person12"]

    # Create an Openspace object with 6 tables
    openspace = Openspace(number_of_tables=6)

    # Organize the people randomly into the tables
    openspace.organize(names_list)

    # Display the tables and occupants
    openspace.display()

    # Store the repartition in a CSV file
    openspace.store("repartition.csv")