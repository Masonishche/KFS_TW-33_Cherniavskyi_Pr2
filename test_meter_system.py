from ElectricMeter import ElectricMeter
from ElectricMeterSystem import ElectricMeterSystem

meter1 = ElectricMeter("1", 0.1, 0.08, 100, 80)
meter2 = ElectricMeter("2", 0.12, 0.09, 120, 90)

meter_system = ElectricMeterSystem()
meter_system.add_meter(meter1)
meter_system.add_meter(meter2)

def test1():
    assert meter_system.update_meter("1", 110, 90) == 1.8

def test2():
    assert meter2.get_meter() == {
            "name": "2",
            "day_rate": 0.12,
            "night_rate": 0.09,
            "day_reading": 120,
            "night_reading": 90,
            "bill": 22.5,
            }

def test3():
    assert meter_system.update_meter("1", 110, 50) == 3.2

def test4():
    assert meter_system.update_meter("1", 60, 50) == 9.0

def test5():
    assert meter_system.update_meter("2", 70, 45) == 9.15