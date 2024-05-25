class Vehicle:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def display_info(self):
        print(f'make: {self.make}, model: {self.model}, mileage: {self.mileage} miles')

    def drive(self,miles,mileages):
        self.mileages += miles

    def maintenance_needed(self, mileage):
        return self.mileage > 100000


    def reset_mileage(self,mileage):
        self.mileage = 0

BMW = Vehicle("BMW", "M5", 96000)
BMW.display_info()

BMW.drive(30000)
BMW.display_info()

print(BMW.maintenance_needed())

BMW.drive(50000)
print(BMW.maintenance_needed())

BMW.reset_mileage()
print(BMW.maintenance_needed())