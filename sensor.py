class Sensor:
    """
    Base sensor class.
    """

    def __init__(self, timestamp):
        self.timestamp = timestamp


class NoiseThermometer(Sensor):
    """
    Cryogenic noise thermometer sensor.
    """

    def __init__(self, timestamp, temperature):
        super().__init__(timestamp)
        self.temperature = float(temperature)
        self.status = "Unknown"

    def get_temperature(self):
        return self.temperature

    def detect_status(self):
        """
        Classifies temperature condition.
        """
        if self.temperature < 0.0152:
            self.status = "Normal"
        elif self.temperature < 0.0155:
            self.status = "Warning"
        elif self.temperature < 0.0160:
            self.status = "Spike"
        else:
            self.status = "Critical"
        return self.status
