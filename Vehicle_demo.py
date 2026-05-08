import vehicles

Car = vehicles.Car('Tesla','Z','60','300,000','4')

Truck = vehicles.Trucks('Ford','6','20','250,000','2WD')

SUV = vehicles.SUV('Honda','2026','100','100,000','8')


cars = [Car,Truck,SUV]


print(f'''
The following car is in inventory:
Make: {Car.get_make()}
Model: {Car.get_modle()}
Mileage: {Car.get_milage()}
Price: {Car.get_price()}
Number of doors: {Car.get_doors()}
      ''')

print(f'''
The following pickup truck is in inventory:
Make: {Truck.get_make()}
Model: {Truck.get_modle()}
Mileage: {Truck.get_milage()}
Price: {Truck.get_price()}
Drive type: {Truck.get_drive_type()}
''')

print(f'''
The following SUV is in inventory:
Make: {SUV.get_make()}
Model: {SUV.get_modle()}
Mileage: {SUV.get_milage()}
Price: {SUV.get_price()}
Drive type: {SUV.get_passanger_capacity()}
''')
