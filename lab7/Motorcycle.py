from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, motorcycle_type):
        Vehicle.__init__(self, vid, model, year)
        self.engine_cc = engine_cc
        self.type = motorcycle_type

    def __str__(self):
        return "[Motorcycle] VID: " + self.vid + " | " + self.model + " (" + str(self.year) + ") | Eng: " + str(self.engine_cc) + "cc | Type: " + self.type
