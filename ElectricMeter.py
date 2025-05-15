class ElectricMeter:
    def __init__(self, name, day_rate, night_rate, day_reading, night_reading, bill=None):
        self.name = name
        self.day_rate = day_rate
        self.night_rate = night_rate
        self.day_reading = day_reading
        self.night_reading = night_reading
        self.bill = (day_reading * self.day_rate) + (night_reading * self.night_rate) if bill is None else bill

    def calculate_bill(self, new_day_reading, new_night_reading):
        day_consumption = new_day_reading - self.day_reading
        night_consumption = new_night_reading - self.night_reading

        if day_consumption < 0:
            day_consumption += 100
            new_day_reading = 100
            
        if night_consumption < 0:
            night_consumption += 80
            new_night_reading = 80

        bill_amount = (day_consumption * self.day_rate) + (night_consumption * self.night_rate)

        self.day_reading = new_day_reading
        self.night_reading = new_night_reading

        self.bill = bill_amount

    
    def get_meter(self):
        meter_dict = {
            "name": self.name,
            "day_rate": self.day_rate,
            "night_rate": self.night_rate,
            "day_reading": self.day_reading,
            "night_reading": self.night_reading,
            "bill": self.bill,
        }

        return meter_dict
    

    def update(self, name=None, day_rate=None, night_rate=None, day_reading=None, night_reading=None):
        self.name = name if name is not None else ...
        self.day_rate = day_rate if day_rate is not None else ...
        self.night_rate = night_rate if night_rate is not None else ...
        self.day_reading = day_reading if day_reading is not None else ...
        self.night_reading = night_reading if night_reading is not None else ...