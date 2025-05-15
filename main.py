from ElectricMeterSystem import ElectricMeterSystem
from ElectricMeter import ElectricMeter
import logging
from prettytable import PrettyTable

logging.basicConfig(
    format='[%(asctime)s]: %(message)s',
    level=logging.DEBUG,
        handlers=[
        logging.FileHandler("program.log"),
    ])

def save(meter_system):
    meter_system.load_to()
    print("Successfully saved")
    logging.debug("Successfully saved")

def help(meter_system):
    table = PrettyTable()
    table.field_names = ["Command", "Description"]

    for field in table.field_names:
        table.align[field] = 'l'

    table.add_row(["help", "Show all commands"])
    table.add_row(["save", "Save data to yaml file"])
    table.add_row(["add", "Add meter"])
    table.add_row(["exit", "Save data and exit"])
    table.add_row(["update", "Update meter day and night reading"])
    table.add_row(["show", "Show all meters"])
    table.add_row(["history", "Show history by meter name"])


    print(table)
    logging.debug("Successfully show help")


def add(meter_system):
    args = input("Input name, day_rate, night_rate, day_reading, night_reading: \n").split()
    
    meter = ElectricMeter(args[0], float(args[1]), float(args[2]), float(args[3]), float(args[4]))
    meter_system.add_meter(meter)
    meter_system.history.append(meter)
    meter_system.load_history()
    
    print("Successfully added meter")
    logging.debug("Successfully added meter")

def update(meter_system):
    args = input("Input name, day_reading, night_reading: \n").split()

    meter_system.update_meter(args[0], float(args[1]), float(args[2]))
    meter_system.load_history()

    print("Successfully meter update")
    logging.debug("Successfully meter update")

def show(meter_system):
    if len(meter_system.meters) != 0:
        table = PrettyTable()
        table.field_names = ["Name", "Day rate", "Day reading", "Night rate", "Night reading", "Bill"]

        for field in table.field_names:
            table.align[field] = 'l'

        for meter in meter_system.meters:
            meter = meter.get_meter()
            table.add_row([meter["name"], meter["day_rate"], meter["day_reading"], meter["night_rate"], meter["night_reading"], meter["bill"]])
        
        print(table)
        logging.debug("Successfully show meters")
    else:
        print("Add meter at first")
        logging.debug("Meter system is 0")

def history(meter_system):
    name = input("Input name: \n")

    meter_system.load_from_history(name)
    if len(meter_system.history) != 0:
        table = PrettyTable()
        table.field_names = ["Name", "Day rate", "Day reading", "Night rate", "Night reading", "Bill", "Time"]

        for field in table.field_names:
            table.align[field] = 'l'

        for meter in meter_system.history:
            table.add_row([meter["name"], meter["day_rate"], meter["day_reading"], meter["night_rate"], meter["night_reading"], meter["bill"], meter["Time"]])
        
        print(table)
        meter_system.clear_history()
        logging.debug("Successfully show history")
    else:
        print("History is 0")
        logging.debug("Meter system is 0")

commands = {
    "help": help,
    "save": save,
    "add": add,
    "update": update,
    "show": show,
    "history": history,
}


if __name__ == "__main__":
    logging.debug("Start programm")
    meter_system = ElectricMeterSystem()
    meter_system.load_from()


    print("Hello! If you are at first here, print 'help'")
    while True:
        command = input(">>> ").lower().split()
        
        if command[0] == "exit":
            meter_system.load_to()
            logging.debug("End programm")
            break
        try: 
            logging.debug(f"Command {command[0]}")
            commands[command[0]](meter_system)
        except Exception as e:
            print(e)
            logging.debug("Incorrect command")
            print("Incorrect format")
