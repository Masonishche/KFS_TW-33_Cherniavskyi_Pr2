from ElectricMeter import ElectricMeter
import yaml
import logging
import datetime

logging.basicConfig(
    format='[%(asctime)s]: %(message)s',
    level=logging.DEBUG,
        handlers=[
        logging.FileHandler("program.log"),
    ])

class ElectricMeterSystem:
    def __init__(self):
        self.meters = []
        self.history = []
    def add_meter(self, meter: ElectricMeter):
        if len(self.meters) != 0:
            flag = False
            idx = -1
            for index, dict_meter in enumerate(self.meters):
                dict_meter = dict_meter.get_meter()
                if dict_meter["name"] == meter.name:
                    flag = True
                    idx = index
                    break

            if flag:
                self.meters.pop(idx)
                self.meters.append(meter)
                print(f"Meter {meter.name} was exist and was rewrite")
                logging.debug(f"Meter {meter.name} was exist and was rewrite")
            else:
                self.meters.append(meter)
        else:
            self.meters.append(meter)

    def update_meter(self, name, new_day_reading, new_night_reading):
        for meter in self.meters:
            if meter.name == name:
                meter.calculate_bill(new_day_reading, new_night_reading)
                self.history.append(meter)
                return meter.bill
        
    
    def load_to(self):
        with open("data.yaml", "w") as f:
            if len(self.meters) != 0:
                meters = [meter.get_meter() for meter in self.meters]
                yaml.dump(meters, f)
            else:
                print("Nothing to save")
        
    def load_from(self):
        with open('data.yaml') as f:
            content = yaml.safe_load(f)
            if content is not None:
                for element in content:
                    meter = ElectricMeter(
                        element["name"], 
                        float(element["day_rate"]), 
                        float(element["night_rate"]), 
                        float(element["day_reading"]), 
                        float(element["night_reading"]),
                        float(element["bill"])
                    )
                    self.meters.append(meter)
    
    def load_history(self):
        
        with open("history.yaml", "a") as f:
            meters = []
            current_time = datetime.datetime.now()
            current_time_formatted = current_time.strftime("%Y-%m-%d %H:%M:%S")

            for meter in self.history:
                meter = meter.get_meter()
                meter["Time"] = current_time_formatted
                meters.append(meter)

            yaml.dump(meters, f)
            self.clear_history()

    def clear_history(self):
        self.history = []

    def load_from_history(self, name):
        with open("history.yaml", "r") as f:
            content = yaml.safe_load(f)
            if content is not None:
                for element in content:
                    if element["name"] == name:
                        self.history.append(element)
                        
            

