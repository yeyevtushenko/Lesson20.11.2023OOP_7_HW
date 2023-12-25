class TemperatureSensor:
    def __init__(self):
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        lower_limit = -50
        upper_limit = 50

        if lower_limit <= value <= upper_limit:
            self._temperature = value
        else:
            print(f"Error: Temperature should be between {lower_limit} and {upper_limit} degrees Celsius.")


temperature_sensor = TemperatureSensor()


try:
    new_temperature = float(input("Enter the temperature in degrees Celsius: "))
    temperature_sensor.temperature = new_temperature
    print(f"Current Temperature: {temperature_sensor.temperature}")
except ValueError:
    print("Error: Please enter a valid numerical value for temperature.")
