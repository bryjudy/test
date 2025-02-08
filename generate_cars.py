import cars

for _ in range(10):
    car = cars.generate_car()
    print(f"Make: {car['make']}, Model: {car['model']}")
