class Car:
    def __init__(self, Name, Fuel_Rate=100, Velocity=0):
        self.Name = Name
        self.Fuel_Rate = Fuel_Rate  # Fuel consumption rate (liters per kilometer)
        self.Velocity = Velocity  # Current speed (km/h)

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self._fuelRate = value
        else:
            print("Invalid fuelRate. Must be between 0 and 100.")

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            print("Invalid velocity. Must be between 0 and 200.")

    def run(self, distance, velocity):
        self.velocity = velocity  # Set the velocity
        if self.velocity == 0:
            print(f"{self.name} is not moving.")
            return

        fuel_consumed = distance
        if fuel_consumed > self.fuelRate:
            distance = self.fuelRate
            self.fuelRate = 0
            self.stop(distance - fuel_consumed)
        else:
            self.fuelRate -= fuel_consumed
            self.stop(0)

    def stop(self, remaining_distance):
        self.velocity = 0  # Stop the car
        if remaining_distance > 0:
            print(f"{self.name} has stopped. {remaining_distance} km remaining to destination.")
        else:
            print(f"{self.name} has arrived at the destination.")
