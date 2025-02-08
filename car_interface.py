import random

def generate_cars(num_cars):
    cars = []
    for _ in range(num_cars):
        if random.random() < 0.5:
            car = Car("Toyota", "Corolla")
        else:
            car = Truck("Ford", "F-150")
        cars.append(car)
    return cars

if __name__ == "__main__":
    cars = generate_cars(5)
    for car in cars:
        car.print_make_and_model()