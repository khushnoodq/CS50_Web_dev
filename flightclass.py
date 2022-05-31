
class Flight():
    def __init__( self, capacity ):
        self.capacity = capacity
        self.passengers = []

    def addPas( self, passnm ):
        if not self.openSeats(): 
            return False

        self.passengers.append(passnm)
        return True

    def openSeats( self ):
        return self.capacity - len(self.passengers)

flight = Flight(3)
names = ["Khushnood","Prajjaval","Ganti","Marieke"]
for nm in names:
    if flight.addPas(nm):
        print("Success")
    else:
        print("Seats full")