class Seat:  # class seat with attributes free and occupant
      
    def __init__(self, free=True, occupant=None):
        self.free = free
        self.occupant = occupant

    def set_occupant(self,name): # allows the program to assign someone a seat if it's free
        if self.free:
            self.occupant = name
            self.free = False 
            return f"{name} has been assigned to the seat."
        else:
            return "Seat is already occupied"   

    def remove_occupant(self): # 1.remove someone from a seat and 2. return the name of the person occupying the seat before
        if not self.free:
            occupant_name = self.occupant
            self.free = True
            self.occupant = None
            print (f"{occupant_name} has been removed from the seat.")
            return occupant_name
        else:
            print ("Seat is already vacant.")


class Table: #Class table with 2 attributes

    def __init__(self, capacity=4): #seats is a list of Seat objects (size = capacity)
        self.capacity = (capacity)
        self.seats = [Seat() for _ in range(capacity)]
    
    def has_free_spot(self): #return True if a spot is available
        #conditional with boolean
        return any(seat.free for seat in self.seats)
    
    def assign_seat(self, name): #place someone at the table
        for seat in self.seats:
            if seat.free:
                return seat.set_occupant(name)
        return "No free spots available at the table."
    
    def left_capacity(self): #returns an integer    
        return sum(seat.free for seat in self.seats)

if  __name__ == '__main__':
    # Example Usage with 6 tables, each having 4 seats:
    tables = [Table() for _ in range(6)]

    # Assigning occupants to seats
    tables[0].assign_seat("Alice")
    tables[1].assign_seat("Bob")
    tables[2].assign_seat("Charlie")
    tables[3].assign_seat("David")

    # Checking if there's a free spot at each table
    for i, table in enumerate(tables):
        print(f"Table {i + 1} has a free spot: {table.has_free_spot()}")

    # Checking left capacity at each table
    for i, table in enumerate(tables):
        print(f"Table {i + 1} has left capacity: {table.left_capacity()}")