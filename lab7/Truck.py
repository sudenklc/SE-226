from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        Vehicle.__init__(self, vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return "[Truck] VID: " + self.vid + " | " + self.model + " (" + str(self.year) + ") | Load: " + str(self.max_load) + "kg | " + str(self.axles) + " Axles"
