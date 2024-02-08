from typing import Self


class Seat:  # class seat with attributes free and occupant
    seats = 4
    
    def __init__(self, free=True, occupant=None):
        self.free = free
        self.occupant = occupant

    def set_occupant(self,name): # allows the program to assign someone a seat if it's free
        if self.free:
            self.occupant = name
            self.free = False 
            return f"{name} has been assigned to the seat"
        else:
            return "Seat is already occupied"   

    def remove_occupant(self): # 1.remove someone from a seat and 2. return the name of the person occupying the seat before
        if not self.free:
            occupant_name = self.occupant
            self.free = True
            self.occupant = None
            return (f"{occupant_name} has been removed from the seat")
        else:
            print ("Seat is already empty.")


class Table: #Class table with 2 attributes

    tables = 6
    def __init__(self, capacity): #seats is a list of Seat objects (size = capacity)
        self.capacity = int(capacity)
        self.seats = [Seat() for - in range(self.capacity)]
    
    def has_free_spot(self): #return True if a spot is available
        #conditional with boolean
        return any (seat.free for seat in self.seats)
    
    def assign_seat(self, name): #place someone at the table
        for seat in self.seats:
            if seat.free:
                return seat.set_occupant(name)
        return "No free spots available at the table."
    
    def left_capacity(self): #returns an integer    
        #return sum(1 for seat in self.seats if seat.free)
