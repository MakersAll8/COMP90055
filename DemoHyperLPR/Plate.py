class Plate(object):
    def __init__(self):
        self.plateNumber = 0
        self.plateLocation = [0, 0, 0, 0]

    def update_plate(self, plate):
        self.plateNumber = plate

    def update_location(self, location):
        self.plateLocation = location

    def reset(self):
        self.plateNumber = 0
        self.plateLocation = [0, 0, 0, 0]
