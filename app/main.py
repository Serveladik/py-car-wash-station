class Car:
    # write your code here
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand



class CarWashStation:
    # write your code here
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> list:
        serve_filter_list = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = 0
                serve_filter_list.append(car)
        return serve_filter_list

    def calculate_washing_price (self, cars: list) -> int:
        for car in cars:
            if car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center:

