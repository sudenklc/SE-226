from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
         Vehicle.__init__(self, vid, model, year)
         self.fuel_type = fuel_type
         self.doors = doors

    def __str__(self):
        return "[Car] VID: " + self.vid + " | " + self.model + " (" + str(
                self.year) + ") | Fuel: " + self.fuel_type + " | " + str(self.doors) + " Doors"
