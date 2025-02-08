class VehicleInterface:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def print_make_model(self):
        print(f"Make: {self.make}, Model: {self.model}")
